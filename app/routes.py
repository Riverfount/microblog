from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Vicente Marçal'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'A wonderful day in São Manuel!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Tha Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
