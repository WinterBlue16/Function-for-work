import os
import re


def replace_dir_path(dir_path):
    """copy한 디렉토리 경로 중 역슬래시(\)를 슬래시(/)로 변경

    Args:
        dir_path ([string]): 변경할 디렉토리 경로

    Returns:
        string: 변경 완료된 경로
    """
    print(dir_path)
    return dir_path.replace("\\", "/")


def reset_idx_in_dir(dir_path):
    """주어진 디렉토리 안에 있는 모든 파일명에 포함된 번호를 초기화하고 재정렬합니다.

    Args:
        dir_path ([string]): 초기화, 재정렬할 파일들이 든 디렉토리의 절대경로
    """
    i = 1
    for file_name in os.listdir(dir_path):
        if file_name.endswith('py') or file_name.endswith('ipynb'):
            base_file_name = file_name[file_name.index('_'):]
            # 반드시 경로 추가
            os.rename(dir_path+'/'+file_name, dir_path +
                      '/'+str(i)+base_file_name)
            i += 1


def set_idx_in_dir(dir_path):
    """주어진 디렉토리 경로의 모든 하위 파일들에 번호를 매깁니다. 
       중간에 번호가 붙은 파일이 있더라도 해당 파일의 번호를 초기화한 후 다시 번호를 매깁니다.

    Args:
        dir_path ([string]): 넘버링을 할 파일들이 소속된 디렉토리 절대 경로
    """
    file_list = os.listdir(dir_path)
    for file_name in file_list:
        # file의 첫글자가 숫자가 아닌 경우
        try:
            int(file_name[0])
            # 기본적으로 번호를 매길 때 숫자 뒤에 '_'가 포함되었다는 전제 있음
            base_file_name = file_name[file_name.index('_'):]
            os.rename(dir_path+'/'+file_name, dir_path+'/'+base_file_name)
        except ValueError:
            continue

    new_file_list = os.listdir(dir_path)
    i = 1
    for file_name in new_file_list:
        os.rename(dir_path+'/'+file_name, dir_path+'/'+str(i)+'_'+file_name)
        i += 1


# sample_path = replace_dir_path(r'파일경로') # r을 붙이지 않을 경우 SyntaxError 발생
# set_idx_in_dir(sample_path)
