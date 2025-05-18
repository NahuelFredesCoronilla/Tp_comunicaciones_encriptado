def inverso_multiplicativo(a,m): #a numero, m modulo
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
    
def crear_tabla1():
    lista_char = [
        'A','B','C','D','E','F','G','H','I','J',
        'K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        ' ', '!', '@', '#', '$', '%', '*', '(', ')', '.', '+', '/', '&', ':', ';', ',',
        '¿', '?', '"', '\'', '[', ']', '°',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'Á', 'É', 'Í', 'Ó', 'Ú'
    ]
    table = {}
    for i, ch in enumerate(lista_char):
        table[ch] = i
    return table

def crear_tabla2():
    lista_char = [
        '9', '8', '7', '6', '5', '4', '3', '2', '1', '0',
        '.', ',', ';', ':', ' ', '´', '"', '°', ')', '(',
        '*', '%', '$', '#', '!', '?', '¿', 'Z', 'Y', 'X',
        'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'Ñ', 'N', 'M', 'L', 'K',
        'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A'
    ]
    table = {}
    for i, ch in enumerate(lista_char):
        table[ch] = i
    return table


# Se utiliza para mayor velocidad a la hora de buscar los valores correspondientes
def crear_tabla_inversa(table):
    inv_table = {}
    for k, v in table.items():
        inv_table[v] = k
    return inv_table


# Utilizado para puebas
def encrypt(text, a, b, m, table, inv_table):
    encrypted_text = []
    for ch in text:
        if ch in table:
            X = table[ch]
            Y = (a * X + b) % m
            encrypted_text.append(inv_table[Y])
        else:
            encrypted_text.append(ch)  # Si el caracter no está en la tabla, lo deja igual
    return ''.join(encrypted_text)


def decrypt(cipher, a_inv, b, m, table, inv_table):
    sb = []
    for ch in cipher:
        Y = table[ch]
        X = ((Y - b) * a_inv) % m
        sb.append(inv_table[X])
    return ''.join(sb)


def main():
    table1 = crear_tabla1()
    inv_table1 = crear_tabla_inversa(table1)

    table2 = crear_tabla2()
    inv_table2 = crear_tabla_inversa(table2)

    print("-------------------------------------TABLA 1-------------------------------------")
    iterador_tabla(table1, inv_table1)
    print("\n")

    print("-------------------------------------TABLA 2-------------------------------------")
    iterador_tabla(table2, inv_table2)

    # La tercera tabla no se utiliza ya que hay caracteres del mensaje que no se encuentran en ella

    
def iterador_tabla(table, inv_table):
    m = len(table)
    b1 = 9784562 % m
    b2 = 30018 % m
    b3 = 375839 % m

    texto_encriptado = "HNÑ8NÑ1624J1RPL1DN41L0D2Ñ1F$2ZNT821L41LT$JFD$8211"
    for a in range(1, m):
        print("-----------------------------------------------------------------------")
        print(f"a = {a}")
        
        a_inv = inverso_multiplicativo(a, m)

        if a_inv == -1:
            print("La semilla:", a, "No tiene inverso multiplicativo" )
            continue

        desencriptado = ""

        prueba1 = decrypt("60F", a_inv, b1, m, table, inv_table)
        if prueba1 == "HSP":
            desencriptado = decrypt(texto_encriptado, a_inv, b1, m, table, inv_table)
        

        prueba2 = decrypt("60F", a_inv, b2, m, table, inv_table)
        if prueba2 == "HSP":
            desencriptado = decrypt(texto_encriptado, a_inv, b2, m, table, inv_table)
        
        
        prueba3 = decrypt("60F", a_inv, b3, m, table, inv_table)
        if prueba3 == "HSP":
            desencriptado = decrypt(texto_encriptado, a_inv, b3, m, table, inv_table)
        
        if desencriptado != "":
            print(f"Descifrado: {desencriptado}")
        else:
            print("Ninguno de lo de los valores de b verifican el encriptado valido")   


if __name__ == "__main__":
    main()

'''
def test():
    table = crear_tabla2()
    inv_table = crear_tabla_inversa(table)
    m = len(table)

    print(table)
    print(inv_table)

    texto_simple = "HOLA"
    a = 5
    b = 3
    
    a_inv = inverso_multiplicativo(a, m)

    encriptado = encrypt(texto_simple, a, b, m, table, inv_table)
    desencriptado = decrypt(encriptado, a_inv, b, m, table, inv_table)
    
    print("Texto Original: ", texto_simple)
    print("Encriptado: ", encriptado)
    print("Desencriptado: ", desencriptado)

test()
'''