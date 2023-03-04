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

# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
x_list=np.linspace(-1,1,100)
y_list=x_list**2
plt.plot(x_list,y_list)

# %%
# 变换矩阵放左边乘，从右往左计算，因为放在右边你也计算不了。
# 下面演示一个逆时针旋转90度的矩阵
rotateMinus90 = np.array([[0, -1],
                         [1, 0]])
# m1=np.dot(np.array([x_list, y_list]),rotateMinus90)
m1 =rotateMinus90@ np.array([x_list, y_list])
plt.plot(m1[0], m1[1])

# %%
# 来一个剪切变换
shear = np.array([[1, 1],
                  [0, 1]])
m2 = shear@np.array([x_list, y_list])
plt.plot(m2[0], m2[1])


# %%
# 然后我们试试先旋转，再剪切
m3= shear@(rotateMinus90 @np.array([x_list, y_list]))
plt.plot(m3[0], m3[1])


# %%
# 存在结合律，只要顺序相同，先计算后边的乘法还是前面的都一样
m4= (shear@rotateMinus90)@np.array([x_list, y_list])
plt.plot(m4[0], m4[1])

# %%
# 顺序不同，结果不同，说明没有交换律
m5= rotateMinus90@shear@np.array([x_list, y_list])
plt.plot(m5[0], m5[1])

# %%
shear@rotateMinus90


# %%
rotateMinus90@shear

# %%
