# Special Method (= Magic Method)
# Python핵심 >  Sequence , Iterator , Function , Class

# 클래스안에 정의할 수 있는 특별(built-in) method


class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info : {} , {}'.format(self._name, self_price)

    def __add__(self, x):
        print("called __add__")
        return self._price + x._price

    def __sub__(self, x):
        print("called __sub__")
        return self._price - x._price

    def __le__(self, x):
        print("called __le__")
        if self._price <= x._price:
            return True
        else:
            return False

    def __ge__(self, x):
        print("called __ge__")
        if self._price >= x._price:
            return True
        else:
            return False


s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

print(s1+s2)
print(s1-s2)
print(s1 >= s2)
print(s1 <= s2)
