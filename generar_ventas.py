import pandas as pd
import numpy as np
import random
import os.path

num_registros = 100000

np.random.seed(42)

categorias = ['Electrónica', 'Ropa', 'Hogar', 'Deportes', 'Juguetes', 'Alimentación', 'Belleza']

# Comprobar si el archivo ya existe
archivo = 'ventas_100k.csv'
if os.path.isfile(archivo):
    print(f"Actualizando archivo existente: {archivo}")
    df = pd.read_csv(archivo)
    
    # Verificar si hay suficientes registros, si no, ajustar num_registros
    if len(df) < num_registros:
        print(f"El archivo solo tiene {len(df)} registros. Se agregarán datos solo a estos registros.")
        num_registros = len(df)
    elif len(df) > num_registros:
        print(f"El archivo tiene {len(df)} registros, más de los esperados. Se actualizarán solo los primeros {num_registros}.")
        df = df.iloc[:num_registros]
else:
    print(f"Creando nuevo archivo: {archivo}")
    # Si no existe, crear un DataFrame vacío con otras columnas necesarias
    df = pd.DataFrame()
    # Añadir columnas que podrían ser necesarias para un dataset completo
    ciudades = ['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena', 'Bucaramanga', 'Pereira']
    estados = ['Cerrada', 'Pendiente', 'Cancelada']
    estados_pesos = [0.6, 0.3, 0.1]
    
    df['Ciudad'] = [random.choice(ciudades) for _ in range(num_registros)]
    df['Estado'] = np.random.choice(estados, size=num_registros, p=estados_pesos)
    df['Cliente'] = [f'Cliente_{i}' for i in range(1, num_registros + 1)]

# Actualizar las columnas solicitadas
df['Precio'] = np.random.uniform(10, 1000, num_registros).round(2)
df['Cantidad'] = np.random.randint(1, 20, num_registros)
df['Categoria'] = [random.choice(categorias) for _ in range(num_registros)]
df['Valor_Venta'] = (df['Precio'] * df['Cantidad']).round(2)
df['Comision'] = (df['Valor_Venta'] * np.random.uniform(0.01, 0.15, num_registros)).round(2)

# Guardar cambios
df.to_csv(archivo, index=False)

print(f"Archivo '{archivo}' actualizado con éxito. Contiene {len(df)} registros.")
print("\nPrimeras 5 filas del archivo:")
print(df.head())
