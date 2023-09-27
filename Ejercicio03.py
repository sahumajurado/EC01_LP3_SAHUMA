#Solicitud de cantidad de horas
horas = int(input("Ingrese la cantidad de horas: "))
#Condiciones
if horas<=4:
    print("Importe a pagar: S/.6 soles")
else: 
    horas>4
    adicional = ((horas - 4) * 2) + 6
    print(f"Importe a pagar: S/. {adicional}")
