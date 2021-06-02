from vkbottle import Keyboard, Text
from db import session, Section, Product

SETTINGS = dict(one_time=False, inline=False)


class BeginButton:
    keyboard = Keyboard(**SETTINGS)
    keyboard.add(Text("Начать", payload={"cmd": "start"}))


class ShowSections:
    queryset = session.query(Section)
    keyboard = Keyboard(**SETTINGS)
    for i in range(len(queryset.all())):
        keyboard.add(Text(queryset.all()[i].title, {"section": queryset.all()[i].title}))
        if (i + 1) % 3 == 0:
            keyboard.row()


class ShowProducts:
    def __init__(self, section):
        self.section = section

    def create_keyboard(self):
        queryset = session.query(Product).filter_by(section=self.section)
        keyboard = Keyboard(**SETTINGS)
        for i in range(len(queryset.all())):
            keyboard.add(Text(queryset.all()[i].title, payload={"section": self.section}))
            if (i + 1) % 3 == 0:
                keyboard.row()
        keyboard.row()
        keyboard.add(Text("Назад", {"cmd": "back"}))
        return keyboard


class ShowProduct:
    def __init__(self, section):
        self.section = section

    def create_keyboard(self):
        keyboard = Keyboard(**SETTINGS)
        keyboard.add(Text("Назад", payload={"cmd": "back", "section": self.section}))
        keyboard.row()
        keyboard.add(Text("Выбрать категории", payload={"cmd": "back_to_sections"}))
        return keyboard
