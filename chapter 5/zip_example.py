students = ['김철수', '이영희', '박민수', '최수진']
scores = [85, 92, 78, 95]

dict_scores = {student: score for student, score in zip(students, scores)}

for st, sc in dict_scores.items():
    print(f"{st} : {sc}점")
print(f"점수별 학생 딕셔너리: {dict_scores}")