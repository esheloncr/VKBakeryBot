from sqlalchemy import Column, ForeignKey, Integer, String, MetaData, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://postgres:b4hxd6u7@localhost:5432/flask_db")
Base = declarative_base()
metadata = MetaData()

# Создание сессии для ORM
Session = sessionmaker(bind=engine)
session = Session()


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

