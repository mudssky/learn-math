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

# %%
a = np.array([[1, 0, -1],
              [2, 2, -3],
              [3, 4, 0]])
b = np.array([[3, 4, -1],
              [1, -3, 0],
              [-1, 1, 2]])
a+b


# %%
# 矩阵乘法
a = np.array([[1, 0, 4],
              [2, 1, 1],
              [3, 1, 0],
              [0, 2, 2]
              ])
b = np.array([[2, 4],
              [1, 1],
              [3, 0],
              ])
print(f'a:{a}')
print(f'b:{b}')
a@b


# %%
# 矩阵转置
a.T

# %%
square = np.array([[1, 1, 0],
                   [1, 0, 1],
                   [0, 1, 0]])
print(f'square:{square}')
square.T


# %%
# 矩阵的交集和并集
A = np.array([[1, 0, 1],
              [0, 1, 0]])
B = np.array([[0, 1, 0],
              [1, 1, 0]])
print(f'A={A}')
print(f'B={B}')
A | B


# %%
A&B

# %%
# 针对0-1矩阵的布尔乘积，也就是矩阵的乘积
A = np.array([[1, 0],
              [0, 1],
              [1, 0]
              ])
B = np.array([[1, 1, 0],
              [0, 1, 1],
              ])
print(f'A={A}')
print(f'B={B}')
A@B
# np.dot(A,B)



# %%
A = np.array([[0, 0, 1],
              [1, 0, 0],
              [1, 1, 0]
              ])
print(f'A={A}')

# def bool_power(arr:np.ndarray,n:int):
#     res=arr
#     for i in range(n-1):
#         res=np.dot(res,arr)
#     return res
# bool_power(A,5)
# np.power(A,6)

np.linalg.matrix_power(A,5)

