import pandas as pd

dict_score = {"이름":['김철수','이영희','박민수','최수진'],"점수":[19,29,32,49]}

a = pd.DataFrame.from_dict(dict_score,orient='columns')

a.to_csv('./grades.csv')

print('학생 성적이 grades.csv에 저장되었습니다.')

read = pd.read_csv('./grades.csv',index_col=0)
print('분석완료')

for i,r in read.iterrows():
    print(f'이름:{r['이름']} 점수: {r['점수']}')
print(f'평균 점수 = {read['점수'].mean():.2f}')

