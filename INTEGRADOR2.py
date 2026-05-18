# Escribir un algoritmo que permita ingresar los números de legajo de los alumnos de un curso
# y su nota de examen final. El fin de la carga se determina ingresando un -1 en el legajo.
# Informar para cada alumno si aprobó o no el examen considerando que se aprueba con nota
# mayor o igual a 4. Se debe validar que la nota ingresada sea entre 1 y 10. Terminada la carga
# de datos, informar:
# • Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
# • Cantidad de alumnos que desaprobaron el examen. Nota menor a 4.
# • Porcentaje de alumnos que están aplazados (tienen 1 en el examen).

total_notas=0
mayor_a_cuatro=0
menor_a_cuatro=0
aplazados=0
total_notas=0

legajo=int(input("Ingrese su legajo, -1 finaliza el programa: "))
while legajo!=-1:
    
    nota=int(input("Ingrese nota: "))
    
    while nota<1 or nota>10:
        print("La nota es invalida: ")
        nota=int(input("Ingrese nota: "))
    
    if nota>1 and nota<4:
        print("DESAPROBADO")
        menor_a_cuatro+=1
        total_notas+=1
    elif nota>=4:
        print("APROBADO")
        mayor_a_cuatro+=1
        total_notas+=1
    elif nota==1:
        print("APLAZADO")
        menor_a_cuatro+=1
        aplazados+=1
        total_notas+=1
    
    porcentaje_aplazos=((aplazados/total_notas)*100)
    
    legajo=int(input("Ingrese su legajo, -1 finaliza el programa: "))

if legajo==-1:
        print("fin del programa")
        
print()
print("Cantidad de notas ingresadas", total_notas)
print("Alumnos que aprobaron con mas de 4: ",mayor_a_cuatro)
print("Alumnos que desaprobaron: ", menor_a_cuatro)
print("Alumnos que desaprobaron con aplazados: ", aplazados)
print("Porcentaje de alumnos aplazados: ",porcentaje_aplazos,"%")