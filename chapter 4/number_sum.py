def number_sum(a:list):
    while True:
        i = input("정수를 입력하세요 (0을 입력하면 종료): ")
        if i == '0':
            break
        else:
            try:
                i = int(i)
                a.append(i)
            except ValueError as Ve:
                print("유효한 정수를 입력하세요.")
    print(f"입력된 정수의 합: {sum(a)}")
iist_integer = []
number_sum(iist_integer)