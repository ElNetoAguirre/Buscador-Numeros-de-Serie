"""
Buscador de Números de Serie
"""
import re
import os
import time
import datetime
from pathlib import Path
import math

inicio = time.time()

ruta = "C:\\EAAE\\Udemy\\Python Total - Progamador Avanzado en 16 días\\Proyecto 09 - Buscador de Números de Serie\\Directorio"
mi_patron = r"N\D{3}-\d{5}"
hoy = datetime.date.today()
numeros_encontrados = []
archivos_encontrados = []


def buscar_numero(archivo, patron):
    """Función para buscar el número de serie"""
    leer_archivo = open(archivo, "r", encoding="utf-8")
    texto = leer_archivo.read()
    leer_archivo.close()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ""


def crear_listas():
    """Función para crear el listado"""
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta, a), mi_patron)
            if resultado != "":
                numeros_encontrados.append(resultado.group())
                archivos_encontrados.append(a.title())


def mostrar_todo():
    """Función para mostrar los resultados y las listas"""
    indice = 0
    print("-" * 50)
    print(f"Fecha de Búsqueda: {hoy.day}/{hoy.month}/{hoy.year}")
    print("\n")
    print("ARCHIVO\t\t\tNúmero de Serie")
    print("-------\t\t\t---------------")
    for a in archivos_encontrados:
        print(f"{a}\t\t{numeros_encontrados[indice]}")
        indice += 1
    print("\n")
    print(f"Números encontrados: {len(numeros_encontrados)}")
    fin = time.time()
    duracion = fin - inicio
    print(f"Duración de la búsqueda: {math.ceil(duracion)} segundos")
    print("-" * 50)



crear_listas()
mostrar_todo()
