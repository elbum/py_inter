# 시퀀스형
# 컨테이너형 container : 서로다른 자료형을 담음. list , tuple , collections.deque
# 플랫 flat : 한개의 자료형 str , bytes , bytearray , array.array , memoryview
# 가변() mutable : list , bytearray , array.array, memoryview , deque
# 불변() immutable : tuple , str  , bytes

# 해시 테이블
# key 에 value 를 저장하는 구조
# 키값의 연산결과에 따라 직접접근이 가능!
# key 값을 해싱 함수 -> 해쉬 주소 -> key 에 대한 value 참조

# print(__builtins__.__dict__)

t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])
print(hash(t1))  # immutable only!~
# print(hash(t2)) ## mutable 이라 해시불가

# Dict Setdefault 예제.  recommended
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)


# Use setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)
# wow!~

# 주의
new_dict3 = {k: v for k, v in source}
print(new_dict3)
