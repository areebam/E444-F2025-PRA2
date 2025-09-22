from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}!</h1>'

# New route for Activity 1.3 (Bootstrap + timestamp)
@app.route('/')
def index():
    return render_template('index.html', name="Areeba", current_time=datetime.utcnow())

