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
 
    def add_finished_courses(self, course_name):
        self.finished_courses.append(course_name)

    def add_courses_in_progress(self, course_name):
        self.courses_in_progress.append(course_name)

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
 
    def _medium_grades(self):
        if len(self.grades) == 0:
            return f'Оценок пока нет!'
        for grade in self.grades.values():
            self.grades_list.append(sum(grade)/len(grade))
        return round((sum(self.grades_list)/len(self.grades_list)), 1)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self._medium_grades()} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}' 

    def __eq__(self, other):
        if len(self.grades) > 0 and len(other.grades) > 0:
            return self._medium_grades() == other._medium_grades()
        else:
            return f'Сравнить нельзя, у одного или обоих студентов еще нет оценок'

    def __lt__(self, other):
        if len(self.grades) > 0 and len(other.grades) > 0:
            return self._medium_grades() < other._medium_grades()
        else:
            return f'Сравнить нельзя, у одного или обоих студентов еще нет оценок'
        
    def get_grades(self):
        return self.grades

     
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

    def add_courses_attached(self, course_name):
        self.courses_attached.append(course_name)

    def _medium_grades(self):
        if len(self.grades_from_students) == 0:
            return f'Оценок пока нет!'
        for grades in self.grades_from_students.values():
            self.grades_list.append(sum(grades)/len(grades))
        return round((sum(self.grades_list)/len(self.grades_list)), 1)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции - {self._medium_grades()}'

    def __eq__(self, other):
        if len(self.grades_from_students) > 0 and len(other.grades_from_students):
            return self._medium_grades() == other._medium_grades()
        else:
            return f'Сравнить нельзя, есть лектор без оценок'
        
    def __lt__(self, other):
        if len(self.grades_from_students) > 0 and len(other.grades_from_students):
            return self._medium_grades() < other._medium_grades()
        else:
            return f'Сравнить нельзя, есть лектор без оценок'
        
    def get_grades(self):
        return self.grades_from_students


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

    def add_courses_attached(self, course_name):
        self.courses_attached.append(course_name) 

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'
    


student_1 = Student('Дмитрий', 'Чернецов', 'М')
student_2 = Student('Александр', 'Груздев', 'М')
lectur_1 = Lecturer('Тимур', 'Анвартдинов')
lectur_2 = Lecturer('Олег', 'Булыгин')
reviewer_1 = Reviewer('Дмитрий', 'Демидов')
reviewer_2 = Reviewer('Александр', 'Бардин')
lectur_1.add_courses_attached('Python')
lectur_2.add_courses_attached('Python')
student_1.add_finished_courses('Основы языка программирования Python')
student_1.add_courses_in_progress('Python')
student_1.add_courses_in_progress('Git')
student_1.making_grade_lecturer(10, lectur_1, 'Python')
student_1.making_grade_lecturer(8, lectur_1, 'Python')
student_2.add_finished_courses('Основы языка программирования Python')
student_2.add_courses_in_progress('Python')
student_2.add_courses_in_progress('Git')
student_2.making_grade_lecturer(10, lectur_2, 'Python')
student_2.making_grade_lecturer(9, lectur_2, 'Python')
print(lectur_2)
print(lectur_1)
print(lectur_1 < lectur_2)
reviewer_1.add_courses_attached('Python')
reviewer_2.add_courses_attached('Python')
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 4)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Python', 7)
reviewer_2.rate_hw(student_1, 'Python', 9)
print(student_1)
print(student_2)
print(student_1 < student_2)


#Функция для подсчета средней оценки всех студентов:
def medium_grades_student(list_student, course_name):
    medium_grades_list = []
    for student in list_student:
        if isinstance(student, Student) and student.get_grades().get(course_name) is not None:
            medium_grades_list += student.get_grades().get(course_name)
        else:
            pass
    if len(medium_grades_list) > 0:
        return f'Средняя оценка всех студентов на курсе {course_name} равна {sum(medium_grades_list)/len(medium_grades_list)}'
    


#Функция для подсчета средней оценки всех студентов:
def medium_grades_lecturers(list_lecturers, course_name):
    medium_grades_list = []
    for lector in list_lecturers:
        if isinstance(lector, Lecturer) and lector.get_grades().get(course_name) is not None:
            medium_grades_list += lector.get_grades().get(course_name)
        else:
            pass
    if len(medium_grades_list) > 0:
        return f'Средняя оценка всех лекторов на курсе {course_name} равна {sum(medium_grades_list)/len(medium_grades_list)}'