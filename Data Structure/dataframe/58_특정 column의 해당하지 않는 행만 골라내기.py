import pandas as pd


def extract_row_by_condition(df, condition_col_name, idx_list):
    """[summary]
    idx_list에 포함된 값이 row에 들어있을 경우 그 row들만 제외한다.

    Args:
        df ([dataframe]): 원래 데이터프레임
        condition_col_name ([series]): 조건을 걸 column 이름
        idx_list ([list]): 조건으로 걸 항목들을 담은 리스트. 이름은 변경 가능

    Returns:
        [dataframe]: [조건에 해당하지 않는 행 데이터]
    """
    df = df[~df[condition_col_name].isin(idx_list)]
    return df
