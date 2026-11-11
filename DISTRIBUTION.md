# 教编签 - 分发包制作指南

## 已生成文件清单

### ✓ 已完成

| 文件/目录 | 大小 | 状态 |
|----------|------|------|
| `dist/教编签.exe` | 11MB | ✓ 已生成 |
| `launcher.py` | - | ✓ GUI 启动器 |
| `backend/` | - | ✓ 后端代码完整 |
| `frontend/` | - | ✓ 前端代码完整 |
| `data/虚拟示例_正常组.docx` | - | ✓ 已生成 |
| `data/虚拟示例_问题组.docx` | - | ✓ 已生成 |
| 文档 | - | ✓ README + INSTALL + 本文件 |

---

## 分发方式

### 方式一：EXE 可执行文件（最简单）

**包含文件**
```
教编签-v1.0.0/
├── 教编签.exe              # 双击即可运行（需环境）
├── data/
│   ├── 虚拟示例_正常组.docx
│   └── 虚拟示例_问题组.docx
├── INSTALL.md              # 安装说明
└── README.md               # 产品介绍
```

**优点**
- 文件最小（仅 EXE + 文档 + 示例）
- 用户体验最好（双击即运行）
- 占用空间小

**缺点**
- 需要用户已安装 Python 和 Node.js
- 首次启动需要安装依赖

**适用场景**
- 校内分发（已有开发环境）
- 技术人员使用

---

### 方式二：完整源代码包（推荐）

**包含文件**
```
jiaobiaoqian-v1.0.0/
├── dist/
│   └── 教编签.exe
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── docx_parser.py
│   ├── rule_engine.py
│   ├── database.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── index.css
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   └── index.html
├── data/
│   ├── 虚拟示例_正常组.docx
│   └── 虚拟示例_问题组.docx
├── launcher.py
├── build_exe.py
├── generate_demo_docx.py
├── README.md
├── INSTALL.md
├── GETTING_STARTED.md
├── IMPLEMENTATION_STATUS.md
├── .env.example
└── .gitignore
```

**优点**
- 包含所有源代码
- 用户可以自定义修改
- 便于后续维护和升级

**缺点**
- 文件较多（约 500MB 解压后）
- 需要用户手动安装依赖

**适用场景**
- 正式发布版本
- 支持长期使用
- 允许二次开发

---

## 打包步骤

### 生成 ZIP 安装包

**使用 Windows 自带工具**

1. 右键 jiaobiaoqian 文件夹
2. 选择「发送到」→「压缩文件夹」
3. 重命名为 `jiaobiaoqian-v1.0.0.zip`

**使用 7-Zip（推荐）**

```bash
# 需要先安装 7-Zip 或 7z 命令行工具
cd C:\Users\56228
7z a -r jiaobiaoqian-v1.0.0.zip jiaobiaoqian
```

**使用 PowerShell**

```bash
Compress-Archive -Path "C:\Users\56228\jiaobiaoqian" -DestinationPath "jiaobiaoqian-v1.0.0.zip"
```

### 生成 MSI 安装程序（高级）

需要 WiX Toolset，后续阶段支持。

---

## 用户安装流程

### 快速安装（3 步）

1. **解压文件**
   ```bash
   # Windows：右键解压，或用 7-Zip
   # 或命令行：
   Expand-Archive -Path jiaobiaoqian-v1.0.0.zip -DestinationPath .
   ```

2. **进入目录**
   ```bash
   cd jiaobiaoqian
   ```

3. **首次运行（仅需一次）**
   ```bash
   # 安装后端依赖
   cd backend
   pip install -r requirements.txt
   
   # 安装前端依赖
   cd ../frontend
   npm install
   
   # 返回项目根目录
   cd ..
   ```

4. **日常启动**
   ```bash
   python launcher.py
   # 或直接双击
   dist\教编签.exe
   ```

---

## 验收清单

部署前检查：

- [x] EXE 文件能正常启动（11MB）
- [x] 后端依赖完整（FastAPI, Pydantic, python-docx 等）
- [x] 前端依赖完整（React, TypeScript, Vite）
- [x] DOCX 解析器能识别课程信息
- [x] 规则引擎运行正常
- [x] 虚拟示例文件已生成
- [x] 文档完整（README, INSTALL, GETTING_STARTED）
- [x] GUI 启动器可用

待浏览器验证：
- [ ] 前端在 localhost:5173 正常显示
- [ ] 文件上传和识别流程完整
- [ ] 检查结果显示正确

---

## 版本信息

```
教编签 v1.0.0 - MVP 版本
发布日期: 2026-11-11
```

**系统要求**
- Windows 7 SP1 或更新版本
- Python 3.8+
- Node.js 16+
- 2GB 内存

**包含功能**
- DOCX 文件上传和解析
- 课程信息识别（名称、代码、学期、课时）
- 基础检查规则（R001-R004）
- 检查结果展示
- 虚拟示例验证

**不包含功能**（后续版本）
- 报告导出（DOCX/JSON）
- 规则编辑界面
- AI 辅助
- Windows 自启动配置

---

## 分发建议

### 推荐方案

1. **内部测试阶段**
   - 分发源代码包 + INSTALL.md
   - 收集反馈和 Bug 报告

2. **正式发布**
   - 发布完整包（源代码 + EXE）
   - 提供 INSTALL.md 和 README.md
   - 设置反馈渠道

3. **后续版本**
   - 自动更新机制
   - 在线文档
   - 社区支持

---

## 上传/分享

### GitHub（开源）
```bash
git init
git add .
git commit -m "初始版本 v1.0.0"
git remote add origin https://github.com/your-repo/jiaobiaoqian.git
git push -u origin main
```

### 校内分享
- 通过网盘（百度网盘、OneDrive 等）
- 上传到教务系统
- Email 直接分享

### 商业分发
- 打包成 MSI 安装程序
- 获取数字签名证书
- 提交到软件分发平台

---

## 后续维护

### 常见更新

1. **bug 修复**
   - 更新 launcher.py 或 backend/ 文件
   - 用户仅需重新安装依赖

2. **功能升级**
   - 第二阶段：报告导出、规则编辑
   - 第三阶段：完整 UI、AI 助手

3. **兼容性**
   - 定期测试新的 Python/Node.js 版本
   - 测试 Windows 新版本

---

## 技术支持

如遇到问题，用户可：
1. 查看 INSTALL.md
2. 运行 `python launcher.py` 查看错误日志
3. 检查是否安装了 Python 和 Node.js
4. 尝试卸载后重新安装依赖
