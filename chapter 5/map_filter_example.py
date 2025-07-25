list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
above_5 = list(filter(lambda x: x > 5, list1))
def square(l:list):
    return l**2

print(f'원본 리스트: {list1}')
print(f'제곱한 리스트: {list(map(square,list1))}')


print(f'5보다 큰 수들: {above_5}')
print(f'5보다 큰 수들의 제곱: {list(map(square,above_5))}')