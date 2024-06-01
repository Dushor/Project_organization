class Head:
    def __init__(self, n):
        self.name = n

    def write(self):
        print(self.name)


class Department(Head):
    def __init__(self, dn, n):
        Head.__init__(self, n)
        self.department_number = dn

    def write(self):
        print(self.name, self.department_number)


h = Head('Maksim')
h.write()

d = Department(23, 'Program')
d.write()
