from flask import Flask, abort

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, this is the index page</h1>'

@app.route('/help')
def help_page():
    return '<h1>Welcome to the Help Page</h1>'

@app.route('/error')
def error_page():

    abort(404)
    

@app.errorhandler(404)
def not_found_error(error):
    return '<h1>404 - huudas oldsongui </h1>', 404

if __name__ == '__main__':
    app.run(debug=True)
