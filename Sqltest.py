import sqlite3
import pandas as pd
conn = sqlite3.connect('master.db')
c = conn.cursor()

listOfTables = c.execute(
  """SELECT name FROM sqlite_master  
  WHERE type='table';""").fetchall()
list1 = list(map(lambda x:x[0],listOfTables))
str_list = ' '.join(map(str, listOfTables))
if "012022" in str_list:
    print("1")
conn = sqlite3.connect('master.db')
c = conn.cursor()
Month = "022022"
#conn.execute("SELECT * FROM UserDB WHERE MonthYear='%s'" % (Month,))
#conn.execute("SELECT * FROM UserDB WHERE instr(column, {}) > 0;".format('012022'), con=conn)
conn.execute("DELETE FROM UserDB WHERE MonthYear = '%s'" % (Month,))

df = pd.read_sql("SELECT * FROM UserDB", con=conn)
df1 = pd.read_sql("select * from '012022'", con=conn)
print(df)
print(df1)