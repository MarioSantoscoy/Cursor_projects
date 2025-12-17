#Programa que cuenta palabras en un archivo de texto
#1.- Pedir al Usuario la ruta de un archivo de texto.
#2.- Leer el archivo de texto.
#3.- Separar el texto en palabras.
#4.- Contar el numero total de palabras.
#5.- Mostrar las 10 palabras más frecuentes y su conteo.


archivo = input("Ingrese la ruta del archivo de texto: ")

try:
    with open(archivo, 'r') as file:
        texto = file.read()

except FileNotFoundError:
    print(f"El archivo {archivo} no existe.")
    exit(1)

#Separar el contenido en palabras

import re

palabras = re.findall(r'\w+', texto.lower())
total_palabras = len(palabras)
print(f"Total de palabras: {total_palabras}")

from collections import Counter

contador = Counter(palabras)
mas_comunes = contador.most_common(10)
print("\nLas 10 palabras más frecuentes:")
for palabra, freq in mas_comunes:
    print(f"{palabra}: {freq}")

    
