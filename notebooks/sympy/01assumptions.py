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
# ## 01.Assumptions 假设体系

# %% [markdown]
# 对于正数，$\sqrt{x^2}=x$，对于负数 $\sqrt{x^2}=-x$。
# 但是对于未知数，将不会被化简，因为x的正负性不明确。

# %%
from sympy import *

sqrt(2**2)

# %%
sqrt((-2)**2)

# %%
x=2
sqrt(x**2) == x

# %%
y = -2
sqrt(y**2) == y

# %%
sqrt(y**2) == -y

# %%
x = Symbol('x')
sqrt(x**2)

# %%
simplify(sqrt(x**2))

# %% [markdown]
# 假设系统有两面，一面是我们可以在定义符号的时候添加假设，另一面是我们可以在表达式用is_*的属性，查询这些假设

# %%
x = Symbol('x', positive=True)
x.is_positive

# %% [markdown]
# 我们可以查询任何表达式的假设

# %%
x = Symbol('x', positive=True)
expr = 1 + x**2
expr

# %%
expr.is_positive

# %%
expr.is_negative

# %% [markdown]
# 下面我们需要print打印出来查看，因为none不会显示

# %%
x = Symbol('x')
y = Symbol('y', positive=True)
z = Symbol('z', negative=True)
print(x.is_positive)

print(y.is_positive)

print(z.is_positive)


# %%
