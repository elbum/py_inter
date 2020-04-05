# 병행성 concurrency - 한 컴퓨터가 여러 일을을 동시에 수행  1:N -> 단일 프로그램 안에서 여러일을 쉽게 해결
# coroutine 이 해결해줌 :


# 병렬성 - 여러 컴퓨터가 여러 작업을 동시에 수행  N:M -> 속도

import itertools


def generator_ex1():
    print('Start')
    yield 'Apoint '
    print('Continue')
    yield 'B point'
    print('END')


temp = iter(generator_ex1())

# print(temp)
# print(next(temp))
# print(next(temp))
# print(next(temp))

# for v in temp:
#     print(v)

# for v in generator_ex1():
#     print(v)
# for v in temp:
#     print(v)

# temp2 = [x*3 for x in generator_ex1()]
# print(temp2)

# for i in temp2:
#     print(i)

temp3 = (x*3 for x in generator_ex1())
print(temp3)

for i in temp3:
    print(i)

# 중요함수

gen1 = itertools.count(1, 2.5)
# print(next(gen1))
# print(next(gen1))

gen2 = itertools.takewhile(lambda x: x < 1000, itertools.count(1, 2.5))
# for v in gen2:
#     print(v)


# 필터반대
gen3 = itertools.filterfalse(lambda x: x < 3, [1, 2, 3, 4, 5])
for v in gen3:
    print(v)

# 누적합계
gen4 = itertools.accumulate([x for x in range(1, 101)])
for v in gen4:
    print(v)

gen5 = itertools.chain('ABCDE', range(1, 11, 2), range(1, 10))
print(list(gen5))

gen6 = itertools.chain(enumerate('ABCDE'))
print(list(gen6))


# 연산 (경우의수)
gen7 = itertools.product('ABCDE', repeat=3)
print(len(list(gen7)))

# 그룹화 !~
gen8 = itertools.groupby('AABBCCCCDDEEE')
# print(list(gen8))
for c, group in gen8:
    print(c, ':', list(group))
