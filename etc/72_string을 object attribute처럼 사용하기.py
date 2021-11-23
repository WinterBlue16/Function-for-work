# DB의 데이터를 수정, 변경할 때는 바꾸고 싶은 attribute를 지정할 수 있어야 합니다.
# 하지만 이 attribute가 입력값이라 고정되지 않고 바뀌거나, string이라 attribute로 줄 수 없는 상황도 발생합니다.
# 이 때 아래와 같은 함수를 써볼 수 있습니다.

# 1. string을 attribute처럼 사용하여 특정한 데이터를 가져오고 싶을 때(get)
getattr(data_object, 'my_column_name')

# 2. string을 attribute처럼 사용해 데이터를 변경하고 싶을 때(set)
new_data_object = setattr(data_object, 'my_column_name', 'new_value')
new_data_object.save()  # 반드시 저장할 것!
