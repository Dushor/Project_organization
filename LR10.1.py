import random


class project_work:
    def __init__(self):
        self.types = []

    @staticmethod
    def factory(type):
        class Circle(project_work):
            def began(self):
                print('work.began')

            def finished(self):
                print('work.finished')

        class Square(project_work):
            def began(self):
                print('corporate.began')

            def finished(self):
                print('corporate.finished')

        if type == 'work':
            return Circle()
        elif type == 'corporate':
            return Square()
        else:
            raise ValueError('Bad shape creation: ' + type)

    def shape_name_gen(n):
        shapes = ['work', 'corporate']
        for i in range(n):
            yield project_work.factory(random.choice(shapes))


if __name__ == '__main__':
    for shape in project_work.shape_name_gen(7):
        shape.began()
        shape.finished()
