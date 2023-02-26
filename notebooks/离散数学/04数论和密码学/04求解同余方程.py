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
# ##  同余方程组
#  有物不知其数
#  三三数只剩二
#  五五数之剩三
#  七七数之剩二

# %%
# 求解一次同余方程，中国剩余定理 CRT chinese remqinder theorem
from sympy.ntheory.modular import solve_congruence
solve_congruence((2, 3), (3, 5), (2, 7))
# print(x)
# 结果的0是小于每个模数乘积的解，1是每个模数的乘积
