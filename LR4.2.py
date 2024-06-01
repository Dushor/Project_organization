class Agreement(object):
    def __init__(self, contract_number, contract_price):
        self.contract_number = contract_number
        self.contract_price = contract_price

    def contract(self, amount):
        self.contract_price += amount


class Worker(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


class WorkerAgreement(Agreement):
    def __init__(self, contract_price=0, firstname=None, lastname=None):
        super(WorkerAgreement, self).__init__(contract_number=None, contract_price=contract_price)
        self.worker = Worker(firstname, lastname)

    def __str__(self):
        return 'Номер контракта: {0} \nЦена контракта: {1} \nИмя: {2} \nФамилия: {3}'.format(
            self.contract_number, self.contract_price, self.worker.firstname, self.worker.lastname)

    def purpose(self, rate):
        self.contract_price *= (1 + rate)


if __name__ == '__main__':
    a = Agreement(1, 100)
    a.contract(50)
    print(a.contract_price)

    wa = WorkerAgreement(100, 'Maksim', 'Salmakov')
    print(wa)
