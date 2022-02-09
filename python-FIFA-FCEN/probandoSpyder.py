# a = float(input("Ingrese el valor del término cuadrático: "))
# b = float(input("Ingrese el valor del término lineal: "))
# c = float(input("Ingrese el término independiente: "))

# discr = b**2 - 4 * a * c

# if (discr < 0):
#     print("No existen raíces reales")
# elif (discr == 0):
#     resp = (-b) / (2 * a)
#     print("Respuesta:", resp)
# else:
#     resp1 = ((-b) + (b**2 - 4 * a * c)**(0.5)) / (2 * a)
#     resp2 = ((-b) - (b**2 - 4 * a * c)**(0.5)) / (2 * a)
#     print('La respuesta dio 2 raíces. La primera es {0} y la segunda {1}'.format(resp1,resp2))

num_ingresado = int(input("Ingrese un número entero: "))

if (not(num_ingresado % 2)):
    print(f'El valor ingresado, {num_ingresado}, es par')
else:
    print("El número ingresado es impar, el siguiente par es ",(num_ingresado+1))