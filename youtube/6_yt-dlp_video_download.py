import os
import yt_dlp


def yt_dlp_video_download(youtube_url, path):

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
        with yt_dlp.youtubeDL(ydl_opts) as ydl:
            ydl.cache.remove()
            meta_data = ydl.extract_info(youtube_url)
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

# 거의 youtube_dl과 동일하다.
