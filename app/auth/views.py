
from flask import Flask, render_template, url_for, flash, redirect, request
from . import auth
from flask_login import login_user, logout_user, login_required
from ..models import User
from .. import db
# from ..email import mail_message
from .forms import RegistrationForm, LoginForm
# Views
app = Flask(__name__)


@app.route('/')
def index():
    title = 'Home- Making the minute count'
    return render_template('index.html', title=title)

# @app.route('/navbar.html')
# def navbar():
#     return render_template('navbar')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.check_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or Password')
    title = "Pitch login"
        
    return render_template('auth/login.html',login_form = login_form,title=title)
    # form = LoginForm()
    # if request.method == 'POST':
    #     username = form.get('username')
    #     password = form.get('password')
    #     print(username)
    #     user = User.query.filter_by(username=username).first()
    #     if user is None:
    #         error = 'A user with that username  does not exist'
    #         return render_template('login.html', error=error)
    #     is_correct_password = user.check_password(password)
    #     print(is_correct_password)
    #     if not is_correct_password:
    #         error = 'A user with that password does not exist'
    #         return render_template('login.html', error=error)
    #     login_user(user)
    #     return redirect('/')
    # return render_template('auth/login.html', login_form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    # if request.method == 'POST':
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect (url_for('auth.login'))
    return render_template('auth/signup.html', registration_form=form)

        # print(form)
        # print("atwoli")
        # username = form.get("username")
        # email = form.get("email")
        # password = form.get("password")
        # confirm_password = form.get("confirm_password")
        # if username is None or password is None or email is None or confirm_password is None:
        #     error = 'Fill all the spaces'
        #     return render_template('signup.html', error=error)
        # if ' ' in username:
        #     error = 'Username should not contain spaces'
        #     return render_template('signup.html', error=error)
        # if password != confirm_password:
        #     error = "Passwords do not match"
        #     return render_template('signup.html', error=error)
        # else:
        #     user = User.query.filter_by(username=username).first()
        #     if user is not None:
        #         error = 'User already exists'
        #         return render_template('signup.html', error=error)
        #     user = User.query.filter_by(email=email).first()
        #     if user is not None:
        #         error = 'Email already registered'
        #         return render_template('signup.html', error=error)
        #     user = User(username=username, email=email)
        #     user.set_password(password)
        #     user.save()
        #     return redirect(url_for('auth.login'))
    


@auth.route('/logout')
def logout():
    logout_user()
    return redirect('auth/login.html')


if __name__ == '__main__':
    app.run(debug=True)
