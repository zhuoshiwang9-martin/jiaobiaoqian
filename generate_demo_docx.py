"""生成虚拟示例 DOCX 文件"""
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from pathlib import Path

def create_normal_group():
    """正常组：课时一致、权重正确、配置无冲突"""
    doc = Document()
    doc.add_heading('课程大纲', 0)

    # 基本信息表
    table = doc.add_table(rows=6, cols=2)
    table.style = 'Light Grid Accent 1'

    cells = table.rows[0].cells
    cells[0].text = '课程名称'
    cells[1].text = '数据结构与算法'

    cells = table.rows[1].cells
    cells[0].text = '课程代码'
    cells[1].text = 'CS101'

    cells = table.rows[2].cells
    cells[0].text = '学期'
    cells[1].text = '第3学期'

    cells = table.rows[3].cells
    cells[0].text = '总课时'
    cells[1].text = '48'

    cells = table.rows[4].cells
    cells[0].text = '课时组成'
    cells[1].text = '理论32学时，实验16学时'

    cells = table.rows[5].cells
    cells[0].text = '课程性质'
    cells[1].text = '必修'

    doc.add_paragraph()
    doc.add_heading('成绩组成', level=1)

    # 成绩构成表
    grade_table = doc.add_table(rows=4, cols=2)
    grade_table.style = 'Light Grid Accent 1'

    cells = grade_table.rows[0].cells
    cells[0].text = '评分项目'
    cells[1].text = '权重'

    cells = grade_table.rows[1].cells
    cells[0].text = '平时作业'
    cells[1].text = '30%'

    cells = grade_table.rows[2].cells
    cells[0].text = '期中考试'
    cells[1].text = '20%'

    cells = grade_table.rows[3].cells
    cells[0].text = '期末考试'
    cells[1].text = '50%'

    Path('data').mkdir(exist_ok=True)
    doc.save('data/虚拟示例_正常组.docx')
    print("✓ 生成正常组示例: data/虚拟示例_正常组.docx")

def create_problem_group():
    """问题组：总课时不符、权重不等于100%、课程代码冲突"""
    doc = Document()
    doc.add_heading('课程大纲', 0)

    # 基本信息表
    table = doc.add_table(rows=6, cols=2)
    table.style = 'Light Grid Accent 1'

    cells = table.rows[0].cells
    cells[0].text = '课程名称'
    cells[1].text = '高等数学'

    cells = table.rows[1].cells
    cells[0].text = '课程代码'
    cells[1].text = 'MATH201'

    cells = table.rows[2].cells
    cells[0].text = '学期'
    cells[1].text = '第1学期'

    cells = table.rows[3].cells
    cells[0].text = '总课时'
    cells[1].text = '48'

    cells = table.rows[4].cells
    cells[0].text = '课时组成'
    cells[1].text = '理论32学时，实验12学时'  # 总和为44，不等于48

    cells = table.rows[5].cells
    cells[0].text = '课程性质'
    cells[1].text = '必修'

    doc.add_paragraph()
    doc.add_heading('成绩组成', level=1)

    # 成绩构成表 - 权重只有90%
    grade_table = doc.add_table(rows=4, cols=2)
    grade_table.style = 'Light Grid Accent 1'

    cells = grade_table.rows[0].cells
    cells[0].text = '评分项目'
    cells[1].text = '权重'

    cells = grade_table.rows[1].cells
    cells[0].text = '平时作业'
    cells[1].text = '40%'

    cells = grade_table.rows[2].cells
    cells[0].text = '期中考试'
    cells[1].text = '30%'

    cells = grade_table.rows[3].cells
    cells[0].text = '期末考试'
    cells[1].text = '20%'  # 总和为90%，不等于100%

    Path('data').mkdir(exist_ok=True)
    doc.save('data/虚拟示例_问题组.docx')
    print("✓ 生成问题组示例: data/虚拟示例_问题组.docx")

if __name__ == '__main__':
    create_normal_group()
    create_problem_group()
