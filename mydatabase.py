import sqlite3

conn = sqlite3.connect('data/thisdata.db')

c = conn.cursor()

#def create_table():
	#c.execute('CREATE TABLE IF NOT EXISTS Contents(number INT, name TEXT, price REAL)')
	
#def data_entry():
#	c.execute("INSERT INTO 	Contents VALUES(1, 'ham', 2)")
#	c.execute("INSERT INTO 	Contents VALUES(2, 'cheese', 2)")
#	c.execute("INSERT INTO 	Contents VALUES(3, 'eggs', 1)")
#	c.execute("INSERT INTO 	Contents VALUES(4, 'milk', 2.5)")
#	c.execute("INSERT INTO 	Contents VALUES(5, 'bananas', 1)")
#	c.execute("INSERT INTO 	Contents VALUES(6, 'apples', 1)")
#	c.execute("INSERT INTO 	Contents VALUES(7, 'yogurt', 1)")
#	c.execute("INSERT INTO 	Contents VALUES(8, 'beer', 10)")
#	c.execute("INSERT INTO 	Contents VALUES(9, 'pizza', 5)")
#	c.execute("INSERT INTO 	Contents VALUES(10, 'wine', 10)")
#	c.execute("INSERT INTO 	Contents VALUES(11, 'bread', 4)")
#	c.execute("INSERT INTO 	Contents VALUES(12, 'sugar', 3)")
#	c.execute("INSERT INTO 	Contents VALUES(13, 'flour', 3)")
#	c.execute("INSERT INTO 	Contents VALUES(14, 'orange juice', 3)")
#	c.execute("INSERT INTO 	Contents VALUES(15, 'coke', 2.5)")
#	c.execute("INSERT INTO 	Contents VALUES(16, 'potatos', 4)")
#	c.execute("INSERT INTO 	Contents VALUES(17, 'carrots', 2)")
#	c.execute("INSERT INTO 	Contents VALUES(18, 'beans', 0.95)")
	
#	conn.commit()	

def create():
	c.execute('CREATE TABLE IF NOT EXISTS Cart( name TEXT, price TEXT)')
    
conn.commit()
    
#data_entry()

c.close
conn.close

if __name__ == "__main__":
    create()
	