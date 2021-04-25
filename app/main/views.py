
from flask import render_template
from app import app

# Views
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/navbar.html')
def navbar():
    return render_template('navbar')

@app.route('/profile.html')
def profie():
    return ender_template('profile.html')

@app.route('/signup.html')
def signup():
    return render_template('signup.html')

@app.route('/comment.html')
def comment():
    return render_template('comment.html')

if __name__=='__main__':
    app.run(debug=True)