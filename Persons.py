import random
class Person:
    def __init__(self,name) -> None:
        self.name=name

class Teacher(Person):
    def __init__(self, name) -> None:
        super().__init__(name)
        
    def teach(self):
        pass
    
    def evaluate_exam(self):
            marks=random.randint(0,100)
            return marks

    def __repr__(self) -> str:
        print(f'{self.name}')

class Student(Person):
    def __init__(self, name,classroom) -> None:
        super().__init__(name)
        self.classroom=classroom
        self.__id=None 
        self.marks ={}
        self.grade=None
        self.subject_grade={}

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,value):
        self.__id=value

        