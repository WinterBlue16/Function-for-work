"""
자막 파일(vtt)를 전체 스크립트(txt)로 변환합니다. 
사전적으로 webvtt가 설치되어 있어야 합니다.
"""
import webvtt
from datetime import datetime


def vtt_to_transcript(file_path):
    text_list = []
    now = datetime.now()
    file_name = now.strftime("%H%M%S")

    for caption in webvtt.read(file_path):
        caption_text = caption.text
        text_list.append(caption_text)

    txt_file = open('transcript' + file_name + ".txt", "w")
    for l in text_list:
        txt_file.write(l+"\n")

    txt_file.close()
