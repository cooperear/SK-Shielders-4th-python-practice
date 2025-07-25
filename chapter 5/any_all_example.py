list1 = [2, 4, 6, 8, 10]
list2 = [1, 3, 5, 7, 9]

def  a(l:list):
    print(f'{l}')
    print(f"모든 수가 짝수인가? {True if all(x % 2 == 0 for x in l) else False}")
    print(f'하나라도 10을 초과하나? {True if any(x > 10 for x in l) else False}')

a(list1)
a(list2)

