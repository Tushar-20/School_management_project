from School import School,Classroom,Subject
from Persons import Student,Teacher
def main():
    school=School('Adamjee Cant','Dhaka')
    eight=Classroom('eight')
    school.add_classroom(eight)
    nine=Classroom('nine')
    school.add_classroom(nine)
    ten=Classroom('ten')
    school.add_classroom(ten)

    
    tanoy=Student('Tanay',eight)
    school.student_admission(tanoy)
    janoy=Student('Janay',eight)
    school.student_admission(janoy)
    panoy=Student('Panay',eight)
    school.student_admission(panoy)
    
    physics_teacher=Teacher('Imrul Kayees')
    physics=Subject('physics',physics_teacher)
    eight.add_subject(physics)
    
    chemistry_teacher=Teacher('Momen Sir')
    chemistry=Subject('chemistry',chemistry_teacher)
    eight.add_subject(chemistry)

    Biology_teacher=Teacher('Ajmol Sir')
    Biology=Subject('Biology',Biology_teacher)
    eight.add_subject(Biology)

    Higher_math_teacher=Teacher('Mokul Sir')
    Higher_math=Subject('Higher_math',Higher_math_teacher)
    eight.add_subject(Higher_math)
    
    eight.take_semester_final()

    print(school)
if __name__ == '__main__':
    main()