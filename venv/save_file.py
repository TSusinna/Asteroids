# Importar las bibliotecas necesarias
import os

#
HIGH_SCORE_FILE = "high_score.txt"

# Verifica si el archivo high_score.txt existe
# Si existe, lo abre y lee su contenido
# Si el contenido es un número, lo convierte a entero y lo devuelve
# Si no, devuelve 0
# Si el archivo no existe, devuelve 0
# Si el archivo no existe, lo crea y devuelve 0
def load_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as file:
            content = file.read().strip()
            return int(content) if content.isdigit() else 0
    return 0 

# Abre el archivo high_score.txt en modo escritura
# Convierte el high_score a string y lo escribe en el archivo
# Cierra el archivo automáticamente al salir del bloque with
def save_high_score(high_score):
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(high_score))
