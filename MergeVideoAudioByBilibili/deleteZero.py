import os


def remove_first_n_bytes(file_path, n):
    """
    删除文件的前 n 个字节
    :param file_path: 文件路径
    :param n: 要删除的字节数
    """
    try:
        # 读取文件内容
        with open(file_path, 'rb') as file:
            content = file.read()

        # 删除前 n 个字节
        modified_content = content[n:]

        # 将修改后的内容写回文件
        with open(file_path, 'wb') as file:
            file.write(modified_content)

        print(f"已处理文件: {file_path}")
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {e}")


def process_pre_directory(directory, n):
    """
    遍历指定目录下的所有文件，并删除每个文件的前 n 个字节
    :param directory: 目录路径
    :param n: 要删除的字节数
    """
    if not os.path.exists(directory):
        print(f"目录 {directory} 不存在")
        return

    # 遍历目录下的所有文件
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # 确保是文件而不是目录
        if os.path.isfile(file_path):
            remove_first_n_bytes(file_path, n)


def delete_zeros():
    pre_directory = os.path.join(os.getcwd(), "pre")
    process_pre_directory(pre_directory, 9)