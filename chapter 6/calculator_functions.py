

def calculator_functions(x,y,c):
    
    return {
        '+': x + y,
        '-': x - y,
        '*': x * y,
        '/': x / y if y != 0 else '0으로 나누셨군요?',
    }.get(c, None)

print(f'{calculator_functions(10,5,'+')}')
print(f'{calculator_functions(10,5,'-')}')
print(f'{calculator_functions(10,5,'*')}')
print(f'{calculator_functions(10,5,'/')}')
