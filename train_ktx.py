# 이 링크를 참고해서 만들었음 https://carpedm20.github.io/korail2/
# 따로 입력을 받지 않고, 정보를 모두 입력한 후에 돌려야 함
# 입력한 시간과 가장 가까운 시간의 KTX를 찾아서 예약해줌. 예약이 되면 결제는 빠르게 해야 함

from korail2 import *
from time import sleep

# 로그인
korail = Korail("ID입력", "비밀번호입력")

# 정보 설정
dep = '출발역(예, 용산)'
arr = '도착역(예, 순천)'
date = '출발 날짜(예, 20190614)'
time = '출발 시각(예, 214500)'
att = 1

# 열차 확인, 5초에 3번씩
while True:
    for i in range(3):
        trains = korail.search_train(dep, arr, date, time, TrainType.KTX, include_no_seats=True)
        print(trains[0])
        if str(trains[0]).find("매진") == -1:
            if str(trains[0]).find("역발매중") == -1:
                if str(trains[0]).find("대기") == -1:
                    seat = korail.reserve(trains[0])
                    finish = 1
                    break
        print(att)
        att += 1
        finish = 0
    if finish: break
    sleep(5)

# 예약 확인
print("드디어 예약 성공!\n", seat)
