import datetime as dt
import random  as rd


now = dt.datetime.now()

print(f"현재 날짜와 시간 = {now}")
formated_now = now.strftime("%Y년 %m월 %d일  %A")
print(formated_now)

print(f'임의의 숫자 = {(rd.randint(0,100))}')

print(f'임의의 실수 = {rd.random()* (10**rd.randint(0,6))}')

list_f = ['포도', '사과', '오렌지', '바나나', '딸기']

print(f'list 중에서 하나 고르기 : {rd.choice(list_f)}')

print(f'섞인 리스트 : {rd.sample(list_f,len(list_f))}')
