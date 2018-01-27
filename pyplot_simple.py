import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()

rc('font', family=font_name)


plt.plot([10,20,30,40,50])

plt.ylabel('y축 이름')

plt.show()