#A very simple script
from flask import Flask, redirect, url_for, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'any secret string'
class LoginForm(FlaskForm):
	username = StringField("username", validators = [InputRequired(), Length( min = 4, max = 15)])
	password = PasswordField("password", validators = [InputRequired(), Length(min = 8, max= 80)])
	remember = BooleanField("remember me")

class RegisterForm(FlaskForm):
	email = StringField("email", validators= [InputRequired(), Email(message = "Invalid email"), Length(max = 50)])
	username = StringField("username", validators = [InputRequired(), Length(min = 4, max = 15)])
	password = PasswordField("password", validators = [InputRequired(), Length(min = 8, max= 80)])
@app.route("/home")
@app.route("/")
def home():
	return render_template("HackMISSO.html")

@app.route("/login")
def account():
	form = LoginForm()
	return render_template("account.html", form = form)
@app.route("/signup")
def signup():
	form = RegisterForm()
	return render_template("signup.html", form = form)

if __name__ == "__main__":
	app.run(debug = True)
