import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()

rc('font', family=font_name)

weight = [54, 63, 66, 78, 70, 77]

height = [164, 170, 173, 175, 177, 180]

import numpy as np

print('키 평균:', np.mean(np.array(weight)) )
print('키 분산:', np.var(np.array(weight)) )
print('키 표준편차:', np.std(np.array(weight)) )

#plt.plot(weight, height, 'ro') # r:빨간색, g:녹색, o: 모양
plt.hist(weight, 10, normed=1, facecolor='g', alpha=0.75)
plt.xlabel('몸무게')
plt.ylabel('키')


#plt.show()

#==================================================

# 시험
testa = [95, 67, 66, 59, 40]

testb = [88, 87, 67, 90, 70]

import numpy as np

print('a평균:', np.mean(np.array(testa)) )
print('a분산:', np.var(np.array(testa)) )
print('a표준편차:', np.std(np.array(testa)) )

print('b평균:', np.mean(np.array(testb)) )
print('b분산:', np.var(np.array(testb)) )
print('b표준편차:', np.std(np.array(testb)) )


c = [2.3, 1.7, 1.4, 0.7, 1.9]

print('c분산:', np.var(np.array(c)) )
print('c표준편차:', np.std(np.array(c)) )

