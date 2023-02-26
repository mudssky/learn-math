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
# 添加python模块搜索路径
# import sys
# sys.path.append("../util/")


# %%
# 用3个3表示一个最大的数
num1=3+3+3
print(f'num1:{num1}')
num2=3*3*3
print(f'num2:{num2}')
num3=3**3**3
print(f'num3:{num3}')

# %%
# 科学计数法
print('{:.2e}'.format(num3))

# %% [markdown]
# 严华经
# - 洛叉 10**5
# - 俱胝 10**7
# - 阿虞罗 10**14
# - 无量 `10**(2.8*10**32)`
# - 无边 `10**(1.1*10**33)`
#

# %% [markdown]
# 高德纳箭头
# 高德纳箭头是一种在数学、计算机科学和逻辑学等领域中经常使用的符号，用于表示递归定义中的自我引用。
# 因此可以用于叠加幂运算

# %% [markdown]
# 葛立恒数是在研究n维立方体的染色问题时得出的
# 即n维立方体，所有点连线，在任意面上的线染上两种颜色，任意面不能出现同色组成完全图，随着n维数的增多，最终会出现一个n维立方体，无法实现这一点，
# 这个n的上界被称为葛立恒数，是一个很大的数。
# 据说用高德纳箭头要叠加64层
