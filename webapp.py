import flask as myfl #imports flask as a variable
from flask import request, g, render_template #imports each component from flask
import sqlite3 #imports sqlite 3

#imports the database
DATABASE = 'data/thisdata.db'
con = sqlite3.connect(DATABASE)
c= con.cursor()
app = myfl.Flask(__name__)

#opens the database
def pullData():
    db = getattr(myfl.g, '_database', None)
    if db is None:
        db = myfl.g._database = sqlite3.connect(DATABASE)
    return db

#closes the database
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(myfl.g, '_database', None)
    if db is not None:
        db.close()

#inserts data into the database
#-------------------------------
@app.route("/data", methods=["POST"])
def database():
    c.execute('INSERT INTO Cart(name, price) VALUES(?,?)',(myfl.request.form['name'],myfl.request.form['price']))
    con.commit()
    return (render_template('basic.html') + str(c.fetchall()) )

#gets the price from the database 
@app.route("/add", methods=[ "GET"])
def added():
    c.execute("Select SUM(price) FROM Cart")
    return (render_template('basic.html') + str(c.fetchall()) )

#shows the contents of the database
#-------------------------------
@app.route("/show", methods=[ "GET"])
def showed():
    c.execute("Select * from Cart")
    return (render_template('basic.html') + str(c.fetchall()) )

#the main app route calls the main html page
#-------------------------------------------
@app.route("/")
def name():
   return render_template('Index.html')

#runs the app
#-----------------------
if __name__ == "__main__":
	app.run()
#refences flask docs, https://github.com/data-representation/example-sqlite, flask exercises on the moodle page