CURRENT_YEAR = 2023
class Person(): # base class
    def __init__(self, name, year_born) -> None:
        self.name = name
        self.year_born = year_born
    def get_age(self):
        return self.year_born - CURRENT_YEAR
    def __str__(self) -> str:
        return '{} ({})'.format(self.name, self.get_age())

class Student(Person): # derived class
    def __init__(self, name, year_born, ) -> None:
        Person.__init__(self, name, year_born)
        self.knowledge = 0
    def study(self):
        self.knowledge+=1
    def get_age(self): # override the parent class method
        print(Person.get_age(self)) # invoke parent class method on dervied class method
        return self.name

p1 = Person('LOL' , 1998)
s1 = Student("Chic" , 1990)
print(p1.get_age())
print(s1.get_age())