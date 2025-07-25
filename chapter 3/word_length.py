words = ['cat', 'elephant', 'dog', 'butterfly', 'ant']

print(f"가장 긴 단어: {max(words, key=len)} ({len(max(words, key=len))}글자)")
print(f"가장 짧은 단어: {min(words, key=len)} ({len(min(words, key=len))}글자)")