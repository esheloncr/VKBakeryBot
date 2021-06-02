import os
from vkbottle.bot import Bot, Message
from keyboard import BeginButton, ShowSections, ShowProducts, ShowProduct
from states import States
from db import session, Section, Product

TOKEN = os.environ.get("TOKEN")

bot = Bot(TOKEN)

START_WORDS = [
    "Привет",
    "Начать",
    "начать",
    "привет"
]

# Запрос всех категорий и товаров в БД
section_names = [s.title for s in session.query(Section).all()]
product_names = [p.title for p in session.query(Product).all()]


# После сообщения из массива START_WORDS или нажатия кнопки "Начать", приходит список категорий.
@bot.on.message(state=None, text=START_WORDS)
async def start(message: Message):
    await message.answer("Добро пожаловать!")
    await message.answer("Предлагаемые к выбору категории: ", keyboard=ShowSections().keyboard.get_json())
    await bot.state_dispenser.set(message.peer_id, States.SECTIONS)


# Список продуктов по выбранной категории
@bot.on.message(state=States.SECTIONS, text=section_names)
async def show_products(message: Message):
    await message.answer("Выбранная категория: " + message.text)
    await message.answer("Доступные продукты: ", keyboard=ShowProducts(message.text).create_keyboard().get_json())
    await bot.state_dispenser.set(message.peer_id, States.PRODUCTS)


# Название, описание продукта, фотография
@bot.on.message(state=States.PRODUCTS, text=product_names)
async def show_product(message: Message):
    await message.answer("Продукт", keyboard=ShowProduct(eval(message.payload).get("section")).create_keyboard().get_json())
    await bot.state_dispenser.set(message.peer_id, States.PRODUCT)


# Возврат к списку разделов
@bot.on.message(state=States.PRODUCTS, payload={"cmd": "back"})
async def back(message: Message):
    await message.answer("Категории: ", keyboard=ShowSections().keyboard.get_json())
    await bot.state_dispenser.set(message.peer_id, States.SECTIONS)


# Возврат к разделам со страницы продуктов
@bot.on.message(state=States.PRODUCT, payload={"cmd": "back_to_sections"})
async def back_to_sections(message: Message):
    await message.answer("Категории", keyboard=ShowSections().keyboard.get_json())
    await bot.state_dispenser.set(message.peer_id, States.SECTIONS)


# Возврат к последней выбранной категории
@bot.on.message(state=States.PRODUCT)
async def back_from_product(message: Message):
    await message.answer("Выбранная категория: " + eval(message.payload).get("section"))
    await message.answer("Доступные продукты: ", keyboard=ShowProducts(eval(message.payload).get("section")).create_keyboard().get_json())
    await bot.state_dispenser.set(message.peer_id, States.PRODUCTS)


# Хендлер любых сообщений с кнопкой "начать"
@bot.on.message(state=None)
async def unknown_message(message: Message):
    await message.answer("Неизвестное сообщение", keyboard=BeginButton().keyboard.get_json())


# Хендлер любых сообщений, на которые не созданы обработчики.
@bot.on.message()
async def unknown_message(message: Message):
    await message.answer("Неизвестное сообщение")


bot.run_forever()
