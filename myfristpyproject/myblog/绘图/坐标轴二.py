# -*- coding: utf-8 -*-
"""
设置坐标轴
"""

import matplotlib.pyplot as plt
import numpy as np

# 绘制普通图像
x = np.linspace(-1, 1, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure()
plt.plot(x, y1)
plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--')

# 设置坐标轴的取值范围
plt.xlim((-1, 1))
plt.ylim((0, 3))

# 设置坐标轴的lable
# 标签里面必须添加字体变量：fontproperties='SimHei',fontsize=14。不然可能会乱码
plt.xlabel(u'这是x轴', fontproperties='SimHei', fontsize=14)
plt.ylabel(u'这是y轴', fontproperties='SimHei', fontsize=14)

# 设置x坐标轴刻度, 之前为0.25, 修改后为0.5
# 也就是在坐标轴上取5个点，x轴的范围为-1到1所以取5个点之后刻度就变为0.5了
plt.xticks(np.linspace(-1, 1, 5))
# 获取当前的坐标轴, gca = get current axis
ax = plt.gca()
# 设置右边框和上边框
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 设置x坐标轴为下边框
ax.xaxis.set_ticks_position('bottom')
# 设置y坐标轴为左边框
ax.yaxis.set_ticks_position('left')
# 设置x轴, y周在(0, 0)的位置
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

plt.show()
