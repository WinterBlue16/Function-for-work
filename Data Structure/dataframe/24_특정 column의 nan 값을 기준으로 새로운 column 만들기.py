import pandas as pd
import numpy as np


def create_new_cols_by_specific_cols_nan(df, cols_name, new_cols_name):
    """
    특정 column의 값이 nan일 경우/nan이 아닐 경우를 기준으로 새로운 column을 생성합니다. 

    df = 전체 데이터프레임
    cols_name = 기준이 되는 column 명
    new_cols_name = 새롭게 생성될 column 명
    """
    df[new_cols_name] = np.where(df[cols_name].notna(), 1, 0)
    return df
