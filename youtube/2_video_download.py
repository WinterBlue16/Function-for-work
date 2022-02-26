"""
youtube_dl 라이브러리로 영상만을 다운로드하는 함수입니다. 
사전적으로 youtube_dl이 설치되어 있어야 합니다!
"""
import youtube_dl
import os


def download_youtube_video(youtube_url, path):
    video_id = youtube_url[-11:]
    movie_path = path
    ydl_opts = {'outmpl': movie_path + '{}'.format(video_id)}

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
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
        'progress_hooks': [download_hook],
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


def download_hook(download):
    """
    다운로드 진행 상황에 대한 데이터를 전달합니다.
    """
    if download['status'] == 'finished':
        file_tuple = os.path.split(os.path.abspath(download['filename']))
        print("{}의 다운로드가 완료되었습니다.".format(file_tuple[1]))

    elif download['status'] == 'downloading':
        percentage_info = download['_percent_str']
        download_speed_info = download['_speed_str']
        percentage_info = percentage_info.replace('%', '')
        print('다운로드 진행 중:', percentage_info)
        print('다운로드 속도:', download_speed_info)


# cache를 꾸준히 삭제해주더라도 다운로드하는 파일이 클 경우, 디스크가 full이 되는 이슈가 발생한다.
