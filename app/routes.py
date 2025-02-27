from app import app
from flask import render_template

from app.forms import LoginForm


@app.route('/')

@app.route('/index')
def index():
    user = {'username': 'Pavel'}
    posts = [
        {
            'author': {'username':'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The avengers movie was cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)