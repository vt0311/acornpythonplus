# t검정

# 문제 : 평균 키가 177.96 인데
# 다음 집단의 평균키가 다음과 같을 때
# 두 집단의 평균키가 같다고 할 수 있을지

data1 = [177.3, 182.7, 169.6, 176.3, 
        180.3, 179.4, 178.5, 177.2, 181.8, 176.5 ]

from scipy import stats 
import numpy as np

result1 = stats.ttest_1samp(data1, 177.96)
print(result1)
print()
# Ttest_1sampResult(statistic=0.0, pvalue=1.0)

print(np.mean(data1))
# ttest_1samp : 하나의 데이터집단의 평균과 
#               비교하고자 하는 관측치와의 검증에 사용.
#               즉 한 집단은 평균값, 한집단은 관측치가 있을 때.


result2 = stats.ttest_1samp(data1, 167.96)
print(result2)
print()
# Ttest_1sampResult(statistic=8.6299585266285188, pvalue=1.2021084053851823e-05)

result3 = stats.ttest_1samp(data1, 175.96)
print(result3)
print()
# Ttest_1sampResult(statistic=1.7259917053257037, pvalue=0.11842756847429547)


# 두 집단이 별도록 있을 때는 
#    ttest_ind 함수를 사용한다.

male = [300, 350, 400, 450, 500, 500]
female = [200, 250, 270, 320, 340, 370]

print('stats.ttest_ind(male, female):')
print(stats.ttest_ind(male, female))
# p가 0.05 보다 작았으므로 -> 두 집단간에 차이가 있다.
