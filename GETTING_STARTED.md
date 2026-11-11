# 教编签 - 快速开始指南

## 一键启动（Windows）

### 方式一：分别启动后端和前端

**1. 启动后端服务**
```bash
cd backend
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```
看到以下输出表示成功：
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

**2. 在新终端启动前端**
```bash
cd frontend
npm run dev
```
看到以下输出表示成功：
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:5173/
```

**3. 打开浏览器访问**
- 访问 http://localhost:5173
- 应看到「教编签 - 课程材料检查助手」页面

### 方式二：测试虚拟示例（无浏览器）

```bash
# 在项目根目录运行
cd backend
python -c "
from docx_parser import parse_course_document
from rule_engine import execute_rules
from models import CheckRule, RuleType
import os

normal = os.path.join('..', 'data', '虚拟示例_正常组.docx')
problem = os.path.join('..', 'data', '虚拟示例_问题组.docx')

m_normal = parse_course_document(normal)
rules = [CheckRule(rule_id='R002', rule_type=RuleType.CONSISTENCY, description='课时组成检查')]

print('正常组检查结果:')
results = execute_rules(normal, rules, m_normal)
for r in results:
    print(f'{r.rule_id}: {r.status.value} - {r.message}')
"
```

## 项目文件清单

| 文件/目录 | 说明 | 状态 |
|----------|------|------|
| `backend/main.py` | FastAPI 主应用 | ✓ 可运行 |
| `backend/docx_parser.py` | DOCX 解析器 | ✓ 已验证 |
| `backend/rule_engine.py` | 检查规则引擎 | ✓ 已验证 |
| `backend/models.py` | 数据模型 | ✓ 完整 |
| `backend/database.py` | 数据库操作 | ✓ 完整 |
| `backend/requirements.txt` | Python 依赖 | ✓ 已安装 |
| `frontend/src/App.tsx` | React 主组件 | ✓ 完整 |
| `frontend/package.json` | Node 依赖 | ✓ 已安装 |
| `data/虚拟示例_正常组.docx` | 正常示例 | ✓ 已生成 |
| `data/虚拟示例_问题组.docx` | 问题示例 | ✓ 已生成 |
| `README.md` | 中文说明 | ✓ 完整 |
| `IMPLEMENTATION_STATUS.md` | 项目进度 | ✓ 完整 |

## 虚拟示例说明

### 正常组 - 虚拟示例_正常组.docx
- 课程名称：数据结构与算法
- 课程代码：CS101
- 总课时：48
- 课时组成：理论32 + 实验16 = 48 ✓（一致）
- 成绩权重：30% + 20% + 50% = 100% ✓（正确）

**预期结果**：
- R001: 已认 ✓
- R002: 已认 ✓

### 问题组 - 虚拟示例_问题组.docx
- 课程名称：高等数学
- 课程代码：MATH201
- 总课时：48
- 课时组成：理论32 + 实验12 = 44 ✗（少4学时）
- 成绩权重：40% + 30% + 20% = 90% ✗（缺10%）

**预期结果**：
- R001: 已认 ✓
- R002: 有误 ✗ （提示相差4学时）

## 实际浏览器验证流程

1. **访问首页**
   - 看到「教编签 - 课程材料检查助手」标题
   - 显示一句话说明：「在教师上传材料前，检查课时、权重和配置冲突，所有问题都有溯源证据。」

2. **测试正常组**
   - 点击「上传 DOCX」按钮
   - 选择 `data/虚拟示例_正常组.docx`
   - 应该看到：课程名称「数据结构与算法」、课程代码「CS101」、总课时「48」
   - 点击「开始检查」
   - 在结果表中应看到：R001 和 R002 都为「已认」状态

3. **测试问题组**
   - 重复上传 `data/虚拟示例_问题组.docx`
   - 应该看到：课程名称「高等数学」、课程代码「MATH201」、总课时「48」
   - 点击「开始检查」
   - 在结果表中应看到：R002 为「有误」，消息提示「课时不符：总课时 48，组成总和 44」

## 环境检查

运行以下命令确认环境就绪：

```bash
# 检查 Python
python --version  # 应为 3.8+

# 检查 Node.js
node --version   # 应为 16+
npm --version    # 应为 7+

# 检查依赖
cd backend
python -c "import fastapi, pydantic, docx; print('✓ 后端依赖就绪')"

cd ../frontend
npm list react  # 应显示 react@18.2.0
```

## 常见问题

**Q: 运行后端时出现「Address already in use」**
- A: 端口 8000 被占用，改用其他端口：`uvicorn main:app --port 8001`

**Q: 前端访问 http://localhost:5173 时白屏**
- A: 检查终端输出是否有错误；运行 `npm run dev` 重新启动；清理浏览器缓存

**Q: 上传 DOCX 后没有识别到课程信息**
- A: 确认 DOCX 文件是标准格式，包含「课程名称」、「课程代码」等标签的表格

**Q: 检查结果始终为「待认」**
- A: 这是正常的，表示数据不足以判断；对于虚拟示例应该看到「已认」或「有误」

## 下一步

- 测试自己的课程 DOCX 文件
- 根据需要修改虚拟示例以适应你的学科特色
- 第二阶段将添加规则编辑、报告导出功能
