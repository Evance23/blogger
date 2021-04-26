
from flask import render_template, flash, redirect, url_for
from app import app
from app.form import LoginForm

# Views


@app.route('/')
def index():
    title = 'Home- Making the minute count'
    return render_template('index.html', title=title)

# @app.route('/navbar.html')
# def navbar():
#     return render_template('navbar')


@app.route('/login' methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # flash('User Log in {}, remember_me{} .format(form.username.data, form.remmeber_me.data)
        return redirect('/index')
    # return render_template('login.html', title='Log In', form=form)

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
