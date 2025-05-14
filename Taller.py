import pandas as pd

dfVentas = pd.read_csv('ventas_100k.csv')

# Cambiamos la columna 'Fecha' a tipo datetime ya que automaticamente se lee como string
dfVentas['Fecha'] = pd.to_datetime(dfVentas['Fecha'])


# 1. ¿Cuántos registros (ventas) hay en total?

# print(dfVentas.head()) //Linea para ver los primeros registros del DataFrame
print("\n-------------------------------1----------------------------\n")
conteoTotalVentas = dfVentas['Cliente'].count()
print(f"El total de Ventas es de: {conteoTotalVentas}")

#2. ¿Cuántas ventas fueron "Cerradas", "Pendientes" y "Canceladas"? (usar .value_counts()) 

print("\n-------------------------------2----------------------------\n")
conteoVentasPorEstado = dfVentas['Estado'].value_counts()
print("\nVentas por estado:")
print(conteoVentasPorEstado)
    
#3. ¿Cuál es el valor total de ventas realizadas? 

print("\n-------------------------------3----------------------------\n")
valorTotalVentas = dfVentas['Valor_Venta'].sum()
print(f"\nEl valor total de ventas realizadas es: ${valorTotalVentas:,.2f}")

#4. ¿Cuál es el promedio de comisión pagada por venta cerrada?

print("\n-------------------------------4----------------------------\n")

promedioComisionCerradas = dfVentas[dfVentas['Estado'] == 'Cerrado']['Comision'].mean()
print(f"\nEl promedio de comisión pagada por venta cerrada es: ${promedioComisionCerradas}")

#5. ¿Qué ciudad generó el mayor número de ventas cerradas?

print("\n-------------------------------5----------------------------\n")
ciudadMayorVentasCerradas = dfVentas[dfVentas['Estado'] == 'Cerrado']['Ciudad'].value_counts().idxmax()
print(f"\nLa ciudad que generó el mayor número de ventas cerradas es: {ciudadMayorVentasCerradas}") 	

# 6. ¿Cuál es el valor total de ventas por ciudad? (usar .groupby()) 

print("\n-------------------------------6----------------------------\n")
Venta_Ciudad = dfVentas.groupby('Ciudad')['Valor_Venta'].sum()
print(f"\nEl valor total de ventas por ciudad es: {Venta_Ciudad}$")



# 7. ¿Cuáles son los 5 productos más vendidos (por número de registros)? 

print("\n-------------------------------7----------------------------\n")
productosMasVendidos = dfVentas['Producto'].value_counts().head(5)
print(f"\n 7) Los 5 productos más vendidos son: \n {productosMasVendidos}" )


# 8. ¿Cuántos productos únicos fueron vendidos? 


print("\n-------------------------------8----------------------------\n")
productosUnicos = dfVentas.groupby("Producto")["Cantidad"].count()
print(f"\nEl número de productos únicos vendidos es: {productosUnicos}")


# 9. ¿Cuál es el vendedor con mayor número de ventas cerradas?

print("\n-------------------------------9----------------------------\n")
   
vendedorMvp = dfVentas[dfVentas['Estado'] == 'Cerrado']['Vendedor'].value_counts().idxmax()
print(f"\nEl vendedor con mayor número de ventas cerradas es: {vendedorMvp}")

# 10. ¿Cuál es la venta con el mayor valor y qué cliente la realizó?

print("\n-------------------------------10----------------------------\n")

ventaMayorValor = dfVentas.loc[dfVentas['Valor_Venta'].idxmax()]
print(f"\nLa venta con el mayor valor es: {ventaMayorValor['Valor_Venta']}, realizada por el cliente: {ventaMayorValor['Cliente']}")

# 11. ¿Existen ventas con valor o comisión nula o negativa? (usar filtros)

print("\n-------------------------------11----------------------------\n")

ventasNulas = dfVentas[(dfVentas['Valor_Venta'].isnull()) | 
                        (dfVentas['Comision'].isnull()) | 
                        (dfVentas['Valor_Venta'] <= 0) | 
                        (dfVentas['Comision'] <= 0)]

if ventasNulas.empty:
    print("\nNo existen ventas con valor o comisión nula o negativa.")
else:
    print("\nExisten ventas con valor o comisión nula o negativa:")
    print(ventasNulas)


# 12. ¿Cuál es la media de ventas por mes? (usar .dt.month)

print("\n-------------------------------12----------------------------\n")



MediaVentasPorMes = dfVentas['Fecha'].dt.month.value_counts().mean()
print(f"\nLa media de ventas por mes es: {MediaVentasPorMes}")


# 13. ¿Cuál fue el mes con más ventas cerradas?

print("\n-------------------------------13----------------------------\n")

mesVentasCerradas = dfVentas[dfVentas['Estado'] == 'Cerrado']['Fecha'].dt.month.value_counts().idxmax()
print(f"\nEl mes con más ventas cerradas es: {mesVentasCerradas}")


