
# 독립성 검정
import numpy as np                                          
from scipy import stats 
import matplotlib.pyplot as plt 

data1 = [5, 11, 1]
data2 = [4, 7, 3]

chis = stats.chisquare(data1, data2)

print(chis)

# Power_divergenceResult(statistic=3.8690476190476186, pvalue=0.1444930586621197)


# pValue 가 0.05 이하일 때만 의미가 있다.

# pvalue=0.144 이므로 별 의미 없음.


plt.plot(data1)

plt.plot(data2)

plt.show()

# 귀무가설 : 둘의 장난감 비율은 별 차이가 없다.

# 대립가설 : 둘의 장난감 비율에 차이가 있다. 