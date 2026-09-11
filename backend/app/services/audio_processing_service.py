import logging
import os
from pathlib import Path
try:
    import librosa
    import numpy as np
    import soundfile as sf
    LIBROSA_AVAILABLE = True
except ImportError:
    LIBROSA_AVAILABLE = False

logger = logging.getLogger(__name__)

class AudioProcessingService:
    """音频处理服务"""
    
    def __init__(self):
        self.librosa_available = LIBROSA_AVAILABLE
    
    def denoise(self, input_path: str, output_path: str, strength: float = 0.5) -> str:
        """去除背景噪音
        
        Args:
            input_path: 输入音频路径
            output_path: 输出音频路径
            strength: 去噪强度 (0-1)，越高去噪越强
        
        Returns:
            输出文件路径
        """
        if not self.librosa_available:
            logger.warning("⚠️ librosa 未安装，音频处理功能不可用")
            raise RuntimeError("librosa 未安装")
        
        if not os.path.exists(input_path):
            logger.error(f"❌ 音频文件不存在: {input_path}")
            raise FileNotFoundError(f"音频文件不存在: {input_path}")
        
        try:
            logger.info(f"🔊 开始去噪: {input_path}")
            
            # 加载音频
            y, sr = librosa.load(input_path, sr=None)
            
            # 计算短时傅里叶变换
            D = librosa.stft(y)
            magnitude, phase = np.abs(D), np.angle(D)
            
            # 估计噪音谱（假设前1秒是噪音）
            noise_duration = min(sr, len(y))  # 最多1秒
            noise_magnitude = np.mean(magnitude[:, :noise_duration//512], axis=1, keepdims=True)
            
            # 应用谱减法去噪
            magnitude_denoised = magnitude - strength * 2 * noise_magnitude
            magnitude_denoised = np.maximum(magnitude_denoised, 0.1 * magnitude)  # 保持最小值
            
            # 重建信号
            D_denoised = magnitude_denoised * np.exp(1j * phase)
            y_denoised = librosa.istft(D_denoised)
            
            # 保存
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            sf.write(output_path, y_denoised, sr)
            
            logger.info(f"✅ 去噪完成: {output_path}")
            return output_path
        
        except Exception as e:
            logger.error(f"❌ 去噪失败: {e}")
            raise
    
    def normalize(self, input_path: str, output_path: str) -> str:
        """音频标准化（调整音量）
        
        Args:
            input_path: 输入音频路径
            output_path: 输出音频路径
        
        Returns:
            输出文件路径
        """
        if not self.librosa_available:
            logger.warning("⚠️ librosa 未安装")
            raise RuntimeError("librosa 未安装")
        
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"音频文件不存在: {input_path}")
        
        try:
            logger.info(f"🔊 开始标准化: {input_path}")
            
            # 加载音频
            y, sr = librosa.load(input_path, sr=None)
            
            # 标准化（将最大幅度设置为 0.95）
            y_normalized = 0.95 * y / (np.max(np.abs(y)) + 1e-9)
            
            # 保存
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            sf.write(output_path, y_normalized, sr)
            
            logger.info(f"✅ 标准化完成: {output_path}")
            return output_path
        
        except Exception as e:
            logger.error(f"❌ 标准化失败: {e}")
            raise
    
    def analyze_loudness(self, audio_path: str) -> dict:
        """分析音频响度
        
        Returns:
            包含 rms, peak, loudness 的字典
        """
        if not self.librosa_available:
            raise RuntimeError("librosa 未安装")
        
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"音频文件不存在: {audio_path}")
        
        try:
            logger.info(f"🔊 分析音频响度: {audio_path}")
            
            y, sr = librosa.load(audio_path, sr=None)
            
            # 计算 RMS 能量
            rms = np.sqrt(np.mean(y**2))
            
            # 计算峰值
            peak = np.max(np.abs(y))
            
            # 转换为分贝
            rms_db = 20 * np.log10(rms + 1e-9)
            peak_db = 20 * np.log10(peak + 1e-9)
            
            return {
                "rms": float(rms),
                "peak": float(peak),
                "rms_db": float(rms_db),
                "peak_db": float(peak_db),
                "loudness": float(rms_db)
            }
        
        except Exception as e:
            logger.error(f"❌ 响度分析失败: {e}")
            raise

# 全局音频处理服务实例
audio_processing_service = AudioProcessingService()
