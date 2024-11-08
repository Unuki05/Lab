from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Database connection helper
def get_db_connection():
    conn = sqlite3.connect('lab8.db')
    conn.row_factory = sqlite3.Row
    return conn

# Branch class with methods to retrieve records
class Branch:
    def __init__(self, id, bname):
        self.id = id
        self.bname = bname

    @staticmethod
    def getRecord(id):
        conn = get_db_connection()
        branch = conn.execute('SELECT * FROM branch WHERE id = ?', (id,)).fetchone()
        conn.close()
        return Branch(branch['id'], branch['bname']) if branch else None

    @staticmethod
    def getRecords():
        conn = get_db_connection()
        branches = conn.execute('SELECT * FROM branch').fetchall()
        conn.close()
        return [Branch(branch['id'], branch['bname']) for branch in branches]

# Worker class with methods to retrieve records
class Worker:
    def __init__(self, id, wname, bid):
        self.id = id
        self.wname = wname
        self.bid = bid

    @staticmethod
    def getRecord(id):
        conn = get_db_connection()
        worker = conn.execute('SELECT * FROM worker WHERE id = ?', (id,)).fetchone()
        conn.close()
        return Worker(worker['id'], worker['wname'], worker['bid']) if worker else None

    @staticmethod
    def getRecords():
        conn = get_db_connection()
        workers = conn.execute('''
            SELECT w.id, w.wname, b.bname
            FROM worker w
            JOIN branch b ON w.bid = b.id
        ''').fetchall()
        conn.close()
        return [{'id': worker['id'], 'wname': worker['wname'], 'bname': worker['bname']} for worker in workers]

# Route to display branches
@app.route('/branch')
def branch_list():
    branches = Branch.getRecords()
    return render_template('branch_view.html', branches=branches)

# Route to display workers
@app.route('/worker')
def worker_list():
    workers = Worker.getRecords()
    return render_template('worker_view.html', workers=workers)

if __name__ == '__main__':
    app.run(debug=True)
