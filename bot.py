# Importamos las librerías necesarias para el bot
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from datetime import datetime
import requests
import time

# Token del bot. Asegúrate de reemplazarlo por el tuyo.
TOKEN = 'AQUI TU TOKEN DE BOTFATHER'

# === FUNCIONES PARA LOS COMANDOS DEL BOT ===

# Función para el comando /start
# Esta función se ejecuta cuando un usuario escribe /start
async def start(update: Update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="¡Hola! Soy tu bot de Telegram David Cano Te Ayuda ¿Que tal estas hoy?")

# Función para el comando /help
# Esta función se ejecuta cuando un usuario escribe /help
async def help_command(update: Update, context):
    help_text = (
        "Lista de comandos disponibles:\n"
        "/start - Inicia el bot\n"
        "/help - Muestra esta ayuda\n"
        "/time - Muestra la hora actual\n"
        "/date - Muestra la fecha actual\n"
        "/weather <ciudad> - Muestra el clima de la ciudad proporcionada\n"
        "/recordatorio <segundos> <mensaje> - Establece un recordatorio en X segundos\n"
        "/addtask <tarea> - Añade una tarea a la lista\n"
        "/showtasks - Muestra las tareas pendientes\n"
        "/cat - Envía una imagen aleatoria de un gato\n"
        "/dog - Envía una imagen aleatoria de un perro\n"
        "/image <categoría> - Envía una imagen aleatoria de la categoría proporcionada\n"
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)

# Función para el comando /time que devuelve la hora actual
async def time_command(update: Update, context):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"La hora actual es {current_time}")

# Función para el comando /date que devuelve la fecha actual
async def date_command(update: Update, context):
    today = datetime.now().strftime("%d-%m-%Y")  # Formato de la fecha: Año-Mes-Día
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"La fecha de hoy es {today}")

# Función para el comando /recordatorio
# Este comando acepta dos argumentos: un tiempo en segundos y un mensaje
async def recordatorio(update: Update, context):
    try:
        delay = int(context.args[0])  # Tiempo en segundos
        message = ' '.join(context.args[1:])  # Mensaje del recordatorio
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Recordatorio programado en {delay} segundos.")
        time.sleep(delay)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    except (IndexError, ValueError):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Uso: /recordatorio <segundos> <mensaje>")

# Función para añadir respuestas automáticas a palabras clave
async def echo(update: Update, context):
    text = update.message.text.lower()  # Convertimos el texto a minúsculas para una mejor comparación
    if "hola" in text:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="¡Hola! ¿Cómo estás?")
    elif "gracias" in text:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="¡De nada!")
    # Puedes seguir añadiendo más respuestas a palabras clave aquí

# === OTRAS FUNCIONALIDADES QUE PUEDES AGREGAR ===

# Función para añadir tareas a una lista (comando /addtask)
tasks = []  # Lista vacía para las tareas

async def add_task(update: Update, context):
    task = ' '.join(context.args)  # Unimos los argumentos en una sola cadena
    tasks.append(task)  # Añadimos la tarea a la lista
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Tarea '{task}' añadida a la lista.")

# Función para mostrar la lista de tareas (comando /showtasks)
async def show_tasks(update: Update, context):
    if tasks:
        task_list = "\n".join(tasks)  # Unimos todas las tareas en una cadena separadas por saltos de línea
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Tareas pendientes:\n{task_list}")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="No tienes tareas pendientes.")

# === FUNCIONALIDADES NUEVAS ===

# Función para obtener el clima de una ciudad (comando /weather)
async def weather(update: Update, context):
    if len(context.args) == 0:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Por favor, proporciona el nombre de una ciudad.")
        return

    city = ' '.join(context.args)  # Ciudad proporcionada por el usuario
    api_key = 'TU_API_KEY_DE_OPENWEATHER'  # Reemplaza con tu clave de API de OpenWeather
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        message = f"El clima en {city} es {weather_description} con una temperatura de {temperature}°C."
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Ciudad no encontrada.")

# Función para convertir divisas (comando /convertir)
async def convert_currency(update: Update, context):
    try:
        amount = float(context.args[0])  # Cantidad a convertir
        from_currency = context.args[1].upper()  # Moneda de origen
        to_currency = context.args[2].upper()  # Moneda de destino
    except (IndexError, ValueError):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Uso: /convertir <cantidad> <moneda_origen> <moneda_destino>")
        return

    api_key = 'TU_API_KEY_DE_EXCHANGERATE_API'  # Reemplaza con tu clave de API de ExchangeRate API
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        exchange_rate = data['conversion_rates'][to_currency]
        converted_amount = amount * exchange_rate
        message = f"{amount} {from_currency} son {converted_amount:.2f} {to_currency}."
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Conversión fallida. Revisa las monedas proporcionadas.")

# Función para enviar una imagen aleatoria de un gato (comando /cat)
async def random_cat(update: Update, context):
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)
    data = response.json()
    cat_image_url = data[0]['url']
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=cat_image_url)

# Función para enviar una imagen aleatoria de un perro (comando /dog)
async def random_dog(update: Update, context):
    url = 'https://api.thedogapi.com/v1/images/search'
    response = requests.get(url)
    data = response.json()
    dog_image_url = data[0]['url']
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=dog_image_url)

# Función para buscar imágenes en Unsplash según una palabra clave (comando /image)
async def unsplash_image(update: Update, context):
    if len(context.args) == 0:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Por favor, proporciona una categoría o palabra clave.")
        return

    query = ' '.join(context.args)  # Categoría proporcionada por el usuario
    api_key = 'TU_API_KEY_DE_UNSPLASH'  # Reemplaza con tu clave de API de Unsplash
    url = f'https://api.unsplash.com/photos/random?query={query}&client_id={api_key}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        image_url = data['urls']['regular']
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="No se encontraron imágenes para esa categoría.")


# === CONFIGURACIÓN DEL BOT ===

def main():
    # Creamos la aplicación con el token de nuestro bot
    application = Application.builder().token(TOKEN).build()

    # Añadimos los comandos al bot
    application.add_handler(CommandHandler("start", start))  # Comando /start
    application.add_handler(CommandHandler("help", help_command))  # Comando /help
    application.add_handler(CommandHandler("time", time_command))  # Comando /time
    application.add_handler(CommandHandler("date", date_command))  # Comando /date
    application.add_handler(CommandHandler("recordatorio", recordatorio))  # Comando /recordatorio
    application.add_handler(CommandHandler("addtask", add_task))  # Comando /addtask
    application.add_handler(CommandHandler("showtasks", show_tasks))  # Comando /showtasks
    application.add_handler(CommandHandler("weather", weather))  # Comando /weather
    application.add_handler(CommandHandler("convertir", convert_currency))  # Comando /convertir
    application.add_handler(CommandHandler("cat", random_cat))  # Comando /cat
    application.add_handler(CommandHandler("dog", random_dog)) #comando /dog
    application.add_handler(CommandHandler("image", unsplash_image)) #imagen aleatoria


    # Añadimos un manejador de mensajes para respuestas automáticas (sin comando específico)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Iniciamos el bot
    print("El bot está activo...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

# Iniciamos el programa
if __name__ == '__main__':
    main()
