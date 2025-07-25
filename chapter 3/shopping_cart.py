store = {'사과':1000, '바나나':800, '오렌지':1500}
cart = {}

def add_item_to_cart(item, quantity):

    if item in store:
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity

add_item_to_cart('사과', 2)
add_item_to_cart('바나나', 3)
add_item_to_cart('오렌지', 1)

for item, quantity in cart.items():
    print(f"{item} : {quantity}개, 개당 {store[item]}원 ")

print(f"총 금액: {sum(store[item] * quantity for item, quantity in cart.items())} 원")
