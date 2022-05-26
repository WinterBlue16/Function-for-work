import re
import docx


def save_episodes_docx(text: list, idices: list):  # txt로 저장할 것인가, docx로 저장할 것인가?
    for i in range(1, len(idices)):
        if i == len(idices) - 1:
            last_episode = text[idices[i] :]
            print("\n".join(last_episode))
        else:
            one_episode = text[: idices[i]]
            # print("\n".join(one_episode))


def seperate_episode(text: list):
    slice_idx_list = []

    # 1. 정규표현식 적용
    for t in text:
        episode_title_pattern = "^\([0-9][0-9]\)"
        if re.match(episode_title_pattern, t):
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
