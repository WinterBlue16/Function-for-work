# 지난번에는 데이터프레임에서 조건에 맞는 행만 추출하는 법을 배웠다.
# 이번에는 행을 추출하거나 삭제하는 것이 아닌, 조건에 맞는 부분만을 찾아내고 그 내용을 원하는 대로 바꾸는 방법을 알아본다.

# 라이브러리 불러오기
import pandas as pd
import itertools

# sample data 만들기
sample_df = pd.DataFrame(data={'positive':['웃음@)', '신남', '감격@)', '희열'], 'neutral':['무덤덤', '지침', '아무 생각 없음', '공허'], 'negative' : ['슬픔', '분노', '역겨움&#', '혐오&#']})
sample_df # 데이터 확인

# 보다시피 데이터프레임 곳곳에 처리해야 할 문자들이 들어있는 것을 볼 수 있다.
# 이를 제거하기 위해서는 replace를 이용한다.

# @) 제거
sample_df['positive'] = sample_df.positive.str.replace("@)", "")

# &# 제거
sample_df['negative'] = sample_df.negative.str.replace("&#", "")

# 지우는 것뿐만 아니라 일부, 혹은 전체 값을 바꾸는 것도 가능하다!
# 분노 => 고통으로 변경
sample_df['negative'] = sample_df.negative.str.replace("분노", "고통")


# 참고 링크 : https://stackoverflow.com/questions/42331992/replace-part-of-the-string-in-pandas-data-frame
