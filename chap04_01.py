# 시퀀스형
# 컨테이너형 container : 서로다른 자료형을 담음. list , tuple , collections.deque
# 플랫 flat : 한개의 자료형 str , bytes , bytearray , array.array , memoryview
# 가변() mutable : list , bytearray , array.array, memoryview , deque
# 불변() immutable : tuple , str  , bytes

# list comprehension
import array
chars = "+_)(*&^%$#@!~"

code_list1 = []
for s in chars:
    code_list1.append(ord(s))
print(code_list1)


code_list2 = [ord(s) for s in chars]
print(code_list2)

# comprehending lists + map + filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
print(code_list3)

code_list4 = list(filter(lambda x: x > 40, map(ord, chars)))
print(code_list4)

# inverse
print(''.join([chr(s) for s in code_list1]))


# Generator 사용

# making genrator # 메모리 유지.
tuple_g = (ord(s) for s in chars)
print(tuple_g)
print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g))


array_g = array.array('I', (ord(s) for s in chars))
print(array_g)
print(array_g.tolist())


# generator 예제
print(('%s' % c+str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)))

for s in ('%s' % c+str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)):
    print(s)


# 리스트 주의!
marks1 = [['~']*3 for _ in range(4)]
print(marks1)

marks2 = [['~']*3]*4
print(marks2)

# 수정
marks1[0][1] = 'X'
print(marks1)

marks2[0][1] = 'X'
print(marks2)  # ??????????????????   # 하나의 id 가 4번 복사됨

# 증명
print([id(i) for i in marks1])
print([id(i) for i in marks2])


# deep copy , shallow copy !!
