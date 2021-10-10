from flask import Flask, render_template, request, flash,  redirect
import utils
import os

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            print(1)
            if not username:
                error = 'Debes ingresar un usuario'
                flash(error)
                return render_template('index.html')
            if not password:
                error = 'Debes ingresar una contraseña'
                flash(error)
                return render_template('index.html')
            if username == 'Prueba' and password == 'Prueba123':
                return redirect("status.html")
            else:
                error = 'usuario o contraseñas invalidos'
                flash(error)
                return render_template('index.html')
        else:
            print(2)
            return render_template('index.html')
    except Exception as ex:
        print(3)
        print(ex)
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
