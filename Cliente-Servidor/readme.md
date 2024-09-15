# Pokémon Information App
Esta es una aplicación web simple construida con Flask que permite a los usuarios buscar información sobre cualquier Pokémon utilizando la PokéAPI. El usuario ingresa el nombre del Pokémon, y la aplicación devuelve detalles como su tipo, altura, peso, y una imagen.

## Características
Buscar Pokémon: El usuario puede ingresar el nombre de un Pokémon y ver detalles relacionados.
Detalles de Pokémon: La aplicación muestra la imagen del Pokémon, su tipo, altura, y peso.
Interfaz amigable: Usa Bootstrap para una apariencia simple y limpia.
API integrada: Consume datos de la PokéAPI.
Instalación
Clona el repositorio:


git clone https://github.com/Fuenmayore/Glosario-Actividad.git
cd pokemon-app
Crea un entorno virtual (opcional pero recomendado):


python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
Instala las dependencias:


pip install -r requirements.txt
## Estructura del proyecto:

La estructura básica del proyecto se verá algo así:


pokemon-app/
|
├── vistas/
│   ├── index.html
│   ├── pokemon.html
|
├── server.py
└── README.md
Uso
## Ejecuta la aplicación:


python server.py
Accede a la aplicación en tu navegador:

Ve a **http://127.0.0.1:5000/** en tu navegador para ver la página de inicio, donde puedes buscar un Pokémon.

API utilizada
Esta aplicación utiliza la PokéAPI para obtener la información de los Pokémon.

Ejemplo
Ingresas el nombre del Pokémon (por ejemplo, "Pikachu").
La aplicación mostrará los detalles de Pikachu:
Nombre: Pikachu
Tipo: Eléctrico
Altura: 4 decímetros
Peso: 60 hectogramos
Imagen del Pokémon.
Manejo de errores
Si el nombre del Pokémon no es encontrado o hay un error con la API, la aplicación mostrará un mensaje indicando que el Pokémon no fue encontrado.

## Dependencias
Flask: Un microframework de Python para construir aplicaciones web.
Requests: Para realizar solicitudes HTTP a la PokéAPI.
Bootstrap: Utilizado para mejorar la presentación de la página.
Contribuir


