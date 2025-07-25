integer = int(input("점수를 입력하세요: "))

match integer:
    case 90 | 100:
        print(f"점수 {integer}점의 학점은 A입니다.")
    case 80 | 89:
        print(f"점수 {integer}점의 학점은 B입니다.")
    case 70 | 79:
        print(f"점수 {integer}점의 학점은 C입니다.")
    case _:
        print(f"점수 {integer}점의 학점은 D입니다.")


    