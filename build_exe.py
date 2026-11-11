"""
将 launcher.py 打包成 Windows EXE 文件
使用 PyInstaller
"""
import subprocess
import sys
import os
from pathlib import Path

def build_exe():
    """构建 EXE 文件"""
    project_root = Path(__file__).parent

    # 确保 PyInstaller 已安装
    try:
        import PyInstaller
    except ImportError:
        print("正在安装 PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller", "-q"])

    print("正在构建 EXE 文件...")

    # PyInstaller 命令
    cmd = [
        sys.executable,
        "-m", "PyInstaller",
        "--onefile",  # 单个 EXE 文件
        "--windowed",  # 无控制台窗口
        "--name=教编签",  # 输出名称
        "--distpath=./dist",  # 输出目录
        "--workpath=./build",  # 构建目录
        str(project_root / "launcher.py")
    ]

    try:
        subprocess.check_call(cmd, cwd=str(project_root))
        print("✓ EXE 文件构建成功！")
        print(f"文件位置: {project_root}/dist/教编签.exe")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ 构建失败: {e}")
        return False

if __name__ == "__main__":
    build_exe()
