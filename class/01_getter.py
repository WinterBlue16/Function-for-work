class Person:
    def __init__(self):
        self._name = 'John'
        self._age = 34
        self._country = 'England'

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def country(self):
        return self._country


person = Person()

print(person.name)
print(person.age)
print(person.country)
