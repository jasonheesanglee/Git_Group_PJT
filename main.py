import random

def firstN():
    num = random.randint(1,9)
    return num
    
<<<<<<< HEAD
    

=======
>>>>>>> 99aa4723b91c0f6c4ce7c9f96971996b499ba79a
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
