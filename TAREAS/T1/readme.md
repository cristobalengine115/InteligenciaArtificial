# TAREA 1 INTELIGENCIA ARTIFICIAL 🤖👨🏻‍💻
## ALUMNOS:
##### _GARCÍA FIGUEROA MUNGUÍA ALBERTO_
##### _GARCÍA GUTIÉRREZ EDGAR CRISTÓBAL_
##### _MORENO PERALTA ÁNGEL EDUARDO_

## ¿Qué se realizó? 📐🔨
En esta tarea se realizó la codificación de las operaciones que se pueden realizar sobre los vectores y los polinomios.
Las operaciones que se codificaron son:
* Vectores
    * Suma
    * Resta
    * Producto por un escalar
    * Norma
    * Ángulo entre dos vectores
* Polinomios
    * Valor del polinomio en un punto dado
    * Suma
    * Resta
    * Multiplicación
    * Derivada
    * Integral

## Ejecución 🖥🖱

Se requiere el uso de python 3.0.0 +
Se debe abrir una terminal en la ubicación de este readme y teclear:
```sh
python3 tarea2.py
```
Se requiere la existencia de un archivo con extensión csv
## Estructura del csv 🏛
Para ingresar valores, se requiere leer un archivo con extension csv, dicho archivo deberá estar guardado en la carpeta T1.
El archivo debe estar estructurado como se muestra a continuación para leer los vectores y polinomios

| Línea del Archivo | Función |
| ------ | ------ |
| 1 | 4,2     -> VECTOR 1 DE TAMAÑO N (En este caso el vector es [4,2]) |
| 2 | 1,4     -> VECTOR 2 DE TAMAÑO N (En este caso el vector es [1,4]) |
| 3 | 4       -> ESCALAR QUE MULIPLICARA A LOS VECTORES (4*[4,2]  4*[1,4]) |
| 4 | 4,3,2,1 -> POLINOMIO GRADO N (En este ejemplo, el polinomio es  4x^3 + 3x^2 + 2x^1 + 1x^0 )|
| 5 | 3,2,1   -> POLINOMIO GRADO M (0x^3 + 3x^2 + 2x^1 + 1x^0 ) |
| 6 | 2       -> PUNTO A EVALUAR EN LOS POLINOMIOS |

