#!/usr/bin/python3

from sqlalchemy import create_engine
from pandas import DataFrame

engine = create_engine("mysql+pymysql://root:1234@127.0.0.1:3306/my_database?charset=utf8")

datas = [
    {'col_name1': 'test1', 'col_name2': 'test1', 'col_name3': 'test1'},
    {'col_name1': 'test1', 'col_name2': 'test1', 'col_name3': 'test1'},
    # ...
]

df = DataFrame(datas)

df.to_sql("test_table", engine, index=False, if_exists="append", schema="dbo")

#########################################################################
# rows_count= [‘50’,’1000',’5000', ‘0.01M’,’0.05M’,’0.1M’,’0.2M’,’0.3M’]
# time(sec)= [0.0230, 0.081, 0.289, 0.589, 3.105, 5.74, 11.769, 20.759]
#########################################################################