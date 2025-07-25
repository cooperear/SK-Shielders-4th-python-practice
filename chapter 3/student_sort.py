student_dict = {
    "김철수": [20, "컴퓨터공학과"],
    "이영희": [22, "영어영문학과"],
    "박민수": [21, "경영학과"],
    "최수진": [23, "수학과"]
   }


print("나이순으로 정렬된 학생 목록 ")
sorted_students = dict(sorted(student_dict.items(), key=lambda x: x[1][0]))

for name, info in sorted_students.items():
    print(f"{name} ({info[0]}세) - {info[1]}")