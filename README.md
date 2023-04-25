<p align="center">
  <a href="https://www.python.org/" target="blank"><img src="https://www.pngmart.com/files/7/Python-PNG-Image.png" width="200" alt="Python Logo" /></a>
</p>

# Buscador de Números de Serie

Es un proyecto de consola, el cual te permite buscar números de serie que cumplan un determinado formato, dentro de un arbol de carpetas. Busca en todos los archivos y subcarpetas de un directorio determinado, y va a buscar cualquier string que coincida con un patrón de número de serie, sabiendo que no puede haber más de un número de serie por archivo.

Para lograrlo vas a usar el módulo os para abrir e iterear por el directorio, y las expresiones regulares para encontrar el formato de número de serie correcto.

En éste caso, la condición del formato que deben cumplir dichos números de serie es:

"[N] + [tres carateres de texto] + [-] + [5 números]"

Por ejemplo: Nryu-12365

La información resultante de la búsqueda que se presentará en pantalla es forma de listado en formato de tabla, el cúal respeta el siguiente formato de ejemplo:

----------------------------------------------------
Fecha de Búsqueda: [fecha actual]

| ARCHIVO | Número de Serie |
| ------- | --------------- |
| texto1.txt | Nter-15496 |
| texto25.txt | Ngba-85235 |

Números encontrados: 2
Duración de la búsqueda: 1 segundos
----------------------------------------------------

IMPORTANTE

* La "Duración de búsqueda" está redondeada hacia arriba.
