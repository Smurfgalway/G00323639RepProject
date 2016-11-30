import flask as myfl
from flask import request, g
import sqlite3

DATABASE = 'data/thisdata.db'
con = sqlite3.connect(DATABASE)
c= con.cursor()
app = myfl.Flask(__name__)

def pullData():
    db = getattr(myfl.g, '_database', None)
    if db is None:
        db = myfl.g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(myfl.g, '_database', None)
    if db is not None:
        db.close()

@app.route("/data", methods=["POST"])
def database():
    c.execute('INSERT INTO Cart(name, price) VALUES(?,?)',(myfl.request.form['name'],myfl.request.form['price']))
    con.commit()
    c.execute("Select * from Cart")
    return  str(c.fetchall()) 

@app.route("/")
def name():
   return app.send_static_file('Index.html')

if __name__ == "__main__":
	app.run()