# Special Method (= Magic Method)
# Python핵심 >  Sequence , Iterator , Function , Class

# 클래스안에 정의할 수 있는 특별(built-in) method

# 벡터
# (5,2) + (4,3) = (9,5)
# (10,3) * 5 = (50,15)
# Max((5,10)) = 10


class Vector(object):
    def __init__(self, *arg):
        '''
        Create a vector, example : v = Vector(5,10)
        '''
        if len(arg) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = arg

    def __repr__(self):
        '''
        return the vector informations.
        '''
        return 'Vector(%r,%r)' % (self._x, self._y)

    def __add__(self, other):
        '''Return vector add value'''
        return Vector(self._x+other._x, self._y+other._y)

    def __sub__(self, other):
        '''Return vector sub value'''
        return Vector(self._x-other._x, self._y-other._y)

    def __mul__(self, y):
        return Vector(self._x*y, self._y*y)

    def __bool__(self):
        return bool(max(self._x, self._y))


v1 = Vector(5, 7)
v2 = Vector(25, 35)
v3 = Vector()

print(v1+v2)
print(v1+v3)
print(v2*3)

print(v1, v2, v3)
print(v1.__init__.__doc__)
