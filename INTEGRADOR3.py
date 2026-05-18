#Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
#• Aplica el precio base a la primera docena de unidades.
# Aplica un 10% de descuento a todas las unidades entre 13 y 100.
#• Aplica un 25% de descuento a todas las unidades por encima de las 100.
#Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. El
#cálculo resultante sería:

precio_base=100
precio_diezporciento=precio_base*0.9
precio_veinticinco=precio_base*0.75
venta=0
diez_off=0
solo_base=0

producto=int(input("Ingrese cantidad solicitada del producto, -1 finaliza el programa: "))

while producto!=-1:
    
    valor_venta=precio_base*producto
    promedio_diez=precio_diezporciento/producto
    promedio_veinticinco=precio_veinticinco/producto
    
    if producto>0 and producto<13:
        print("valor de la venta: $",valor_venta)
        venta+=1
        solo_base+=1
    
    elif producto>=13 and producto <=100:
        print("10% OFF, Nuevo precio: $",precio_diezporciento*producto)
        venta+=1
        diez_off+=1
    
    else:
        print("25% OFF, Nuevo precio: $", precio_veinticinco*precio_base)
        venta+=1
    
    producto=int(input("Ingrese cantidad solicitada del producto, -1 finaliza el programa: "))

if producto==-1:
    print("Finalizo su consulta")
    
print()
print("Cantidad de ventas realizadas total: ",venta)
print("Ventas con 10% OFF, :", diez_off)
print("Ventas a precio de lista: ", solo_base)