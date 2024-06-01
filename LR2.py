from multipledispatch import dispatch


class Project_organization:
    pass


class Departmen:
    def __init__(self, department_name, level, telephone, head_of_department):
        self.department_name = department_name
        self.level = level
        self.telephone = telephone
        self.head_of_department = head_of_department

    @dispatch(str, str, str, str)
    def print_info1(self, department_name, level, telephone, head_of_department):
        print('Отдел')
        print(f"\nИмя отдела: {self.department_name} \nЭтаж: {self.level}"
              f"\nТелефон: {self.telephone} \nГлава отдела: {self.head_of_department}")
        print(' ')

    @dispatch(str, str)
    def print_info1(self, department_name, head_of_department):
        print('Отдел')
        print(f"\nИмя отдела: {self.department_name} \nГлава отдела: {self.head_of_department}")
        print(' ')


class Staff:
    def __init__(self, fio, post, department_number, floor, address, date_of_birth):
        self.fio = fio
        self.post = post
        self.department_number = department_number
        self.floor = floor
        self.address = address
        self.date_of_birth = date_of_birth

    @dispatch(str, str, str, str, str, str)
    def print_info2(self, fio, post, department_number, floor, address, date_of_birth):
        print("Cотрудники")
        print(f"\nФИО: {self.fio} \nДолжность: {self.post} \nНомер отдела: {self.department_number}"
              f"\nПол: {self.floor} \nАдрес: {self.address} \nДата рождения: {self.date_of_birth}")
        print(' ')

    @dispatch(str, str, str)
    def print_info2(self, fio, post, date_of_birth):
        print('Cотрудники')
        print(f"\nФИО: {self.fio} \nДолжность: {self.post} \nДата рождения: {self.date_of_birth}")
        print(' ')


class Organizations:
    def __init__(self, name_organization, type_of_activity, country, city, address1, fio_director):
        self.name_organization = name_organization
        self.type_of_activity = type_of_activity
        self.country = country
        self.city = city
        self.address1 = address1
        self.fio_director = fio_director

    @dispatch(str, str, str, str, str, str)
    def print_info3(self, name_organization, type_of_activity, country, city, address1, fio_director):
        print('Организации')
        print(f"\nНазвание организации: {self.name_organization} \nТип деятельности: {self.type_of_activity}"
              f"\nСтрана: {self.country} \nГород: {self.city} \nАдрес: {self.address1}"
              f"\nФИО директора: {self.fio_director}")
        print(' ')

    @dispatch(str, str, str)
    def print_info3(self, country, city, address1):
        print('Организации')
        print(f"\nСтрана: {self.country} \nГород: {self.city} \nАдрес: {self.address1}")
        print(' ')


class Agreement:
    def __init__(self, contract_number, date_conclusion_contract, organization1, contract_price):
        self.contract_number = contract_number
        self.date_conclusion_contract = date_conclusion_contract
        self.organization1 = organization1
        self.contract_price = contract_price

    @dispatch(str, str, str, str)
    def print_info4(self, contract_number, date_conclusion_contract, organization1, contract_price):
        print('Договора')
        print(f"\nНомер договора: {self.contract_number} \nДата заключения договора: {self.date_conclusion_contract}"
              f"\nОрганизация: {self.organization1} \nСтоимость договора: {self.contract_price}")
        print(' ')

    @dispatch(str, str)
    def print_info4(self, contract_number, contract_price):
        print('Договора')
        print(f"\nНомер договора: {self.contract_number} \nСтоимость договора: {self.contract_price}")
        print(' ')


class Project_work:
    def __init__(self, start_work, completion_work, contract_number, department_name):
        self.start_work = start_work
        self.completion_work = completion_work
        self.contract_number = contract_number
        self.department_name = department_name

    @dispatch(str, str, str, str)
    def print_info5(self, start_work, completion_work, contract_number, department_name):
        print('Проектные работы')
        print(f"\nДата начала проектной работы: {self.start_work}"
              f"\nДата завершения проектной работы: {self.completion_work}"
              f"\nНомер договора: {self.contract_number}, \nОтдел: {self.department_name}")
        print(' ')

    @dispatch(str, str)
    def print_info5(self, start_work, completion_work):
        print('Проектные работы')
        print(f"\nДата начала проектной работы: {self.start_work}"
              f"\nДата завершения проектной работы: {self.completion_work}")
        print(' ')


Departmen1 = Departmen('Отдел Технологий', '5', '+74362372718',
                       'Вадим Салмаков Ильич')

Departmen1.print_info1('Отдел Технологий', 'Вадим Салмаков Ильич')
Departmen1.print_info1('Отдел Технологий', '5', '+74362372718', 'Вадим Салмаков Ильич')

staff1 = Staff('Салмаков Максим Ильич', 'програмист', 'програмирование',
               'мужской', 'Галушина 10', '10.02.2015')

staff1.print_info2('Салмаков Максим Ильич', 'програмист', '10.02.2015')
staff1.print_info2('Салмаков Максим Ильич', 'програмист', 'програмирование', 'мужской', 'Галушина 10', '10.02.2015')

Organizations1 = Organizations('ProgramIntoAction', 'Програмирование',
                               'Россия', 'Архангельск', 'Дачная 27',
                               'Щетнева Ольга Александровна')

Organizations1.print_info3('Россия', 'Архангельск', 'Дачная 27')
Organizations1.print_info3('ProgramIntoAction', 'Програмирование', 'Россия', 'Архангельск',
                           'Дачная 27', 'Щетнева Ольга Александровна')

Agreement1 = Agreement('14', '19.05.2019', 'Technology',
                       '10 000 рублей')

Agreement1.print_info4('14', '10 000 рублей')
Agreement1.print_info4('14', '19.05.2019', 'Technology', '10 000 рублей')

project_work1 = Project_work('20.01.2021', '20.01.2024', '14',
                             'Технологии')

project_work1.print_info5('20.01.2021', '20.01.2024')
project_work1.print_info5('20.01.2021', '20.01.2024', '14', 'Технологии')
