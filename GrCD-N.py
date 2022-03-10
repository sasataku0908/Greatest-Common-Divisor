list = [int(x) for x in input().split()]

def gcd_t(list_g1):
    for i in reversed(range(1, min(list_g1)+1)):
        print(i)
        for j in list_g1:
            if j%i!=0:
                break
        else:
            return i
print(gcd_t(list))
###########
入力例:
3
12 18 24 

出力:
6
