"""
youtube_dl 라이브러리로 영상만을 다운로드하는 함수입니다. 
사전적으로 youtube_dl이 설치되어 있어야 합니다!
"""
import youtube_dl


def download_youtube_video(youtube_url, path):
    video_id = youtube_url[-11:]
    movie_path = path
    ydl_opts = {'outmpl': movie_path + '{}'.format(video_id)}

    try:
        with.youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
    except:
        print('message : 이 동영상을 다운로드할 수 없습니다.')


def download_video_info(youtube_url, path):
    """
    동영상의 fps, runtime, title 등 정보만을 다운로드합니다.
    """

    ydl_opts = {
        'noplaylist': True,
        'coninue_dl': True,
        'forceduration': True,
        'postgrocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192'
        }]
    }

    try:
        with youtube_dl.youtubeDL(ydl_opts) as ydl:
            ydl.cache.remove()
            meta_data = ydl.extract_info(youtube_url, download=False)
            return meta_data

    except Exception as e:
        return False
