import subprocess
import os
import shutil
import webbrowser


def get_ffmpeg_path():
    """
    获取系统安装的 ffmpeg 路径
    :return: ffmpeg 的路径
    """
    try:
        # 检查系统是否安装了 ffmpeg
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return "ffmpeg"  # 如果系统安装了 ffmpeg，直接返回 "ffmpeg"
    except (subprocess.CalledProcessError, FileNotFoundError):
        # 如果系统未安装 ffmpeg，打开浏览器跳转到下载页面
        print("未找到系统安装的 ffmpeg")
        print("正在跳转到 ffmpeg 下载页面...")
        webbrowser.open("https://ffmpeg.org/download.html")
        raise FileNotFoundError("请下载并安装 ffmpeg")


def m4s2mp4(video_m4s_path, audio_m4s_path, output_mp4_path):
    """
    将 m4s 视频和音频文件合并为 mp4 格式
    :param video_m4s_path: 视频文件路径
    :param audio_m4s_path: 音频文件路径
    :param output_mp4_path: 输出文件路径
    """
    # 检查文件是否存在
    if not os.path.exists(video_m4s_path):
        print(f"视频文件 {video_m4s_path} 不存在")
        return
    if not os.path.exists(audio_m4s_path):
        print(f"音频文件 {audio_m4s_path} 不存在")
        return

    # 获取 ffmpeg 路径
    try:
        ffmpeg_path = get_ffmpeg_path()
    except FileNotFoundError as e:
        print(e)
        return

    # 使用 ffmpeg 将视频和音频合并为 MP4
    command = [
        ffmpeg_path,  # 使用系统的 ffmpeg
        '-i', video_m4s_path,  # 输入视频文件
        '-i', audio_m4s_path,  # 输入音频文件
        '-c:v', 'copy',  # 直接复制视频流
        '-c:a', 'aac',  # 重新编码音频流为 AAC
        '-strict', 'experimental',
        output_mp4_path  # 输出文件
    ]

    try:
        # 执行命令
        subprocess.run(command, check=True)
        print(f"文件已成功合并为: {output_mp4_path}")

        # 合并成功后删除 pre 文件夹中的文件
        delete_pre_files(video_m4s_path, audio_m4s_path)
    except subprocess.CalledProcessError as e:
        print(f"合并失败: {e}")


def delete_pre_files(video_m4s_path, audio_m4s_path):
    """
    删除 pre 文件夹中的视频和音频文件
    :param video_m4s_path: 视频文件路径
    :param audio_m4s_path: 音频文件路径
    """
    try:
        os.remove(video_m4s_path)
        print(f"已删除文件: {video_m4s_path}")
        os.remove(audio_m4s_path)
        print(f"已删除文件: {audio_m4s_path}")
    except Exception as e:
        print(f"删除文件时出错: {e}")


def convert_to_mp4():
    # 文件路径
    video_m4s_path = 'pre/video.m4s'
    audio_m4s_path = 'pre/audio.m4s'
    output_mp4_path = 'result/output.mp4'

    # 确保输出目录存在
    os.makedirs(os.path.dirname(output_mp4_path), exist_ok=True)

    # 调用函数
    m4s2mp4(video_m4s_path, audio_m4s_path, output_mp4_path)


if __name__ == '__main__':
    convert_to_mp4()