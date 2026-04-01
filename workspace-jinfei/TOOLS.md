# TOOLS.md - 本地笔记

Skill 定义了工具_如何_工作。这个文件是用于_你_的细节 —— 那些对你特定设置的东西。

## 这里放什么

- 相机名称和位置
- SSH 主机和别名
- TTS 首选语音
- 扬声器/房间名称
- 设备昵称
- 任何环境特定的东西

## 项目管理

- 项目统一放在 `C:\1\projects\claw-projects\` 目录下
- 掘金量化：`C:\1\projects\claw-projects\gefly_quant\`
- Brooks 楔形策略：`C:\1\projects\claw-projects\brooks_wedge\`
- 完成后告知项目位置

## Python 环境

- **用 `uv` 而不是 `pip`**
- 安装：`uv pip install xxx`
- 运行：`uv run python <script.py>`
- 创建虚拟环境：`uv venv`
- 创建项目：`uv init`

## Claude Code 使用规范

- 先 `cd` 到项目目录
- 参数：`--permission-mode bypassPermissions --print --bare`
- 长任务加 `--background`
- Claude Code 适合：复杂功能、重构、文件探索类任务
- 不适合：太简单的单行修改（直接 edit 更省）

## 长任务（>1分钟）
- spawn 子 agent，后台跑
- 主动向用户汇报进度

### 改代码规范
- 项目代码 → 自由改
- skill/其他文件 → 先问用户

---

添加任何能帮助你工作的东西。这是你的小炒。
