# 教编签 - 软件打包和安装指南

## 方式一：使用 GUI 启动器（推荐）

### 前置准备
- 已安装 Python 3.8+
- 已安装 Node.js 16+
- 已安装项目依赖（见下文）

### 安装依赖

**1. 安装后端依赖**
```bash
cd backend
pip install -r requirements.txt
```

**2. 安装前端依赖**
```bash
cd frontend
npm install
```

### 启动应用

**方式 A：直接运行 launcher.py**
```bash
python launcher.py
```

会弹出 GUI 窗口，点击「启动服务」即可。

**方式 B：生成 EXE 文件（一键启动）**
```bash
python build_exe.py
```

生成的 `dist/教编签.exe` 可以直接双击运行，无需任何其他步骤。

---

## 方式二：打包成完整安装包

### 创建便携式包（推荐用于分发）

```bash
# 1. 准备目录
mkdir jiaobiaoqian-portable
cd jiaobiaoqian-portable

# 2. 复制项目文件
xcopy ..\jiaobiaoqian .\* /E /I /Y

# 3. 打包成 ZIP
# 使用 Windows 自带工具或 7-Zip 压缩

# 结构应该是：
# jiaobiaoqian-portable/
# ├── backend/
# ├── frontend/
# ├── data/
# ├── launcher.py
# ├── build_exe.py
# ├── README.md
# └── ... 其他文件
```

### 用户安装步骤

1. **解压文件**
   - 下载 `jiaobiaoqian-portable.zip`
   - 解压到任意目录（如 `C:\Program Files\jiaobiaoqian`）

2. **安装依赖（首次使用）**
   ```bash
   cd backend
   pip install -r requirements.txt
   
   cd ../frontend
   npm install
   ```

3. **启动应用**
   ```bash
   python launcher.py
   ```
   或直接生成 EXE 后双击运行。

---

## 方式三：编译成单个 EXE（完全独立）

### 要求
- 需要所有依赖的 Python wheel 文件
- 需要 Node 和 npm 路径信息

### 步骤

1. **安装 PyInstaller**
   ```bash
   pip install pyinstaller
   ```

2. **运行打包脚本**
   ```bash
   python build_exe.py
   ```

3. **获取 EXE**
   - 文件位置：`dist/教编签.exe`
   - 大小：约 50-100MB（取决于依赖）

### 注意
- EXE 文件包含 Python 运行环境和所有依赖
- 但仍需要系统中有 Node.js 和 npm
- 首次运行时会稍微慢一些

---

## 分发建议

### 最简单方案：直接分发源代码 + 说明

**包含文件**
```
jiaobiaoqian/
├── README.md（中文使用说明）
├── GETTING_STARTED.md（快速开始）
├── launcher.py（GUI 启动器）
├── backend/
├── frontend/
├── data/（虚拟示例 DOCX）
└── requirements.txt
```

**用户只需**
1. 解压
2. 安装 Python 和 Node.js
3. 运行 `python launcher.py`

### 高端方案：Electron 打包（未来）

- 将前端打包成 Electron 应用
- 包含 Python 子进程
- 单个 .exe 完全独立
- 大小 300MB+ 但用户体验最佳

---

## 系统要求

| 组件 | 要求 | 备注 |
|------|------|------|
| 操作系统 | Windows 7+ 或 macOS 10.12+ | 主要测试在 Windows 10/11 |
| Python | 3.8+ | 推荐 3.11+ |
| Node.js | 16+ | npm 7+ |
| 磁盘空间 | 500MB | 包括依赖和数据 |
| 内存 | 2GB+ | 运行后端和前端 |

---

## 常见问题

**Q: 为什么不能直接生成单个 EXE？**
- A: 因为需要 Node.js 运行前端，无法完全打包。但后端可以单独打包。

**Q: 能否在企业内网分发？**
- A: 可以。打包成 ZIP 或 MSI 安装程序，只要用户能访问内网即可。

**Q: 能否添加自启动和快捷方式？**
- A: 可以通过 NSIS 或 MSI 打包工具实现，下一阶段支持。

---

## 版本更新

当有新版本时，用户只需：
1. 下载新的 `launcher.py` 和 `backend/` 文件
2. 重新运行 launcher 即可（前端依赖通常不变）

---

## 反馈和支持

- 遇到问题请检查 README.md 的「常见问题」
- 后端启动失败通常是端口被占用或依赖问题
- 前端白屏通常是需要清理浏览器缓存
