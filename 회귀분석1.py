from sklearn.datasets import load_boston
import pandas as pd

boston = load_boston()
#print(boston.DESCR)



dfx = pd.DataFrame(boston.data, columns=boston.feature_names)
#print(dfx.head())
print('dfx.tail():')

print(dfx.tail())

print()


dfy = pd.DataFrame(boston.target, columns=["MEDV"])
print('dfy.tail():')

print(dfy.tail())

print()

df = pd.concat([dfx, dfy], axis=1)
print(df.tail())

# 데이터에 대한 중간값, 평균, 카운트....
# 데이터 요약
print(df.describe())


import seaborn as sns
import matplotlib.pyplot as plt
#cols = ["LSTAT", "NOX", "RM", "MEDV"]
cols = ["LSTAT", "NOX", "RM"]
sns.pairplot(df[cols]) # 데이터를 한눈에 보여줄때
plt.show()






