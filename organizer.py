import os
from pathlib import Path

# Esta variable define la ruta del directorio donde se encuentran los archivos que van a ser organizados.
point_dir = Path("C:/Users/Isabel/Desktop/DOWNLOADS")

# Aquí se define un diccionario llamado 'categories' que se utiliza para clasificar extensiones de archivos en diferentes categorías.
# Las claves del diccionario son los nombres de las categorías como "Images", "Docs", "Videos" y "Audio".
# Los valores asociados a cada clave son listas de extensiones de archivos (por ejemplo, ".jpg" para imágenes, ".pdf" para documentos, etc.).
# Por ejemplo, si un archivo tiene la extensión ".mp4", se considerará dentro de la categoría "Videos".

categories = {
    "Images": [".png", ".jpg", ".jepg", ".gif"],
    "Docs": [".docx", ".pdf", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav"]
}

# Además, se define una lista llamada 'various_cat' con el valor "Others".
# Esta lista se suele usar para agrupar archivos que no encajan en ninguna de las categorías anteriores.

various_cat = ["Others"]


# Creamos un diccionario vacío llamado 'ext_to_cat' que servirá para mapear cada extensión de archivo (en minúsculas)
# a su categoría correspondiente (por ejemplo, ".jpg" a "Images").
# Recorremos cada elemento del diccionario 'categories'. Para cada categoría y su lista de extensiones asociadas,
# añadimos una entrada en 'ext_to_cat' donde la clave es la extensión (en minúsculas) y el valor es la categoría.

ext_to_cat = {}
for category, exts in categories.items():
    for ext in exts:
        ext_to_cat[ext.lower()] = category



# Este bloque de código organiza los archivos del directorio "point_folder" en subcarpetas según su extensión.
# Para cada archivo en "point_folder", determina la categoría correspondiente usando el diccionario 'ext_to_cat';
# si la extensión no está en el diccionario, se clasifica como "Others".
# Luego, mueve el archivo a la subcarpeta de la categoría dentro de "point_folder", creando la carpeta si no existe.
# Finalmente, imprime un mensaje indicando que el archivo ha sido movido.

files = [f for f in point_dir.iterdir() if f.is_file()]

for file in files:
        
    if file.name == "organizer.py":
        continue
    ext = file.suffix.lower()
    category = ext_to_cat.get(ext, "Others")
    destinated_dir = point_dir / category
    destinated_dir.mkdir(exist_ok=True)
    file.rename(destinated_dir / file.name)
    print(f'Moved {file.name} to {category}/')


