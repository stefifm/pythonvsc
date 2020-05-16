print("Verficacion de acceso")


nota_alumno=input()

def evaluacion(nota):
    valor="aprobado"
    if nota<5:
        valor="suspenso"
    return valor

print(evaluacion(int (nota_alumno)))
