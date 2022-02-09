# Ejercicio 1.5 - Pelota que rebota

initial_height = 100
height_bounce = 3 / 5

heights = []

height = initial_height

for iter in range(10):
    actual_height = height * height_bounce
    heights.append(round(actual_height, 4))
    height = actual_height
print(*heights, sep='\n')
