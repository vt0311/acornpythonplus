import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 현재 프로그램이 작동중인 디렉토리에서 파일 읽기
data = pd.read_excel('./weight.xlsx', header=0)

print(data.head())

print('===================================')
# 앞의 데이터 4줄만 출력하라.
print(data.tail())

print('키평균:', np.mean(data.height)) 
print('몸무게평균:', np.mean(data.weight))

plt.plot(data.height, data.weight )
plt.show()
