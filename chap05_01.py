# 일급함수
# 함수특징
# 1. 런타임 초기화
# 2. 변수 항당 가능
# 3. 함수인수 전달 가능
# 4. 함수 결과 반환 가능


from functools import partial
from operator import mul
from operator import add
from functools import reduce


def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)


class A:
    pass


print(set(sorted(dir(factorial)))-set(sorted(dir(A))))

var_func = factorial
print(list(map(var_func, range(1, 11))))


print([var_func(i) for i in range(1, 6) if i % 2])
# same
print(list(map(var_func, filter(lambda x: x % 2 == 1, range(1, 6)))))
print('\n\n\n')

# reduce
print(sum(range(1, 11)))
print(reduce(add, range(1, 11)))


# lambda !
# 가급적 주석, 가급적 함수 , 일반함수로 리팩토링  권장

# same
print(reduce(lambda x, t: x+t, range(1, 11)))


print('\n\n\n')


# callable : 메소드로 호출가능한지 확인
print(callable(str), callable(list), callable(var_func), callable(3.14))

# partial 사용법 : 인수고정 -> 콜백함수에
mul(1, 5)

five = partial(mul, 5)  # => 5 * ???

# 고정 추가
six = partial(five, 6)
print(five(10))
print(six())
print([five(i) for i in range(1, 11)])
