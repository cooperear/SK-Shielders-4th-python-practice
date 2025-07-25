import os,sys


print(f'현재 작업 디렉토리 : {os.getcwd()}')
print(f'python 버전: {sys.version} ')
print(f'os버전 : {os.name} ')

print(f'환경변수 : {os.environ}')

print('파일 경로 정보')

text_file = os.path.abspath('난중일기.txt')
print(f'디렉토리 : {os.path.dirname(text_file)}')
print(f'파일명 : {os.path.basename(text_file)}')
print(f'확장자 : {os.path.splitext(os.path.basename(text_file))[1]}')
print(f'파일 존재 여부 : {os.path.exists(text_file)}')