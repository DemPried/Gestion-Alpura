from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    try:
        if request.method =='POST':

            username = request.form['username']

            password = request.form['password']

            if not username:
                error = 'Debes ingresar un usuario'
                flash(error)
                return render_template('index.html')

            if not password:
                error = 'Debes ingresar una contraseña'
                flash(error)
                return render_template('index.html')

            username == 'BACCA1' and password == '1234'

            return render_template('VisualizarUsuarioFinal.html')
        else:
            return render_template('index.html')
    except Exception as ex:
        print(ex)
        return render_template('index.html')

   # return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():  # put application's code here
    try:
        if request.method =='POST':
            username = request.form['username']
            password = request.form['password']

            if not username:
                error = 'Debes ingresar un usuario'
                flash(error)
                return render_template('index.html')

            if not password:
                error = 'Debes ingresar una contraseña'
                flash(error)
                return render_template('index.html')

            if username == 'SuperADM' and password == '1234':
                return render_template('gestorUsuarioSuper.html')
            if username == 'ADMIN' and password == '1234':
                return render_template('gestorEmpleadosAdmin.html')
            if username == 'empleado'and password == '1234':
                return redirect(url_for('menu_empleado'))
            else:
                return render_template('index.html')
        else:
            return render_template('index.html')
    except Exception as ex:
        print(ex)
        return render_template('index.html')

   # return render_template('index.html')

@app.route('/menu_empleado', methods=['GET', 'POST'])
def menu_empleado():
    return render_template('VisualizarUsuarioFinal.html')


@app.route('/menu_administrador', methods=['GET', 'POST'])
def menu_administrador():
    return render_template('gestorEmpleadosAdmin.html')


@app.route('/AgregarEmpleados', methods=['GET', 'POST'])
def agregarEmpleados():
    return render_template('AgregarEmpleados.html')


@app.route('/BuscarEmpleados', methods=['GET', 'POST'])
def buscarEmpleados():
    return render_template('BuscarEmpleado.html')


@app.route('/EditarEmpleados', methods=['GET', 'POST'])
def editarEmpleados():
    return render_template('EditarEmpleados.html')


@app.route('/DesempeñoEmpleados', methods=['GET', 'POST'])
def desempeñoEmpleados():
    return render_template('DesempeñoEmpleado.html')


@app.route('/VisualizadordesdeAdmin', methods=['GET', 'POST'])
def visualizadordesdeAdmin():
    return render_template('VisualisadordesdeAdmin.html')


@app.route('/GestorUsuariosSuper', methods=['GET', 'POST'])
def gestorUsuariSuper():
    return render_template('gestorUsuarioSuper.html')


@app.route('/AgregarUsuarioSuper', methods=['GET', 'POST'])
def agregarUsuarioSuper():
    return render_template('AgregarUsuario.html')


@app.route('/EditarUsuariosuper', methods=['GET', 'POST'])
def editarUsuariosuper():
    return render_template('EditarUsuarioSuper.html')


@app.route('/BuscaryEliminarUsuario', methods=['GET', 'POST'])
def buscaryEliminarUsuario():
    return render_template('BuscarEliminarUsuario.html')


@app.route('/DesempeñoUsuarioSuper', methods=['GET', 'POST'])
def desempeñoUsuarioSuper():
    return render_template('DesempeñodesdeSuper.html')


@app.route('/VisualizarUsuarioSuper', methods=['GET', 'POST'])
def visualizarUsuarioSupe():
    return render_template('VisualizardesdeSuper.html')


if __name__ == '__main__':
    app.run()
