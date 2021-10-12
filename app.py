from flask import Flask, render_template, request, flash,  redirect

app = Flask(__name__)

if __name__ == '__main__':
    app.run()


@app.route('/',methods=['GET', 'POST'])
def index():  # put application's code here
    return render_template('index.html')

@app.route('/status', methods=['GET', 'POST'])
def status():
    return render_template('status.html')

@app.route('/Menu_adm' , methods=['GET', 'POST'])
def Menu_adm():  # put application's code here
    return render_template('menu_administrador.html')

@app.route('/edit_user' ,methods=['GET', 'POST'])
def edit_user():  # put application's code here
    return render_template('edit_user.html')

@app.route('/add_new_user',methods=['GET', 'POST'])
def a_n_u():  # put application's code here
    return render_template('add_new_user.html')


    """""
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

"""""

