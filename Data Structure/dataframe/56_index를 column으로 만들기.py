def created_idx_cols(df):
    """
    dataframe의 index를 하나의 column으로 생성한다.
    """
    df['id'] = df.index
    return df
