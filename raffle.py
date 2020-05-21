import random

# 인원 수 입력
candidate = int(input("추첨 돌릴 인원 수를 입력하세요: "))
winner = int(input("당첨자 수를 입력하세요: "))

# 사람 수만큼 입력 받기
name = []
for i in range(candidate):
    print("\n", i+1, "번째 사람 이름을 입력하세요.")
    name.append(input())
print("\n")

# 최초 추첨
raffle = random.randint(0, candidate-1)

# 결과 검증 및 발표
if winner == 1:
    print("당첨자는 ", name[raffle], "입니다! 축하합니다!")
else:
    result = []
    for j in range(winner):
        if j == 0:
            result.append(raffle)
            print(j+1, "번째 당첨자는 ", name[raffle], "입니다! 축하합니다!")
            continue

        # 2번째 이상 추첨 진행
        raffle = random.randint(0, candidate-1)

        while True:
            for k in range(j):
                if result[k] == raffle:
                    raffle = random.randint(0, candidate-1)
                    check = 1
                    break
                check = 0
            if check == 0:
                result.append(raffle)
                break

        print(j+1, "번째 당첨자는 ", name[raffle], "입니다! 축하합니다!")
