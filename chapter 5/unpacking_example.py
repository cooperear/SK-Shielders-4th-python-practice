
def args(*args):
    ascii = list(chr(c) for c in range(ord('a'), ord('z') + 1))
    return dict(zip(ascii,list(args)))


def kwargs(**kwargs):
    return kwargs

def kfun(s:str,d = dict):
    for k,v in d.items():
        print(f'{s}: {k} = {v}',end = ", ")
    print('\n')


kfun("좌표 :", kwargs(x = 10, y = 20))
print("리스트 언패킹",args(1,2,3,4))



print(f"가변인수의 합: {sum(args(1, 2, 3, 4, 5))}")
kfun ("키워드 인수들",kwargs(name = '박시훈', age = 27, city = 'paju'))


