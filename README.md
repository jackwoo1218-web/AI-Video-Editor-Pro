# 🎬 AI-Video-Editor-Pro

一个功能齐全的 AI 智能视频生成和剪辑平台，完全免费开源，支持自动字幕生成、智能场景检测、音频处理和专业级视频渲染。

## ✨ 核心功能

### 🎯 视频编辑
- ✅ **拖拽式可视化编辑**：直观的时间线编辑器
- ✅ **多轨道编辑**：视频、音频、字幕同时编辑
- ✅ **丰富的转场效果**：淡出、滑动、缩放等专业级转场
- ✅ **视频特效和滤镜**：调色、模糊、亮度对比度调整

### 🤖 AI 智能功能
- ✅ **自动字幕生成**：通过 OpenAI Whisper 识别音频自动生成字幕
- ✅ **多语言翻译**：自动翻译字幕到 50+ 种语言
- ✅ **场景智能检测**：自动识别视频场景变化、自动分镜
- ✅ **音频智能处理**：背景音乐推荐、音量自动化、去噪处理

### 📹 视频生成
- ✅ **图文转视频**：将图片序列、文字转换为专业视频
- ✅ **模板库**：预设的视频模板快速生成
- ✅ **自动排版**：AI 智能安排文字、图片、音乐的呈现方式

### ⚡ 高级功能
- ✅ **批量处理**：一次处理多个视频文件
- ✅ **自动化工作流**：设定规则自动剪辑和渲染
- ✅ **智能调色**：AI 自动调整视频色彩和亮度
- ✅ **水印管理**：自动添加、定位和样式化水印

### 📊 输出
- ✅ **多格式导出**：MP4、WebM、MOV、MKV 等
- ✅ **多分辨率支持**：720p、1080p、2K、4K 一键导出
- ✅ **优化预设**：YouTube、TikTok、Instagram 等平台优化预设

## 🚀 快速开始

### 系统要求
- Python 3.9+
- Node.js 16+
- FFmpeg 4.4+
- 8GB+ RAM（推荐 16GB）
- 20GB+ 硬盘空间

### 安装步骤

#### 1. 克隆仓库
\`\`\`bash
git clone https://github.com/jackwoo1218-web/AI-Video-Editor-Pro.git
cd AI-Video-Editor-Pro
\`\`\`

#### 2. 后端设置（Python）
\`\`\`bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
\`\`\`

#### 3. 前端设置（React）
\`\`\`bash
cd ../frontend
npm install
\`\`\`

#### 4. 启动项目
\`\`\`bash
# 启动后端服务（终端 1）
cd backend
python main.py

# 启动前端（终端 2）
cd frontend
npm start
\`\`\`

访问 http://localhost:3000 开始使用！

## 📖 使用指南

### 基础工作流

1. **导入媒体**
   - 点击"导入"按钮上传视频、音频或图片
   - 支持批量上传多个文件

2. **创建项目**
   - 点击"新建项目"，选择分辨率和帧率
   - 推荐：1080p@30fps（速度快、质量好）

3. **编辑视频**
   - 将媒体拖到时间线中
   - 使用鼠标调整长度、位置
   - 添加转场、特效、字幕

4. **AI 功能**
   - 选择视频→右键→"生成字幕"（自动识别音频）
   - 选择字幕→"翻译"（自动翻译到其他语言）
   - 选择视频→"场景检测"（自动分镜）

5. **导出视频**
   - 点击"导出"
   - 选择格式、分辨率、质量
   - 点击"开始渲染"（后台处理）

## 🛠️ 技术栈

| 组件 | 技术 | 说明 |
|------|------|------|
| 前端 | React 18 + TypeScript | 现代化 Web UI |
| 后端 | Python FastAPI | 高性能异步 API |
| 视频处理 | FFmpeg | 专业级视频编码 |
| 音频处理 | librosa + scipy | 音频分析和处理 |
| AI 字幕 | OpenAI Whisper | 语音识别和转录 |
| 场景检测 | OpenCV | 计算机视觉处理 |
| 数据库 | SQLite/PostgreSQL | 项目和配置存储 |
| 部署 | Docker | 容器化部署 |

## 📁 项目结构

\`\`\`
AI-Video-Editor-Pro/
├── backend/                    # 后端服务
│   ├── app/
│   │   ├── main.py            # 主应用入口
│   │   ├── api/               # API 路由
│   │   │   ├── video.py       # 视频处理 API
│   │   │   ├── audio.py       # 音频处理 API
│   │   │   ├── subtitle.py    # 字幕处理 API
│   │   │   └── render.py      # 渲染 API
│   │   ├── services/          # 业务逻辑
│   │   │   ├── video_service.py
│   │   │   ├── audio_service.py
│   │   │   ├── subtitle_service.py
│   │   │   └── ai_service.py
│   │   ├── models/            # 数据模型
│   │   └── utils/             # 工具函数
│   ├── requirements.txt        # Python 依赖
│   └── config.py              # 配置文件
├── frontend/                  # 前端应用
│   ├── src/
│   │   ├── components/        # React 组件
│   │   │   ├── Timeline/      # 时间线编辑器
│   │   │   ├── MediaPanel/    # 媒体面板
│   │   │   ├── PropertyPanel/ # 属性面板
│   │   │   └── Preview/       # 预览窗口
│   │   ├── pages/             # 页面
│   │   ├── services/          # API 服务
│   │   ├── store/             # 状态管理
│   │   └── App.tsx            # 主应用
│   ├── package.json
│   └── tsconfig.json
├── docs/                      # 文档
├── docker-compose.yml         # Docker 编排
└── README.md
\`\`\`

## 🎓 详细文档

- [安装指南](docs/INSTALLATION.md)
- [使用教程](docs/TUTORIAL.md)
- [API 文档](docs/API.md)
- [扩展开发](docs/DEVELOPMENT.md)
- [性能优化](docs/PERFORMANCE.md)
- [故障排除](docs/TROUBLESHOOTING.md)

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (\`git checkout -b feature/AmazingFeature\`)
3. 提交更改 (\`git commit -m 'Add some AmazingFeature'\`)
4. 推送到分支 (\`git push origin feature/AmazingFeature\`)
5. 开启 Pull Request

## 📝 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 💬 社区和支持

- 📧 邮件：support@aivideoeditor.com
- 💬 讨论区：[GitHub Discussions](https://github.com/jackwoo1218-web/AI-Video-Editor-Pro/discussions)
- 🐛 报告问题：[GitHub Issues](https://github.com/jackwoo1218-web/AI-Video-Editor-Pro/issues)

## 🙏 致谢

感谢以下开源项目的支持：
- [FFmpeg](https://ffmpeg.org/)
- [OpenAI Whisper](https://github.com/openai/whisper)
- [OpenCV](https://opencv.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [React](https://react.dev/)

---

**最后更新**：2025 年 9 月
**版本**：1.0.0-beta
