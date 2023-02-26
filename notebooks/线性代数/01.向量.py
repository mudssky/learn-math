# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# %% [markdown]
# ## 什么是向量  
# 物理专业学生的角度看，向量是空间中的一个箭头，决定一个向量的是它的长度和它所指的方向  
# 计算机专业学生的角度看，向量是一个有序数字列表，比如你可以用一个二维向量对房屋进行建模，每一位分别表示房屋的面积，还有价格  
# 数学家会概括两种观点,向量可以是任何事物，只要保证两个向量相加和相乘是有意义的即可  
#

# %%
import sys
sys.path.append('../../util/')

# %%
# 使用matplotlib绘制向量
# quiver，前四个值也可以传入array，这样就是绘制多个向量
import matplotlib.pyplot as plt
import numpy as np

# 创建向量
v = np.array([3, 4])
# 创建绘图对象
fig, ax = plt.subplots()

# 边框置于原点
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
# 绘制原点
# ax.scatter(0, 0, color='red')

# 绘制向量
ax.quiver(0, 0, v[0],v[1], angles='xy', scale_units='xy', scale=1,color='r')

# 设置坐标轴范围
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.legend(np.array2string(v))
# 显示图形
plt.show()




# %% [markdown]
# ## 向量加法
# 向量加法的概念就是两个向量产生位移的叠加

# %%
# 向量加法的绘制
import paint_vector
v1=np.array([1,2])
v2=np.array([3,-1])
v3=v1+v2
paint_vector.paint_vectors2d([{'v':v1},{'start':v1,'v':v2},{'v':v3}])

# %% [markdown]
# ## 向量数乘
# 向量数乘的概念就是向量的缩放

# %%
# 向量数乘的绘制,乘负数就是先反向再缩放
import paint_vector
v1=np.array([1,2])
v2=v1*-2
paint_vector.paint_vectors2d([{'v':v1},{'v':v2}])

# %%
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 生成3D向量
X, Y, Z = np.array([0, 0, 0]), np.array([1, 2, 3]), np.array([2, 3, 1])
U, V, W = np.array([1, 2, 3]), np.array([2, 3, 1]), np.array([0, 0, 0])

# 绘制向量
ax.quiver(X, Y, Z, U, V, W, length=1, normalize=True)

# 设置坐标轴
ax.set_xlim([-1, 4])
ax.set_ylim([-1, 4])
ax.set_zlim([-1, 4])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

