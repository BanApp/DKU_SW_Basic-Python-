import time

now = time.time()
thisYear = int(1970+now//(365*24*3600))

print("올해는 " + str(thisYear) +"년 입니다.")
age = int(input("현재나이는? "))
p_year = int(input("내 나이를 알고싶은 년도: "))

print(str(p_year)+"년에는 " + str(age+p_year-thisYear) +"세가 됩니다.")