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
# ## 搜索算法
# 线性搜索
# 二分搜索

# %%
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

import random

def generate_sorted_array(n, start=1, end=10000):
    """生成 n 个升序排列的随机整数"""
    arr = [random.randint(start, end) for _ in range(n)]
    arr.sort()
    return arr



# %%
test_arr=generate_sorted_array(100)
test_arr

# %%

# %%
test_range=range(10,100,5)

# %%
# %%timeit 
for i in test_range:
	binary_search(test_arr,test_arr[i])


# %%
def binary_search2(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) >> 1
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        

    return -1

# %%
# %%timeit 
for i in test_range:
	binary_search2(test_arr,test_arr[i])


# %%
def binary_search3(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low+ ((high-low)>>1)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# %%
# %%timeit 
for i in test_range:
	binary_search3(test_arr,test_arr[i])

# %%
import matplotlib.pyplot as plt
import numpy as np

# 定义两个向量 a 和 b
a = np.array([2, 3])
b = np.array([1, 4])

# 计算向量差 c = a - b
c = a - b

# 绘制坐标系
fig, ax = plt.subplots()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

# 绘制向量 a 和 b
ax.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1, color='r')
ax.quiver(0, 0, b[0], b[1], angles='xy', scale_units='xy', scale=1, color='b')

# 绘制向量 c
ax.quiver(b[0], b[1], c[0], c[1], angles='xy', scale_units='xy', scale=1, color='g')

# 从原点出发
ax.quiver(0, 0, c[0], c[1], angles='xy', scale_units='xy', scale=1, color='yellow')
# 添加图例
ax.legend(['a', 'b', 'a - b','from 0,0'])

# 显示图形
plt.show()


# %%
ax.spines['right'].get_position()

# %%
