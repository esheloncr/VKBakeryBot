from sqlalchemy import Column, ForeignKey, Integer, String, Text, MetaData, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# create connection and metadata
engine = create_engine("postgresql://postgres:b4hxd6u7@localhost:5432/flask_db")
Base = declarative_base()
metadata = MetaData()

# make a session for ORM
Session = sessionmaker(bind=engine)
session = Session()


# models
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
    price = Column(Integer())
    photo = Column(String())

    def __str__(self):
        return self.title


class Cart(Base):
    __tablename__ = "cart"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    product_id = Column(Integer(), ForeignKey("product.id", ondelete="CASCADE"))
    count = Column(Integer())
    sum = Column(Integer())


class User(Base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(255))
