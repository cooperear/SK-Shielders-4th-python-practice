import logging
import datetime
import pandas as pd

logging.basicConfig(filename='factoriallog.txt',level=logging.DEBUG, format = '%(asctime)s %(levelname)s %(message)s',encoding='utf-8')


def factorial(n):
    logging.debug(f'start {n}')
    tot = 1

    for i in range(1,n+1):
        tot *= i
        logging.debug(f"{datetime.datetime.now()} {'짝수' if i % 2 == 0 else '홀수'} {i} is {str(i)} + total is + {str(tot)}")

    logging.debug(f"{datetime.datetime.now()}  end of factrorial {n}")
    return tot


print(factorial(10))
logging.debug(f'{datetime.datetime.now()}  end of program')


print("\n--- 짝수만 ---")
with open('factoriallog.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if '짝수' in line:
            print(line.strip())

print("\n--- 홀수만 ---")
with open('factoriallog.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if '홀수' in line:
            print(line.strip())

    
