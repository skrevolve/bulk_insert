#!/usr/bin/python3

from sqlalchemy import create_engine, event
from pandas import DataFrame

engine = create_engine("mysql+pymysql://root:1234@127.0.0.1:3306/my_database?charset=utf8")

datas = [
    {'col_name1': 'test1', 'col_name2': 'test1', 'col_name3': 'test1'},
    {'col_name1': 'test1', 'col_name2': 'test1', 'col_name3': 'test1'},
    # ...
]

df = DataFrame(datas)

@event.listens_for(engine, "before_cursor_execute")
def receive_before_cursor_execute(
    conn, cursor, statement, params, context, executemany
):
    if executemany:
        cursor.fast_executemany = True

df.to_sql("test_table", engine, index=False, if_exists="append", schema="dbo")

#########################################################################
# rows_count= [‘50’,’1000',’5000', ‘0.01M’,’0.05M’,’0.1M’,’0.2M’,’0.3M’]
# time(sec)= [0.017, 0.015, 0.031, 0.063, 0.146, 0.344, 0.611, 0.833]
#########################################################################