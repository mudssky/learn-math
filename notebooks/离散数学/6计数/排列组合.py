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
# 计算排列数，注意factorial计算的结果是浮点数，所以用整出符号就能转为整数
import math

n = 5  # 从 5 个元素中取出 m 个元素进行排列
m = 3

# 计算排列数
permutations = math.factorial(n) // math.factorial(n-m)

print("排列数为:", permutations)


# %%
from scipy.special import perm

n = 5
m = 3
permutations = perm(n, m, exact=True)
print("scipy 库计算排列数为:", permutations)
# 使


# %%
# 计算组合数
import math
from scipy.special import comb

# 使用 math 库计算排列数
n = 5
m = 3
permutations = math.factorial(n) //(math.factorial(m)* math.factorial(n-m))
print("math 库计算组合数为:", permutations)
combinations= comb(n, m, exact=True)
print("scipy 库计算组合数为:",combinations)


# %%
# python 生成排列
import itertools

# 生成列表 [1, 2, 3] 的所有排列
lst = [1, 2, 3]
perms = list(itertools.permutations(lst))

# 输出排列结果
for perm in perms:
    print(perm)


# %%
# python 生成组合
import itertools

# 生成列表 [1, 2, 3] 的所有排列
lst = [1, 2, 3]
perms = list(itertools.combinations(lst,2))

# 输出排列结果
for perm in perms:
    print(perm)


# %%
# 不使用标准库，也可以用递归实现
def permutations(lst, m):
    """
    计算列表 lst 的所有长度为 m 的排列
    """
    n = len(lst)
    if m == 0:  # 如果排列长度为 0，返回空列表,退出条件
        return [[]]
    if n < m:   # 如果列表长度小于排列长度，返回空列表，这里是参数错误返回空列表
        return []
    result = []
    for i in range(n):
        # 生成 lst 中剩余元素的长度为 m-1 的排列
        rest_perms = permutations(lst[:i] + lst[i+1:], m-1)
        for perm in rest_perms:
            # 将新的排列与 lst[i] 组合成长度为 m 的排列
            result.append([lst[i]] + perm)
    return result
lst = [1, 2, 3]
perms = permutations(lst, 3)

# 输出排列结果
for perm in perms:
    print(perm)


# %%
def combinations(lst, m):
    """
    计算列表 lst 的所有长度为 m 的组合
    """
    n = len(lst)
    if m == 0:  # 如果组合长度为 0，返回空列表
        return [[]]
    if n < m:   # 如果列表长度小于组合长度，返回空列表
        return []
    result = []
    for i in range(n):
        # 生成 lst 中剩余元素的长度为 m-1 的组合
        rest_combs = combinations(lst[i+1:], m-1)
        for comb in rest_combs:
            # 将新的组合与 lst[i] 组合成长度为 m 的组合
            result.append([lst[i]] + comb)
    return result
# 生成列表 [1, 2, 3] 中长度为 2 的所有组合
lst = [1, 2, 3]
combs = combinations(lst, 2)

# 输出组合结果
for comb in combs:
    print(comb)



# %%
