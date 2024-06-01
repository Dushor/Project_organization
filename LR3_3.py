import pickle


class Department(object):
    def __init__(self):
        self.department_name = 'Технология'
        self.head_of_department = 'Алекс'
        self.levels = []
        self.telephone = '+7 984 956 12 51'
        try:
            self.open_department()
        except:
            self.save_department()

    def open_department(self):
        with open(self.department_name, 'rb') as f:
            self.levels = pickle.load(f)

    def save_department(self):
        with open(self.department_name, 'wb') as f:
            pickle.dump(self.levels, f)

    def add_department(self, balance):
        self.levels.append(DepartmentLevel(len(self.levels) + 1, balance))
        self.save_department()
        print('Отдел успешно открыт!')

    def demolish_department(self, number):
        for level in self.levels:
            if level.number == number:
                self.levels.remove(level)
                self.save_department()
                print('Отдел успешно закрыт!')
                return
        print('Отдел с указанным номером не найден!')

    def change_balance(self, number, balance):
        for level in self.levels:
            if level.number == number:
                level.balance = balance
                self.save_department()
                print('Баланс отдела успешно изменен!')
                return
        print('Отдел с указанным номером не найден!')

    def print_levels(self):
        for level in self.levels:
            print('Отдел номер {0}, баланс {1}'.format(level.number, level.balance))


class DepartmentLevel(object):
    def __init__(self, number, balance):
        self.number = number
        self.balance = balance


class BankTerm(object):
    def __init__(self):
        self.test_department = Department()

    def print_db(self):
        self.test_department.print_levels()

    def run(self):
        choice = 0
        choices = {
            1: lambda: self.print_db(),
            2: lambda: self.test_department.add_department(int(input('Введите баланс: '))),
            3: lambda: self.test_department.demolish_department(int(input('Введите номер отдела: '))),
            4: lambda: self.test_department.change_balance(int(input('Введите номер отдела: ')),
                                                           int(input('Введите новый баланс: ')))
        }
        while choice != 3:
            print()
            print('1. Открыть отдел')
            print('2. Закрыть отдел')
            print('3. Выход')
            print('Выберите пункт:')
            choice = int(input())
            if choice in choices:
                choices[choice]()


if __name__ == '__main__':
    BankTerm().run()
