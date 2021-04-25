from fask import render_template
from app import app

# Views
@app.route('/')
def index():
    render_template('index.html')

@app.route('/navbar.html')
def index():
    render_template('navbar')

@app.route('/profile.html')
def index():
    render_template('profile.html')

@app.route('/signup.html')
def index():
    render_template('signup.html')

@app.route('/comment.html')
def index():
    render_template('comment.html')

if __name__=='__main__':
    app.run(debug=True)