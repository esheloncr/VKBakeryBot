import os
from sqlalchemy import Column, ForeignKey, Integer, String, MetaData, create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = os.environ.get("DB_URL")
DB_ASYNC_URL = os.environ.get("DB_URL_ASYNC")


engine = create_engine(DB_URL)
Base = declarative_base()
metadata = MetaData()

# Создание сессии для ORM
Session = sessionmaker(bind=engine)
session = Session()

# Асинхронная сессия для ORM
async_engine = create_async_engine(DB_ASYNC_URL)
aSession = sessionmaker(bind=async_engine, class_=AsyncSession)
asession = aSession()


class Section(Base):
    __tablename__ = "section"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    title = Column(String(255), unique=True)

    def __str__(self):
        return self.title


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    section = Column(String(255), ForeignKey("section.title", ondelete="CASCADE"))
    title = Column(String(255), nullable=False)
    description = Column(String())
    photo = Column(String())

    def __str__(self):
        return self.title

