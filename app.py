from flask import Flask,render_template,request,redirect,session
from flask_session import Session
import sqlite3
# from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# from flask_sqlalchemy import SQLAlchemy

# from flask_sqlalchemy import SQLAlchemy




# import random
app = Flask(__name__)
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"] ="filesystem"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Jerry/Desktop/WD/Pro1/Flask-Demo/venv/Scripts/templates/demo.db'
db = SQLAlchemy(app)
Session(app)


@app.route('/')
def index():
	# n = random.randint(1,50)
	# return "<h1>hello world guys</h1>"
	# return render_template("index.html",name="John",number=n)
	if "A" not in session:
		session["A"] = []
		
	return render_template("index.html",todo=session["A"])

# A = []

# @app.route("/goodby")
# def bye():
# 	return "Goodbye"

@app.route("/hello")
def hello():
	name = request.args.get("name")
	if not name:
		return render_template("failure.html")
	return render_template("hello.html",name=name)

@app.route("/jv")
def jvs():
	return render_template("jv.html")

@app.route("/sqldemo")
def sqldemo():
	rows = db.session.execute("SELECT * FROM regs")
	return render_template("sqldemo.html",rows=rows)

@app.route("/addi",methods=["GET","POST"])
def addi():
	if request.method == "GET":
		return render_template("addi.html")
	else:
		x = request.form.get("item")
		session["A"].append(x)
		return redirect("/")




if __name__ == '__main__':
	app.run(debug=True)




# commands to start flask server
# 1		.\venv\Scripts\activate
# 2		flask run








