print('defaultdict')
print()

from collections import defaultdict

Departmens = (
    ('Имя отдела', 'Отдел Технологий'),
    ('Этаж', '5'),
    ('Телефон', '+74362372718'),
    ('Глава отдела', 'Вадим Салмаков Ильич'),)
beneficial_Departmens = defaultdict(list)
for name, Departmen in Departmens:
    beneficial_Departmens[name].append(Departmen)
print(beneficial_Departmens)

print()
print('OrderedDict')
print()

from collections import OrderedDict

Organizations = OrderedDict([("кабинет", 120), ("офис", 170), ("аудитория", 160)])
for key, value in Organizations.items():
    print(key, value)

print()
print('Counter')
print()

from collections import Counter

Staff_names = ['Андрей',
               'Максим',
               'Вадим',
               'Вадим',
               'Максим',
               'Максим',
               ]

count = Counter(Staff_names)
print(count)

print()
print('deque')
print()

from collections import deque

d = deque([2, 4])
d.extendleft([0])
d.extend([6, 8])
print(d)

print()
print('namedtuple')
print()

from collections import namedtuple

address = namedtuple('address', 'name home korpus')
Дачная = address(name="Дачная", home=49, korpus="к4")
print(Дачная)
print(Дачная.name)
print(Дачная.home)
print(Дачная.korpus)

print()
print('enum.Enum')
print()

from collections import namedtuple
from enum import Enum


class Staff(Enum):
    programist = 1
    director = 2
    dizaner = 3


Staff1 = namedtuple('Project_organization', 'name age type')
Vadim = Staff1(name="Perry", age=26, type=Staff.programist)
Maksim = Staff1(name="Maksim", age=29, type=Staff.programist)
Olga = Staff1(name="Tom", age=53, type=Staff.director)
Nastia = Staff1(name="Charlie", age=30, type=Staff.dizaner)

print(Vadim)
print(Maksim)
print(Olga)
print(Nastia)

