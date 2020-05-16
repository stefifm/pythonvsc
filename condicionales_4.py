# print("Asignacion de becas año 2020")

# distancia_escuela=int(input("Introduce distancia en km: "))
# print(distancia_escuela)

# num_hermanos=int(input("Introduce el numero de hermanos: "))
# print(num_hermanos)

# sueldo_familia=int(input("Introduce sueldo familia: "))
# print(sueldo_familia)

 # if distancia_escuela>40 and num_hermanos>2 and sueldo_familia<=20000:
 #     print("Beca aprobada")
 # 
 # else: 
 #     print("Beca no aprobada")

#if distancia_escuela>40 and num_hermanos>2 or sueldo_familia<=20000:
#    print("Beca aprobada")

#else: 
#    print("Beca no aprobada")

print("Materias optativas Año 2020")
print("Testing de Software - Informatica grafica - Accesibilidad en WEB")
opcion=input("Escribe la materia elegida: ")

materia=opcion.lower()

if materia in ("Testing de Software", "Informatica Grafica", "Accesibilidad WEB"):
    print("Materia elegida: ", materia)
else:
    print("La materia elegida no esta contemplada")
