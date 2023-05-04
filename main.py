import random

def firstN():
    num = random.randint(1,9)
    return num
    
def secondN():
    num = random.randint(1,9)
    return num


def ThardN():
    num = random.randint(1,9)
    return num

def FourthN():
    num = random.randint(1,9)
    return num

fir = firstN()
sec = secondN()
thi = ThardN()
fou = FourthN()

# 랜덤 숫자가 같다면 계속 반복
while(fir == sec):
    sec = random.randrange(1, 10, 1)
while(fir == thi or sec == thi):
    thi = random.randrange(1, 10, 1)
while(fir == fou or sec == fou or thi == fou):
    fou = random.randrange(1, 10, 1)

try_number = 0
strike_number = 0
ball_number = 0

correct_number=[fir,sec,thi,fou]

print("숫자야구를 시작합니다.")
print("--------------------------")
while (strike_number < 4):

    number = str(input("숫자 4자리를 입력하세요: "))

    strike_number = 0
    ball_number = 0

    for i in range(0, 4): # i 값의 범위 0~3
        for j in range(0, 4):
            if(number[i] == str(correct_number[j]) and i == j):
                strike_number += 1
            elif(number[i] == str(correct_number[j]) and i != j):
                ball_number += 1
    print("결과: [",strike_number,"]스트라이크 [",ball_number,"]볼")
    try_number += 1

print("--------------------------")
print("축하합니다! 정답입니다!")
print("[",try_number,"]번 만에 맞췄습니다")
