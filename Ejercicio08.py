#Solicitando al usuario la cantidad de citas
citas = int(input("Cantidad de citas: "))
#Condiciones
if citas <= 3:
    c1 = citas * 200
    print(f"Total a pagar: {c1}")
elif 4 <= citas <= 5:
    c2 = (citas-3) * 150 + 600
    print(f"Total a pagar: {c2}")
elif 6 <= citas <=8:
    c3 = (citas-5) * 100 + 900
    print(f"Total a pagar: {c3}")
else:
    c4 = (citas-8) * 50 + 1200
    print(f"Total a pagar: {c4}")