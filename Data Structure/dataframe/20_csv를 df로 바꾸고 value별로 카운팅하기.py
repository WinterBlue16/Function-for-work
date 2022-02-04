"""
해당 코드는 아래의 조건이 충족될 경우에 유용하게 사용할 수 있습니다.

1. 데이터를 구성하는 조사 대상이 한정되어 있을 때(ex. 설문 조사 시 A,B,C,D 네 사람에게만 의견을 물을 때)
2. 조사의 답변 역시 한정되어 있을 때(ex. 답변이 아주 좋음, 좋음, 보통, 나쁨, 매우 나쁨 5가지로 한정될 때) 
"""

import pandas as pd


def caculate_total_score(name, df):
    # 1. 해당 name의 데이터만 필터링
    name_data = df.filter(regex=name)

    # 2. 해당 name의 답변 종류를 나눠 합 구하기
    count_1 = (name_data.values == '답변 종류 1')
    count_2 = (name_data.values == '답변 종류 2')
    count_3 = (name_data.values == '답변 종류 3')
    total_score = (count_1, count_2, count_3)

    return total_score


data = pd.read_csv('통계를 내고 싶은 조사 결과 데이터.csv', sep=',')
caculate_total_score('필터하고 싶은 참여자 name', data)
