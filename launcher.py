"""
教编签 - GUI 启动器
"""
import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import sys
import os
import time
import threading
from pathlib import Path

class LauncherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("教编签 - 课程材料检查助手")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # 设置样式
        self.root.configure(bg="#f5f5f5")
        style = ttk.Style()
        style.theme_use('clam')

        self.backend_process = None
        self.frontend_process = None
        self.backend_running = False
        self.frontend_running = False

        self.setup_ui()
        self.project_root = Path(__file__).parent

    def setup_ui(self):
        # 标题
        title_frame = tk.Frame(self.root, bg="#1e88e5")
        title_frame.pack(fill=tk.X, padx=0, pady=0)

        title = tk.Label(
            title_frame,
            text="教编签",
            font=("微软雅黑", 24, "bold"),
            bg="#1e88e5",
            fg="white",
            pady=15
        )
        title.pack()

        subtitle = tk.Label(
            title_frame,
            text="课程材料检查助手",
            font=("微软雅黑", 12),
            bg="#1e88e5",
            fg="white",
            pady=5
        )
        subtitle.pack()

        # 内容区域
        content = tk.Frame(self.root, bg="#f5f5f5")
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # 说明
        desc = tk.Label(
            content,
            text="在教师上传材料前，检查课时、权重和配置冲突，所有问题都有溯源证据。",
            font=("微软雅黑", 11),
            bg="#f5f5f5",
            fg="#666",
            wraplength=500,
            justify=tk.LEFT
        )
        desc.pack(pady=(0, 20))

        # 状态显示
        status_frame = tk.LabelFrame(
            content,
            text="服务状态",
            font=("微软雅黑", 10),
            bg="#f5f5f5",
            fg="#333"
        )
        status_frame.pack(fill=tk.X, pady=10)

        backend_frame = tk.Frame(status_frame, bg="#f5f5f5")
        backend_frame.pack(fill=tk.X, padx=10, pady=8)

        self.backend_indicator = tk.Label(
            backend_frame,
            text="●",
            font=("Arial", 12),
            fg="#999",
            bg="#f5f5f5"
        )
        self.backend_indicator.pack(side=tk.LEFT, padx=(0, 10))

        self.backend_label = tk.Label(
            backend_frame,
            text="后端服务 - 未启动",
            font=("微软雅黑", 10),
            bg="#f5f5f5",
            fg="#666"
        )
        self.backend_label.pack(side=tk.LEFT)

        frontend_frame = tk.Frame(status_frame, bg="#f5f5f5")
        frontend_frame.pack(fill=tk.X, padx=10, pady=8)

        self.frontend_indicator = tk.Label(
            frontend_frame,
            text="●",
            font=("Arial", 12),
            fg="#999",
            bg="#f5f5f5"
        )
        self.frontend_indicator.pack(side=tk.LEFT, padx=(0, 10))

        self.frontend_label = tk.Label(
            frontend_frame,
            text="前端服务 - 未启动",
            font=("微软雅黑", 10),
            bg="#f5f5f5",
            fg="#666"
        )
        self.frontend_label.pack(side=tk.LEFT)

        # 按钮区域
        button_frame = tk.Frame(content, bg="#f5f5f5")
        button_frame.pack(fill=tk.X, pady=20)

        self.start_btn = tk.Button(
            button_frame,
            text="启动服务",
            command=self.start_services,
            font=("微软雅黑", 12),
            bg="#43a047",
            fg="white",
            padx=30,
            pady=12,
            border=0,
            cursor="hand2"
        )
        self.start_btn.pack(side=tk.LEFT, padx=10)

        self.open_btn = tk.Button(
            button_frame,
            text="打开应用",
            command=self.open_browser,
            font=("微软雅黑", 12),
            bg="#1e88e5",
            fg="white",
            padx=30,
            pady=12,
            border=0,
            cursor="hand2",
            state=tk.DISABLED
        )
        self.open_btn.pack(side=tk.LEFT, padx=10)

        self.stop_btn = tk.Button(
            button_frame,
            text="停止服务",
            command=self.stop_services,
            font=("微软雅黑", 12),
            bg="#e53935",
            fg="white",
            padx=30,
            pady=12,
            border=0,
            cursor="hand2",
            state=tk.DISABLED
        )
        self.stop_btn.pack(side=tk.LEFT, padx=10)

        # 日志区域
        log_frame = tk.LabelFrame(
            content,
            text="启动日志",
            font=("微软雅黑", 10),
            bg="#f5f5f5",
            fg="#333"
        )
        log_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        scrollbar = tk.Scrollbar(log_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.log_text = tk.Text(
            log_frame,
            height=8,
            font=("Courier", 9),
            bg="#fff",
            fg="#333",
            yscrollcommand=scrollbar.set,
            state=tk.DISABLED
        )
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        scrollbar.config(command=self.log_text.yview)

    def log(self, message):
        """添加日志"""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)
        self.root.update()

    def start_services(self):
        """启动服务"""
        self.start_btn.config(state=tk.DISABLED)
        self.log("正在启动服务...")

        thread = threading.Thread(target=self._start_services_thread)
        thread.daemon = True
        thread.start()

    def _start_services_thread(self):
        """后台线程启动服务"""
        try:
            backend_dir = self.project_root / "backend"
            frontend_dir = self.project_root / "frontend"

            # 启动后端
            self.log("启动后端服务 (http://127.0.0.1:8000)...")
            self.backend_process = subprocess.Popen(
                [sys.executable, "-m", "uvicorn", "main:app", "--reload", "--host", "127.0.0.1", "--port", "8000"],
                cwd=str(backend_dir),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0
            )
            self.log("✓ 后端服务已启动")
            self.backend_running = True
            self.backend_indicator.config(fg="#43a047")
            self.backend_label.config(text="后端服务 - 运行中 (127.0.0.1:8000)")

            time.sleep(2)

            # 启动前端
            self.log("启动前端服务 (http://localhost:5173)...")
            self.frontend_process = subprocess.Popen(
                ["npm", "run", "dev"],
                cwd=str(frontend_dir),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0
            )
            self.log("✓ 前端服务已启动")
            self.frontend_running = True
            self.frontend_indicator.config(fg="#43a047")
            self.frontend_label.config(text="前端服务 - 运行中 (localhost:5173)")

            self.log("\n✓ 所有服务已启动！")
            self.log("准备打开浏览器，请稍候...")

            # 更新按钮状态
            self.root.after(0, self._update_buttons_running)

            time.sleep(3)
            self.root.after(0, self.open_browser)

        except Exception as e:
            self.log(f"✗ 启动失败: {str(e)}")
            self.root.after(0, self._update_buttons_stopped)

    def _update_buttons_running(self):
        self.start_btn.config(state=tk.DISABLED)
        self.open_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.NORMAL)

    def _update_buttons_stopped(self):
        self.start_btn.config(state=tk.NORMAL)
        self.open_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.DISABLED)

    def open_browser(self):
        """打开浏览器"""
        import webbrowser
        self.log("正在打开浏览器...")
        webbrowser.open("http://localhost:5173")
        self.log("✓ 浏览器已打开")

    def stop_services(self):
        """停止服务"""
        self.log("正在停止服务...")

        if self.backend_process:
            self.backend_process.terminate()
            self.backend_process = None
            self.backend_running = False
            self.backend_indicator.config(fg="#999")
            self.backend_label.config(text="后端服务 - 已停止")
            self.log("✓ 后端服务已停止")

        if self.frontend_process:
            self.frontend_process.terminate()
            self.frontend_process = None
            self.frontend_running = False
            self.frontend_indicator.config(fg="#999")
            self.frontend_label.config(text="前端服务 - 已停止")
            self.log("✓ 前端服务已停止")

        self._update_buttons_stopped()
        self.log("所有服务已停止")

    def on_closing(self):
        """关闭应用"""
        if self.backend_running or self.frontend_running:
            if messagebox.askokcancel("确认", "是否停止服务并退出？"):
                self.stop_services()
                self.root.destroy()
        else:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = LauncherApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
