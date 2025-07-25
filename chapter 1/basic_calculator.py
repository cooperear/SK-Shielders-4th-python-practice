x, y = (lambda a, b: [a, b])(int(input("첫 번째 숫자를 입력하세요: ")), int(input("두 번째 숫자를 입력하세요: ")))

print(f"{x} + {y} = {x+y}")
print(f"{x} - {y} = {x-y}")
print(f"{x} * {y} = {x*y}")
try:
    print(f"{x} / {y} = {(x/y):.2f}")
except ZeroDivisionError:  
    print("0으로 나눌 수 없습니다.")

    

