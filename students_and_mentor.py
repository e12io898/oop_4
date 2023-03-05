class BaseMethod:
    def avg(self):
        average = []
        for i in self.grades.values():
            for j in i:
                average.append(j)
        self.avg_grades = round((sum(average) / len(average)), 1)

    def __eq__(self, other):
        return self.avg_grades == other.avg_grades

    def __lt__(self, other):
        return self.avg_grades < other.avg_grades

    def __le__(self, other):
        return self.avg_grades <= other.avg_grades

class Student(BaseMethod):
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_grades = 0

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) \
                and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        self.avg()
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за лекции: {self.avg_grades}\n'
               f'Курсы в процессе изучения: '
               f'{", ".join(self.courses_in_progress)}\n'
               f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return res
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor, BaseMethod):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.avg_grades = 0

    def __str__(self):
        self.avg()
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за лекции: {self.avg_grades}')
        return res

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) \
                and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}')
        return res

#создание студента 1
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']

#создание студента 2
other_student = Student('Bob', 'Dylan', 'man')
other_student.courses_in_progress += ['Python', 'Git']
other_student.finished_courses += ['Введение в программирование']

#создание проверяющего
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']

#создание лектора 1
some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']

#создание лектора 2
other_lecturer = Lecturer('Some', 'Buddy')
other_lecturer.courses_attached += ['Python']
other_lecturer.courses_attached += ['Git']

#выставление оценок студенту 1
some_reviewer.rate_hw(some_student, 'Python', 8)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Git', 7)

#выставление оценок студенту 2
some_reviewer.rate_hw(other_student, 'Python', 8)
some_reviewer.rate_hw(other_student, 'Python', 10)
some_reviewer.rate_hw(other_student, 'Git', 7)

#выставление оценок лектору 1
some_student.rate_lec(some_lecturer, 'Python', 5)
some_student.rate_lec(some_lecturer, 'Python', 8)
some_student.rate_lec(some_lecturer, 'Git', 4)

#выставление оценок лектору 2
some_student.rate_lec(other_lecturer, 'Python', 5)
some_student.rate_lec(other_lecturer, 'Python', 8)
some_student.rate_lec(other_lecturer, 'Git', 4)

#проверка вывода
print(some_reviewer)
print()
print(some_lecturer)
print()
print(some_student)
print()
#проверка сравнений студентов
print(some_student >= other_student)
print(some_student <= other_student)
print(some_student > other_student)
print(some_student < other_student)
print(some_student == other_student)
print(some_student != other_student)
print()
#проверка сравнений лекторов
print(some_lecturer >= other_lecturer)
print(some_lecturer <= other_lecturer)
print(some_lecturer > other_lecturer)
print(some_lecturer < other_lecturer)
print(some_lecturer == other_lecturer)
print(some_lecturer != other_lecturer)