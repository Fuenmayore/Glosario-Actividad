# Proyecto de Servidor y Cliente en Python

Este proyecto implementa un servidor y un cliente utilizando sockets en Python. El servidor escucha mensajes entrantes y responde a cada mensaje recibido. El cliente se conecta al servidor, envía un mensaje y recibe una respuesta.

## Descripción

El proyecto consiste en dos partes:

- **Servidor**: Escucha en un puerto específico, acepta conexiones de clientes y maneja la comunicación con ellos en hilos separados.
- **Cliente**: Se conecta al servidor, envía un mensaje y recibe una respuesta del servidor.

## Características

- Comunicación basada en sockets.
- El servidor maneja múltiples clientes simultáneamente utilizando hilos.
- El cliente envía un mensaje y recibe una confirmación del servidor.

## Instalación

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/Fuenmayore/Glosario-Actividad.git


Uso
**Para iniciar el servidor:**

python peer.py
Luego, selecciona la opción 'servidor' cuando se te pida.

**Para iniciar el cliente:**


python peer.py
Luego, selecciona la opción 'cliente' y proporciona el mensaje que deseas enviar al servidor.

## Ejemplo
**Servidor:**


$ python peer.py
Elige 'servidor' para iniciar como servidor o 'cliente' para iniciar como cliente: servidor
Servidor escuchando en **localhost:5000**
Conexión establecida con **('127.0.0.1', 12345)**
Mensaje recibido: Hola
Cliente:


$ python peer.py
Elige 'servidor' para iniciar como servidor o 'cliente' para iniciar como cliente: cliente
Ingresa el mensaje para enviar al servidor: Hola
Respuesta del servidor: Mensaje recibido
Dependencias
Python 3.x
No se requieren bibliotecas adicionales fuera de las que vienen con Python por defecto.

