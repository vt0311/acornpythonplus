
# 문제 1) 데이터 파일 하나를 만들어서 숫자만 넣고, 
#이 파일을 읽어서, 합계, 최대값, 최소값 출력하기.

f = open('ans1.txt', 'r')

 # 파일 한꺼번에 읽기
data = f.readlines()
#print(data)
f.close() # 파일 닫기

nums = [int(i) for i in data]

#print(nums, sum(nums), max(nums), min(nums))

print(nums)

print('합계 :', sum(nums))

print('최대:', max(nums))

print('최소:', min(nums))


# 이 부분 이후는 내가 한것
sum = 0

for line in data:
    #print(line)
    sum = sum + int(line)
    
# 화면에 출력

'''
print("합계:")
print(sum)
print()

print("최대값:")
print(max(data))

print("최소값:")
print(min(data))
'''

