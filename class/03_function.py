from datetime import datetime, date


class User:
    def __init__(self, name, age, company):
        self._name = name
        self._age = age
        self._company = company

    @property
    def name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def set_korean_age(self, birthday: str):
        print("만 나이를 계산합니다.")
        today = date.today()
        birthday = datetime.strptime(str(today.year) + birthday, "%Y%m%d").date()
        if today > birthday:
            print("생일이 지났습니다.")
            self._age = self._age + 1
            return self._age

        print("생일이 아직 지나지 않았습니다.")
        self._age = self._age + 2
        return self._age


user = User("Harry", 26, "Meta")
print(user.set_korean_age("1204"))
