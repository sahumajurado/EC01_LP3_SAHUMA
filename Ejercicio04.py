#Solicitar dato al usuario
ganancia = int(input("Ingrese su ganancia: "))
#Condiciones
if 0 <= ganancia <= 1000:
    r1 = ganancia * (5/100)
    print(f"Donación: {r1}")
elif 1000 < ganancia <= 1500:
    r2 = ganancia * (7/100)
    print(f"Donación: {r2}")
elif 1500 < ganancia <= 2000:
    r3 = ganancia * (8/100)
    print(f"Donación: {r3}")
elif 2000 < ganancia <= 5000:
    r4 = ganancia * (10/100)
    print(f"Donación: {r4}")
else:
    r5 = ganancia * (15/100)
    print(f"Donación: {r5}")
