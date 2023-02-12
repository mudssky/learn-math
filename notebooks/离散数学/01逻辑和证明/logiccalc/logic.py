

# 双条件语句，双向蕴含，pq两个命题都为真时才为真。
def biconditional_statement(p: bool, q: bool) -> bool:
    '''
    双条件语句，双向蕴含，pq两个命题都为真时才为真。
    '''
    # p和q有相同的真值时，为真
    if p == q:
        return True
    return False


def calc_inverse(p: bool, q: bool):
    '''
    反命题计算
    '''
    return condition_statement(not p, not q)

# 下面计算一下逆否命题，可以发现和原命题的真值一样


def calc_contrapositive(p: bool, q: bool):
    return condition_statement(not q, not p)

# 这里写一些通用函数
# 转换bool变量为T和F,这样真值表会比较简洁


def bool_to_TF(isTrue: bool):
    if isTrue:
        return 'T'
    return 'F'

# 条件语句


def condition_statement(p: bool, q: bool):
    '''
    条件命题
    '''
    if q:
        return True
    # q为假的情况
    else:
        if p:
            return False
        return True
