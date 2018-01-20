#import pickle # 객체를 직렬화 해주는 클래스

class MyScore:
    
    #  생성자
    def __init__(self, name="", kor=0, eng=0, mat=0):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

    def process(self):
        self.total = self.kor + self.eng + self.mat

    def output(self):
        print("{0} {1} {2} {3} {4}".format
            (self.name, self.kor, self.eng, self.mat, self.total))


# 텍스트 파일에 데이터 넣어놓고 데이터 읽으면서 객체 리스트가 만들어진다.
f = open("myscore.dat", "r", encoding='utf-8')

myList = []

line = f.readline() #한줄 읽어서 토큰을 분리한다.(단어 분리)

while(line != ""): #더이상 읽을 데이터가 없을 때까지
    temp = line.split(" ") # 공백으로 데이터들을 분리한다.
    data = MyScore(temp[0], int(temp[1]), int(temp[2]), int(temp[3]) )
    myList.append(data)
    data.process()
    line = f.readline() #한줄 읽어서 토큰을 분리한다.(단어 분리)

f.close()

for item in myList:
    item.output()


print('---------------------------------')

'''
# 파일에 저장하기
f = open("myscore.bin", "wb")
pickle.dump(myList, f)

f.close()


# 파일 불러오기
f = open("myscore.bin", "rb")
myList2 = pickle.load(f)

f.close()

for item in myList2:
    item.output()

'''

