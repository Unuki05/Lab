from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Route for home page
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/branch', methods=['GET', 'POST'])
def branch_list():
    conn = sqlite3.connect("Employee.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Handle POST request to add a new branch
    if request.method == 'POST':
        branch_name = request.form['branch_name']
        if branch_name.strip():
            cursor.execute("INSERT INTO Branch (bname) VALUES (?)", (branch_name,))
            conn.commit()
    
    # Fetch all branches
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
# Route to delete a branch
@app.route('/branch/delete/<int:id>', methods=['GET'])
def delete_branch(id):
    conn = sqlite3.connect("Employee.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Branch WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('branch_list'))

# Route to edit a branch
@app.route('/branch/edit/<int:id>', methods=['GET', 'POST'])
def edit_branch(id):
    conn = sqlite3.connect("Employee.db")
    cursor = conn.cursor()

    if request.method == 'POST':
        new_name = request.form['bname']
        cursor.execute("UPDATE Branch SET bname = ? WHERE id = ?", (new_name, id))
        conn.commit()
        conn.close()
        return redirect(url_for('branch_list'))
    
    cursor.execute("SELECT * FROM Branch WHERE id = ?", (id,))
    branch = cursor.fetchone()
    conn.close()
    return render_template("edit_branch.html", branch=branch)

# Route to delete a worker
@app.route('/worker/delete/<int:id>', methods=['GET'])
def delete_worker(id):
    conn = sqlite3.connect("Employee.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Worker WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('worker_list'))

# Route to edit a worker
@app.route('/worker/edit/<int:id>', methods=['GET', 'POST'])
def edit_worker(id):
    conn = sqlite3.connect("Employee.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    if request.method == 'POST':
        worker_name = request.form['worker_name']
        branch_id = request.form['branch_id']
        cursor.execute("UPDATE Worker SET wname = ?, bid = ? WHERE id = ?", (worker_name, branch_id, id))
        conn.commit()
        conn.close()
        return redirect(url_for('worker_list'))

    # Fetch worker details with the branch ID
    cursor.execute("SELECT id, wname, bid FROM Worker WHERE id = ?", (id,))
    worker = cursor.fetchone()

    # Fetch all branches for the dropdown
    cursor.execute("SELECT id, bname FROM Branch")
    branches = cursor.fetchall()
    conn.close()

    return render_template("edit_worker.html", worker=worker, branches=branches)



if __name__ == '__main__':
    app.run(debug=True)
