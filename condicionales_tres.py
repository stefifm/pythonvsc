sueldo_ceo=int(input("Introduce sueldo CEO"))
print("Sueldo de CEO: " + str(sueldo_ceo))

sueldo_director=int(input("Introduce sueldo director"))
print("Sueldo de CEO: " + str(sueldo_director))

sueldo_gerente=int(input("Introduce sueldo gerente"))
print("Sueldo de CEO: " + str(sueldo_gerente))

sueldo_senior=int(input("Introduce sueldo senior"))
print("Sueldo de CEO: " + str(sueldo_senior))

if sueldo_senior<sueldo_gerente<sueldo_director<sueldo_ceo:
    print("Funciona")
else:
    print("Algo falla en la empresa")

#edad=45 concatenar operadores de comparacion

#if 0<edad<100:
#    print("Edad es correcta")
#else:
#    print("Edad incorrecta")
