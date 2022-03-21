class Person:
    def __init__(self):
        self._name = 'John'
        self._age = 34
        self._country = 'England'

    @property
    def name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    def set_age(self, value):
        self._age = value

    @property
    def country(self):
        return self._country

    def set_country(self, value):
        self._country = value


person = Person()

person.set_name('Jane')
person.set_age(14)
person.set_country('USA')

print(person.name)
print(person.age)
print(person.country)
