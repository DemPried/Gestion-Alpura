from flask import Flask, render_template, request, flash, redirect, url_for
from db import get_db

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'] )
def index():
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            db = get_db()
            error = None

            if not username:
                error = 'Debes ingresar un usuario'
                flash(error)
                return render_template('index.html')

            if not password:
                error = 'Debes ingresar una contraseña'
                flash(error)
                return render_template('index.html')

            user = db.execute(
                'SELECT usuario, id_empleado FROM empleados WHERE correo= ? AND contraseña= ?', (username, password)).fetchone()
            print(user[0])

            if user is None:
                error = 'Usuario o contraseña inválidos'
            else:
                if user[0] == 1:
                    return redirect(url_for('menu_empleado'))
                elif user[0] == 2:
                    return redirect(url_for('menu_administrador'))
                elif user[0] == 3:
                    return redirect(url_for('menuSuperAdmin'))
                db.close_db()

        return render_template('index.html')
    except Exception as ex:
        print(ex)
        return render_template('index.html')


@app.route('/menu_empleado', methods=['GET', 'POST'])
def menu_empleado():
    return render_template('VisualizarUsuarioFinal.html')

@app.route('/menu_administrador', methods=['GET', 'POST'])
def menu_administrador():
    return render_template('gestorEmpleadosAdmin.html')

@app.route('/AgregarEmpleados', methods=['GET', 'POST'])
def btn_agregarEmpleados():

    try:

        db = get_db()

        num = db.executemany("SELECT id_doc, id_cargo, id_contrato, id_dependencia FROM documento, cargo, contrato, dependencia WHERE desc_documento = '?' AND des_cargo = '?' AND des_contrato ='?'  AND des_dependencia = '?';", (selectIDtype, selectCargo, selectContractType, selectDependencia)).fetchone()

        user = db.executemany("INSERT INTO empleados (tipo_doc, documento, usuario, nombres, apellidos, salario, cod_tipo_contrato, cargo, dependencia, fecha_inicio, fecha_final, correo, contraseña) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (num[0], IDnumber, 1, name, lastNames, Salary, num[2], num[1], num[3], fechadeingreso, Findelcontrato, Mail, Password))
        db.commit()

    except Exception as ex:
        print(ex)


    return render_template('AgregarEmpleados.html')

# esto es para crear un empleado nuevo

"""
def convertir_foto_a_binario(foto):
    with open(foto, 'rb') as f:
        blob = f.read()
        
    return blob

def crearEmpleado(db, usuario):
    foto_binario = convertir_foto_a_binario(usuario[-1])
    
    db = get_db()
    usuario = db.execute("INSERT INTO usuario (usuario, nombres, apellidos, salario, cod_tipo_contrato, dependencia, fecha_inicio, fecha_final, correo, contraseña, foto) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"%
                        (usuario[0], usuario[1], usuario[2], usuario[3], usuario[4], usuario[5], usuario[6], usuario[7], usuario[8], usuario[9], foto_binario))
    db.commit()        
    
foto_archivo = '/static/images/foto empleado.png'

empleado_creado = 'Usuario Creado Correctamente'
flash(empleado_creado) 
"""

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

@app.route('/menuSuperAdmin', methods=['GET', 'POST'])
def menuSuperAdmin():
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
    app.run(host='127.0.0.1', port=443, ssl_context=('micertificado.pem', 'llaveprivada.pem'))
