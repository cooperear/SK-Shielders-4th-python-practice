dict_grades = {
    "김철수": 85,"이영희": 92,
    "박민수": 78, "최수진": 95}

for key, value in dict_grades.items():
    print(f"{key} : {value}점")

print(f"평균 점수: {sum(dict_grades.values()) / len(dict_grades):.1f}점")
