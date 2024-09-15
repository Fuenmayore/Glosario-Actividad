# Proyecto por Capas

Este es un proyecto que sigue la arquitectura por capas, separando la lógica de la aplicación en diferentes componentes: **Modelo**, **Vista** y **Controlador**. La aplicación permite consultar el nombre de un usuario dado su ID.

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

# Flask Users List Application

Este proyecto es una aplicación básica en Flask que muestra una lista de usuarios utilizando un blueprint para las rutas y DataTables para mejorar la visualización de la tabla.

## Estructura del Proyecto



### Componentes

1. **Modelo (`model/user.py`)**
   - Define las clases y la lógica de acceso a datos. En este caso, se incluye la clase `UserRepository`, que es responsable de gestionar la información de los usuarios.

2. **Controlador (`controller/user_controller.py`)**
   - Gestiona la lógica de la aplicación y coordina la interacción entre el modelo y la vista. En este caso, se incluye la clase `UserController`, que utiliza un repositorio para obtener el nombre de un usuario a partir de su ID.

3. **Vista (`view/user_view.py`)**
   - Maneja la interacción con el usuario. En este caso, se encarga de solicitar al usuario el ID del usuario y de mostrar el nombre obtenido.

4. **Punto de Entrada (`main.py`)**
   - Ejecuta la función `main()` desde la vista, iniciando la aplicación.

## Cómo Ejecutar el Proyecto

Para ejecutar el proyecto, sigue estos pasos:

1. Asegúrate de tener Python instalado en tu sistema.
2. Navega al directorio raíz del proyecto en la terminal.
3. Ejecuta el archivo `main.py` con el siguiente comando:


   python main.py




## Requisitos
1. Python 3.x



Este README proporciona una visión general clara del proyecto, la estructura de archivos y cómo ejecutarlo. Si necesitas más detalles específicos o ajustes, no dudes en decírmelo.
