#Leer números que representan edades de un grupo de personas, finalizando la lectura cuando
#se ingrese el número 999. Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o
#más y el promedio de edad de ambos grupos. Descartar valores que no representan una edad
#válida. (Se considera válido una edad entre 0 y 100).

menor = 0
mayor = 0

suma_menor = 0
suma_mayor = 0

masviejo = 0

edad = int(input("Ingrese edad: "))

while edad != 999:

    if 0 <= edad <= 100:

        if edad > masviejo:
            masviejo = edad

        if edad < 18:
            menor += 1
            suma_menor += edad
        else:
            mayor += 1
            suma_mayor += edad

    else:
        print("Edad inválida")

    edad = int(input("Ingrese edad: "))

print("FIN")
print("Menores:", menor)
print("Mayores:", mayor)
print("Más viejo:", masviejo)

if menor > 0:
    print("Promedio menores:", suma_menor / menor)

if mayor > 0:
    print("Promedio mayores:", suma_mayor / mayor)