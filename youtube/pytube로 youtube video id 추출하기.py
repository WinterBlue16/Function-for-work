"""
youtube 영상 데이터를 다룰 때 유용한 고유값으로 video id가 있습니다. 
통상적으로 video id는 url 가장 끝의 11자리이지만(watch 뒤), youtube url은 패턴이 한두 가지가 아니라
단순한 인덱싱만으로는 video id를 추출하기 힘듭니다.

이 때 유용한 라이브러리가 바로 pytube입니다.  
먼저 pip install pytube를 통해 pytube를 설치해주세요.
"""
from pytube import extract


def get_video_id(url):
    """
    youtube url 패턴은 아래와 같습니다.
    url1='http://youtu.be/SA2iWivDJiE'
    url2='http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu'
    url3='http://www.youtube.com/embed/SA2iWivDJiE'
    url4='http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US'
    url5='https://www.youtube.com/watch?v=rTHlyTphWP0&index=6&list=PLjeDyYvG6-40qawYNR4juzvSOg-ezZ2a6'
    url6='youtube.com/watch?v=_lOT2p_FCvA'
    url7='youtu.be/watch?v=_lOT2p_FCvA'
    url8='https://www.youtube.com/watch?time_continue=9&v=n0g-Y0oo5Qs&feature=emb_logo'

    위의 패턴들은 모두 pytube를 통해 video id를 추출할 수 있습니다.
    """
    video_id = extract.video_id(url)
    return video_id
