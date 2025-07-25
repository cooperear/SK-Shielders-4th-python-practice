def  statistics_function(*args):
    values = args[:-1]
    op = args[-1]
    return {
        'sum': lambda: sum(args[:-1]),
        'max': lambda: max(args[:-1]),
        'min': lambda: min(args[:-1]),
        'mean': lambda: sum(args[:-1]) / len(args[:-1]),
        'std': lambda: (sum((x - sum(args[:-1]) / len(args[:-1]))**2 for x in args[:-1]) / len(args[:-1]))**0.5
    }.get(args[-1], lambda: None)()


list_num =  [10, 20, 30, 40, 50]
print(f' 합계 : {statistics_function(*list_num,"sum")}')
print(f' 최대값 : {statistics_function(*list_num,"max")}')
print(f' 최소값 : {statistics_function(*list_num,"min")}')
print(f' 평균 : {statistics_function(*list_num,"mean")}')
print(f' 표준편차 :{statistics_function(*list_num, 'std')}' ) 
