from pytube import extract, Youtube
import os
import errno


def youtube_downloader(url, output_path):
    """
    Download youtube video using pytube.
    This function can download YOUTUBE ONLY.

    default file type:  mp4
    """
    try:
        yt = Youtube(url)
        title = yt.title
        runtime = yt.length
        print('video_title:', title)
        print('video_duration:', runtime)

        t = yt.streams.filter(only_audio=True)

        if not os.path.exists(os.path.dirname(output_path)):
            try:
                os.makedirs(os.path.dirname(output_path))
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        t[0].download(output_path)
        print('다운로드가 완료되었습니다.')

    except Exception as e:
        print('이 영상을 다운로드할 수 없습니다.')
        return False
