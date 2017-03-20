from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)


@app.route('/')
def default():
    return '<h1>Home page</h1>'


@app.route('/admin/')
def hello_admin():
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return render_template('hello.html', name=guest)


@app.route('/user/<name>')
def hello_user(name):
    if name=='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))


@app.route('/version/')
def revision():
    return 'Version 0.1'

if __name__ == '__main__':
    app.run(port=5000, debug=True)
