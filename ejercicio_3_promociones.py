'''No se completò el ejercicio, pero era una parte de solicitud de los datos y hacer validaciòn.'''


import pandas as pd

# crear el df
df = pd.read_csv('Prueba_Promociones.csv')

# Ingresar datos requeridos
fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
categoria = input("Ingrese la categoría : ")
uso = input("Ingrese el uso: ")
sku = input("Ingrese el SKU: ")
while not sku:
    sku = input("El campo SKU no puede estar vacío. Ingrese el SKU: ")
porcentaje = float(input("Ingrese el porcentaje de crecimiento : "))
inventario_inicial = int(input("Ingrese el inventario inicial: "))