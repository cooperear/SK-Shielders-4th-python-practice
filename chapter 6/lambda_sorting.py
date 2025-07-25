list_scores = [('김철수', 85), ('이영희', 92), ('박민수', 78), ('최수진', 95)]



print(f'이름순 정렬: { (lambda:sorted(list_scores, key = lambda x: x[0]))()}')
print(f'점수순 정렬: { (lambda:sorted(list_scores, key = lambda x: x[1]))()}')
print(f'점수순 내림차순: { (lambda:sorted(list_scores, key = lambda x: x[1], reverse=True))()}')