import pandas as pd


def change_df_values_by_condition(df, condition_col_name, change_col_name):
    """
    특정 column의 값에 따라 조건을 주어 기존 값을 변경할 수 있습니다.
    하지만 조건에 따라 값이 다르게 들어갈 때는 사용할 수 없습니다.
    """
    df.loc[df[condition_col_name] "조건 넣기", change_col_name] = "바꿀 값"
    return df
