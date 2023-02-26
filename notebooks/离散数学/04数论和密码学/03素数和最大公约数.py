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
# ## 试除法

# %% tags=["func"]
# 使用试除法判断素数
def is_prime(n):
    """
    判断一个数是否为素数
    """
    if n < 2:  # 小于2的数都不是素数
        return False
    for i in range(2, int(n**0.5)+1):  # 判断 n 是否能被 2 到 sqrt(n) 之间的数整除
        if n % i == 0:
            return False
    return True



# %%
is_prime(999)

# %%
# %%timeit
# for i in range (1,10000):
# 	if is_prime(i):
# 		print(i)
# 下面用列表生成式求出1-100的素数
[i for i in range(1,1000) if is_prime(i)]


# %% [markdown]
# 上面的算法还可以优化,因为偶数可以被2整数,不是素数  
# 所以我们先判断是不是偶数,如果是偶数,就不是素数  
# 另外在2-根号n的范围内的试除也只用奇数进行,因为偶数和任意数乘积为偶数,之前已经排除了偶数的可能性了,  
# 所以这里只要判断奇数

# %%
def is_prime2(n):
    """
    判断一个数是否为素数,先排除偶数
    """
    # 小于2的数都不是素数
    if n < 2:
        return False
    # 2是素数
    if n == 2:
        return True
    # 偶数都不是素数
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


# %%
# %%timeit
[i for i in range(1,1000) if is_prime2(i)]

# %% [markdown]
# ## Miller-Rabin 素性测试算法
# 目前已知的最快速的素数判断算法是 Miller-Rabin 算法，它的时间复杂度为 $O(k \log^3 n)$，其中 $k$ 是算法中的参数，通常需要选取几十到几百次。
#
# Miller-Rabin素性测试算法是一种常用的素数判定算法，其基本思想是利用费马小定理的一个变形来判断一个数是否为素数。它的优点是能够高效地判定大数是否为素数。
#
# 下面是Miller-Rabin素性测试算法的步骤：
#
# 1. 将待判定的数 $n-1$ 分解成 $d \cdot 2^s$ 的形式，其中 $d$ 是奇数，$s$ 是正整数。
# 2. 随机选择一个小于 $n$ 的整数 $a$，计算 $a^d \bmod n$。如果 $a^d \bmod n = 1$ 或者 $a^d \bmod n = n-1$，则 $n$ 可能是一个素数，进入下一个循环。
# 3. 如果 $a^d \bmod n \neq 1$ 且 $a^d \bmod n \neq n-1$，则重复计算 $a^{2^r \cdot d} \bmod n$，其中 $r=1,2,\dots,s-1$。如果在这些计算中存在 $a^{2^r \cdot d} \bmod n = n-1$，则 $n$ 可能是一个素数，进入下一个循环。
# 4. 如果在步骤3中没有找到 $a^{2^r \cdot d} \bmod n = n-1$，则 $n$ 肯定不是素数。
# 5. 重复步骤2-4 $k$ 次，其中 $k$ 是一个控制算法正确性的参数。如果在所有循环中都没有找到 $n$ 是素数的证据，则 $n$ 肯定是合数。
#
# 需要注意的是，由于Miller-Rabin素性测试算法采用了随机数，因此算法的正确性是有一定概率的，但是随着$k$的增大，算法正确性也会逐渐提高。因此，在实际应用中，通常会选择合适的$k$值来保证算法的正确性。

# %% tags=["func"]
import random

