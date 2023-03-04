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
# 先算一个简单的6倍的行列式吧
a=np.array([[2,0],
            [0,3]])
np.linalg.det(a)

# %%
# 再算一个复杂一些的
a=np.array([[2,0,1],
            [0,3,2],
            [2,3,1]])
np.linalg.det(a)

# %%
import sympy

# 创建一个 3x3 的符号矩阵
a, b, c, d, e, f, g, h, i = sympy.symbols('a b c d e f g h i')
A = sympy.Matrix([[a, b, c], 
                  [d, e, f], 
                  [g, h, i]])

# 计算矩阵的行列式
A.det()

# %%
b = sympy.Matrix([[a, b],
                  [c, d]])
b.det()


# %%
a = sympy.symbols('1:a:4')

print(a)

# %%
import sympy

# 定义矩阵的位置变量
a = sympy.IndexedBase('a')
i, j = sympy.Idx('i', 3), sympy.Idx('j', 3)

# 定义矩阵
A = sympy.Matrix(3, 3, lambda i, j: a[i*3+j])

# 输出矩阵的表达式
A


# %%
a[1, 2]
