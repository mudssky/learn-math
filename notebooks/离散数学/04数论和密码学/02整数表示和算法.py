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
# ## 整数的进制表示

# %%
#传入一个十进制数，转换成2到16进制的字符
def int_to_base(n, base=10):
	if base < 2 or base > 16:
		raise ValueError("Base must be between 2 and 16")
	if base == 10:
		return n+''
	digits = "0123456789ABCDEF"
	result = ""
	while n > 0:
		# 取最后一位数
		remainder = n % base
		result = digits[remainder] + result
		# 去掉最后一位
		n //= base
	return result or "0"


# %%
int_to_base(100, 16)


# %% [markdown]
# 整数的模指数运算

# %%
# 先来一个计算大整数幂的函数
# 比如我们计算 3**644,其实python内部已经实现了高效的算法.
# 我们主要是学一下用分治法来实现这个算法，可以将幂指数分解为2进制数，然后相乘，这样运算次数就少了很多，时间复杂度是O(logn)
def big_power(base, exponent):
    """
    计算大整数的幂运算
    """
    result = 1
    while exponent > 0:
        # 如果指数是奇数，则将底数乘入结果中
        if exponent % 2 == 1:
            result *= base
        # 将底数平方，指数除以2
        base *= base
        exponent //= 2
    return result
# 2**14
# 2**(0b1110)



# %%
0b1110

# %%
# %%timeit
big_power(3,644)


# %%
# 用位运算优化一下，发现优化后的速度还不如优化前的
# 可能python本身对除2的运算就有优化,所以你改成位运算之后反而更慢
def big_power2(base, exponent):
    """
    计算大整数的幂运算
    """
    if exponent <= 0:
        return 1
    if base == 1:
        return 1
    result = 1
    while exponent > 0:
        # 如果指数是奇数，则将底数乘入结果中
        if exponent & 1 == 1:
            result *= base
        # 将底数平方，指数右移1位
        # print(f'base={base}')
        base *= base
        exponent >>= 1
    return result
# 2**14
# 2**(0b1110)



# %%
# %%timeit
big_power2(3,644)

# %%
# %%timeit
3**644
# 我们实现的这个方法，比python内置的慢一截,可见内置算法的优化更好

# %%
# %%timeit
3**644%645


# %%
# 下面在那个基础上写一个模指数运算的方法
def mod_power(base, exponent, modulus):
    """
    计算模指数运算
    """
    result = 1
    while exponent > 0:
        # 如果指数是奇数，则将底数乘入结果中
        if exponent % 2 == 1:
            result = (result * base) % modulus
        # 将底数平方，指数除以2, 这里是否进行模运算,对结果没有影响,但是(减少运算位数)提升了性能
        base = (base * base) % modulus
        exponent //= 2
    return result



# %%
# %%timeit
mod_power(3,644,645)
# 模指数运算的效率和原生的接近,说明用的算法比较类似