# 14. ¿Cuántas ventas se realizaron en cada trimestre del año?

print("\n-------------------------------14----------------------------\n")

ventasPorTrimestre = dfVentas['Fecha'].dt.to_period('Q').value_counts()
print(f"\nEl número de ventas realizadas en cada trimestre del año es: {ventasPorTrimestre}")


# 15. ¿Qué productos han sido vendidos en más de 3 ciudades diferentes?

print("\n-------------------------------15----------------------------\n")

# Agrupar productos por ciudades y contar ciudades únicas para cada producto
ciudades_por_producto = dfVentas.groupby('Producto')['Ciudad'].nunique()
# Filtrar productos vendidos en más de 3 ciudades
productos_mas_de_3_ciudades = ciudades_por_producto[ciudades_por_producto > 3]
print(f"\nProductos vendidos en más de 3 ciudades diferentes:")
print(productos_mas_de_3_ciudades)

# 16. ¿Existen duplicados en los datos? ¿Cómo los identificarías?

print("\n-------------------------------16----------------------------\n")

duplicados = dfVentas.duplicated(subset=['Cliente', 'Producto', 'Valor_Venta'], keep=False)
print(f"\nExisten duplicados en los datos: {duplicados.sum()}")

# 17. Eliminar las filas que tengan valores nulos en columnas clave (CLIENTE, PRODUCTO,
# VALOR_VENTA).

print("\n-------------------------------17----------------------------\n")

# Contar registros antes de eliminar nulos
registros_antes = len(dfVentas)
# Eliminar filas con valores nulos en columnas clave
dfVentasSinNulos = dfVentas.dropna(subset=['Cliente', 'Producto', 'Valor_Venta'])
# Contar registros después de eliminar nulos
registros_despues = len(dfVentasSinNulos)
print(f"\nRegistros originales: {registros_antes}")
print(f"Registros después de eliminar nulos: {registros_despues}")
print(f"Se eliminaron {registros_antes - registros_despues} registros con valores nulos en las columnas clave")

# 18. Crear una nueva columna llamada UTILIDAD que sea igual al 95% del VALOR_VENTA
# (simulando costo), y analizar cuál producto dejó mayor utilidad total

print("\n-------------------------------18----------------------------\n")

# Crear columna UTILIDAD (considerando que la utilidad es el 5% del valor de venta)
dfVentas['UTILIDAD'] = dfVentas['Valor_Venta'] * 0.05

# Analizar qué producto dejó mayor utilidad total
utilidad_por_producto = dfVentas.groupby('Producto')['UTILIDAD'].sum().sort_values(ascending=False)
producto_mayor_utilidad = utilidad_por_producto.index[0]
valor_mayor_utilidad = utilidad_por_producto.iloc[0]

print(f"\nProducto con mayor utilidad total: {producto_mayor_utilidad}")

###############Preguntas específicas para practicar groupby() con Pandas:##############

# • ✅ ¿Cuál es el valor total de ventas por ciudad?
print ("\n-------------------------------19----------------------------\n")
valor_total_ventas_por_ciudad = dfVentas.groupby('Ciudad')['Valor_Venta'].sum().sort_values(ascending=False)
print("\nEl valor total de ventas por ciudad es:")
print(valor_total_ventas_por_ciudad)

# • ✅ ¿Cuál es el promedio de comisión por vendedor?
print ("\n-------------------------------20----------------------------\n")
valor_promedio_comision_por_vendedor = dfVentas.groupby('Vendedor')['Comision'].mean().sort_values(ascending=False)
print("\nEl promedio de comisión por vendedor es:")
print(valor_promedio_comision_por_vendedor)

# • ✅ ¿Cuál es el número de ventas por estado y por ciudad?
print ("\n-------------------------------21----------------------------\n")
valor_ventas_estado_ciudad = dfVentas.groupby(['Estado', 'Ciudad']).size().unstack(fill_value=0)
print("\nEl número de ventas por estado y por ciudad es:")
print(valor_ventas_estado_ciudad)

# • ✅ ¿Qué categoría de producto tiene el mayor valor de ventas?
print ("\n-------------------------------22----------------------------\n")
valor_categoria_producto = dfVentas.groupby('Categoria')['Valor_Venta'].sum().sort_values(ascending=False)
categoria_mayor_ventas = valor_categoria_producto.index[0]
valor_mayor_categoria = valor_categoria_producto.iloc[0]
print(f"\nLa categoría de producto con mayor valor de ventas es: {categoria_mayor_ventas} con ${valor_mayor_categoria:,.2f}")
print("\nValor de ventas por categoría:")
print(valor_categoria_producto)

# • ✅ ¿Cuál es el total de ventas mensuales por ciudad? (requiere convertir fecha a datetime y agrupar)
print ("\n-------------------------------23----------------------------\n")
# Agregamos una columna de mes-año para mejor legibilidad
dfVentas['Mes_Año'] = dfVentas['Fecha'].dt.strftime('%Y-%m')
valor_ventas_mensuales_por_ciudad = dfVentas.groupby(['Mes_Año', 'Ciudad'])['Valor_Venta'].sum()
print("\nEl total de ventas mensuales por ciudad es:")
print(valor_ventas_mensuales_por_ciudad.head(20))  # Mostramos solo las primeras 20 filas para no saturar la salida

