# 병행성 Concurrency
# 이터레이터 , 제너레이터
# 제너레이터는 이터를 반환

# 반복이 가능한 타입
# collections , text file , list , dict , set , tuple , unpacking , *args => iterable

# 반복이 가능한 이유 iter(x) 함수 호출
from collections import abc
t = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
# print(dir(t))


# for 를 구현함
w = iter(t)
while True:
    try:
        print(next(w))
    except StopIteration:
        break


print(hasattr(t, '__iter__'))
print(isinstance(t, abc.Iterable))


# next pattern 으로 구현
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration.')
        self._idx += 1
        return word

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)


wi = WordSplitter('Do today what you could do tomorrow')
print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))

print('\n\n\n')

# generator pattern 으로 구현
# 1. 지능형 리스트 , 딕셔너리 , 집합 -> 데이터 양 증가시 메모리 증가 -> 제너레이터 권장
# 2. 단위 실행 가능한 코루틴 (Coroutine) 구현과 연동
# 3. 작은 메모리 조각


class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word  # this is key
        return

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)


wg = WordSplitGenerator('Do today what you could do tomorrow')
wt = iter(wg)
print(wg)

for i in wt:
    print(i)
