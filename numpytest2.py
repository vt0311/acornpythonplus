import numpy as np 

# 배열을 만드는 방법 np.array 함수를 사용한다.

a = np.array([1,2,3])
b = np.array([4,5,6])

# 각 배열의 요소의 합 구하기
c = a + b   # c = np.add(a,b)
print(c)    
print(a-b)  # c = np.subtract(a,b)
print(a*b)  # c = np.multiply(a,b)
print(a/b)  # c = np.divide(a,b)

print('===============================================')
print()
# 행렬의 경우
a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])
print('a+b:')
print(a + b)
print()

print('a*b:')
print(a*b)
print()

# 실제 행렬의 곱은 dot 함수를 사용한다.
print('np.dot(a, b):')
print(np.dot(a, b))
print()

# 행렬의 각 요소들에 대한 합과 곱 구하기
print('np.sum(a):')
print(np.sum(a))
print()
print('np.prod(a):') 
print(np.prod(a)) 
print()


# axis=0 컬럼끼리 더함(열끼리 더함)
# axis=1 행끼리 더함)
print('np.sum(a, axis=0):')
print(np.sum(a, axis=0))
print()
print('np.prod(a, axis=0):')
print(np.prod(a, axis=0))
print()

print('np.sum(a, axis=1):')
print(np.sum(a, axis=1))
print()

print('np.prod(a, axis=1):')
print(np.prod(a, axis=1))
print()

print('==================================================')
# 배열 자동 생성
a = np.zeros((2,2)) # 모든 요소의 값이 0인 2X2 행렬 생성
print(a)

a = np.ones((3,3)) # 모든 요소의 값이 1인 3X3 행렬 생성
print(a)

a = np.full((3,4), 9) # 모든 요소의 값이 9인 3X4 행렬 생성
print(a)


a = np.eye(3) # 단위행렬, 전체요소가 0이고, 대각선은 1인 행렬을 단위행렬이라 한다.
print(a)

# random하게 값을 채운다.
a = np.random.random((3,3))
print(a)

# arange : 규칙적으로 값 생성
x = np.arange(0, 100, 5)
print(x)

print('===============================================')
# sin 함수 그리기
import matplotlib.pyplot as plt
x = np.arange(0, 10, 0.1) # x축 눈금 0, 0.1, 0.2, ....
y = np.sin(x) # x축에 대해서 각각 sin 값 구하기

plt.plot(x, y) # x축, y축을 저 좌표점으로 해서 차트 그리기

plt.plot(x, np.cos(x))
plt.show()# 차트 내용 출력

#print(a-b)
#print(a/b)

