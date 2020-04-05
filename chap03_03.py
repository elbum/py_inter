# Special Method (= Magic Method)
# Python핵심 >  Sequence , Iterator , Function , Class
# 클래스안에 정의할 수 있는 특별(built-in) method

# 일반튜플
# 두점간의 거리

from collections import namedtuple
from math import sqrt

pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

leng1 = sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)

print(leng1)


# 네임드튜플

# 선언
Point = namedtuple('Point', 'x y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3, pt4.x)
leng2 = sqrt((pt3.x-pt4.x)**2 + (pt3.y-pt4.y)**2)
print(leng2)

# 또다른 선언
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x,y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True)  # default = false

# dict to unpacking
temp_dict = {'x': 75, 'y': 55}


p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)
print()
print(p1, p2, p3, p4, p5)

temp = [52, 38]
p6 = Point1._make(temp)

print(p6._fields)

# _asdict() : orderedDict 반환
print(p6._asdict())


# lets practice~!
Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹리스트
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()


students = [Classes(rank, number) for rank in ranks for number in numbers]
print(len(students))
print(students)

# better
students2 = [Classes(rank, number)
             for rank in 'A B C D'.split()
             for number in [str(n) for n in range(1, 21)]]

print(len(students2))
for s in students2:
    print(s)
