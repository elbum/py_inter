# AsyncIO
# 비동기 IO Coroutine 작업
# Generator -> 반복적인 객체 Return
# Non Blocking 비동기 처리

# Blocking I/O
# 호출된 함수가 자신의 작업이 완료될 때 까지 제어권을 가지고 있음. 타함수는 대기
# urllib , requests

# Non-Blocking I/O
# 호출된 함수가(서브루틴)  리턴후 호출한 함수(메인루틴) 에 제어권 전달. ->  타 함수는 일 지속

# 스레드 : 디버깅,자원접근시 레이스컨디션(경쟁상태),데드락) -> 고려 후 코딩
# 코루틴 장점 : 하나의 루틴만 실행 -> 락관리 필요X -> 제어권으로 실행 ->
# 단점 사용함수가 비동기로 구현되 있어야 함, 또는 직접 비동기로 구현해야 함

import asyncio
import timeit
from urllib.request import urlopen  # block 함수  -> 스레드와 결합해서 -> async 구현
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import threading

# 실행시작시간
start = timeit.default_timer()

# 서비스 방향이 비슷한 사이트 (게시판성 )
urls = ['http://daum.net', 'https://naver.com', 'http://mlbpark.donga.com',
        'https://tistory.com', 'https://wemakeprice.com']


async def fetch(url, executor):
    # 쓰레드명
    print('Thread name : ', threading.current_thread().getName(), 'Start', url)

    # 실행
    res = await loop.run_in_executor(executor, urlopen, url)
    soup = BeautifulSoup(res.read(), 'html.parser')

    # 전체 페이지 소스
    # print(soup.prettify())

    result_data = soup.title

    print('Thread name : ', threading.current_thread().getName(), 'Done', url)
    # 결과 반환
    return result_data


async def main():
    # 스레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)

    # future 객체 모아서 gather 에서 실행
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]

    # 결과 취합
    rst = await asyncio.gather(*futures)

    print()
    print('Result : ', rst)


if __name__ == "__main__":
    # 루프 초기화
    loop = asyncio.get_event_loop()
    # 작업 완료까지 대기
    loop.run_until_complete(main())
    # 수행 시간 계산
    duration = timeit.default_timer() - start
    # 총실행시간
    print('Total Running Time :', duration)
