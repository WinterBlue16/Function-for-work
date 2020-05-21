# 특정 column의 단어들로 행을 분류, 엑셀 파일로 저장할 수 있다
import pandas as pd

# column 단어 리스트
# 해당 column값이 '태그 1', '태그 2', '태그 3'인 것들을 찾아 같은 것끼리 묶고, 태그명.xlsx로 저장
tag_list = ['태그 1', '태그 2', '태그 3']

def seperate_data(dataframe, column, tag):
    data = dataframe[dataframe[column] == tag]
    data.to_excel('{}.xlsx'.format(tag)) # tag 이름으로 저장됨
