import requests as r
from db import session, Product

urls = {}
queryset = session.query(Product).all()
# Перевод картинки в BytesIO для работы во фреймфорке vkbottle
for q in queryset:
    link = r.get(q.photo).content
    urls[q.title] = link
