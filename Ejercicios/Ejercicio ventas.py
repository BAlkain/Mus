import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# a) Crea un DataFrame con las siguientes columnas: 'Fecha', 'Producto', 'Cantidad', 'Precio_Unitario'.
np.random.seed(42)
fecha_inicio = datetime(2023, 1, 1)
fecha_fin = datetime(2023, 12, 31)
rango_fechas = pd.date_range(start=fecha_inicio, end=fecha_fin, freq='D')
productos = ['Pintxo', 'Kaña', 'Kafe', 'Colacao', 'Cocacola']

# b) Genera datos aleatorios para 1000 ventas en el último año.
n_registros = 1000
fechas = np.random.choice(rango_fechas, n_registros)
productos_vendidos = np.random.choice(productos, n_registros)
cantidades = np.random.randint(1, 11, n_registros)
precios = np.random.uniform(50, 1000, n_registros).round(2)
df = pd.DataFrame({
    'Fecha': fechas,
    'Producto': productos_vendidos,
    'Cantidad': cantidades,
    'Precio_Unitario': precios
})
df = df.sort_values('Fecha').reset_index(drop=True)

# c) Calcula el total de ventas por producto y visualízalo en un gráfico de barras.
df['Total_Venta'] = df['Cantidad'] * df['Precio_Unitario']
ventas_por_producto = df.groupby('Producto')['Total_Venta'].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 6)) # Gráfico de barras
ventas_por_producto.plot(kind='bar')
plt.title('Total de Ventas por Producto')
plt.xlabel('Producto')
plt.ylabel('Total de Ventas (€)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print("Total de ventas por producto:")
print(ventas_por_producto)
print("\n")

# d) Identifica los 5 días con mayores ventas y muéstralos.
ventas_por_dia = df.groupby('Fecha')['Total_Venta'].sum().sort_values(ascending=False)
top_5_dias = ventas_por_dia.head(5)
print("Los 5 días con mayores ventas:")
for fecha, venta in top_5_dias.items():
    print(f"{fecha.strftime('%Y-%m-%d')}: {venta:.2f}€")

# e) Calcula y muestra la tendencia de ventas mensuales en un gráfico de líneas.
df['Mes'] = df['Fecha'].dt.to_period('M')
ventas_mensuales = df.groupby('Mes')['Total_Venta'].sum().reset_index()
ventas_mensuales['Mes'] = ventas_mensuales['Mes'].dt.to_timestamp()
plt.figure(figsize=(12, 6)) # Gráfico de líneas
plt.plot(ventas_mensuales['Mes'], ventas_mensuales['Total_Venta'], marker='o')
plt.title('Tendencia de Ventas Mensuales')
plt.xlabel('Mes')
plt.ylabel('Total de Ventas (€)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
print("\nVentas mensuales:")
print(ventas_mensuales)

#f) Encuentra todas las ventas de más de 50 €.
ventas50 = df[df['Total_Venta'] > 50].sort_values('Total_Venta', ascending=False)
print("\nVentas de más de 50 €:")
print(ventas50[['Fecha', 'Producto', 'Cantidad', 'Precio_Unitario', 'Total_Venta']])