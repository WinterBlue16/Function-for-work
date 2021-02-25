# django 버전 확인하기
# 설치를 했어도 jupyter notebook에서는 버전을 확인할 수 없다.
# cmd 혹은 anaconda prompt에서 확인하는 방법

# c 드라이브로 이동
cd /

# django가 설치된 폴더로 이동
cd work_django

# 가상환경이 설치된 폴더로 이동
cd django_mldl

# 가상환경 켜기
django_env\Script\activate

# django project 폴더로 이동
cd project_1

# 버전 확인
python manage.py --version
