class Departmen:
    def __init__(self, department_name, level, telephone, head_of_department):
        self.department_name = department_name
        self.level = level
        self.telephone = telephone
        self.head_of_department = head_of_department

    def print_departmen(self):
        try:
            level = hell
            print(level)
        except:
            print("Такого этажа нет")

        print(f"\nИмя отдела: {self.department_name}"
              f"\nЭтаж: {self.level}"
              f"\nТелефон: {self.telephone}"
              f"\nГлава отдела: {self.head_of_department}")


d = Departmen('Отдел Технологий', '5', '+74362372718',
              'Вадим Салмаков Ильич')
d.print_departmen()
