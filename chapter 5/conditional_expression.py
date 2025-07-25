def conditiona_expression(score:int,grade:dict):
     return next( (k for k,v in grade.items() if score >= v),None) 

grade_dict = {'a':90,'b':80,'c':70,'d':60,'f':0}

age_dict = {'성인':18,'미성년자':0}


print(f'{conditiona_expression(0,grade_dict)}')
print(f'{conditiona_expression(15,age_dict)}')

a = list(i for i in range(-10,10,2))
print(f'숫자들의 최대값: {max(a)}')

print(f'양수들 = {list(x for x in a if x > 0)}')