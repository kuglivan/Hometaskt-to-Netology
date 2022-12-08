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
        #    grades_count = 0
        #   for k in self.grades:
        #      grades_count += len(self.grades[k])
        # self.average_rating = sum(map(sum, self.grades.values())) / grades_count
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

peter = Student('Peter', 'Johnson', 'male')
peter.courses_in_progress += ['Python']
peter.courses_in_progress += ['Java']

mason = Student('Mason', 'Bethell', 'male')
mason.courses_in_progress += ['Web-development']

emily = Student('Emily', 'Bott', 'female')
emily.courses_in_progress += ['Web-development']
emily.courses_in_progress += ['Java']
emily.courses_in_progress += ['Django']
emily.courses_in_progress += ['Git and Github']

jacob = Student('Jacob', 'Edwards', 'male')
jacob.courses_in_progress += ['Django']
jacob.courses_in_progress += ['Java']

william = Student('William', 'Gates', 'male')
william.courses_in_progress += ['Python']
william.courses_in_progress += ['Git and Github']

christian = Lecturer('Christian', 'Andersen')
christian.courses_attached += ['Python']
christian.courses_attached += ['Java']

jordan = Lecturer('Jordan', 'Green')
jordan.courses_attached += ['Django']
jordan.courses_attached += ['Git and Github']
jordan.courses_attached += ['Python']

mark = Reviewer('Mark', 'Adrian')
mark.courses_attached += ['Java']
mark.courses_attached += ['Django']
mark.courses_attached += ['Python']
mark.courses_attached += ['Git and Github']

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
#print(list(jacob.grades.values()))
print(f'\n{jacob}')
print(f'\n{christian}')

print(peter.comparison(jacob))
print(christian.comparison(jordan))


#best_student = Student('Ruoy', 'Eman', 'your_gender')
#best_student.courses_in_progress += ['Python']

#cool_mentor = Mentor('Some', 'Buddy')
#cool_mentor.courses_attached += ['Python']

#cool_mentor.rate_hw(best_student, 'Python', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)

#print(best_student.grades)


'''class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.srgr = float()

    def srgr(self):
        grades_count = 0
        if not self.grades:
            return 0
        
        spisok = []
        for k in self.grades:
            grades_count += len(self.grades[k])
            spisok.append(k)
        return float(sum(spisok) / max(len(spisok), 1))

    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)

        res = f'Имя:{self.name}\n' \
              f'Фамилия:{self.surname}\n' \
              f'Средняя оценка за домашнее задание:{self.srgr}\n' \
              f'Курсы в процессе обучени:{courses_in_progress_string}\n' \
              f'Завершенные курсы:{finished_courses_string}'
        return res

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.srgr < other.srgr


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        # self.average_rating = float()
        self.grades = {}
        self.srgr = float()

    def srgr(self):
        grades_count = 0
        if not self.grades:
            return 0
        spisok = []
        for k in self.grades.values():
            grades_count += len(self.grades[k])
            spisok.append(k)
        return float(sum(spisok) / max(len(spisok), 1))

    def __str__(self):
        #    grades_count = 0
        #   for k in self.grades:
        #      grades_count += len(self.grades[k])
        # self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.srgr}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.srgr < other.srgr


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
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


best_lecturer_1 = Lecturer('Ivan', 'Ivanov')
best_lecturer_1.courses_attached += ['Python']
best_lecturer_2 = Lecturer('Petr', 'Petrov')
best_lecturer_2.courses_attached += ['Java']
best_lecturer_3 = Lecturer('Semen', 'Zarev')
best_lecturer_3.courses_attached += ['Python']

cool_rewiewer_1 = Reviewer('Some', 'Buddy')
cool_rewiewer_1.courses_attached += ['Python']
cool_rewiewer_1.courses_attached += ['Java']
cool_rewiewer_2 = Reviewer('Ostap', 'Bender')
cool_rewiewer_2.courses_attached += ['Python']
cool_rewiewer_2.courses_attached += ['Java']
student_1 = Student('Denis', 'Sviridov')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']
student_2 = Student('Roman', 'Malikov')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']
student_3 = Student('Sidor', 'Petrov')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_2, 'Python', 5)
student_1.rate_hw(best_lecturer_2, 'Python', 7)
student_1.rate_hw(best_lecturer_2, 'Python', 8)
student_1.rate_hw(best_lecturer_1, 'Python', 7)
student_1.rate_hw(best_lecturer_1, 'Python', 8)
student_1.rate_hw(best_lecturer_1, 'Python', 9)
student_2.rate_hw(best_lecturer_2, 'Python', 10)
student_2.rate_hw(best_lecturer_2, 'Python', 8)
student_2.rate_hw(best_lecturer_2, 'Python', 9)
student_3.rate_hw(best_lecturer_3, 'Python', 5)
student_3.rate_hw(best_lecturer_3, 'Python', 6)
student_3.rate_hw(best_lecturer_3, 'Python', 7)
cool_rewiewer_1.rate_hw(student_1, 'Python', 8)
cool_rewiewer_1.rate_hw(student_1, 'Python', 9)
cool_rewiewer_1.rate_hw(student_1, 'Python', 10)
cool_rewiewer_2.rate_hw(student_2, 'Java', 8)
cool_rewiewer_2.rate_hw(student_2, 'Java', 7)
cool_rewiewer_2.rate_hw(student_2, 'Java', 9)
cool_rewiewer_2.rate_hw(student_3, 'Python', 8)
cool_rewiewer_2.rate_hw(student_3, 'Python', 7)
cool_rewiewer_2.rate_hw(student_3, 'Python', 9)
cool_rewiewer_2.rate_hw(student_3, 'Python', 8)
cool_rewiewer_2.rate_hw(student_3, 'Python', 7)
cool_rewiewer_2.rate_hw(student_3, 'Python', 9)
print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()
print()
print(f'Перечень лекторов:\n\n{best_lecturer_1}\n\n{best_lecturer_2}\n\n{best_lecturer_3}')
print()
print()
print(f'Результат сравнения студентов(по средним оценкам за ДЗ): '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} ={student_1 > student_2}')
print()
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname} = {best_lecturer_1 > best_lecturer_2}')
print()
student_list = [student_1, student_2, student_3]
lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]


def student_rating(student_list, course_name):
    sum_all = 0
    count_all = []
    for stud in student_list:
        if stud.courses_in_progress == [course_name]:
            sum_all += len(student_list[stud])
            count_all.append(stud)
    # average_for_all = sum_all / count_all
    return float(sum(count_all) / max(len(count_all), 1))  # average_for_all


def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += len(lecturer_list[lect])
            count_all.append(lect)
    # average_for_all = sum_all / count_all
    return float(sum(count_all) / max(len(count_all), 1))  # average_for_all


print(f"Средняя оценка для всех студентов по курсу Python: {student_rating(student_list, 'Python')}")
print(f"Средняя оценка для всех лекторов по курсу Python: {lecturer_rating(lecturer_list, 'Python')}")'''