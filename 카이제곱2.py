
# 적합성 검정
'''
교회 또는 학교 구성원의 인종 통계가 미국 전체 인구의 
인종 인구 통계와 일치하는지 여부를 확인하고자 할때 
범주형 데이터(비수치형)로 작업할 때 
남성, 여성, 기타와 같은 범주에는 
수학적 의미가 없어서 관측값 자체가 통계적 의미가 없다.
범주형 데이터를 취급할 때는
변수의 값보다는 개수를 기반으로 한다.
'''
import numpy as np  
import pandas as pd                                        
from scipy import stats 
import matplotlib.pyplot as plt 

# json 형태로 데이터 저장
#data = {
#    white : 
#}

national = pd.DataFrame(
    ["white"]*100000
    + ["hispanic"]*60000
    + ["black"]*50000
    + ["asian"]*15000
    + ["other"]*35000)

minnesota = pd.DataFrame(
    ["white"]*600
    + ["hispanic"]*300
    + ["black"]*250
    + ["asian"]*75
    + ["other"]*150)    

#print('national:')
#print(national)
#print('minnesota:')
#print(minnesota)

# r에서의 table 분할표 작성
national_table = pd.crosstab(index=national[0], columns="count")
print('national_table:') 
print(national_table) 
print()

minnesota_table = pd.crosstab(index=minnesota[0], columns="count")
print('minnesota_table:') 
print(minnesota_table) 
print()

data1 = [50000, 60000, 35000, 100000]
data2 = [250, 300, 150, 600 ]

#chis = stats.chisquare(data1, data2)

#print('chis:')
#print(chis)

# pValue 가 0.05 이하일 때만 의미가 있다.

#plt.plot(data1)

#plt.plot(data2)

#plt.show()

# 귀무가설 : 둘의 장난감 비율은 별 차이가 없다.

# 대립가설 : 둘의 장난감 비율에 차이가 있다. 


# 비율 구하기 - 지역
national_ratios = national_table / len(national)

print('national_ratios:')
print(national_ratios)
print()


# 기대치 구하기
expected = national_ratios * len(minnesota)

print('expected:')
print(expected)
print()

data1 = minnesota_table
chis = stats.chisquare(data1, expected) # 파이썬에서는 기대치 넣어줘야 함.

print('chis1:')
print(chis)
print()


# 멘델의 유전법칙(어떤 데이터)의 비율이 (1:2:7)
# 관측치 40, 200, 600가 이럴 때
# 저 비율과 맞는지 여부.

observe = [40, 200, 600]
expected = [40*0.1, 200*0.2, 600 * 0.7]

chis = stats.chisquare(observe, expected)
print(' 멘델의 유전법칙 chis:')
print(chis)
print()
# 결과가 매우 작았으므로 요구조건에 충족하지 않는다.
