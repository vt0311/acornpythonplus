#f = open('c:\\temp\\test.txt', 'w')

#f = open('test.txt', 'w', encoding="utf-8")

f = open('c:/temp/test.txt', 'w', encoding="utf-8")

f.write('파일에 정보를 저장한다.')

f.write('Hello Python')

f.close()


# 저장한 파일 읽어서 화면에 출력하기
f = open('test.txt', 'r', encoding='utf-8')

s = f.read()

print(s)

f.close()