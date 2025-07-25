
price,discount = int(input("상품의 가격을 입력하세요: ")), int(input("할인율을 입력하세요(%): "))

print(f"원래 가격: {price}원")
print(f"할인율: {discount}%")
print(f"할인 금액: {(price * discount / 100):.0f}원")
print(f"최종 가격: {(price - (price * discount / 100)):.0f}원")
