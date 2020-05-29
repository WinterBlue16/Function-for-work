# list 안에서 특정 값이 들어간 item이 있는지 확인하고, 추출하고 싶을 때가 많다.
# list 안을 검색해 필요한 값만 리스트에 추가해 확인한다.

# 샘플 리스트
sample_url_li = ['https://weejw.tistory.com/264', 'https://weejw.tistory.com/263?category=805843', 'https://m.cafe.daum.net/flowlife/RUrO/42?q=D_MCiUSfMukTI0&', 'https://stackoverflow.com/questions/42948160/scraping-with-beautiful-soup-and-python-keyerror-href?rq=1', 'https://twpower.github.io/84-how-to-use-beautiful-soup']

search_keyword = 'tistory'
keyword_url = []


# 정석 검색
for url in sample_url_li:
    if search_keyword in url:
        print('{} 발견!'.format(url))
        keyword_url.append(url)

print(keyword_url)

# 코드 간략화
keyword_url_s = [url for url in sample_url_li if search_keyword in url]
