

total_litros=0
mayor_produccion=0
total_altacalidad=0
dia_calidadbaja=0

dias=int(input("Ingrese cantidad de dias: "))
while dias<0:
    print("Cant. dias no puede ser menor a 0")
    dias=int(input("Ingrese cantidad de dias: "))

for d in range(dias): 
    print("----- DIA",d+1,"-----")
    litros_dia=0
    print()
    
    alta_calidad=0
    calidad_media=0
    calidad_baja=0
    
    tanques=int(input("ingrese cantidad de tanques a evaluar: "))
    while tanques<0:
        print("Cantidad de tanques debe ser mayor a 0")
        tanques=int(input("ingrese cantidad de tanques a evaluar: "))
    
    for t in range(tanques):
        print("~ TANQUE",t+1,"~")
        litros=int(input("litros producidos: "))

        while litros<0:
            print("Litros no puede ser menor que 0")
            litros=int(input("litros producidos: "))

        litros_dia += litros
        total_litros += litros
        
        if litros>1000:
            alta_calidad+=1
            
            
            print("Calidad de produccion: ALTA")
        elif litros>=500 and litros <=1000:
            print("Calidad de produccion: MEDIA")
            calidad_media+=1
            
            
        elif litros <500:
            print("Calidad de produccion: BAJA")
            calidad_baja+=1
            
            
            
        promedio=litros_dia/tanques
          
    if calidad_baja>2:
        dia_calidadbaja+=1
        
        promedio=litros_dia/tanques

    print()
    print("-----ESTADISTICAS DEL DIA-----")
    print("Litros del dia: ",litros_dia)
    print("Cantidad de tanques de baja calidad:",calidad_baja)
    print("Cantidad de tanques de alta calidad:",alta_calidad)
    print("Cantidad de tanques de calidad media:",calidad_media)
    print("Promedio de produccion del dia: ",promedio)
    print() 
      
total_altacalidad=alta_calidad 
promedio_gral=total_litros/dias

print("-----ESTADISTICAS GENERALES-----")
print("Litros totales producidos: ",total_litros)
print("Promedio general de produccion: ",promedio_gral)
print("Dia con  mayor produccion: ", mayor_produccion)
print("Cantidad de dias con alta productividad: ",total_altacalidad)
print("Dias con calidad baja: ",dia_calidadbaja)