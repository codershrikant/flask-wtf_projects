import os
from flask import Flask, render_template, request, redirect, url_for 
from flask_wtf import FlaskForm 
from wtforms import StringField, validators, PasswordField, SubmitField 
from wtforms.validators import DataRequired, Email 
from flask_bootstrap import Bootstrap
import email_validator


class contactForm(FlaskForm): 
    name = StringField(label='Name', validators=[DataRequired()]) 
    email = StringField(label='Email', validators=[DataRequired(), Email(granular_message=True)])
    message = StringField(label='Message') 
    submit = SubmitField(label="Log In") 


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    Bootstrap(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'


    @app.route('/index', methods=["GET", "POST"]) 
    def home(): 
        cform=contactForm() 
        if cform.validate_on_submit(): 
                print(f"Name:{cform.name.data}, E-mail:{cform.email.data}, message:{cform.message.data}")
        else:
            print("wrong data received")
            
        return render_template("contact.html",form=cform) 



    return app