from configparser import ConfigParser


def read_ini(file_path):
    """ini 파일을 읽습니다.

    Args:
        file_path (string): ini 파일 경로
    """
    config = ConfigParser()
    config.section()
    return config.read(file_path)
    