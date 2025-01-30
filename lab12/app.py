from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Initialize the database
def init_db():
    with sqlite3.connect("app.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )''')
        conn.commit()

init_db()

# Utility functions
def get_user(username):
    with sqlite3.connect("app.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return cursor.fetchone()

def get_all_users():
    with sqlite3.connect("app.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, role FROM users")
        return cursor.fetchall()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def update_user_role(user_id, role):
    with sqlite3.connect("app.db") as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET role = ? WHERE id = ?", (role, user_id))
        conn.commit()

def delete_user(user_id):
    with sqlite3.connect("app.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()

# Routes
@app.route('/')
def home():
    user = session.get('user')
    if user:
        if user['role'] == 'Admin':
            return redirect(url_for('admin_home'))  # Redirect to Admin Home Page
        return render_template('home.html', user=user)
    return render_template('home.html', user=None)
@app.route('/adminhome')
def admin_home():
    user = session.get('user')
    if user and user['role'] == 'Admin':
        return render_template('adminhome.html', user=user)
    return redirect(url_for('home'))
@app.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('user'):
        return redirect(url_for('home'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password != confirm_password:
            flash("Passwords do not match!", "error")
            return redirect(url_for('register'))
        if get_user(username):
            flash("Username already exists!", "error")
            return redirect(url_for('register'))
        hashed_password = hash_password(password)
        with sqlite3.connect("app.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", 
                           (username, hashed_password, 'User'))
            conn.commit()
        flash("Registered successfully! Please log in.", "success")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('user'):
        return redirect(url_for('home'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_user(username)
        if user and hash_password(password) == user[2]:
            session['user'] = {'id': user[0], 'username': user[1], 'role': user[3]}
            flash(f"Welcome back, {user[1]}!", "success")
            return redirect(url_for('home'))
        flash("Invalid credentials!", "error")
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for('home'))

@app.route('/admin', methods=['GET', 'POST'])
def admin_dashboard():
    user = session.get('user')
    if not user or user['role'] != 'Admin':
        flash("Access denied!", "error")
        return redirect(url_for('home'))

    if request.method == 'POST':
        action = request.form['action']
        user_id = int(request.form['user_id'])
        if action == 'delete':
            delete_user(user_id)
            flash("User deleted successfully!", "success")
        elif action == 'promote':
            update_user_role(user_id, 'Admin')
            flash("User promoted to Admin!", "success")
        elif action == 'demote':
            update_user_role(user_id, 'User')
            flash("User demoted to User!", "success")

    users = get_all_users()
    return render_template('admin.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
