print("Verificacion de acceso")

nota_alumno=int(input("Introduce nota: "))

if nota_alumno<=1:
    print("Abandono")
elif nota_alumno<=4:
    print("Libre")
elif nota_alumno<=6:
    print("Regular")
elif nota_alumno<=7:
    print("Promocionado")
else:
    print("Aprobacion Directa")
print("El programa ha finalizado")