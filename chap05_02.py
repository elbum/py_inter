# 일급함수
# 클로저 기초


b = 20
# 변수 범위 scope


def func_v1(a):
    global b
    print(a)
    print(b+10)
    b = 1


func_v1(10)
print(b)

# 클로저 사용 이유
# 서버프로그래밍 핵심 => 동시성 제어
# 교착상태, 레이스컨디션
# 클로저는 공유하되 변경되지 않음 (Immutable , Readonly) 적극적으로 사용 -> 함수형 프로그래밍
# 클로저는 불변자료구조 및 atom,STM -> 멀티스레드 프로그래밍에 강점

a = 100
print(a+100)
print(a+1000)  # 1200 나오게 하려면

# 클래스로 구현


class Averager:
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print('inner ==> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series)/len(self._series)


# 생성
averager_cls = Averager()
print(dir(averager_cls))

print(averager_cls(10))
print(averager_cls(10))
print(averager_cls(10))
print(averager_cls(50))
