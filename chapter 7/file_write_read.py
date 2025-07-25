with open ('./test_text.txt', 'w',encoding='utf-8')as f:
    f.write('안뇽하세용 \n')
    f.write('cooperear이에요 \n')
    f.write('좋은 날씨에요 \n')
    f.write('파이썬 연습하고 있어요\n')

    f.close()

with open('./test_text.txt', 'r',encoding='utf-8')as f:
    for i in f.readlines():
        print(i)
        
    f.close()