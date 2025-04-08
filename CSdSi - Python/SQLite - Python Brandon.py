import sqlite3
db_file = 'C:/Users/CompuAula 03/Downloads/Brandon.db'
con = sqlite3.connect(db_file)
cur = con.cursor()
cur.execute("Select * from Materias;")           
table_list = cur.fetchall()
for row in table_list:
    print(row)    #(print row[0]) #print(row)
con.close()