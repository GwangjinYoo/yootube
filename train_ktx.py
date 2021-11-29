# 이 링크를 참고해서 만들었음 https://github.com/carpedm20/korail2
# 따로 입력을 받지 않고, 정보를 모두 입력한 후에 돌려야 함
# 입력한 시간과 가장 가까운 시간의 열차를 찾아서 예약해줌. 예약이 되면 결제는 빠르게 해야 함

from korail2 import *
from time import sleep

# 로그인
korail = Korail("ID입력", "비밀번호입력")

# 정보 설정
dep = '출발역(예, 용산)'
arr = '도착역(예, 순천)'
date = '출발 날짜(예, 20190614)'
time = '출발 시각(예, 214500)'
att = 0
finish = 0
# 인원 설정 (어른 1, 어린이 1)
psgrs = [AdultPassenger(), ChildPassenger()]

# 열차 확인, 2초마다 0.1초 단위로 3개의 열차를 순서대로 시도
while True:
	for i in range(3):
		trains = korail.search_train(dep, arr, date, time, TrainType.KTX, passengers=psgrs, include_no_seats=True)		
		for j in range(3):
			att += 1        
			print(att, trains[j])
			try:
				seat = korail.reserve(trains[j], passengers=psgrs)
			except:
				sleep(0.1)
				continue
			finish = 1
			break
		if finish: break
	if finish: break
	sleep(2)

# 예약 확인
print("드디어 예약 성공!\n", seat)
