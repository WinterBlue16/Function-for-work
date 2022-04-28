import subprocess

url = 'https://www.youtube.com/watch?v=Tl2W-N7zhbA'
p = subprocess.Popen('yt-dlp {}'.format(url),
                     stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
print('동영상 다운로드가 완료되었습니다!')
