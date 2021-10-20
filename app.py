from flask import Flask, render_template, request, flash,  redirect, g
from db import get_db
#import utils
import os

app = Flask(__name__)

if __name__ == '__main__':
    app.run()

@app.route('/',methods=['GET', 'POST'])
def index():  # put application's code here
    return render_template('index.html')

@app.route('/menu_empleado', methods=['GET', 'POST'])
def menu_empleado():
    return render_template('/templates/Paginas Usuario/Pagina visualizar informacion/VisualizarUsuarioFinal.html')

@app.route('/menu_administrador' , methods=['GET', 'POST'])
def menu_administrador():  # put application's code here
    return render_template('/templates/Paginas Administrador/GestorAdmin/gestorEmpleadosAdmin.html')

@app.route('/admin_editar_empleado' ,methods=['GET', 'POST'])
def admin_editar_empleado():  # put application's code here
    return render_template('/templates/Paginas Administrador/EditarEmpleado/EditarEmpleados.html')

@app.route('/admin_agregar_empleado',methods=['GET', 'POST'])
def admin_agregar_empleado():  # put application's code here
    return render_template('/templates/Paginas Administrador/AgregarEmpleados/AgregarEmpleados.html')

@app.route('/admin_buscar_empleado',methods=['GET', 'POST'])
def admin_buscar_empleado():
    return render_template('/templates/Paginas Administrador/BuscarEmpleados/BuscarEmpleado.html')

@app.route('/desempeño_empleado_desde_admin',methods=['GET', 'POST'])
def desempeño_empleado_desde_admin():
    return render_template('/templates/Paginas Administrador/NotaEmpleado/DesempeñoEmpleado.html')

@app.route('/visualizar_empleado_desde_admin',methods=['GET', 'POST'])
def desempeño_empleado_desde_admin():
    return render_template('/templates/Paginas Administrador/VisualAdmin/VisualisadordesdeAdmin.html')

@app.route('/menu_superadministrador',methods=['GET', 'POST'])
def menu_superadministrador():
    return render_template('/templates/Paginas Super Admin/GestorAdmin/gestorUsuarioSuper.html')

@app.route('/superadmin_editar_usuario' ,methods=['GET', 'POST'])
def superadmin_editar_usuario():  # put application's code here
    return render_template('/templates/Paginas Super Admin/EditarUsuario/EditarUsuarioSuper.html')

@app.route('/superadmin_agregar_usuario',methods=['GET', 'POST'])
def superadmin_agregar_usuario():  # put application's code here
    return render_template('/templates/Paginas Super Admin/AgregarUsuario/AgregarUsuario.html')

@app.route('/superadmin_buscar_y_eliminar_usuarios',methods=['GET', 'POST'])
def superadmin_buscar_y_eliminar_usuarios():  # put application's code here
    return render_template('/templates/Paginas Super Admin/BuscaryEliminarUsers/BuscarEliminarUsuario.html')

@app.route('/desempeño_usuario_desde_superadmin',methods=['GET', 'POST'])
def desempeño_usuario_desde_superadmin():
    return render_template('/templates/Paginas Super Admin/NotaUsuario/DesempeñodesdeSuper.html')

@app.route('/visualizar_usuario_desde_superadmin',methods=['GET', 'POST'])
def visualizar_usuario_desde_superadmin():
    return render_template('/templates/Paginas Super Admin/VisualAdmin/VisualizardesdeSuper.html')


    """
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            print(1)
                        
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
            
            user = db.execute('SELECT * FROM usuario WHERE usuario= ?', (username, )).fetchone()
            
            if user is None:
                error = 'Usuario o contraseña inválidos'
            else:
                return "Hola" 
            
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
        return render_template('index.html')"""
