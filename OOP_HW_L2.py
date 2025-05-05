from functools import total_ordering


@total_ordering
class Student:
    """
    Класс описывает студента Нетологии, внутри хранится информация по завершенным курсам, 
    курсам, которые в процессе изучения, а так же оценки
    Этот класс может выставлять оценки лекторам
    """
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grades_list = []
 
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
 
    def medium_grades(self):
        for grade in self.grades.values():
            self.grades_list.append(sum(grade)/len(grade))
        return round((sum(self.grades_list)/len(self.grades_list)), 1)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.medium_grades()} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}' 

    def __eq__(self, other):
        return self.medium_grades() == other.medium_grades()

    def __lt__(self, other):
        return self.medium_grades() < other.medium_grades()

     
class Mentor:
    """
    Класс Ментор, является родительским для Lecturer и Reviewer
    """
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
 

@total_ordering
class Lecturer(Mentor):
    """
    Класс лекторы, получает оценки от класса Students
    Умеет выводить на экран информацию об оценках от студентов
    """
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_from_students = {}
        self.grades_list = []

    def show_grades(self):
        print(f'У лектора {self.name} {self.surname} выставлены следующие оценки: \n{self.grades_from_students}')

    def medium_grades(self):
        for grades in self.grades_from_students.values():
            self.grades_list.append(sum(grades)/len(grades))
        return round((sum(self.grades_list)/len(self.grades_list)), 1)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции - {self.medium_grades()}'

    def __eq__(self, other):
        return self.medium_grades() == other.medium_grades()

    def __lt__(self, other):
        return self.medium_grades() < other.medium_grades()
    

class Reviewer(Mentor):
    """
    Класс Эксперты, выставляют оценки студентам за домашнюю работу
    """
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'
    




