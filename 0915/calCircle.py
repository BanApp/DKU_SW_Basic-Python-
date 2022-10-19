import sys
import math

def circle():
    print("원의 반지름을 입력하세요")
    r = int(sys.stdin.readline())
    a = (r*r*math.pi,math.pi*r*2)

    return a


x,y = circle()

print("원의 넓이는 " + str(x) + "이고" + " 원의 둘레는 " + str(y) +" 이다.")