# • ✅ ¿Cuántas ventas cerradas hizo cada vendedor por ciudad?
print ("\n-------------------------------24----------------------------\n")
ventas_cerradas_por_vendedor_ciudad = dfVentas[dfVentas['Estado'] == 'Cerrado'].groupby(['Vendedor', 'Ciudad']).size().unstack(fill_value=0)
print("\nNúmero de ventas cerradas por vendedor y ciudad:")
print(ventas_cerradas_por_vendedor_ciudad)

print ("""
       ⣠⠴⠒⠒⠲⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡤⠶⠲⠦⣄⠀⠀⠀⣀⣀⣀⣀⣤⣤⣼⣃⣀⡴⠋⠛⢦⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣰⢋⡴⠖⠦⣄⣨⠷⠚⠉⠉⠀⠀⠀⠀⠀⠀⠈⠉⠲⢤⡀⢈⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣏⢸⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣼⠃⠀⠀⠀⠀⠀⠀⠀⢀⣀⡠⠤⠤⠤⠤⠄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢻⡜⢦⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⢀⠴⠋⢡⣦⣤⣀⠀⠀⠀⠀⠀⠀⠉⠑⠲⠤⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢹⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠀⠀⠀⠀⠀⢷⠀⠀⠀⣰⠃⠀⠀⣾⣿⠛⠻⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠢⣄⠀⠀⠀⠀
⠀⠀⠀⢸⡇⠀⠀⠀⠀⠐⠶⠆⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⢸⡄⠀⠀⡇⠀⠀⣸⣿⣷⣶⣶⠿⠃⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀
⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⣠⡀⣀⠤⠒⠋⠉⠙⠒⠾⣿⠇⠀⠀⠀⠀⠀⢧⠀⠀⢧⠀⢠⣿⡏⠀⠈⣿⡦⠀⣿⡇⢀⣼⣶⢄⣀⣀⡀⠀⠀⢠⣦⡌⢣⡀
⠀⠀⠀⢸⡇⠀⠀⠀⠀⠈⢿⠟⠁⠀⠰⢿⡿⠂⠀⠀⠈⢣⠀⠀⠀⠀⠀⠸⡇⠀⠈⢦⠘⠻⠿⣶⣾⡿⠃⠀⣿⣥⣾⠟⢡⣾⡟⠛⢿⣧⠀⣼⣿⠃⠀⢳
⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⡞⠀⠀⣄⣠⣼⢿⣦⣴⠆⠀⠈⡆⠀⠀⠀⠀⢠⡇⠀⠀⠀⠳⣄⠀⠀⠀⠀⠀⣠⣿⡿⠃⠀⣾⣿⠛⠻⢿⡿⢰⣿⠏⠀⠀⢸
⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⢷⠀⠀⠈⠉⠷⠴⠟⠀⠀⠀⣰⠃⠀⠀⠀⣠⡞⠀⠀⠀⠀⠀⠈⠑⢦⣀⠀⠼⠿⠋⠀⠀⠀⠈⠻⢷⣶⡆⢠⣬⡉⠀⠀⢀⡾
⠀⠀⠀⠀⠹⣄⠀⠀⠀⠀⠈⠣⣀⠀⠀⠀⠀⠀⠀⢀⡴⠃⠀⣀⡤⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢑⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠁⣀⡤⠞⠀
⠀⠀⠀⠀⠀⠈⠓⢦⣤⣄⣀⣀⣈⣓⣒⣤⣤⣶⡾⠿⢶⣾⣯⣭⣤⣤⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⡴⠋⠀⠀⣄⣠⡴⠞⠒⠢⠤⠀⠐⠒⠚⠋⠉⠀⠀⠀
⠀⠀⠀⠀⣀⣤⠶⠚⠉⠁⣸⠟⠉⠉⠙⢧⣀⠀⠀⠀⡸⢻⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠑⠒⠊⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣸⠋⠉⠉⠁⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⠀⠈⠑⠒⠚⠁⢸⡟⠶⢤⣄⡀⠀⠀⢠⣦⣤⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢹⡄⠀⠀⠀⠀⠀⠀⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠈⠙⢳⣄⠈⢻⣿⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠳⣤⣀⣀⣀⣤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠇⠀⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠹⣏⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⠿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⠀⠀⢀⣄⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠉⠻⣦⠀⠀⠀⣀⣤⠞⠛⠲⣤⣀⣤⠶⠶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠘⣟⠛⢿⡁⠀⠀⠀⠀⠀⠀⠀⠀⢿⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠈⢳⠀⠛⢦⣄⠀⠀⠀⠀⠀⣰⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣄⠀⠀⢀⣤⠀⣠⡾⠀⠀⠀⠙⠷⣄⣀⢀⣾⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀y⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀
       """)



