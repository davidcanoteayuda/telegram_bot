
# Bot de Telegram en Python - David Cano Te Ayuda

Este repositorio contiene un bot de Telegram creado en Python, diseñado para realizar tareas útiles y divertidas. Con comandos para obtener clima, convertir divisas, recordatorios, imágenes aleatorias de gatos y perros, e imágenes de Unsplash según categoría, este bot es ideal para quienes desean aprender a automatizar tareas en Telegram.

## Características
- Muestra la hora y fecha actual.
- Envía imágenes aleatorias de gatos y perros.
- Proporciona información del clima de cualquier ciudad.
- Configura recordatorios personalizados.
- Convierte divisas.
- Obtiene imágenes de categorías específicas desde Unsplash.

## Requisitos
- Python 3.7 o superior.
- Cuenta en Telegram y creación de un bot a través de [BotFather](https://core.telegram.org/bots#botfather).
- API key de OpenWeather para el comando `/weather`.
- API key de ExchangeRate API para el comando `/convertir`.
- API key de Unsplash para el comando `/image`.

## Instalación

1. Clona este repositorio en tu máquina local.
   ```bash
   git clone https://github.com/tu-usuario/telegram-bot.git
   cd telegram-bot
   ```

2. Crea un entorno virtual.
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

3. Instala las dependencias.
   ```bash
   pip install python-telegram-bot requests
   ```

4. Configura el bot:
   - Reemplaza `TOKEN` en el código con el token de tu bot de Telegram.
   - Reemplaza `TU_API_KEY_DE_OPENWEATHER`, `TU_API_KEY_DE_EXCHANGERATE_API`, y `TU_API_KEY_DE_UNSPLASH` con tus respectivas API keys.

## Uso

1. Ejecuta el bot.
   ```bash
   python nombre_del_archivo.py
   ```

2. Comandos disponibles en el bot:
   - `/start` - Inicia el bot y muestra un mensaje de bienvenida.
   - `/help` - Muestra los comandos disponibles.
   - `/time` - Muestra la hora actual.
   - `/date` - Muestra la fecha actual.
   - `/weather <ciudad>` - Muestra el clima de la ciudad indicada.
   - `/recordatorio <segundos> <mensaje>` - Configura un recordatorio.
   - `/addtask <tarea>` - Añade una tarea a la lista.
   - `/showtasks` - Muestra la lista de tareas pendientes.
   - `/cat` - Envía una imagen aleatoria de un gato.
   - `/dog` - Envía una imagen aleatoria de un perro.
   - `/image <categoría>` - Envía una imagen de Unsplash basada en la categoría.

## Contribuciones
Las contribuciones son bienvenidas. Por favor, crea un fork del repositorio, haz tus cambios y envía un pull request.

## Licencia
Este proyecto está bajo la Licencia MIT.
