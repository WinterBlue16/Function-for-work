import pandas as pd


def create_new_raw(dataframe, new_data):
    """데이터프레임에 새로운 행을 생성합니다.

    Args:
        dataframe ([Pandas.DataFrame]): 새로운 행 데이터를 추가할 데이터프레임입니다.
        new_data ([dictionary]): 데이터프레임에 추가할 새로운 행 데이터입니다.

    Returns:
        dataframe : 새롭게 행 데이터가 추가된 데이터프레임입니다.

    조건을 넣어 해당 조건에 맞을 경우에만 새로운 행을 추가하는 것도 가능합니다.
    """
    dataframe = dataframe.append(new_data, ignore_index=True)
    return dataframe
