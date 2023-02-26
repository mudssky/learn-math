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

# %%
# python中整除运算
a=10
b=3
a//b

# %%
# python中的取模运算
a%b

# %%
a=10
b=5
m=3
# 关于取模的等式1
(a+b)%m==(a%m+b%m)%m

# %%
(a*b)%m==((a%m)*(b%m))%m
