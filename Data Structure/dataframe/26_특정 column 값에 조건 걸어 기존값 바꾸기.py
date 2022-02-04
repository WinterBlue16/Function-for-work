import pandas as pd


def change_df_values_by_condition(df, condition_col_name, change_col_name):
    """
    특정 column의 값에 따라 조건을 주어 기존 값을 변경할 수 있습니다.
    하지만 조건에 따라 값이 다르게 들어갈 때는 사용할 수 없습니다.
    """
    df.loc[df[condition_col_name] "조건 넣기", change_col_name] = "바꿀 값"
    return df


def change_df_value_by_another_column(df, another_col_name, change_col_name, sample_list):
    """
    특정 리스트, 데이터프레임 안의 column에 조건을 주어 특정 column의 값을 변경할 수 있습니다.
    """
    for i in df.change_col_name:
        try:
            df.loc[df[another_col_name] == i, change_col_name] = sample_list[i]
        except KeyError:
            print('조건에 맞는 값이 존재하지 않습니다.')
