text = "Python is awesome programming language"
text_split = text.split()
text_joined = "-".join(text_split)

print (f"Original text: {text}")
print (f"분리된 단어들 : {text_split}")
print (f"하이픈으로 연결 : {text_joined}")
print(f"대문자로 변환 후 공백으로 연결 : {" ".join(word.upper() for word in text_split)}" )