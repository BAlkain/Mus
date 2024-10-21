import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# a) Crea un DataFrame con las siguientes columnas: 'Fecha', 'Producto', 'Cantidad', 'Precio_Unitario'.
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
date_range = pd.date_range(start=start_date, end=end_date, freq='D')
products = ['Pintxo', 'Kaña', 'Kafe', 'Colacao', 'Cocacola']
n_records = 1000

# b) Genera datos aleatorios para 1000 ventas en el último año.
dates = np.random.choice(date_range, n_records)
products_sold = np.random.choice(products, n_records)
quantities = np.random.randint(1, 11, n_records)
prices = np.random.uniform(50, 1000, n_records).round(2)
df = pd.DataFrame({ #Generar Dataframe
    'Fecha': dates,
    'Producto': products_sold,
    'Cantidad': quantities,
    'Precio_Unitario': prices
})
df = df.sort_values('Fecha').reset_index(drop=True)

# c) Calcula el total de ventas por producto y visualízalo en un gráfico de barras.
df['Total_Venta'] = df['Cantidad'] * df['Precio_Unitario'] # Total ventas por producto
ventas_por_producto = df.groupby('Producto')['Total_Venta'].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 6)) # Gráfico de barras
ventas_por_producto.plot(kind='bar')
plt.title('Total de Ventas por Producto')
plt.xlabel('Producto')
plt.ylabel('Total de Ventas ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print(ventas_por_producto)

# d) Identifica los 5 días con mayores ventas y muéstralos.
ventas_por_dia = df.groupby('Fecha')['Total_Venta'].sum().sort_values(ascending=False)
top_5_dias = ventas_por_dia.head(5)
print("Los 5 días con mayores ventas:")
for fecha, venta in top_5_dias.items():
    print(f"{fecha.strftime('%Y-%m-%d')}: ${venta:.2f}")

#e) Visualización de la tendencia de ventas mensuales (gráfico de líneas)
df['Mes'] = df['Fecha'].dt.to_period('M')
ventas_mensuales = df.groupby('Mes')['Total_Venta'].sum().reset_index()
ventas_mensuales['Mes'] = ventas_mensuales['Mes'].dt.to_timestamp()

plt.figure(figsize=(12, 6)) # Gráfico de líneas
plt.plot(ventas_mensuales['Mes'], ventas_mensuales['Total_Venta'], marker='o')
plt.title('Tendencia de Ventas Mensuales')
plt.xlabel('Mes')
plt.ylabel('Total de Ventas ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# f) Encuentra todas las ventas de más de 50 €.
ventas_altas = df[df['Total_Venta'] > 50].sort_values('Total_Venta', ascending=False)
print("\nVentas de más de 50 €:")
print(ventas_altas[['Fecha', 'Producto', 'Cantidad', 'Precio_Unitario', 'Total_Venta']])

