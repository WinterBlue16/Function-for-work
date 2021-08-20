# 새로운 경로에 파일 저장 시 새로운 디렉토리를 두 개 이상 생성해야 할 경우, 에러가 발생한다.
# 이 에러 없이 성공적으로 디렉토리를 생성하고, 파일을 저장한다.

import os
import errno

filename = "/new/file/text1.txt"

if not os.makedirs(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

with open(filename, 'w') as f:
    f.write("This is new text file.")


# python 3.2+
filename = "new/file/text2.txt"

os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as f:
    f.write("This is new text file.")
