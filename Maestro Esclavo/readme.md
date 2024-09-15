# Proyecto Maestro-Esclavo para Cálculo de Cuadrados

Este proyecto utiliza la biblioteca `multiprocessing` de Python para calcular el cuadrado de una lista de números en paralelo. El script principal crea varios procesos "esclavos" que realizan el cálculo y envían los resultados de vuelta al proceso "maestro", que luego muestra los resultados.

## Descripción

El script principal (`main`) solicita al usuario una lista de números enteros separados por comas. Luego, crea un proceso separado para calcular el cuadrado de cada número usando la función `worker`. Los resultados se almacenan en una cola (`multiprocessing.Queue`), que el proceso maestro utiliza para recoger y mostrar los resultados.

## Requisitos

- Python 3.x

## Cómo Ejecutar el Proyecto

1. **Clona el repositorio o copia el script a tu máquina local.**
   
   ```bash
   git clone <URL del repositorio>


## Funcionamiento Interno
**Función worker(num, queue)**:

Recibe un número num y una cola queue.
Calcula el cuadrado del número.
Envía una tupla (num, result) a la cola.
**Función main()**:

Solicita al usuario una lista de números.
Crea un proceso separado para cada número en la lista.
Espera a que todos los procesos terminen.
Recoge los resultados de la cola.
Muestra los resultados al usuario.


**Ejemplo de Salida**
Ingrese una lista de números separados por comas: 2,4,6
Resultados:
El cuadrado de 2 es 4
El cuadrado de 4 es 16
El cuadrado de 6 es 36

## Notas
Asegúrate de tener Python 3.x instalado en tu máquina.
La biblioteca multiprocessing está incluida en la biblioteca estándar de Python, por lo que no es necesario instalar paquetes adicionales.

