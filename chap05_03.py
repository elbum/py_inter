# 클로저
# 외부에서 호출된 함수의 변수값 , 상태(레퍼런스) 복사 후 저장. -> 후에 접근가능

# averager 를 클로저로 구현


def closure_ex1():
    #  Free variable
    # 클로저 영역
    series = []
    print('Im closure ex1')

    def averager(v):
        nonlocal series
        series.append(v)
        print('inner ==> {} / {}'.format(series, len(series)))
        return sum(series)/len(series)
    return averager


avg_closure1 = closure_ex1()

print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))

print('\n\n\n')

print(dir(avg_closure1))
print()
print(avg_closure1.__code__.co_freevars)
print(avg_closure1.__closure__[0].cell_contents)


# 잘못된 클로저
# def closure_ex2():
#     cnt = 0
#     total = 0

#     def averager(v):
#         cnt += 1
#         total += v
#         return total/cnt
#     return averager

# avg_closure2 = closure_ex2()
# print(avg_closure2(10))


# 수정
def closure_ex3():
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total/cnt
    return averager


avg_closure3 = closure_ex3()

print(avg_closure3(10))
