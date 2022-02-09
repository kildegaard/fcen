a = float(input("Ingrese el valor del término cuadrático"))
b = float(input("Ingrese el valor del término lineal"))
c = float(input("Ingrese el término independiente"))

discr = b**2 - 4 * a * c

if (discr < 0):
    print("No existen raíces reales")
elif (discr == 0):
    resp = (-b) / (2 * a)
    print("Respuesta:", resp)
else:
    resp1 = ((-b) + (b**2 - 4 * a * c)**(0.5)) / (2 * a)
    resp2 = ((-b) - (b**2 - 4 * a * c)**(0.5)) / (2 * a)
    print("Raíz 1:", resp1)
    print("Raíz 2:", resp2)
