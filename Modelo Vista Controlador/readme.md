# Flask Users List Application

Este proyecto es una aplicación básica en Flask que muestra una lista de usuarios utilizando un blueprint para las rutas y DataTables para mejorar la visualización de la tabla.

## Estructura del Proyecto

your_project/ ├── app/ │ ├── init.py │ ├── controllers/ │ │ └── user_controller.py │ ├── models/ │ │ └── user_model.py ├── templates/ │ └── user_view.html └── run.py


### Archivos Principales

- **`__init__.py`**: Configura y crea la aplicación Flask, registrando los blueprints.
- **`user_controller.py`**: Define las rutas y la lógica de la vista para mostrar la lista de usuarios.
- **`user_model.py`**: Contiene la función `get_users()` que devuelve una lista estática de usuarios para propósitos de prueba.
- **`user_view.html`**: Plantilla HTML que muestra la lista de usuarios en una tabla interactiva utilizando DataTables.
- **`run.py`**: Script para ejecutar la aplicación Flask.

## Instalación

1. **Clona el repositorio**:
    ```bash
    git clone https://github.com/Fuenmayore/Glosario-Actividad.git
    ```

2. **Crea un entorno virtual**:
    ```bash
    python -m venv venv
    ```

3. **Activa el entorno virtual**:
    - En Windows:
        ```bash
        venv\Scripts\activate
        ```
    - En macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Instala las dependencias**:
    ```bash
    pip install Flask
    ```

## Ejecución

Para iniciar la aplicación, ejecuta el siguiente comando en la raíz del proyecto:

```bash
python run.py
```

La aplicación estará disponible en http://127.0.0.1:5000/users.

## Uso
**Lista de Usuarios:** Accede a la ruta /users para ver la lista de usuarios en una tabla. La tabla utiliza DataTables para funcionalidades como búsqueda y ordenamiento.
Contribución
Si deseas contribuir al proyecto, por favor sigue estos pasos:

