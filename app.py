from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')
"""""
@app.route('/login')
def login():  # put application's code here
    return render_template('index.html')
"""""
@app.route('/menu_empleado', methods=['GET', 'POST'])
def menu_empleado():
    return  render_template('VisualizarUsuarioFinal.html')

@app.route('/menu_administrador', methods=['GET', 'POST'])
def menu_administrador():
    return  render_template('gestorEmpleadosAdmin.html')

@app.route('/AgregarEmpleados', methods=['GET', 'POST'])
def AgregarEmpleados():
    return  render_template('AgregarEmpleados.html')

@app.route('/BuscarEmpleados', methods=['GET', 'POST'])
def BuscarEmpleados():
    return  render_template('BuscarEmpleado.html')

@app.route('/EditarEmpleados', methods=['GET', 'POST'])
def EditarEmpleados():
    return  render_template('EditarEmpleados.html')

@app.route('/DesempeñoEmpleados', methods=['GET', 'POST'])
def DesempeñoEmpleados():
    return  render_template('DesempeñoEmpleado.html')

@app.route('/VisualizadordesdeAdmin', methods=['GET', 'POST'])
def VisualizadordesdeAdmin():
    return  render_template('VisualisadordesdeAdmin.html')

@app.route('/GestorUsuariosSuper', methods=['GET', 'POST'])
def GestorUsuariSuper():
    return  render_template('gestorUsuarioSuper.html')

@app.route('/AgregarUsuarioSuper', methods=['GET', 'POST'])
def AgregarUsuarioSuper():
    return  render_template('AgregarUsuario.html')

@app.route('/EditarUsuariosuper', methods=['GET', 'POST'])
def EditarUsuariosuper():
    return  render_template('EditarUsuarioSuper.html')

@app.route('/BuscaryEliminarUsuario', methods=['GET', 'POST'])
def BuscaryEliminarUsuario():
    return  render_template('BuscarEliminarUsuario.html')

@app.route('/DesempeñoUsuarioSuper', methods=['GET', 'POST'])
def DesempeñoUsuarioSuper():
    return  render_template('DesempeñodesdeSuper.html')

@app.route('/VisualizarUsuarioSuper', methods=['GET', 'POST'])
def VisualizarUsuarioSupe():
    return  render_template('VisualizardesdeSuper.html')

if __name__ == '__main__':
    app.run()
