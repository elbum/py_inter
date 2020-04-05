# 데코레이터

# 장점
# 1.중복제거,코드간결,공통함수작성
# 2.로깅 , 프레임워크 , 유효성체크 -> 공통함수
# 3. 조합해서 사용 용이


# 단점
# 1. 디버깅 가독성 , 불편
# 2. 특정 기능에 한정된 함수는 -> 단일 함수가 유리할 수 있다


# 데코레이터 실습
import time


def perf_clock(func):
    def perf_clocked(*args):
        # 함수시작시간
        st = time.perf_counter()
        # 실행
        result = func(*args)
        # 함수종료시간
        et = time.perf_counter() - st
        # 함수명
        name = func.__name__
        # 함수파라미터
        arg_str = ', '.join(repr(arg) for arg in args)
        # 출력
        print('[%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))

        return result
    return perf_clocked


@perf_clock
def time_func(seconds):
    time.sleep(seconds)


@perf_clock
def sum_func(*numbers):
    return sum(numbers)


# 데코레이터 미활용
none_deco1 = perf_clock(time_func)
none_deco2 = perf_clock(sum_func)

print(none_deco1, none_deco1.__code__.co_freevars)
print(none_deco2, none_deco2.__code__.co_freevars)

print('-'*40, 'Called None Decorator -> time_func')
print()
none_deco1(1.5)
print('-'*40, 'Called None Decorator -> time_func')
print()
none_deco2(100, 200, 300, 400, 500)
print('\n\n\n')


# 데코레이터 사용
print('-'*40, 'Called Decorator -> time_func')
print()
time_func(1.5)
print('-'*40, 'Called Decorator -> time_func')
print()
sum_func(100, 200, 300, 400, 500)

a = [100, 200, 300, 400, 500]
b = ','.join(str(a) for a in a)
print(b)
