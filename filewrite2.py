#f = open('c:\\temp\\test.txt', 'w')

lines = [
        "유시민",
        "정재승",
        "황교익",
        "김영하",
        "유희열"

]

f = open('test2.txt', 'w', encoding="utf-8")

#f = open('c:/temp/test.txt', 'w', encoding="utf-8")

#f.write('파일에 정보를 저장한다.')

#f.write('Hello Python')
# f.writelines(lines)

for item in lines:
    f.write(item+'\n')
f.close()


# 저장한 파일 읽어서 화면에 출력하기
f = open('test2.txt', 'r', encoding='utf-8')

data = f.readlines()

for line in data:
    print(line)



f.close()