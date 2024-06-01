class Project_organization:
    pass


class Department(object):
    def __init__(self, department_name, level, telephone, head_of_department):
        self.department_name = department_name
        self.level = level
        self.telephone = telephone
        self.head_of_department = head_of_department

    def __str__(self):
        return (f"\nОтдел: "
                + f"\nИмя отдела: {str(self.department_name)}"
                + f"\nЭтаж: {str(self.level)}"
                + f"\nТелефон: {str(self.telephone)}"
                + f"\nГлава отдела: {str(self.head_of_department)}")


class Department1(Department):
    def __init__(self, department_name=None, level=0, telephone=None, head_of_department=None):
        super(Department1, self).__init__(department_name, level, telephone, head_of_department)

    def __str__(self):
        return super(Department1, self).__str__()

    def interest(self, rate):
        self.level *= (1 + rate)


d = Department('технологии', 5, '+7 984 956 12 51', 'Алекс')
print(d)


class Staff(object):
    def __init__(self, fio, post, department_number, floor, address, date_of_birth):
        self.fio = fio
        self.post = post
        self.department_number = department_number
        self.floor = floor
        self.address = address
        self.date_of_birth = date_of_birth

    def __str__(self):
        return (f"\nCотрудники: "
                + f"\nФИО: {str(self.fio)}"
                + f"\nДолжность: {str(self.post)}"
                + f"\nНомер отдела: {str(self.department_number)}"
                + f"\nПол: {str(self.floor)}"
                + f"\nАдрес: {str(self.address)}"
                + f"\nДата рождения: {str(self.date_of_birth)}")


class Staff1(Staff):
    def __init__(self, fio=None, post=None, department_number=0, floor=None, address=None, date_of_birth=None):
        super(Staff1, self).__init__(fio, post, department_number, floor, address, date_of_birth)

    def __str__(self):
        return super(Staff1, self).__str__()

    def interest(self, rate):
        self.department_number *= (1 + rate)


s = Staff('Салмаков Максим Ильич', 'програмист', 'програмирование',
          'мужской', 'Галушина 10', '10.02.2015')
print(s)


class Organizations(object):
    def __init__(self, name_organization, type_of_activity, country, city, address1, fio_director):
        self.name_organization = name_organization
        self.type_of_activity = type_of_activity
        self.country = country
        self.city = city
        self.address1 = address1
        self.fio_director = fio_director

    def __str__(self):
        return (f"\nОрганизации: "
                + f"\nНазвание организации: {str(self.name_organization)}"
                + f"\nТип деятельности: {str(self.type_of_activity)}"
                + f"\nСтрана: {str(self.country)}"
                + f"\nГород: {str(self.city)}"
                + f"\nАдрес: {str(self.address1)}"
                + f"\nФИО директора: {str(self.fio_director)}")


class Organizations1(Organizations):
    def __init__(self, name_organization=None, type_of_activity=None, country=None,
                 city=None, address1=None, fio_director=None):
        super(Organizations1, self).__init__(name_organization, type_of_activity, country, city, address1, fio_director)

    def __str__(self):
        return super(Organizations1, self).__str__()


o = Organizations('ProgramIntoAction', 'Програмирование',
                  'Россия', 'Архангельск', 'Дачная 27',
                  'Щетнева Ольга Александровна')
print(o)


class Agreement(object):
    def __init__(self, contract_number, date_conclusion_contract, organization1, contract_price):
        self.contract_number = contract_number
        self.date_conclusion_contract = date_conclusion_contract
        self.organization1 = organization1
        self.contract_price = contract_price

    def __str__(self):
        return (f"\nДоговора: "
                + f"\nНомер договора: {str(self.contract_number)}"
                + f"\nДата заключения договора: {str(self.date_conclusion_contract)}"
                + f"\nОрганизация: {str(self.organization1)}"
                + f"\nСтоимость договора: {str(self.contract_price)}")


class Agreement1(Agreement):
    def __init__(self, contract_number=0, date_conclusion_contract=None, organization1=None, contract_price=0):
        super(Agreement1, self).__init__(contract_number, date_conclusion_contract, organization1, contract_price)

    def __str__(self):
        return super(Agreement1, self).__str__()

    def interest(self, rate):
        self.contract_number *= (1 + rate)
        self.contract_price *= (1 + rate)


a = Agreement(14, '19.05.2019', 'Technology',
              10000)
print(a)


class Project_work(object):
    def __init__(self, start_work, completion_work, contract_number, department_name):
        self.start_work = start_work
        self.completion_work = completion_work
        self.contract_number = contract_number
        self.department_name = department_name

    def __str__(self):
        return (f"\nПроектные работы: "
                + f"\nДата начала проектной работы: {str(self.start_work)}"
                + f"\nДата завершения проектной работы: {str(self.completion_work)}"
                + f"\nНомер договора: {str(self.contract_number)}"
                + f"\nОтдел: {str(self.department_name)}")


class Project_work1(Project_work):
    def __init__(self, start_work=None, completion_work=None, contract_number=0, department_name=None):
        super(Project_work1, self).__init__(start_work, completion_work, contract_number, department_name)

    def __str__(self):
        return super(Project_work1, self).__str__()

    def interest(self, rate):
        self.contract_number *= (1 + rate)


p = Project_work('20.01.2021', '20.01.2024', 14, 'Технологии')
print(p)
