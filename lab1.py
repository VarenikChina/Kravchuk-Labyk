class Raf:
    def __init__(self, name=None, surname=None, birth_year=None, manual_course=None):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.manual_course = manual_course

    def college_year_calc(self):
        if self.manual_course is not None and 1 <= self.manual_course <= 4:
            return self.manual_course

        if self.birth_year is None:
            return "невідомо"

        current_year = 2025
        age = current_year - self.birth_year

        if age == 16:
            return 1
        elif age == 17:
            return 2
        elif age == 18:
            return 3
        elif age == 19:
            return 4
        else:
            return "невідомо"

    def get_names_list(self, students):
        return [f"{student.name or 'Імʼя невідоме'} {student.surname or 'Прізвище невідоме'}" for student in students]


Student1 = Raf("Діма", "Поліщук", 2008)
Student2 = Raf("Дімон", None, 2000)
Student3 = Raf("Дмітрій", "Поляков", 2007, 2)

Students = [Student1, Student2]
Names_list = Student1.get_names_list(Students)

print("Список імен:", Names_list)
print(*vars(Student1).values())

print(f"Студент {Student1.name} {Student1.surname} знаходиться на {Student1.college_year_calc()} курсі.")
print(f"Студент {Student2.name} {Student2.surname} знаходиться на {Student2.college_year_calc()} курсі.")
print(f"Студент {Student3.name} {Student3.surname} знаходиться на {Student3.college_year_calc()} курсі.")
