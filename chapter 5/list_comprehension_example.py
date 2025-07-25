list_integer =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2 = [x for x in list_integer if x % 2 == 0]

print(f"짝수들:{list2}")
print(f"짝수의 제곱들: {[x**2 for x in list2]}")