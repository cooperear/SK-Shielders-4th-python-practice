import json
import pandas as pd


list_name = ['박시훈','이철곤','마철두']
list_age = [25,11,23]
list_sex = ['남','여','남']

df  = pd.DataFrame(columns = ['이름','나이','성별'])


for n,a,s in list_name,list_age,list_sex:
    df_new_row = pd.DataFrame.from_records([{'이름':n,'나이':a,'성별':s}])
    df = pd.concat([df,df_new_row],ignore_index=True)




df.to_json('data.json')
print(f'데이터가 data.json에 저장되었습니다.')


df2 = pd.read_json('data.json')



for i in df2.items():
    print(i)

