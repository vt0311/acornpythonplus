from sklearn.datasets import load_boston
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

boston = load_boston()

from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
df = pd.concat([pd.DataFrame(diabetes.data, columns=["x%d" % (i + 1) for i in range(diabetes.data.shape[1])]),
                pd.DataFrame(diabetes.target, columns=["target"])],
               axis=1)
print(df.tail())

#df.describe()

sns.pairplot(df.ix[:,:4])
#plt.show()

from sklearn.linear_model import LinearRegression

model = LinearRegression().fit(boston.data, boston.target)

# 예측
predictions = model.predict(boston.data)

print(predictions)

plt.scatter(boston.target, predictions)
plt.show()