#f = open('test.py','r')
# 동일 폴더 내에 test.py 파일이 존재해야 한다.

#f = open('c:/temp/test.txt', 'w')
f = open('test.txt', 'w')

data = f.read() # 파일 한꺼번에 읽기

print(data) # 화면에 출력

f.close() # 파일 닫기