#Una empresa cuenta con N empleados, divididos en tres categorías A, B y C. Por cada empleado
#se lee su legajo, categoría y salario. Se solicita elaborar un informe que contenga:
#• Importe total de salarios pagados por la empresa.
#• Cantidad de empleados que ganan más de $20000.
#• Cantidad de empleados que ganan menos de $5000, cuya categoría sea “C”.
#• Legajo del empleado que más gana.
#• Sueldo más bajo.
#• Importe total de sueldos por cada categoría.
#• Salario promedio.

total_salarios = 0
mas_20000 = 0
menos_5000_c = 0

mayor_sueldo = 0
legajo_mayor = 0
menor_sueldo = 999999999

total_a = 0
total_b = 0
total_c = 0

empleados = int(input("Ingrese cantidad de empleados: "))

for e in range(empleados):

    print("EMPLEADO", e+1)

    legajo = int(input("Ingrese legajo: "))

    categoria = input("Ingrese categoria (A, B o C): ")

    while categoria != "A" and categoria != "B" and categoria != "C":
        print("Categoria invalida")
        categoria = input("Ingrese categoria (A, B o C): ")

    salario = int(input("Ingrese salario: $"))

    while salario < 0:
        print("Ingrese un monto valido")
        salario = int(input("Ingrese salario: $"))

    total_salarios += salario

    if salario > 20000:
        mas_20000 += 1

    if salario < 5000 and categoria == "C":
        menos_5000_c += 1

    if salario > mayor_sueldo:
        mayor_sueldo = salario
        legajo_mayor = legajo

    if salario < menor_sueldo:
        menor_sueldo = salario

    if categoria == "A":
        total_a += salario
    elif categoria == "B":
        total_b += salario
    else:
        total_c += salario

promedio = total_salarios / empleados

print()
print("Importe total pagado: $", total_salarios)
print("Empleados que ganan mas de $20000:", mas_20000)
print("Empleados categoria C que ganan menos de $5000:", menos_5000_c)
print("Legajo del que mas gana:", legajo_mayor)
print("Sueldo mas bajo: $", menor_sueldo)
print("Total categoria A: $", total_a)
print("Total categoria B: $", total_b)
print("Total categoria C: $", total_c)
print("Salario promedio: $", promedio)
    