def is_prime3(n, k=10):
    """
    判断一个数是否为素数，使用 Miller-Rabin 素性测试算法
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # 将 n - 1 分解为 d * 2^s 的形式，其中 d 是奇数
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # 进行 k 次测试
    for i in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True



# %%
# %%timeit
[i for i in range(1,1000) if is_prime3(i)]

# %% tags=["func"]
from tqdm import tqdm
def prime_list(n:int):
    '''
    用Miller-Rabin算法判断1-n之前的素数,求素数列表
    '''
    prime_list=[2,3]
    # 直接遍历奇数列表
    for i in tqdm(range(5,n+1,2)):
        if is_prime3(i):
            prime_list.append(i)
    return prime_list

                
    

# %%
# 使用Miller-Rabin算法逐个判断一亿以内的素数，需要5分钟左右
primelist=prime_list(10**8)

# %%
len(primelist)

# %%
# 对上面Miller-Rabin算法 计算出来的素数列表验算一遍
# 使用试除法，需要10分钟左右
filteredPrime=[]
for i in tqdm(primelist):
    if is_prime2(i):
        filteredPrime.append(i)

    

# %%
len(filteredPrime)


# %% [markdown]
# ## 埃拉托色尼筛选法
#
# 埃拉托色尼筛选法（Sieve of Eratosthenes）是一种求素数的算法。它的基本思想是：从小到大枚举所有可能的质数，并将它们的倍数标记为合数，这样，最终没有被标记的数就是素数。
#
# 具体做法是：
#
# 1. 初始化一个长度为n（待筛数的范围）的布尔数组，将所有元素都设置为True，表示这些数字都是可能的质数。
# 2. 从2开始，依次枚举每个数字，如果这个数字是质数（即在之前的筛选中没有被排除），则将它的所有倍数都标记为非质数（即将对应的数组元素设置为False）。
# 3. 经过上述筛选后，所有未被标记为非质数的数字都是质数。
#
# 比如，要求100以内的所有素数，可以按照以下步骤进行筛选：
#
# 1. 初始化一个长度为100的布尔数组is_prime，将所有元素都设置为True。
# 2. 从2开始，依次枚举每个数字，如果这个数字是质数，则将它的所有倍数都标记为非质数。
# 3. 最终，is_prime中所有值为True的下标，就是100以内的所有素数。

# %%
def prime_bool_list(n:int):
    '''
    使用埃拉托色尼筛选法快速计算n以内的所有素数表
    '''
    # 初始化标记数组
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    
    # 标记合数
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return is_prime


# %%
# %%time
is_prime_arr=prime_bool_list(10**8)


# %%
# is_prime_arr = [True] * (10**9)
# 10亿级别的数组，内存占用已经在10gb了,所以假设我们要计算100亿以内的素数，光布尔数组就要占用100gb内存
# python中的布尔数组，是每一位占8字节的，所以10亿的布尔数组，占用比8gb大一些
# 这时我们可以用第三方库bitarray
# 实际上用numpy更好,numpy也支持bool数组
# import numpy as np
# arr = np.zeros(10**10, dtype=bool)
# 这样10亿的numpy布尔数组会占用1gb的内存空间,100亿才占用10gb空间
# 这样一般的电脑也能计算100亿级别的数据了

# %%
import numpy as np
def prime_bool_list2(n:int):
    '''
    使用埃拉托色尼筛选法快速计算n以内()的所有素数表
    使用numpy布尔数组优化,这样占用空间会更小
    '''
    is_prime = np.ones(n+1, dtype=bool) # 初始化所有数字为可能是质数
    is_prime[0] = False
    is_prime[1] = False
    # 从2开始，枚举所有数字
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:  # 如果当前数字是质数
            # 将当前质数的所有倍数标记为非质数
            for j in range(i * i, n, i):
                is_prime[j] = False

    return is_prime


# %%
# %%time
is_prime_arr=prime_bool_list2(10**8)
# 改成numpy布尔数组后,比python原生的列表慢一点,变成12秒,原生只要6秒

# %%
# 计算True数量的几种方法
# 方法1
# np.sum(is_prime_arr)

# 方法2
np.count_nonzero(is_prime_arr)

# %%
import sys
sys.getsizeof(is_prime_arr)


# %% [markdown]
# ## 欧拉筛法
#
# 埃拉托色尼筛选法有一个问题就是会有重复标记的情况，比如2的倍数，和3的倍数有很多重复的
#
# 欧拉筛优化了这一点，每个合数只标记一次。
#
#
# 欧拉筛算法是一种高效的质数筛法，用于求解一定范围内的素数。它的基本思想是遍历自然数时，将每个合数只标记一次，以避免重复操作。
#
# 算法步骤：
#
# 1. 初始化一个长度为 n+1 的布尔数组 `is_prime`，其中 `is_prime[i]` 表示 i 是否为素数。
# 2. 初始化一个空列表 `primes`，用于存储筛选出来的素数。
# 3. 从 2 开始遍历到 n：
#    1. 如果 `is_prime[i]` 为 True，说明 i 是素数，则将其添加到素数列表 `primes` 中。
#    2. 对于素数列表中的每个素数 p，如果 i * p > n，则跳出循环；否则将 i * p 标记为合数。
#    3. 如果 i 能整除 p，则跳出循环（因为 i 的最小质因子一定是 p，如果还有其他质因子，它们的倍数已经在之前的循环中被标记为合数了）。
#
# 欧拉筛由于每个合数只会标记一次,所以时间复杂度是O(n),空间复杂度也是O(n)

# %%
def euler_sieve(n):
    '''
    欧拉筛法,每个合数只会标记一次

    '''
    primes = []  # 存储筛选出来的素数
    is_prime = [True] * (n+1)  # 初始假设所有数都是素数
    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)  # 把当前素数添加到素数列表中
        for p in primes:
            # 如果当前数是p的倍数，则将其标记为合数
            if i * p > n:
                break
            is_prime[i * p] = False
            # 如果当前数是p的最小因子(说明是素数,因为p的倍数之前的循环已经标记了 is_prime[i * p] = False)，则跳出循环
            if i % p == 0:
                break
    return primes



# %%
# %%time
arr=euler_sieve(10**8)

# %%
import numpy as np
def euler_sieve2(n):
    '''
    欧拉筛法,numpy优化空间占用,使用位运算优化速度
    另外布尔数组只需要维护到n/2,因为只需要标记奇数,偶数必不是素数,所以不用标记了.
    布尔数组的第n位,表示的是第2*n+1这个奇数
    '''
    primes = []  # 存储筛选出来的素数
    is_prime = np.ones((n+1)//2,dtype=bool)  # 初始假设所有奇数都是素数
    is_prime[0] = False  # 1不是素数
    for i in range(1, (n+1)//2):
        # 根据i计算出当前的奇数
        odd = 2 * i + 1
        if is_prime[i]:
            # 当前素数添加到primes列表
            primes.append(odd)  
        for p in primes:
            # 如果当前数是p的倍数，则将其标记为合数
            if odd * p > n:
                break
            composite=odd*p
            # 如果是偶数,直接跳过
            if composite%2==0:
                continue
        
            # 奇数的情况,算出奇数对应的n
            position=(composite-1)//2
            is_prime[position] = False
    
            # 如果当前数是p的最小因子(说明是素数,因为p的倍数之前的循环已经标记了 is_prime[i * p] = False)，则跳出循环
            if odd % p == 0:
                break
    return primes



# %% [markdown]
# 折腾taichi半天，我发现局限性还是很大的，如果用不到gpu cuda的计算不如用julia，julia的限制更少，会比较快  
# 比如算10`**`8的质数，taichi和julia其实差不多速度。算10`**`10，因为taichi不支持这么大的数组，算不了。julia只需要100秒差不多，感觉应该是julia更快。  
# 在没优化的情况下，Julia更容易写出高性能代码。因为我只用了单线程，没有用到并行计算。 
# taichi用了并行计算，也许会比较快

# %%
# %%time
arr=euler_sieve2(10**8)

# %%
import numpy as np
from tqdm import tqdm

def euler_sieve_tqdm(n):
    '''
    欧拉筛法,numpy优化空间占用,使用位运算优化速度
    另外布尔数组只需要维护到n/2,因为只需要标记奇数,偶数必不是素数,所以不用标记了.
    布尔数组的第n位,表示的是第2*n+1这个奇数
    '''
    primes = []  # 存储筛选出来的素数
    is_prime = np.ones((n+1)//2,dtype=bool)  # 初始假设所有奇数都是素数
    is_prime[0] = False  # 1不是素数
    for i in tqdm(range(1, (n+1)//2)):
        # 根据i计算出当前的奇数
        odd = 2 * i + 1
        if is_prime[i]:
            # 当前素数添加到primes列表
            primes.append(odd)  
        for p in primes:
            # 如果当前数是p的倍数，则将其标记为合数
            if odd * p > n:
                break
            composite=odd*p
            # 如果是偶数,直接跳过
            if composite%2==0:
                continue
        
            # 奇数的情况,算出奇数对应的n
            position=(composite-1)//2
            is_prime[position] = False
    
            # 如果当前数是p的最小因子(说明是素数,因为p的倍数之前的循环已经标记了 is_prime[i * p] = False)，则跳出循环
            if odd % p == 0:
                break
    return primes



# %%
# import numpy as np
from tqdm import tqdm
import taichi as ti
ti.init(arch=ti.cpu,cpu_max_num_threads=1,debug=True)
# 最大长度只有int32，属于是坑了
n=10**8
is_prime=ti.field(shape=(n+1)//2,dtype=bool) # 初始假设所有奇数都是素数
is_prime.fill(True)
primes=ti.field(dtype=ti.u64,shape=n//10)

@ti.kernel
def euler_sieve_tqdm_ti():
    '''
    欧拉筛法,numpy优化空间占用,使用位运算优化速度
    另外布尔数组只需要维护到n/2,因为只需要标记奇数,偶数必不是素数,所以不用标记了.
    布尔数组的第n位,表示的是第2*n+1这个奇数
    '''
    # primes=[] # 存储筛选出来的素数
    count=0
    # is_prime. 
    is_prime[0] = False  # 1不是素数
    # print('ok')
    for i in  range(1, (n+1)//2):
        # 根据i计算出当前的奇数
        # print('test',i)
        odd = 2 * i + 1
        if is_prime[i]:
            # 当前素数添加到primes列表
            
            primes[count]=odd
            count+=1
        #     # np.append(primes,odd)
        for index in range(count):
            p=primes[index]
            # 如果当前数是p的倍数，则将其标记为合数
            if odd * p > n:
                break
            composite=odd*p
            # 如果是偶数,直接跳过
            if composite%2==0:
                continue
        
            # 奇数的情况,算出奇数对应的n
            position=(composite-1)//2
            is_prime[position] = False
    
            # 如果当前数是p的最小因子(说明是素数,因为p的倍数之前的循环已经标记了 is_prime[i * p] = False)，则跳出循环
            if odd % p == 0:
                break
    # return primes




# %%
# euler_sieve_tqdm_ti()

# %%
# import numpy as np
# primes=primes.to_numpy().tolist()

# %% magic_args="false" language="script"
# import h5py
#
# # 创建一个HDF5文件
# f = h5py.File('primes20yi.hdf5', 'w')
#
# # 创建一个数据集
# # data = [1, 2, 3, 4, 5]
# dset = f.create_dataset('primes', data=newP)
#
# # 设置数据集的属性
# dset.attrs['description'] = '20亿以内的素数'
#
# # 关闭HDF5文件
# f.close()
#

# %% magic_args="false" language="script"
# import h5py
# import numpy as np
# f = h5py.File('primes100yi.hdf5', 'r')
# primes=np.array(f['primes'])
# f.close()

# %% [markdown]
# ## 最大公约数
# 令a和b是两个整数，不全为0。能使d|a和d|b的最大整数d称为a和b的最大公约数。a和b的最大公约数记作gcd（a，b）。

# %%
# python中最大公约数的计算
import math

a = 12
b = 18

gcd = math.gcd(a, b)

print(gcd)  # 输出 6


# %%
# 欧几里得算法（辗转相除法）计算最大公约数
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a = 12
b = 18

gcd_value = gcd(a, b)

print(gcd_value)  # 输出 6


# %%
# 欧几里得扩展
def Exgcd(a, b):
    if b == 0:
        # 最后一项的x，y分别为1，0
        return a, 1, 0
    d, x, y = Exgcd(b, a % b)
    return d, y, x - (a // b) * y

