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
import matplotlib
import pyvenn.venn as venn

# %% [markdown]
# ## 文氏图

# %%
# 下面使用pyvenn这个库绘制简单的venn图
# # %matplotlib inline
set1={'1','2','3'}
set2={'2','3','4'}
labels=venn.get_labels([set1,set2],fill=['number','logic','percent'])
venn.venn2(labels,names=['set1','set2']) 

# %%
# 下面写了一个求幂集的函数，由于python的set里面不能嵌套dict，所以最外层是list
import itertools
def power_set(s:set):
    res=[]
    s_list=list(s)
    res.append({})
    # 从1到元素个数，生成所有取值的可能，组成集合
    for length in range(1,len(s)+1):
        res.extend(map(lambda x :set(x),itertools.combinations(s_list,length)))
    return res
    # for i in s:
        # print(i)
power_set(set1)

    

# %%
# 下面计算笛卡尔积
list(itertools.product(set1,set2))

# %% [markdown]
# ## 集合运算

# %%
A={'1','2','3','4'}
B={'4','5','6'}
print(A)
print(B)

# 并集运算
print(f'A∪B: {A.union(B)}')
print(f'A∪B: {A|B}')

print(f'A∩B: {A.intersection(B)}')
print(f'A∩B: {A&B}')

print(f'A-B: {A.difference(B)}')
print(f'A-B: {A-B}')
