class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def making_grade_lecturer(self, grade, lector, course):
        if grade < 0 or grade > 10:
            print("Оценки выставляются в диапазоне от 0 до 10")
            return
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades_from_students:
                lector.grades_from_students[course] += [grade]
                print('Оценка выставлена')
            else:
                lector.grades_from_students[course] = [grade]
                print('Оценка выставлена')
        else:
            return 'Здесь какая-то ошибка'
 
     
class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
 

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_from_students = {}

    def show_grades(self):
        print(f'У лектора {self.name} {self.surname} выставлены следующие оценки: \n{self.grades_from_students}')


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().init(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


stud = Student('Alex', 'Gruzdev', 'M')
lect = Lecturer('Timur', 'Anvartdinov')
stud.courses_in_progress.append('python')
lect.courses_attached.append('python')
stud.making_grade_lecturer(10, lect, 'python')
stud.making_grade_lecturer(10, lect, 'python')
stud.making_grade_lecturer(8, lect, 'python')
lect.show_grades()