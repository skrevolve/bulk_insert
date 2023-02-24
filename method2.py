
from pyodbc import connect
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

cursor = cnxn.cursor()

for row_count in range(0, df_op.shape[0]):
      chunk = df_op.iloc[row_count:row_count + 1,:].values.tolist()
      tuple_of_tuples = tuple(tuple(x) for x in chunk)
      cursor.executemany("insert into test" + " ([col_name1],[col_name2],[col_name3],[col_name4],[col_name5],[col_name6],[col_name7],[col_name8],[col_name9],[col_name10]) values   (?,?,?,?,?,?,?,?,?,?)",tuple_of_tuples)