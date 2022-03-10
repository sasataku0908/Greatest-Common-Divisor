import functools 
N = int(input())

list = [int(x) for x in input().split()]

def gcd_e(a, b):
    while b:
        a, b = b, a % b
    return a

print(functools.reduce(gcd_e, list)) 
###########
reduce関数を用いて、作成した二つの値の最大公約数を求める関数にlistの値を一つづつ代入していく。
例：
list = [12,18,24] 12 18　→ 6 24 → 6
