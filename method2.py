#!/usr/bin/python3

from pandas import DataFrame
from pyodbc import connect

cnxn = connect(
    driver="{MYSQL ODBC 8.0 Unicode Driver}",
    server='127.0.0.1',
    uid='root',
    pwd='1234',
    database='my_database'
)

cursor = cnxn.cursor()

datas = [
    {'col_name1': 'test1', 'col_name2': 'test1', 'col_name3': 'test1'},
    {'col_name1': 'test1', 'col_name2': 'test1', 'col_name3': 'test1'},
    # ...
]

df = DataFrame(datas)

for row_count in range(0, df.shape[0]):
    chunk = df.iloc[row_count:row_count + 1,:].values.tolist()
    tuple_of_tuples = tuple(tuple(x) for x in chunk)
    cursor.executemany("insert into test" + "([col_name1],[col_name2],[col_name3]) values (?,?,?)", tuple_of_tuples)

#########################################################################
# rows_count= [‘50’,’1000',’5000', ‘0.01M’,’0.05M’,’0.1M’,’0.2M’,’0.3M’]
# time(sec)= [0.005, 0.098, 0.440, 0.903, 4.290, 8.802, 17.776, 26.982]
#########################################################################