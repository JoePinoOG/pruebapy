"""La clínica dental “El Diente de Oro” hizo un convenio con DUOC y le ha ofrecido algunos tratamientos para sus trabajadores y su grupo familiar. 
Los tratamientos serán descontados por planilla mensualmente por un periodo de 12 meses. Todos los tratamientos incluyen:  
✓ Limpieza y destartraje  ✓ Aplicación de sellante   ✓ Aplicación de fluor.  
  
Los tratamientos ofrecidos son:   
Tratamientos 	Valor  
Carillas Porcelana  	$250.000  
Implantes Dentales 	$475.000  
Ortodoncia Brackets  	$800.000  

Adicionalmente, se presentan los siguientes descuentos, sobre el total a pagar:  
✓	Trabajador Auxiliar, se aplicará un descuesto del 15%
  ✓ Trabajador Administrativo, se aplica un descuento del 10%  
  ✓ Trabajador Docente, 5% descuento.  
 
Por lo tanto, se pide que desarrolle un programa en Python que permita determinar el total a pagar por una cotización.   
  
Las condiciones generales del programa son:   
  
✓	Presentar un menú con las siguientes opciones:   
 
1.	Cotización:   o Debe ofrecer los tratamientos disponibles. 
o	Debe calcular el total de la cotización, además debe consultar si tiene descuento y aplicarlo si corresponde.  
o	Desplegar el total de la cotización e indicar el valor de las cuotas mensuales  
  
2.	Renunciar:  o Debe permitir eliminar la cotización echa anteriormente, volver al menú y permitir realizar una nueva cotización. 
 
3.	Salir del programa sin considerar la cotización que se pueda haber ingresado.   

"""
op=0
puesto=0
total=0
total1=0
total2=0
total3=0
dsc=0
ccp=0
cip=0
cob=0
print("*"*30)
print("BIENVENIDO A EL DIENTE DE ORO")
print("*"*30)
print("Presione 4 cuando este lista la cantidad de tratamientos seleccionados")
print("  Tratamientos 	         Valor  ")
print("1.Carillas Porcelana  	$250.000")
print("2.Implantes Dentales 	$475.000")
print("3.Ortodoncia Brackets  	$800.000")
print("Presione 4 cuando este lista la cantidad de tratamientos seleccionados")
while True:
    try:
        op=int(input("seleccione su tipo de tratamiento: "))
        if op==1:
            total1=total1+250000
            ccp=ccp+1
        elif op==2:
            total2=total2+475000
            cip=cip+1
        elif op==3:
                    total3=total3+800000
                    cob=cob+1
        elif op==4:
                    break
        else:
            print("#"*30)
            print("ERROR:ingrese una opcion valida!!!!")
    except:
        print("#"*30)
        print("ERROR:ingrese un valor numerico!!!")
while True:
    try:
            print("*"*15)
            print("1.Si")
            print("2.No")
            print("*"*15)
            dsc=int(input("usted posee descuento?: "))
            if dsc==1:

                while True:
                    try:
                        print("1.Trabajador Auxiliar")
                        print("2.Trabajador Administrativo")
                        print("3.Trabajador Docente")
                        puesto=int(input("Seleccione su puesto de trabajo para acceder al descuento:"))
                        if puesto==1:
                            print("usted posee un descuento del 15%")
                            break
                        elif puesto==2:
                            print("usted posee un descuento del 10%")
                            break
                        elif puesto==3:
                            print("usted posee un descuento del 5%")
                            break
                        else:
                            print("#"*30)
                            print("ERROR:ingrese una opcion valida!!!!")
                    except:
                        print("#"*30)
                        print("ERROR:ingrese un valor numerico!!!")
                break
            elif dsc==2:
                break
            else:
                print("#"*30)
                print("ERROR:ingrese una opcion valida!!!!")
    except:
            print("#"*30)
            print("ERROR:ingrese un valor numerico!!!")
print("#"*20)
print("      COTIZACION      ")
print("#"*20)
if ccp>1:
        print(f"{ccp} tratamiento(s) carillas de porcelana: ${total1}")
if cip>1:
        print(f"{cip}tratamiento(s) implantes dentales: ${total2}")
if cob>1:
        print(f"{cob}tratamiento(s) ortodoncia brakets: ${total3}")
total=total1+total2+total3
print(f"subtotal: {total}")
if dsc==1:
    if puesto==1:
        print("descuento de 15%")
        dt=total=total-total*15/100
        print(f"total: {dt}")
        cuota=dt/12
        print(f"son 12 cuotas de: ${cuota}")
    if puesto==2:
        print("descuento de 10%")
        dt=total=total-total*10/100
        print(f"total: {dt}")
        cuota=dt/12
        print(f"son 12 cuotas de: ${cuota}")
    if puesto==3:
        print("descuento de 5%")
        dt=total=total-total*5/100
        print(f"total: {dt}")
        cuota=dt/12
        print(f"son 12 cuotas de: ${cuota}")
    if dsc==2:
        print("no aplica descuento")
        print(f"total:{total}")
        cuota=total/12
        print(f"total cuota: {cuota}")
print("Sonría Bonito!!!!")
