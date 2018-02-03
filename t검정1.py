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


# 두 집단이 별도로 있을 때는 
#    ttest_ind 함수를 사용한다.

male = [300, 350, 400, 450, 500, 500]
female = [200, 250, 270, 320, 340, 370]

print('stats.ttest_ind(male, female):')
print(stats.ttest_ind(male, female))
print()
# p가 0.05 보다 작았으므로 -> 두 집단간에 차이가 있다. 두 집단간의 관련 없다.



# 연습 문제 2 (126쪽)

#갤럭시와 아이폰 의 선호도가 다음과 같을때 
# 남자와 여자간의 선호도의 차이가 있을까? 
# 선호도란 좋다/싫다의 범주형 데이터이므로 빈도수로 표현해야 한다. 
# 즉 카이제곱 검정을 해야 한다.

male2 = [72, 55]
female2 = [28, 67] 

Ttest = stats.ttest_ind(male2, female2)
print(' 갤럭시와 아이폰 남녀 선호도 chis:')
print(Ttest)
# Ttest_indResult(statistic=0.75216079155562943, pvalue=0.53042618329300073)
# p가 0.5-> 즉 관련 있음.


# T 검정 연습 문제 (p.144)

# 작년도 대기업의 대졸 신입 사원 월임금은 평균 160만원 이었다. 
# 금년도 대졸자의 초임을 알아보기 위하여 
# 15명을 단순확률 추출하여 
# 성별과 월임금을 조사하니 다음과 같다.
# 이 자료를 통해 대졸 신입 초임이 작년보다 인상되었는지 
# 유의수준 5%로 가설 검정하라.

#성별 급여     성별 급여 
# 1 163        1 162
# 2 157        1 172
# 1 161        2 165
# 1 162        2 165
# 1 158        1 159
# 2 160        2 161
# 2 165        1 168
# 1 170

data2 = [163,162,157,172,161,165,162,165,158,159,160,161,165,168,170]
#Ttest = stats.ttest_ind(male2, female2)
Ttest2 = stats.ttest_1samp(data2, 160)
print(' Ttest2:')
print(Ttest2)
print()
#Ttest_1sampResult(statistic=2.8627123416821774, pvalue=0.012531656550447192)
# 0.05 보다 작음. -> 차이 있다. 


# 두 대응집단 간의 검정.
# 복부 수술 전 9명의 몸무게와
# 복부 수술 후 
# 몸무게 변화

pre = [67.2, 67.4, 71.5, 77.6, 86, 89.1, 59.5, 81.9, 105.5]
post = [62.4, 64.6, 70.4, 62.6, 80.1, 73.2, 58.2, 71, 101] 

paired_sample = stats.ttest_rel(pre, post)
print('paired_sample:')
print(paired_sample)
# Ttest_relResult(statistic=3.6681166519351103, pvalue=0.0063266508559336621)
# 0.05 보다 작음. -> 차이가 있다. -> 유의미함. 


# 시험
test7 = [58, 39, 49, 99, 32, 88, 62, 30, 55, 65, 44, 55, 57, 53, 88, 42, 39]
Ttest7 = stats.ttest_1samp(test7, 55)
print(' Ttest7:')
print(Ttest7)
print()


