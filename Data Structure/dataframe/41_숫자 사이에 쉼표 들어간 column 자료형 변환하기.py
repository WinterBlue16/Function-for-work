# 데이터프레임 내 column들 중 숫자 사이에 ,(쉼표)가 있어 단순히 astype으로는 자료형 변환이 되지 않는 경우가 있다.
# 그런 column을 한 번에 int로 바꿀 수 있는 코드를 알아본다.

def object_to_int(column):
    column = column.str.replace(',', '').astype('int')
    return column
