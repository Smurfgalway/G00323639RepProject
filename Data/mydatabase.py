import sqlite3

conn = sqlite3.connect('db.db')

c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS Ploting(unix REAL, datestamp TEXT, keyword TEXT, value Real)')
	
def data_entry():
	c.execute("INSERT INTO 	Ploting VALUES(10, '28-11', 'hm', 07)")
	conn.commit()
	c.close()
	conn.close()
	
create_table()
data_entry()
	