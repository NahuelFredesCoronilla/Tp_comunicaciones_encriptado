
def mcd(a,b):
    if(b > a):
        temp = a
        a = b
        b = temp

    while b != 0:
        resto = a % b
        a = b
        b = resto

    return a


a = 105
b = 252
resp = mcd(a,b)
print("El mcd es ", resp)







