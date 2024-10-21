import numpy as np

#1. Crear un vector con valores dentro del rango 1 a 10.
a=(np.linspace(0,10,11))
#a=np.random.random(10)
print("Array: ",a)

#2. Sobre el vector anterior dar el valor “8” al quinto elemento.
a[5]=8
print("Array 8: ",a)

#3. Invertir el vector anterior.
a_invertido=a[::-1]
print ("Array invertido: ",a_invertido)

#4. Encontrar el valor medio (con dos decimales) y los índices del valor máximo y mínimo del vector anterior.
valor_medio=np.mean(a_invertido)
valor_medio=np.round(valor_medio,2)
print("Valor medio:", valor_medio)
indice_max = np.argmax(a_invertido)
print("Índice del valor máximo: ",indice_max)
indice_min = np.argmin(a_invertido)
print("Índice del valor mínimo: ",indice_min)

#5. Crear dos vectores (v1, v2) y encontrar los valores comunes.
v1=np.random.random(10)
v1=np.round(v1,1)
print("v1: ",v1)
v2=np.random.random(10)
v2=np.round(v2,1)
print("v2: ",v2)
valores_comunes = np.intersect1d(v1,v2)
print("Valores comunes: ",valores_comunes)

#6. Crear una matriz 3x3 con valores de 0 a 8.
matriz = [[0,1,2],[3,4,5],[6,7,8]]
print("Matriz: ",matriz)

#7. Encontrar los índices que no son ceros del arreglo [1,5,4,7,0,5,0,9,0,1,2].
arreglo = np.array([1,5,4,7,0,5,0,9,0,1,2])
print("Arreglo: ",arreglo)
indices = np.nonzero(arreglo)[0]
print("Índices que no son ceros: ",indices)

#8. Crear una matriz identidad de 4x4 y multiplicarla por 3.
matriz_identidad = np.eye(4)
print("Matriz_identidad: ",matriz_identidad)
matriz_identidad3 = matriz_identidad*3
print("Matriz_identidad x3: ",matriz_identidad3)

#9. Crea un arreglo de 10 elementos y selecciona los elementos en las posiciones pares
arreglo10 = np.arange(10)
print("Arreglo de 10 elementos: ",arreglo10)
elementos_pares = arreglo10[::2]
print("Elementos en posiciones pares: ",elementos_pares)

#10. Crear un arreglo float de 32 bits y convertirlo a un integer de 32 bits.
arreglo_float = np.array([1.5, 2.7, 3.1, 4.9, 5.0], dtype=np.float32)
print ("Arreglo float32: ",arreglo_float)
arreglo_int = arreglo_float.astype(np.int32)
print("Arreglo int32: ",arreglo_int)
