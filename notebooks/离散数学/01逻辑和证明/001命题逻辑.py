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
import pandas as pd


# %%
# 这里写一些通用函数
# 转换bool变量为T和F,这样真值表会比较简洁
def bool_to_TF(isTrue:bool):
	if isTrue:
		return 'T'
	return 'F'

# %%
# 真值表基本的p q两个命题的真值排列组合
truthTableBase={
	'p':[True ,True,False,False],
	'q':[True,False,True,False],
}
df=pd.DataFrame(truthTableBase)
df.applymap(lambda x : 'T' if x else 'F')

# %%
# 下面试一下与运算符
df['p∧q']=df['p']&df['q']
# 不会影响原数据,会返回一个新的dataframe
df.applymap(bool_to_TF)

# %%
# 或运算符
df['p∨q']=df['p']|df['q']
df.applymap(bool_to_TF)

# %%
# 异或运算符
df['p⊕q']=df['p']^(df['q'])
df.applymap(bool_to_TF)


# %%
def condition_statement(p:bool,q:bool):
    if q:
        return True
    # q为假的情况
    else:
        if p:
            return False
        return True
# 条件语句 
# apply 函数默认axis=0,作用是对每一列执行,改为axis=1则是对每一行执行
df['p→q']=df.apply(lambda row : condition_statement(row['p'],row['q']),axis=1)

df.applymap(bool_to_TF)


# %%
# 下面计算一下逆否命题，可以发现和原命题的真值一样
def calc_contrapositive(p:bool,q:bool):
    return condition_statement(not q, not p)
df['¬q→¬p']=df.apply(lambda row : calc_contrapositive(row['p'],row['q']),axis=1)
df.applymap(bool_to_TF)


# %%
# 下面计算一下逆命题
def calc_converse(p:bool,q:bool):
    return condition_statement( q,p)
df['q→p']=df.apply(lambda row : calc_converse(row['p'],row['q']),axis=1)
df.applymap(bool_to_TF)


# %%
# 下面计算一下反命题
def calc_inverse(p:bool,q:bool):
    return condition_statement( not p,not q)
df['¬p→¬q']=df.apply(lambda row : calc_inverse(row['p'],row['q']),axis=1)
df2 =df.applymap(bool_to_TF)
df2

# %%
import pyperclip
pyperclip.copy(df2.to_markdown(index=False))


# %%
# 双条件语句，双向蕴含，pq两个命题都为真时才为真。
def biconditional_statement(p:bool,q:bool)->bool:
    # p和q有相同的真值时，为真
    if p==q:
        return True
    return False
df['p↔q']=df.apply(lambda row : biconditional_statement(row['p'],row['q']),axis=1)
df.applymap(bool_to_TF)


# %%
# 下面试着用上面的运算方法算一个复合命题
df['(p∨¬q)→(p∧q)']=df.apply(lambda row : condition_statement(row['p']|(not row['q']),row['p']&row['q']),axis=1)
df.applymap(bool_to_TF)

# %%
pyperclip.copy(df.applymap(bool_to_TF).to_markdown())

# %%
# 下面用真值表证明德摩根律
df3 =pd.DataFrame(truthTableBase)
df3['p∨q']=df3['p']|df3['q']
df3['¬(p∨q)']=~df3['p∨q']
df3['¬p']= ~df3['p']
df3['¬q']=~df3['q']
df3['¬p∧¬q']=df3['¬p']&df3['¬q']
df3.applymap(bool_to_TF)


# %%
pyperclip.copy(df3.applymap(bool_to_TF).to_markdown())

# %%
import logiccalc as lgc
# 证明一个条件命题的等价式
df3 =pd.DataFrame(truthTableBase)
df3['¬p']= ~df3['p']
df3['¬p∨q']=df3['¬p']|df3['q']
df3['p→q']=df.apply(lambda row :lgc.condition_statement(row['p'],row['q']),axis=1)
df3.applymap(bool_to_TF)


# %%
