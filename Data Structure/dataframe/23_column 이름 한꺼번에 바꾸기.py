def rename_one_cols_name(df, cols_old_name, cols_new_name):
    """
    dataframe의 column 명을 변경합니다.(단수)
    """
    df.rename(columns={cols_old_name: cols_new_name}, inplace=True)
    return df


def rename_multiple_cols_name(df, cols_old_name_list, cols_new_name_list):
    """
    dataframe의 column 명을 변경합니다.(복수)
    """
    length = len(cols_old_name_list)

    for i in range(length):
        df.rename(
            columns={cols_old_name_list[i]: cols_new_name_list[i]}, inplace=True)
    return df


# one line(rename multiple cols name)
df.rename(columns={old_cols_name1: new_cols_name1, old_cols_name2: new_cols_name2, ..., inplace=True})
