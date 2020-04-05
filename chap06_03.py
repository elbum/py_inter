# 병행성 concurrency - 한 컴퓨터가 여러 일을을 동시에 수행  1:N -> 단일 프로그램 안에서 여러일을 쉽게 해결
# coroutine 이 해결해줌 :

# 병렬성 - 여러 컴퓨터가 여러 작업을 동시에 수행  N:M -> 속도


# coroutine : 단일 스레드에서 , 스택을 기반으로 동작하는 비동기 작업
# 쓰레드 : os관리 , CPU코어에서 실시간  , 시분할 비동기 작업 -> 멀티스레드
# yield <-> send : 메인 <-> 서브
# 코루틴 제어 , 상태 , 양방향 전송

# 서브루틴 : 메인루틴 호출 -> 서브루틴에서 수행 (흐름제어)
# 코루틴 : 루틴 실행 중 중지 -> 동시성 프로그래밍
# 코루틴 : 스레드에 비해 오버헤드 감소
# 쓰레드 : 싱글스레드 -> 멀티스레드 -> 복잡 -> 공유되는 자원 -> 교착상태 발생 가능성,
#        컨텍스트 스위칭 비용이 큼!!!! 자원 소비 가능성 증가.


# 코루틴 Ex1
def coroutine1():
    print('>>> coroutine started.')
    i = yield
    print('>>> coroutine recieved : {}'.format(i))


# 제너레이터 선성
cr1 = coroutine1()
print(cr1, type(cr1))

# yield 지점까지 서브루틴을 수행
next(cr1)
# 값 전송
cr1.send(10)   # auto next


# 잘못된 사용   next 없이 send
cr2 = coroutine1()
# cr2.send(100)


# 코루틴 Ex2 : 상태값 확인
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : Yield 대기 상태
# GEN_CLOSED : 실행 완료 상태

def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x    # 왼쪽은 받는거 오른쪽은 주는거
    print('>>> coroutine received : {}'.format(y))
    z = yield x+y
    print('>>> coroutine received : {}'.format(z))


cr3 = coroutine2(10)
print(next(cr3))
