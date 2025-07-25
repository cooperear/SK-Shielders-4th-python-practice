integer = int(input("숫자를 입력하시오 "))
print(f"{integer}은(는) 소수입니다." if all(integer % i != 0 for i in range(2, int(integer**0.5) + 1)) and integer > 1 else f"{integer}은(는) 소수가 아닙니다.")
