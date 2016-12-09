from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import webbrowser as wb
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'connect_to_mongo_dipjal'
app.config['MONGO_URI'] = 'mongodb://dipjal:12345@ds127998.mlab.com:27998/connect_to_mongo_dipjal'

mongo = PyMongo(app) # connect mongo DB with our flask app

if mongo :
	print 'Connected Successfully'
else :
	print 'Connection failed'

@app.route('/add' , methods=['GET','POST'])
def add() :
	if request.method == 'POST': 
		firstname = request.form['fname']
		lastname = request.form['lname']
		db = mongo.db.Names
		existing = db.find_one({'firstname' : firstname , 'lastname' : lastname})
		if existing :
			return 'Username Already Exists'
		else :
			if len(firstname) < 4 :
				return 'First name should have atleast 4 characters'
			if len(lastname) < 4 :
				return 'Last name should have atleast 4 characters'
			db.insert(
				{'firstname' : firstname,
				'lastname' : lastname})
			return 'Added Successfully'

	return render_template('index.html')


@app.route('/transfer' , methods = ['GET' , 'POST'])
def transfer() :
	if request.method == 'POST' :
		return render_template('delete.html')
	return render_template('index.html')

@app.route('/remove' , methods = ['GET' , 'POST'])
def remove() :
	if request.method == 'POST' :
		firstname = request.form['fname']
		lastname = request.form['lname']
		db = mongo.db.Names
		existing = db.find_one({'firstname' : firstname, 'lastname' : lastname})
		if existing is None : 
			return 'Deletion failed : Name not found!!'
		else :
			db.remove({'firstname' : firstname , 'lastname' : lastname})
			return 'Name Successully Deleted'

	return render_template('index.html')


@app.route('/viewall' , methods = ['GET', 'POST'])
def viewall():
	if request.method == 'POST' :
		db = mongo.db.Names

@app.route('/')
def index() :
	return render_template('index.html')

if __name__ == "__main__" :
	app.run()
