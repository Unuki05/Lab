from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Route for home page
@app.route('/')
def index():
    return render_template("index.html")

# Route for listing branches
@app.route('/branch')
def branch_list():
    conn = sqlite3.connect("Employee.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Branch")
    branches = cursor.fetchall()
    conn.close()
    return render_template("branch_view.html", branches=branches)

# Route for displaying and adding workers
@app.route('/worker', methods=['GET', 'POST'])
def worker_list():
    conn = sqlite3.connect("Employee.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    if request.method == 'POST':
        # Handle new worker addition
        worker_name = request.form['worker_name']
        branch_id = request.form['branch_id']
        cursor.execute("INSERT INTO Worker (wname, bid) VALUES (?, ?)", (worker_name, branch_id))
        conn.commit()
        return redirect(url_for('worker_list'))
    
    # Fetch all workers
    cursor.execute("""
        SELECT Worker.id, Worker.wname, Branch.bname
        FROM Worker
        LEFT JOIN Branch ON Worker.bid = Branch.id
    """)
    workers = cursor.fetchall()
    
    # Fetch branches for dropdown
    cursor.execute("SELECT * FROM Branch")
    branches = cursor.fetchall()
    
    conn.close()
    return render_template("worker_view.html", workers=workers, branches=branches)

if __name__ == '__main__':
    app.run(debug=True)
