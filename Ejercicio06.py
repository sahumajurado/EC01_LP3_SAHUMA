#Solicitud de la cantidad de alumnos 
est = int(input("Cantidad de alumnos: "))
#Condiciones
if est <30:
    r1 = 4000/est
    c1 = round(r1, 1)
    print(f"Costo por alumno: {c1}")
    print("Total a pagar: S/. 4000")
elif 30 <= est <= 49:
    r2 = 95 * est
    c2 = round(r2, 1)
    print("Costo por estudiante: S/. 95")
    print(f"Total a pagar: {c2}")
elif 50 <= est <= 99:
    r3 = 70 * est
    c3 = round(r3, 1)
    print("Costo por estudiante: S/. 70")
    print(f"Total a pagar: S/.{c3}")
else:
    r4 = 65 * est
    c4 = round(r4,1)
    print("Costo por alumno: S/. 65")
    print(f"Total a pagar: {c4}")