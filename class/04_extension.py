class User:
    def __init__(self, name, age, company):
        self._name = name
        self._age = age
        self._company = company

    def call_name(self):
        return "{} 씨, 잠시 괜찮으십니까?".format(self._name)


class Developer(User):  # class extension
    def __init__(self, name, age, company, language):  # add attribute 'language'
        self._language = language
        super().__init__(name, age, company)

    def call_name(self):
        return super().call_name()


developer = Developer("Tina", 40, "Shazam", "swift")
print(developer._name)
print(developer._age)
print(developer._company)
print(developer._language)
print(developer.call_name())
