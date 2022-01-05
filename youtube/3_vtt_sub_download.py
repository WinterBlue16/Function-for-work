"""
youtube_dl 라이브러리를 통해 자막 파일(vtt)를 다운로드합니다. 
사전적으로 youtube_dl이 설치되어 있어야 합니다!
"""
import youtube_dl


def download_youtube_sub(youtube_url, vtt_path):
    video_id = youtube_url[-11:]
    ydl_opts = {
        'outtmpl': vtt_path + 'sub_{}'.format(video_id),  # 자막 파일을 저장할 로컬 경로
        'subtitleslangs': ['en'],  # 영상에 수록된 자막에서 원하는 언어의 자막만 다운로드 가능
        'writesubtitles': True,
        # 'allsubtitles': True, # 해당 동영상에서 다운로드 가능한 모든 언어의 자막을 다운로드함
        'skipdownload': True
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        dict_meta = ydl.download([youtube_url, vtt_path])
