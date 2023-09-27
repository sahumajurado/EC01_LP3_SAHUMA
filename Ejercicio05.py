#Solicitar las 4 notas al usuario
n1 = int(input("Ingrese su nota del Examen 01: "))
n2 = int(input("Ingrese su nota del Examen 02: "))
n3 = int(input("Ingrese su nota del Examen 03: "))
n4 = int(input("Ingrese su nota del Examen 04: "))
#Ponderando las notas
p1 = n1 * (1/4)
p2 = n2 * (1/4)
p3 = n3 * (1/10)
p4 = n4 * (2/5)
prom = p1 + p2 + p3 +p4
#Devolviendo el promedio final
print(f"Promedio: {prom}")