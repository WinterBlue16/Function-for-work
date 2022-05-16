
class Person:
    def __init__(self) -> None:
        self.name = 'winter'
        self.job = 'developer'
        self.favorite = 'blue'
        
person = Person()

# get attribute
print(getattr(person, 'job'))

# set attribute
print(setattr(person, 'job', 'engineer'))
print(person.job)
