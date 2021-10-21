"""
youtube 영상 데이터를 다룰 때 유용한 고유값으로 video id가 있습니다. 
통상적으로 video id는 url 가장 끝의 11자리이지만(watch 뒤), youtube url은 패턴이 한두 가지가 아니라
단순한 인덱싱만으로는 video id를 추출하기 힘듭니다.

이 때 유용한 라이브러리가 바로 pytube입니다.  
먼저 pip install pytube를 통해 pytube를 설치해주세요.
"""
from pytube import extract


def get_video_id(url):
    video_id = extract.video_id(url)
    return video_id
