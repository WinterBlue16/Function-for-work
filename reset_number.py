import os


def reset_idx_in_dir(dir_path):
    """주어진 디렉토리 안에 있는 모든 파일명에 포함된 번호를 초기화하고 재정렬합니다.

    Args:
        dir_path ([string]): 초기화, 재정렬할 파일들이 든 디렉토리의 절대경로
    """
    i = 1
    for filename in os.listdir(dir_path):
        if filename.endswith('py') or filename.endswith('ipynb'):
            base_file_name = filename[filename.index('_'):]
            # 반드시 경로 추가
            os.rename(dir_path+'/'+filename, dir_path +
                      '/'+str(i)+base_file_name)
            i += 1


# TODO: 번호가 붙어있지 않은 파일들에 번호 붙이는 함수 생성
# reset_idx_in_dir('C:/Users/CUCHO/Function-for-work/Data Structure/tuple')
