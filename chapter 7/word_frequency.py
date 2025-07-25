
#print(full_text)
import os

def count(s:str, p:str):
    full_text = ""
    with open(os.path.abspath(p),'r',encoding='utf-8') as f:
    
        for i in f.readlines():
            full_text += i
        f.close()

    splited_text = full_text.split()
    #print(splited_text)
    print(f'{s} : {full_text.count(s)}')

count('공무','./난중일기.txt')
count('원균','./난중일기.txt')
count('판옥선','./난중일기.txt')
count('전하','./난중일기.txt')
count('활','./난중일기.txt')
count('곤장','./난중일기.txt')
count('왜적','./난중일기.txt')
count('파도','./난중일기.txt')