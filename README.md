# VKBakeryBot
База данных - PostgreSQL
Для запуска:
1. Рекомендую создать файл config, в нём записать переменные окружения:
TOKEN - Токен группы ВК
DB_URL - путь к серверу БД, пример: postgresql://username:password@localhost:5432/flask_db
DB_ASYNC_URL - тот-же путь, только необходимо указать асинхронный драйвер: postgresql+asyncpg://username:password@localhost:5432/flask_db
2. В файле alembic.ini на 42 строке указать тот же путь, что и в DB_URL
3. В проекте находится дамп БД db.sql, в котором уже содержатся данные(категории, продукты).
4. Если создаётся новая база данных, то необходимо выполнить миграцию.
   4.1 для создания миграции необходимо написать команду alembic revision --autogenerate, затем alembic upgrade head.
5. Запустить файл main.py