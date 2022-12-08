class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course):
        self.finished_courses.append(course)

    def rate_hw_to_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_to_lecturer:
                lecturer.grades_to_lecturer[course] += [grade]
            else:
                lecturer.grades_to_lecturer[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade_to_student(self):
        if not self.grades:
            return 0
        summ_grades = 0
        grade_count = 0
        for grade_list in list(self.grades.values()):
            for grade in grade_list:
                summ_grades += int(grade)
                grade_count += 1
        return (round(float(summ_grades / grade_count), 1))

    def __str__(self):

        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)

        res = f'Имя:{self.name}\n' \
              f'Фамилия:{self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_grade_to_student()}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def comparison(self, student):
        if isinstance(student, Student):
            if self.average_grade_to_student() > student.average_grade_to_student():
                return f'Средняя оценка {self.name}({self.average_grade_to_student()})' \
                       f' больше чем средняя оценка {student.name}({student.average_grade_to_student()})'

            elif self.average_grade_to_student() < student.average_grade_to_student():
                return f'Средняя оценка {student.name}({student.average_grade_to_student()})' \
                       f' больше чем средняя оценка {self.name}({self.average_grade_to_student()})'

            else:
                return f'Средние оценки лекторов одинаковы({self.average_grade_to_student()})'

        else:
            return 'Ошибка'

class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):

    def __init__(self, name, surname):

        super().__init__(name, surname)
        self.grades_to_lecturer = {}

    def average_grade_to_lecturer(self):

        if not self.grades_to_lecturer:
            return 0
        summ_grades = 0
        grade_count = 0
        for grade_list in list(self.grades_to_lecturer.values()):
            for grade in grade_list:
                summ_grades += int(grade)
                grade_count += 1
        return (round(float(summ_grades / grade_count), 1))

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade_to_lecturer()}'
        return res

    def comparison(self, lecturer):

        if isinstance(lecturer, Lecturer):
            if self.average_grade_to_lecturer() > lecturer.average_grade_to_lecturer():
                return f'Средняя оценка {self.name}({self.average_grade_to_lecturer()})' \
                       f' больше чем средняя оценка {lecturer.name}({lecturer.average_grade_to_lecturer()})'

            elif self.average_grade_to_lecturer() < lecturer.average_grade_to_lecturer():
                return f'Средняя оценка {lecturer.name}({lecturer.average_grade_to_lecturer()})' \
                       f' больше чем средняя оценка {self.name}({self.average_grade_to_lecturer()})'

            else:
                return f'Средние оценки лекторов одинаковы({self.average_grade_to_lecturer()})'

        else:
            return 'Ошибка'


class Reviewer(Mentor):

    def rate_hw_to_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res



def average_grades_of_all_students(list_of_students: list, course):
    summ_grades = 0
    count_grades = 0
    for student in list_of_students:
        for student.grade in student.grades[course]:
            summ_grades += int(student.grade)
            count_grades += 1
    return (round(float(summ_grades / count_grades), 1))

def average_grades_of_all_lecturers(list_of_lecturers: list, course):
    summ_grades = 0
    count_grades = 0
    for lecturer in list_of_lecturers:
        for lecturer.grade in lecturer.grades_to_lecturer[course]:
            summ_grades += int(lecturer.grade)
            count_grades += 1
    return (round(float(summ_grades / count_grades), 1))




Peter = Student('Peter', 'Johnson', 'male')
Peter.courses_in_progress += ['Python']
Peter.courses_in_progress += ['Java']

Emily = Student('Emily', 'Bott', 'female')
Emily.courses_in_progress += ['Web-development']
Emily.courses_in_progress += ['Java']
Emily.courses_in_progress += ['Django']
Emily.courses_in_progress += ['Git and Github']


Christian = Lecturer('Christian', 'Andersen')
Christian.courses_attached += ['Python']
Christian.courses_attached += ['Java']

Jordan = Lecturer('Jordan', 'Green')
Jordan.courses_attached += ['Django']
Jordan.courses_attached += ['Git and Github']
Jordan.courses_attached += ['Python']


Mark = Reviewer('Mark', 'Adrian')
Mark.courses_attached += ['Java']
Mark.courses_attached += ['Django']
Mark.courses_attached += ['Python']
Mark.courses_attached += ['Git and Github']

Theodore = Reviewer('Theodore', 'Higgins')
Theodore.courses_attached += ['Java']
Theodore.courses_attached += ['Django']
Theodore.courses_attached += ['Python']
Theodore.courses_attached += ['Git and Github']

mark.rate_hw_to_student(jacob, 'Java', 5)
mark.rate_hw_to_student(jacob, 'Java', 4)
mark.rate_hw_to_student(jacob, 'Django', 5)
mark.rate_hw_to_student(peter, 'Java', 5)
mark.rate_hw_to_student(emily, 'Java', 7)

peter.rate_hw_to_lecturer(christian, 'Python', 4)
peter.rate_hw_to_lecturer(jordan, 'Python', 3)
peter.rate_hw_to_lecturer(christian, 'Java', 5)

emily.rate_hw_to_lecturer(jordan, 'Django', 9)
emily.rate_hw_to_lecturer(jordan, 'Git and Github', 5)

print(average_grades_of_all_lecturers([jordan, christian], 'Python'))
print(average_grades_of_all_students([emily, peter], 'Java'))

print(f'{christian.name} {christian.surname}: {christian.grades_to_lecturer}')
print(f'{jacob.name} {jacob.surname}: {jacob.grades}')
print(f'{jordan.name} {jordan.surname}: {jordan.grades_to_lecturer}')
print(f'{peter.name} {peter.surname}: {peter.grades}')

print(f'\n{jacob}')
print(f'\n{christian}')

print(peter.comparison(jacob))
print(christian.comparison(jordan))
