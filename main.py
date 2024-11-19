class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        total = 0
        count = 0
        for grades_list in self.grades.values():
            total += sum(grades_list)
            count += len(grades_list)
        return round(total / count, 1) if count != 0 else 0

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        total = 0
        count = 0
        for grades_list in self.grades.values():
            total += sum(grades_list)
            count += len(grades_list)
        return round(total / count, 1) if count != 0 else 0

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_grade()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()


student_1 = Student('Ruoy', 'Eman', 'male')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Иван', 'Иванов', 'male')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['C+']


lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Василий', 'Васильков')
lecturer_2.courses_attached += ['Python', 'C+']


reviewer_1 = Reviewer('Some', 'Бадди')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Петр', 'Петров')
reviewer_2.courses_attached += ['C+']


reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 8)


student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_2.rate_lecturer(lecturer_2, 'C+', 7)


print(reviewer_1)
print()
print(lecturer_1)
print()
print(student_1)
print()


print('Сравнение лекторов:')
print(f'{lecturer_1.name} < {lecturer_2.name}:', lecturer_1 < lecturer_2)
print()
print('Сравнение студентов:')
print(f'{student_1.name} < {student_2.name}:', student_1 < student_2)
print()


def average_student_grade(students, course):
    total = 0
    count = 0
    for student in students:
        if course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    return round(total / count, 1) if count != 0 else 0

def average_lecturer_grade(lecturers, course):
    total = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return round(total / count, 1) if count != 0 else 0


students_list = [student_1, student_2]
lecturers_list = [lecturer_1, lecturer_2]

print('Средняя оценка за домашние задания по Python:', average_student_grade(students_list, 'Python'))
print('Средняя оценка за лекции по Python:', average_lecturer_grade(lecturers_list, 'Python'))
