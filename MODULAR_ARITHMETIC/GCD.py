a = 66528
b = 52920

def gcd(a,b):
    if(a==0 or b==0):
        return a if a else b
    return gcd(b%a,a)

print(gcd(a,b))