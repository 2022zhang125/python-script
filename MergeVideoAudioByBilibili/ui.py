import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil


def upload_audio(root, audio_entry):
    file_path = filedialog.askopenfilename(
        title="选择音频文件",
        filetypes=[("音频文件", "*.m4s")]
    )
    if file_path:
        file_size = os.path.getsize(file_path)  # 获取文件大小
        if file_size > 10 * 1024 * 1024:  # 如果文件大于 10MB，提示用户
            messagebox.showwarning("警告", "选择的文件较大，可能是视频文件，请重新选择！")
            return
        audio_entry.delete(0, tk.END)  # 清空输入框
        audio_entry.insert(0, file_path)  # 显示文件路径


def upload_video(root, video_entry):
    file_path = filedialog.askopenfilename(
        title="选择视频文件",
        filetypes=[("视频文件", "*.m4s")]
    )
    if file_path:
        file_size = os.path.getsize(file_path)  # 获取文件大小
        if file_size < 10 * 1024 * 1024:  # 如果文件小于 10MB，提示用户
            messagebox.showwarning("警告", "选择的文件较小，可能是音频文件，请重新选择！")
            return
        video_entry.delete(0, tk.END)  # 清空输入框
        video_entry.insert(0, file_path)  # 显示文件路径


def delete_audio(audio_entry):
    audio_entry.delete(0, tk.END)  # 清空音频文件路径


def delete_video(video_entry):
    video_entry.delete(0, tk.END)  # 清空视频文件路径


def confirm(root, audio_entry, video_entry):
    audio_file = audio_entry.get()
    video_file = video_entry.get()

    if audio_file and video_file:
        # 确保 pre 文件夹存在
        pre_dir = os.path.join(os.getcwd(), "pre")
        if not os.path.exists(pre_dir):
            os.makedirs(pre_dir)

        # 保存音频文件并重命名
        audio_dest = os.path.join(pre_dir, "audio.m4s")
        try:
            shutil.copy(audio_file, audio_dest)
            print(f"音频文件已保存为: {audio_dest}")
        except Exception as e:
            messagebox.showerror("错误", f"音频文件保存失败: {e}")
            return

        # 保存视频文件并重命名
        video_dest = os.path.join(pre_dir, "video.m4s")
        try:
            shutil.copy(video_file, video_dest)
            print(f"视频文件已保存为: {video_dest}")
        except Exception as e:
            messagebox.showerror("错误", f"视频文件保存失败: {e}")
            return

        messagebox.showinfo("成功", "文件已成功上传并重命名！")
        root.destroy()  # 关闭 GUI 界面
    else:
        messagebox.showwarning("警告", "请先选择音频和视频文件！")


def close(root):
    root.destroy()


def show_ui():
    # 创建主窗口
    root = tk.Tk()
    root.title("文件上传界面")
    root.geometry("500x350")

    # 提示标签
    tip_label = tk.Label(root, text="提示：小的是音频文件（通常小于10MB），大的是视频文件（通常大于10MB）", fg="blue")
    tip_label.pack(pady=10)

    # 音频上传部分
    audio_frame = tk.Frame(root)
    audio_frame.pack(pady=10)

    audio_entry = tk.Entry(audio_frame, width=40)
    audio_entry.pack(side=tk.LEFT, padx=5)

    audio_button = tk.Button(audio_frame, text="上传音频", command=lambda: upload_audio(root, audio_entry))
    audio_button.pack(side=tk.LEFT, padx=5)

    audio_delete_button = tk.Button(audio_frame, text="删除", command=lambda: delete_audio(audio_entry))
    audio_delete_button.pack(side=tk.LEFT, padx=5)

    # 视频上传部分
    video_frame = tk.Frame(root)
    video_frame.pack(pady=10)

    video_entry = tk.Entry(video_frame, width=40)
    video_entry.pack(side=tk.LEFT, padx=5)

    video_button = tk.Button(video_frame, text="上传视频", command=lambda: upload_video(root, video_entry))
    video_button.pack(side=tk.LEFT, padx=5)

    video_delete_button = tk.Button(video_frame, text="删除", command=lambda: delete_video(video_entry))
    video_delete_button.pack(side=tk.LEFT, padx=5)

    # 确认和关闭按钮
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    confirm_button = tk.Button(button_frame, text="确认", command=lambda: confirm(root, audio_entry, video_entry))
    confirm_button.pack(side=tk.LEFT, padx=10)

    close_button = tk.Button(button_frame, text="关闭", command=lambda: close(root))
    close_button.pack(side=tk.LEFT, padx=10)

    # 运行主循环
    root.mainloop()


if __name__ == '__main__':
    show_ui()