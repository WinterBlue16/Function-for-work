import re
import docx


# 파일명에서 데이터를 분리하는 함수(title, episode range etc) 외에는 class에 함수를 포함시킨다
# class WebNovel은 전체 문서를 대상으로 하고, episode별 문서의 경우 이를 상속하는 별도 class로 분리
class WebNovel:
    def __init__(self, title, episode_number, text):
        self.title = title
        self.episode_number = episode_number
        self.text = text

    def get_title(self):
        return self.title

    def get_episode_number(self):
        return self.episode_number

    def get_text(self):
        return self.text

    def set_title(self, title):
        self.title = title

    def set_episode_number(self, episode_number):
        self.episode_number = episode_number

    def set_text(self, text):
        self.text = text

    def sperate_episode(text: list):
        slice_idx_list = []

    def sperate_episode(text: list):
        slice_idx_list = []

        for t in text:
            episode_title_pattern = r"\(\d\d\)"
            if re.search(episode_title_pattern, t):
                slice_idx_list.append(text.index(t))

        print("분리할 index 목록:", slice_idx_list)

        save_episodes_docx(text, slice_idx_list)

    def extract_title(self, text: list):
        all_title_list = []

        for t in text:
            episode_title_pattern = r"\(\d\d\)"
            if re.search(episode_title_pattern, t):
                # TODO: 후방탐색 추가
                all_title_list.append(t)

        # TODO: 에피소드 번호 추출해서 dict로 ex) [{episode_number : title}, {episode_number2: title}...]

        print("title 목록 :", all_title_list)

        return all_title_list

    def extract_episode_number(self, text: list):
        all_episode_number_list = []

        for t in text:
            episode_title_pattern = r"\(\d\d\)"
            if re.search(episode_title_pattern, t):
                # TODO: 후방탐색 추가
                all_episode_number_list.append(t)

        # do something
        return

    def get_episode_info_dict():
        return


def save_episodes_docx(text: list, idices: list):

    for i in range(len(idices)):
        if i + 1 == len(idices):
            last_episode = text[idices[i] :]
            last_episode = "\n".join(last_episode)

            # save docx
            doc = docx.Document()
            doc.add_paragraph(last_episode)
            # doc.save("text_{}.docx".format(i))  # title, episode number 추출 필요

        else:
            one_episode = text[idices[i] : idices[i + 1]]
            one_episode = "\n".join(one_episode)

            # save docx
            doc = docx.Document()
            doc.add_paragraph(one_episode)
            # doc.save("text_{}.docx".format(i))


def seperate_episode(text: list):
    slice_idx_list = []

    # 1. 정규표현식 적용
    for t in text:
        episode_title_pattern = r"\(\d\d\)"  # 개선 필요
        if re.search(episode_title_pattern, t):
            slice_idx_list.append(text.index(t))

    print("분리할 index 목록:", slice_idx_list)

    save_episodes_docx(text, slice_idx_list)


def extract_docx_text(path: str):
    doc = docx.Document(path)
    full_text = []
    for p in doc.paragraphs:
        if p.text == "":
            full_text.append("\n")
        else:
            full_text.append(p.text)

    # full_text = "\n".join(full_text)
    seperate_episode(full_text)
    return full_text
