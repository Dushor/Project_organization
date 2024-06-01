import random

class Department(object):
    def accept(self, visitor):
        visitor.visit(self)

    def pollinate(self, pollinator):
        print(f"{self} getting started by {pollinator}")

    def eat(self, eater):
        print(f"{self} end work by {eater}")

    def __str__(self):
        return self.__class__.__name__


class Department_123(Department):
    pass


class Department_186(Department):
    pass


class Department_134(Department):
    pass


class Visitor:
    def __str__(self):
        return self.__class__.__name__


class Human(Visitor):
    pass


class Worker(Human):
    pass


class Director(Human):
    pass


class Nastya(Worker):
    def visit(self, department):
        department.pollinate(self)


class Maxim(Director):
    def visit(self, department):
        department.pollinate(self)


class Vadim(Worker):
    def visit(self, department):
        department.eat(self)


def department_generator(n):
    departments = Department.__subclasses__()
    for i in range(n):
        yield random.choice(departments)()


if __name__ == '__main__':
    nastya = Nastya()
    maxim = Maxim()
    vadim = Vadim()
    for department in department_generator(10):
        department.accept(nastya)
        department.accept(maxim)
        department.accept(vadim)
