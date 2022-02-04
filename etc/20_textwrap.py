
# pprint와 같이 깔끔한 출력을 도와주는 textwrap 라이브러리 사용법
from pprint import pprint
import textwrap

text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
example = textwrap.fill(text)
print(example)

# pprint와 비교
pprint(text)  # pprint로 출력된 텍스트는 Nonetype
