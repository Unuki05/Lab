from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('lab8.db')
    conn.row_factory = sqlite3.Row
    return conn

# Route: Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route: View Workers
@app.route('/workers')
def view_workers():
    conn = get_db_connection()
    workers = conn.execute('SELECT Worker.id, Worker.wname, Branch.bname FROM Worker JOIN Branch ON Worker.bid = Branch.id').fetchall()
    conn.close()
    return render_template('worker_list.html', workers=workers)

# Route: Add Worker Form
@app.route('/add_worker', methods=('GET', 'POST'))
def add_worker():
    conn = get_db_connection()
    branches = conn.execute('SELECT * FROM Branch').fetchall()

    if request.method == 'POST':
        wname = request.form['wname']
        bid = request.form['branch_id']

        if wname and bid:
            conn.execute('INSERT INTO Worker (wname, bid) VALUES (?, ?)', (wname, bid))
            conn.commit()
            conn.close()
            return redirect(url_for('view_workers'))

    conn.close()
    return render_template('worker_form.html', branches=branches)

# Route: Add Branch (optional for testing)
@app.route('/add_branch', methods=('GET', 'POST'))
def add_branch():
    if request.method == 'POST':
        bname = request.form['bname']
        conn = get_db_connection()
        conn.execute('INSERT INTO Branch (bname) VALUES (?)', (bname,))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('branch_form.html')

if __name__ == '__main__':
    app.run(debug=True)
