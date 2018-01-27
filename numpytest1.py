import numpy as np

list1 = [1,2,3,4]

a = np.array(list1)  # list 타입을 numpy 배열 타입으로 전환한다.
print(a.shape)
print(type(a))
print(a.dtype)

a.mean(a)

# 파이썬만으로 합계, 평균, 중위값(위치상 중간), 1/4 