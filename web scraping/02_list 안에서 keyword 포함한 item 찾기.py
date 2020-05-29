# list 안에서 특정 값이 들어간 item이 있는지 확인하고, 추출하고 싶을 때가 많다.
# list 안을 검색해 필요한 값이 들어있는지 알고 싶을 때 사용한다.

# 샘플 리스트
sample_url_li = ['https://weejw.tistory.com/264', 'https://m.cafe.daum.net/flowlife/RUrO/42?q=D_MCiUSfMukTI0&', 'https://stackoverflow.com/questions/42948160/scraping-with-beautiful-soup-and-python-keyerror-href?rq=1', 'https://twpower.github.io/84-how-to-use-beautiful-soup']

search_keyword = 'github'

# 정석 검색
for url in sample_url_li:
    if search_keyword in url:
        print('{} 발견!'.format(search_keyword))
        print(url)

# 검색 멈추기
for url in sample_url_li:
    if search_keyword in url:
        print('{} 발견!'.format(search_keyword))
        print('{} 을 찾았습니다. 검색을 멈춥니다.'.format(url))
        break;


# 코드 간략화
if any(search_keyword in url for url in sample_url_li):
    print('{} 빠르게 발견!'.format(search_keyword))
    print(url)
