from deleteZero import delete_zeros
from ms42mp4 import convert_to_mp4
from ui import show_ui


def main():
    print("正在上传文件...")
    try:
        # 第一步：用户上传文件
        show_ui()
    except Exception as e:
        print(f"上传文件失败: {e}")
        return
    print("上传文件成功...")

    print("正在删除前导0...")
    try:
        # 第二步：删除前导0，并重命名
        delete_zeros()
    except Exception as e:
        print(f"删除前导0失败: {e}")
        return
    print("删除前导0成功...")

    print("正在合并文件...")
    try:
        # 第三步：合并为一个文件
        convert_to_mp4()
    except Exception as e:
        print(f"合并文件失败: {e}")
        return
    print("合并成功！！！文件在result下")


if __name__ == "__main__":
    main()