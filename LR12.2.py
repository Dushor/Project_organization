class Agreement:
    def __init__(self):
        self.__templateMethod()

    def __templateMethod(self):
        for i in range(5):
            self.customize1()
            self.customize2()
            self.customize3()


class MyAg(Agreement):
    def customize1(self):
        print('прибытие в мероприятие')

    def customize2(self):
        print('обсуждение о цене')

    def customize3(self):
        print('покупка договора')


if __name__ == '__main__':
    MyAg()
