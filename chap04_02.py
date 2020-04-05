# 시퀀스형
# 컨테이너형 container : 서로다른 자료형을 담음. list , tuple , collections.deque
# 플랫 flat : 한개의 자료형 str , bytes , bytearray , array.array , memoryview
# 가변() mutable : list , bytearray , array.array, memoryview , deque
# 불변() immutable : tuple , str  , bytes

# 튜플 고급
# unpacking
print(divmod(100, 9))
print(divmod(*(100, 9)))
print(*divmod(*(100, 9)))


x, y, *rest = range(10)
print(x, y, rest)

x, y, *rest = range(2)
print(x, y, rest)

x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)

print()
print()
print()

# mutable vs immutable
l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2

print(l, id(l))
print(m, id(m))

l *= 2
m *= 2
print(l, id(l))
print(m, id(m))  # no change

print()
print()
print()

# sort vs sorted

# sorted : 정렬 후 새로운 객체로 반환
f_list = ['orange', 'apple', 'mango',
          'papaya', 'lemon', 'strawberry', 'coconut']
print(f_list)
print('sorted - ', sorted(f_list))
print(f_list)
print('sorted - ', sorted(f_list, reverse=True))
print('sorted - ', sorted(f_list, key=len))
print('sorted - ', sorted(f_list, key=lambda x: x[-1]))  # 끝글자 기준
print('sorted - ', sorted(f_list, key=lambda x: x[-1], reverse=True))


# sort : 정렬 후 객체를 직접 변경 (원본을 건드림)
print(f_list)
print('sort - ', f_list.sort())  # no return
print(f_list)
print('sort - ', f_list.sort(reverse=True))  # no return
print(f_list)
print('sort - ', f_list.sort(key=len))  # no return
print(f_list)


# List vs Array 적합한 사용
# List :  다양한 자료 , 범용적 , 융통성

# Array : 숫자기반 = 리스트와 거의 호환됨

