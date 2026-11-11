# 教编签 - 课程材料检查助手

## 产品简介

教编签是面向各学科任课教师的课程材料检验工具。在教师上传课程大纲、教学进程等材料前，自动检查课时、权重和配置中的冲突，所有问题都有溯源证据。

## 环境要求

- Python 3.8+
- Node.js 16+
- Windows/macOS/Linux

## 快速开始

### 1. 后端配置

```bash
# 进入后端目录
cd backend

# 创建虚拟环境（可选但推荐）
python -m venv venv
venv\Scripts\activate  # Windows
# 或
source venv/bin/activate  # macOS/Linux

# 安装依赖
pip install -r requirements.txt

# 启动服务
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

后端将在 `http://127.0.0.1:8000` 运行。

### 2. 前端配置

```bash
# 进入前端目录
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

前端将在 `http://localhost:5173` 运行。

### 3. 使用虚拟示例材料

项目包含两组虚拟示例 DOCX 文件，已生成在 `data/` 目录：

- `虚拟示例_正常组.docx` - 课时一致、权重正确、配置无冲突的示例
- `虚拟示例_问题组.docx` - 包含课时不符、权重不等于100%等问题的示例

在首页的「体验示例」中选择这些文件进行检查。

## 数据保存

- **上传的文件** 临时存放在 `data/uploads/` 目录，检查后自动清理
- **检查结果** 保存在 `data/checks.db` SQLite 数据库中
- **用户数据和凭据不上传** - 所有处理均在本地进行，无网络传输

## 规则模板

当前已实现以下检查规则：

- **R001** - 课程代码、课程名称、学期一致性检查
- **R002** - 课时组成等于总课时检查
- **R003** - 进程中课时计数检查（需进程数据）
- **R004** - 成绩权重总计100%检查

规则配置保存在数据库中，支持添加和编辑。

## 项目结构

```
jiaobiaoqian/
├── backend/              # FastAPI 后端
│   ├── main.py          # 主应用入口
│   ├── models.py        # Pydantic 数据模型
│   ├── docx_parser.py   # DOCX 文件解析
│   ├── rule_engine.py   # 检查规则引擎
│   ├── database.py      # 数据库操作
│   └── requirements.txt  # Python 依赖
├── frontend/            # React/TypeScript 前端
│   ├── src/
│   │   ├── main.tsx
│   │   ├── App.tsx
│   │   └── index.css
│   ├── package.json
│   ├── tsconfig.json
│   └── vite.config.ts
├── data/                # 数据目录
│   ├── uploads/         # 上传文件临时目录
│   ├── checks.db        # 检查结果数据库
│   ├── 虚拟示例_正常组.docx
│   └── 虚拟示例_问题组.docx
└── IMPLEMENTATION_STATUS.md  # 项目进度文档
```

## 已验证的功能

- ✓ 后端 API 启动正常
- ✓ DOCX 文件上传和解析
- ✓ 前端页面展示
- ✓ 虚拟示例文件生成

## 未验证项

- 浏览器端上传和检查流程（需实际浏览器验证）
- 数据库持久化完整性
- 完整的报告导出功能（第二阶段开发）

## 限制与已知问题

- 尚未实现完整的 DOCX 修改和标记功能
- AI 辅助功能默认禁用（需配置 API_KEY）
- 暂不支持 PDF/图片 OCR

## 后续开发

- **第二阶段**：规则模板持久化、报告生成、DOCX 修改功能
- **第三阶段**：完整 UI、错误处理优化、可选 AI 配置、Windows 自启动体验

## 支持

遇到问题？检查：
1. Python/Node 环境是否正确安装
2. 端口 8000（后端）和 5173（前端）是否被占用
3. DOCX 文件是否有效（非损坏的 Word 文档）
