def searching_fruit(inventory):
    fruit = input("찾을 과일을 입력하세요: ")
    if inventory.count(fruit) > 0:
        print(f"{fruit}이(가) 목록에 있습니다.")
    else:
        print(f"{fruit}이(가) 목록에 없습니다.")

fruits = ['사과', '바나나', '오렌지', '포도', '딸기']

searching_fruit(fruits)