from flask import Flask, request, redirect, url_for, render_template, session
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key for your application

# Dummy user database for demonstration
users = {
    'user1': {'username': 'user1', 'password': 'password1'},
    'user2': {'username': 'user2', 'password': 'password2'},
}

# Decorator for checking if the user is authenticated
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    return 'Welcome to the home page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
    return render_template('C:/Users/KiranKumarBR-Int-215/Desktop/pythonProject/Python_Ramup/index.html')

@app.route('/dashboard')
@login_required  # This route can only be accessed by authenticated users
def dashboard():
    username = session['username']
    return f'Hello, {username}. This is your dashboard.'

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
