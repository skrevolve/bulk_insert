#!/usr/bin/python3

from random import randint

from sqlalchemy import create_engine, Integer, Column, VARCHAR
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker

url = URL.create(
    drivername='mysql+pymysql',
    username='root',
    password='1234',
    host='127.0.0.1',
    database='my_database'
)

engine = create_engine(url)
Base = declarative_base()

class Rank(Base):
    __tablename__ = 'updown'

    id = Column(Integer, primary_key=True)
    wallet_addr = Column(VARCHAR(200), index=True)
    point = Column(Integer, index=True)

Session = sessionmaker(bind=engine)
session = Session()

TOTAL = 10000000
SUB = 500000

for i in range(TOTAL // SUB):
    objects = [
        Rank(wallet_addr=str(i * SUB * x), point=randint(0, 100000000))
        for x in range(SUB)
    ]

    session.bulk_save_objects(objects)
    session.commit()

    print(f'{(i + 1) * SUB} / {TOTAL}')