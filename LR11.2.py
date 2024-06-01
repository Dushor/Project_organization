from abc import ABC, abstractmethod


class Agreement(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


class ContractNumber(Agreement):
    def get_description(self):
        return "Number 1.42"

    def get_cost(self):
        return 1.0


class DateConclusionContract(Agreement):
    def __init__(self, may):
        self.may = may

    def get_description(self):
        return self.may.get_description()

    def get_cost(self):
        return self.may.get_cost()


class conditions(DateConclusionContract):
    def get_description(self):
        return self.may.get_description() + ", terms of the agreement"

    def get_cost(self):
        return self.may.get_cost() + 1.0


class cost(DateConclusionContract):
    def get_description(self):
        return self.may.get_description() + ", cost 15.000 RUB"

    def get_cost(self):
        return self.may.get_cost() + 1.0


def main():
    contract_number = ContractNumber()
    print(contract_number.get_description(), 'V', contract_number.get_cost())

    contract_number_conditions = conditions(contract_number)
    print(contract_number_conditions.get_description(), 'V', contract_number_conditions.get_cost())

    contract_number_conditions_and_cost = cost(contract_number_conditions)
    print(contract_number_conditions_and_cost.get_description(), 'V',
          contract_number_conditions_and_cost.get_cost())


if __name__ == "__main__":
    main()
