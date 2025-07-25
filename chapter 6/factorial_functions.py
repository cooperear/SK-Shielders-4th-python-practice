def factorial_functions(a:int):
    return 0 if a==0 else 1 if a==1 else a * factorial_functions(a-1)



print(f'{factorial_functions(3)}')