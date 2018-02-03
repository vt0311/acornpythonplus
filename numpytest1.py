import numpy as np

list1 = [1,2,3,4]

a = np.array(list1)  # list 타입을 numpy 배열 타입으로 전환한다.
print(a.shape)
print(type(a))
print(a.dtype)

#a.mean(a)

print('합계:', sum(list1))
print('평균:', sum(list1)/len(list1))
print('=========================================')
# 파이썬만으로 합계, 평균, 중위값(위치상 중간)
list1 = [9, 11, 12, 15, 4, 2, 3, 7, 9, 29]

print('합계:', sum(list1))
print('평균:', sum(list1)/len(list1))

list1.sort()

if len(list1)%2 == 0:
    pos = len(list1)//2
    mean = (list1[pos-1] + list1[pos])/2
else :
    pos = len(list1)//2
    mean = list1[pos]

print('중위수 : ', mean)    
print('=========================================')

list2 = np.array(list1) # numpy 타입으로 수정한다.
print('합계:', np.sum(list2))
print('평균:', np.mean(list2))
print('중위수:', np.median(list2))
print('최대:', np.max(list2))
print('최소:', np.min(list2))

print('=========================================')
list3 = [4,3,6,7,5,3,1,9]
list3 = np.array(list3)
print(list3)
print('중위수3:', np.median(list3))

print('=========================================')

a = np.array([1,2,3])
print(type(a))
print(a.ndim)
print(a.shape)

#a = np.array([1,2,3], [4,5,6]) # 오타 있는 듯
print(a.shape)


print('=========================================')

