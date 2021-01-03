from flask import render_template, url_for, flash, redirect,request
from cyberworld import app, db, bcrypt
# from flask_session import Session
from cyberworld.RegLog import RegistrationForm, LoginForm
from cyberworld.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
# app.config["SESSION_PERMANENT"]=False
# app.config["SESSION_TYPE"] ="filesystem"

# Session(app)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]
# session={}
@app.route('/home')
@app.route('/')
def index():
	# if "A" not in session:
	# 	session["A"] = []
	return render_template("index.html",posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/hello")
def hello():
	name = request.args.get("name")
	if not name:
		return render_template("failure.html")
	return render_template("hello.html",name=name)

@app.route("/jv")
def jvs():
	return render_template("jv.html",title="JavaScript")

@app.route("/test")
def test():
	return render_template("test.html",title="Test")


# @app.route("/addi",methods=["GET","POST"])
# def addi():
# 	if request.method == "GET":
# 		return render_template("addi.html",todo=session["A"])
# 	else:
# 		x = request.form.get("item")
# 		session["A"].append(x)
# 		return redirect("/addi")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)



@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))



@app.route("/account")
@login_required
def account():
    return render_template('myaccount.html', title='Account')

