class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lect:
                lecturer.grades_lect[course] += [grade]
            else:
                lecturer.grades_lect[course] = [grade]
        else:
            return 'Ошибка'

    def avere_grade_for_stud(self):
        for course, grade in self.grades.items():
            return round(sum(grade)/len(grade),1)

    def average_grade_to_course_stud(self, course):
        if course in self.courses_in_progress:
             for grades_lec in self.grades.values():
                  return sum(grades_lec) / len(grades_lec)
        else:
             return 'Студента нет  на этом курсе'

    def __str__(self):
        result_lect = f' Имя студента: {self.name} \n Фамилия студента:{self.surname} \n Средняя оценка за ДЗ:{round((Student.avere_grade_for_stud(self)), 1)}\n' \
                     f'Курсы в процессе изучения: {self.courses_in_progress} \n Завершенные курсы: {self.finished_courses }'
        return result_lect

    def __lt__(self, other):
       if not isinstance(other, Student):
           print('Студента нет в списке')
           return
       return round((Student.avere_grade_for_stud(self)), 1) < round((other.avere_grade_for_stud()), 1)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lect = {}

    def aver_grade_for_lect(self):
        for cour, grade in self.grades_lect.items():
             return round(sum(grade) / len(grade),1)

    def average_grade_to_course(self, course):
         if course in self.courses_attached:
             for grades_lec in self.grades_lect.values():
                   return sum(grades_lec) / len(grades_lec)
         else:
             return 'Лектор не преподает на этом курсе'


    def __str__(self):
        result_lect = f'Имя лектора: {self.name} \n Фамилия лектора: {self.surname} \n Средняя оценка за лекции:{round((Lecturer.aver_grade_for_lect(self)), 1)}'
        return result_lect

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Лектора нет в списке')
            return
        return round((Lecturer.aver_grade_for_lect(self)), 1) < round((other.aver_grade_for_lect()), 1)
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        result_lect = f'Имя эксперта: {self.name}\n Фамилия эксперта: {self.surname}'
        return result_lect

    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def avg_all_lec(course, list_lect):
     grades_all_lec = 0
     counter = 0
     for lecture in list_lect:
         if course in lecture.courses_attached:
             grades_all_lec += round((lecture.average_grade_to_course(course)), 1)
             counter += 1
             average_grade = round((grades_all_lec / counter), 1)
     return f'Средняя оценка всех лекторов за курс "{course}" - {round(average_grade, 1)}'

def avg_all_students(course, list):
     grades_all_lec = 0
     counter = 0
     for lecture in list:
         if course in lecture.courses_in_progress:
             grades_all_lec += round((lecture.average_grade_to_course_stud(course)), 1)
             counter += 1
         average_grade = round((grades_all_lec/ counter), 1)
     return f'Средняя оценка всех студентов за курс "{course}" = {round(average_grade, 1)}'


second_student = Student ('Andrey', 'Sidorov')
second_student.courses_in_progress += ['Python', 'GO']
second_student.finished_courses += ['Java']
best_student = Student('Ruoy', 'Eman',)
best_student.courses_in_progress += ['GO', 'Python']
best_student.finished_courses += ['C+']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'GO']
new_reviewer = Reviewer('Vova', 'Putin')
new_reviewer.courses_attached += ['Python']

first_lect = Lecturer('Ivan', 'Ivanov')
first_lect.courses_attached += ['Python', 'GO']
second_lect = Lecturer('Anna', 'Ivanova')
second_lect.courses_attached += ['Python']

best_student.rate_lect(first_lect, 'GO', 1)
second_student.rate_lect(first_lect, 'GO', 7)
best_student.rate_lect(second_lect, 'GO', 10)
second_student.rate_lect(second_lect, 'GO', 10)

best_student.rate_lect(first_lect, 'Python', 0)
second_student.rate_lect(first_lect, 'Python', 1)
best_student.rate_lect(second_lect, 'Python', 2)
second_student.rate_lect(second_lect, 'Python', 4)



cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(second_student, 'Python', 9)
cool_reviewer.rate_hw(second_student, 'Python', 6)
cool_reviewer.rate_hw(best_student, 'GO', 7)
cool_reviewer.rate_hw(second_student, 'GO', 10)



lectors_list = [first_lect, second_lect]
list_students = [best_student, second_student]

print(cool_reviewer)
print(first_lect)
print(best_student)
print(second_lect < first_lect)
print(best_student < second_student)
print(avg_all_lec('Python', lectors_list))

print(avg_all_students('GO', list_students))


