from flask import (
    flash,
    redirect,
    render_template,
    url_for,
)

from app import app
from app.forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user: {form.username.data}, remember me: {form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login_form.html', title='Sign In', form=form)
