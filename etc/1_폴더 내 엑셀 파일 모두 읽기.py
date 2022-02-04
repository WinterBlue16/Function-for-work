import pandas as pd
import numpy as np
import glob

# 만약 excel_files라는 폴더에 들어있는 모든 xlsx 파일을 불러와 하나의 엑셀 파일로 만들고 싶다면
all_data = pd.DataFrame() # 모든 데이터를 합칠 데이터 틀
files = glob.glob('./excel_files/*.xlsx') # excel_files 폴더 내 모든 엑셀 파일

for file in files: # 파일을 하나씩 꺼내어
    data = pd.read_excel(file, index_col=0) # 읽어들인다
    all_data = all_data.append(data, ignore_index=True) #읽어들인 파일을 all_data로 계속 추가한다
