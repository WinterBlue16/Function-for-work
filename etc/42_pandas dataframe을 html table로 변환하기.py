# django 등에서 python 코드를 사용할 때, 이미 만들어둔 데이터프레임을 그대로 html 문서에 출력할 수 있다.
# 하이퍼링크가 자동으로 걸리지 않으므로 주의한다

# 라이브러리 불러오기
import pandas as pd

# 데이터프레임 만들기
sample_df = pd.DataFrame(data={'col 1' : ['가', '나', '다', '라'], 'col 2' : ['A', 'B', 'C', 'D']})

# HTML 형식의 table로 변환하기
sample_df = sample_df.to_html()
sample_df = sample_df.to_html(index=False) # index 열 없음
