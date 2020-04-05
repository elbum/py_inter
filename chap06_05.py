# coroutine ex3
# stop iteration 자동처리 (3.5 -> await 에서 해결해줌)
# 중첩코루틴 처리


def generator1():
    for x in 'AB':
        yield x
    for y in range(1, 4):
        yield y


t1 = generator1()
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))


t2 = generator1()
print(list(t2))
print()
print()

# iterator 를 순차적으로 반환


def generator2():
    yield from 'AB'
    yield from range(1, 4)


t3 = generator2()
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
