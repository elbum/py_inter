# hash summary
# hash table can manage large datasets efficiently.

# dict 및 set 심화
# immutable dict

from unicodedata import name
from dis import dis
from types import MappingProxyType
d = {'key1': 'value1'}

# read only
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))

d['key2'] = 'value2'

# cannot assign
# d_frozen['key2'] = 'value2'

print('\n\n\n')


s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Mango', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Mango', 'Kiwi'])
s3 = {3}
s4 = {}
s5 = set()
s6 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Mango', 'Kiwi'})


print(s1)
print(type(s4))
print(type(s5))

s1.add('Melon')
print(s1)

# s6.add('Melon')  # 불가

print(s2)
print(s3)
print(s4)


# 선언 최적화
# 파이썬은 실행할때 인터프리터가  바이트코드를 실행

print('----------------------')
print(dis('{10}'))
print('----------------------')
print(dis('set({10})'))   # 미세하지만 좀더 어셈블 단계가 있음.


# set comprehension
print({chr(i) for i in range(0, 256)})

print({name(chr(i), '') for i in range(0, 256)})
