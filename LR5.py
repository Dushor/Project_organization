from abc import ABC
from abc import abstractmethod


class Project(ABC):
    @abstractmethod
    def start_work(self):
        pass

    @abstractmethod
    def completion_work(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Organization(ABC):
    @abstractmethod
    def date_conclusion_contract(self):
        pass

    @abstractmethod
    def organization1(self):
        pass

    @abstractmethod
    def contract_price(self):
        pass


class Project_work(Project):
    def start_work(self):
        print('Начало работы')

    def completion_work(self):
        print('Завершение работы')

    def get_info(self):
        print('Это проектные работы')


class Agreement(Organization):
    def date_conclusion_contract(self):
        print('14.11.2022')

    def organization1(self):
        print('Blizzard Entertainment')

    def contract_price(self):
        print('15 000 000')


Pw1 = Project_work()
Pw1.start_work()
Pw1.completion_work()
Pw1.get_info()
A1 = Agreement()
A1.date_conclusion_contract()
A1.organization1()
A1.contract_price()
