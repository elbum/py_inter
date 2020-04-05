# 코루틴 Ex2 : 상태값 확인
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : Yield 대기 상태
# GEN_CLOSED : 실행 완료 상태


from inspect import getgeneratorstate


def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x    # 왼쪽은 서브루틴이 받는거 오른쪽은 메인루틴에게 주는거
    print('>>> coroutine received : {}'.format(y))
    z = yield x+y
    print('>>> coroutine received : {}'.format(z))


cr3 = coroutine2(10)

print(getgeneratorstate(cr3))

print(next(cr3))
print(getgeneratorstate(cr3))

print('main routine', cr3.send(100))
print('main routine', cr3.send(100))
