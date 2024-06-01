class Project_organization:
    pass


class Departmen:
    def __init__(self, department_name, level, telephone, head_of_department):
        self.department_name = department_name
        self.level = level
        self.telephone = telephone
        self.head_of_department = head_of_department

    def print_info1(self):
        print('Отдел')
        print(f"Имя отдела: {self.department_name}")
        print(f"Этаж: {self.level}")
        print(f"Телефон: {self.telephone}")
        print(f"Глава отдела: {self.head_of_department}")
        print(' ')


class Staff:
    def __init__(self, fio, post, department_number, floor, address, date_of_birth):
        self.fio = fio
        self.post = post
        self.department_number = department_number
        self.floor = floor
        self.address = address
        self.date_of_birth = date_of_birth

    def print_info2(self):
        print("Cотрудники")
        print(f"ФИО: {self.fio}")
        print(f"Должность: {self.post} ")
        print(f"Номер отдела: {self.department_number}")
        print(f"Пол: {self.floor} ")
        print(f"Адрес: {self.address} ")
        print(f"Дата рождения: {self.date_of_birth}")
        print(' ')


class Organizations:
    def __init__(self, name_organization, type_of_activity, country, city, address1, fio_director):
        self.name_organization = name_organization
        self.type_of_activity = type_of_activity
        self.country = country
        self.city = city
        self.address1 = address1
        self.fio_director = fio_director

    def print_info3(self):
        print('Организации')
        print(f"Название организации: {self.name_organization}")
        print(f"Тип деятельности: {self.type_of_activity}")
        print(f"Страна: {self.country}")
        print(f"Город: {self.city}")
        print(f"Адрес: {self.address1}")
        print(f"ФИО директора: {self.fio_director}")
        print(' ')


class Agreement:
    def __init__(self, contract_number, date_conclusion_contract, organization1, contract_price):
        self.contract_number = contract_number
        self.date_conclusion_contract = date_conclusion_contract
        self.organization1 = organization1
        self.contract_price = contract_price

    def print_info4(self):
        print('Договора')
        print(f"Номер договора: {self.contract_number}")
        print(f"Дата заключения договора: {self.date_conclusion_contract}")
        print(f"Организация: {self.organization1}")
        print(f"Стоимость договора: {self.contract_price}")
        print(' ')


class Project_work:
    def __init__(self, start_work, completion_work, contract_number, department_name):
        self.start_work = start_work
        self.completion_work = completion_work
        self.contract_number = contract_number
        self.department_name = department_name

    def print_info5(self):
        print('Проектные работы')
        print(f"Дата начала проектной работы: {self.start_work}")
        print(f"Дата завершения проектной работы: {self.completion_work}")
        print(f"Номер договора: {self.contract_number}")
        print(f"Отдел: {self.department_name}")
        print(' ')


Departmen1 = Departmen('Отдел Технологий', '5', '+74362372718',
                       'Вадим Салмаков Ильич')

Departmen1.print_info1()

staff1 = Staff('Салмаков Максим Ильич', 'програмист', 'програмирование',
               'мужской', 'Галушина 10', '10.02.2015')

staff1.print_info2()

Organizations1 = Organizations('ProgramIntoAction', 'Програмирование',
                               'Россия', 'Архангельск', 'Дачная 27',
                               'Щетнева Ольга Александровна')

Organizations1.print_info3()

Agreement1 = Agreement('14', '19.05.2019', 'Technology',
                       '10 000 рублей')

Agreement1.print_info4()

project_work1 = Project_work('20.01.2021', '20.01.2024', '14',
                             'Технологии')

project_work1.print_info5()

