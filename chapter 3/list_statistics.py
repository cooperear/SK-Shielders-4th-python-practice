def statistics(numbers: list):
    print(f"숫자들: {numbers}")
    print(f"합계: {sum(numbers)}")
    print(f"평균: {sum(numbers) / len(numbers):.2f}")

numbers = [10, 20, 30, 40, 50]

statistics(numbers)
