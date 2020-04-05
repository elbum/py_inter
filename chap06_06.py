# 병렬 . futures 동시성
# 비동기 작업을 동시에 시작
# 지연시간 (block) CPU 및 리소스 낭비 방지 -> File 쓰거나 Network I/O 관련 작업 -> 동시성 활용 권장
# 비동기 작업과  적합한 프로그램일 경우 압도적으로 성능 향상.

# futures 패키지 : 비동기 실행을 위한 API 를 고수준으로 작성 -> 사용하기 쉽도록 새선
# concurrent.Futures
# 1. 멀티스레딩 / 멀티프로세싱 API 를 통일 -> 매우 사용하기 쉬움
# 2. 실행중인 작업 취소,완료체크 , 타임아웃 옵션, 콜백함수 , 동기화코드 매우 쉽게 작성 -> promise 개념


# 2가지 핵심패턴
# concurrent.futures 사용법 1
# concurrent.futures 사용법 2


# GIL : Global Interpreter Lock
# 두개 이상의 스레드가 동시에 실행될때 , 하나의 자원을 액세스하는경우 문제를 방지하기위해  사용됨
# GIL 실행 , 리소스 전체에 락이 걸린다. context switch (문맥교환)
#

# GIL 우회
# 멀티프로세싱


import os
import time
from concurrent import futures

WORK_LIST = [100000,1000000,10000000,100000000]

def sum_generator(n):
    return sum(n for n in range(1,n+1))

def main():
    # Worker count
    worker = min(10,len(WORK_LIST))
    # 시작시간
    start_time = time.time()

    # 결과건수
    # ProcessPoolExecutor
    # ThreadPoolExecutor
    with futures.ProcessPoolExecutor(max_workers=worker) as executor:
        # map 은 작업순서를 유지하고 즉시실행함.
        result = executor.map(sum_generator,WORK_LIST)






    # 종료시간
    end_time = time.time() - start_time

    msg = '\n Result -> {} time : {:.2f}s'
    print(msg.format(list(result),end_time))

if __name__=='__main__':
    main()
