import pandas as pd

# example_json.json이라는 파일을 불러와 읽고 싶을 때
example = pd.read_json('./example_json.json', typ='frame', encoding='utf-8')
