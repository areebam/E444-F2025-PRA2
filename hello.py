from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from datetime import datetime
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'devkey'
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/hello')
def hello():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}!</h1>'


# Form
class NameEmailForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your UofT Email address?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameEmailForm()
    name = None
    email = None
    message = None

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data

        if "utoronto" in email.lower():
            message = f"Your UofT email is {email}."
        else:
            message = "Please use your UofT email."

        # reset fields
        form.name.data = ''
        form.email.data = ''

    return render_template(
        "index.html",
        form=form,
        name=name,
        message=message,
        current_time=datetime.utcnow()
    )

