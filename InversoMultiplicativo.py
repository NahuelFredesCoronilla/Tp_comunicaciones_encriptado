def inverso_modular(a,m): #a numero, m modulo
    r0 = m
    r1 = a
    s0 = 0
    s1 = 1
    t0 = 1
    t1 = 0

    while r1 != 0:
        q = r0 // r1

        #Actualizamos r, s y t
        r2 = r0 - q * r1
        s2 = s0 - q * s1
        t2 = t0 - q * t1

        #Desplazamos los valores para el proximo ciclo
        r0 = r1
        r1 = r2
        s0 = s1
        s1 = s2
        t0 = t1
        t1 = t2

    if r0 == 1:
        return (s0 % m + m) % m
    else:
        return -1

a = 5
m = 12
inverso = inverso_modular(a,m)

print(inverso)
