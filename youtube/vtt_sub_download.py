"""
youtube_dl 라이브러리를 통해 자막 파일(vtt)를 다운로드합니다. 
사전적으로 youtube_dl이 설치되어 있어야 합니다!
"""
import youtube_dl


def download_youtube_sub(youtube_url, vtt_path):
    video_id = youtube_url[-11:]
    ydl_opts = {
        'outtmpl': vtt_path + 'sub_{}'.format(video_id),
        'forceduration': True,
        'subtitleslangs': ['en'],
        'allsubtitles': True,
        'skipdownload': False
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        dict_meta = ydl.download([youtube_url, vtt_path])
