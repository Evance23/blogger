
from flask import render_template, flash, redirect, url_for
from app import app
from . import auth


from flask_login import login_user, logout_user ,login_required
from ..models import User

from .forms import RegistrationForm
from .. import db
from ..email import mail_message

# Views


@app.route('/')
def index():
    title = 'Home- Making the minute count'
    return render_template('index.html', title=title)

# @app.route('/navbar.html')
# def navbar():
#     return render_template('navbar')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = request.form
        username = form.get('username')
        password = form.get('password')
        print(username)
        user = User.query.filter_by(username=username).first()
        if user is None:
            error = 'A user with that username  does not exist'
            return render_template('login.html', error=error)
        is_correct_password = user.check_password(password)
        print(is_correct_password)
        if not is_correct_password:
            error = 'A user with that password does not exist'
            return render_template('login.html', error=error)
        login_user(user)
        return redirect('/')
    return render_template('login.html')


@ app.route('/profile.html')
def profie():
    return ender_template('profile.html')


@ app.route('/signup.html')
def signup():
    return render_template('signup.html')


@ app.route('/comment.html')
def comment():
    return render_template('comment.html')


if __name__ == '__main__':
    app.run(debug=True)
