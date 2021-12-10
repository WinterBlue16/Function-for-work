import os


def rename_dir(dir_path, new_path):
    os.rename(dir_path, new_path)
    print('파일명 변경이 완료되었습니다.')
    return new_path
