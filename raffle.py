import random

# 인원 수 입력
n = int(input("추첨 돌릴 인원 수를 입력하세요: "))
k = int(input("당첨자 수를 입력하세요: "))

# 사람 수만큼 입력 받기
name = []
for i in range(n):
    print("\n", i+1, "번째 사람 이름을 입력하세요.")
    name.append(input())
print("\n")

# 추첨!
t = -1
for j in range(k):
    while True:
        c = random.randint(0, n-1)
        if t == c:
            continue
        t = c
        if k == 1:
            print("당첨자는 ", name[c], "입니다! 축하합니다!")
            break
        else:
            print(j+1, "번째 당첨자는 ", name[c], "입니다! 축하합니다!")
            break
