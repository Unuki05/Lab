from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Connect to the database and fetch branch data
@app.route('/branch')
def branch_list():
    conn = sqlite3.connect("Employee.db")
    conn.row_factory = sqlite3.Row  # This will allow us to access columns by name
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Branch")
    branches = cursor.fetchall()
    conn.close()
    return render_template("branch_view.html", branches=branches)

# Connect to the database and fetch worker data
@app.route('/worker')
def worker_list():
    conn = sqlite3.connect("Employee.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Worker.id, Worker.wname, Branch.bname
        FROM Worker
        LEFT JOIN Branch ON Worker.bid = Branch.id
    """)
    workers = cursor.fetchall()
    conn.close()
    return render_template("worker_view.html", workers=workers)

if __name__ == '__main__':
    app.run(debug=True)
