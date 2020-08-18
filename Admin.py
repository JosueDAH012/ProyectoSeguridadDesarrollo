# importaciones de la libreria de Flask para la base de datos y web
from flask import Flask, render_template, request, flash, redirect, url_for, session, abort
from flask_mysqldb import MySQL
import bcrypt
import re

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

# inicializacion
app = Flask(__name__, static_url_path='/static')
mysql = MySQL(app)

# conexion a base de datos
app.config['MYSQL_HOST'] = '35.235.106.218'
app.config['MYSQL_USER'] = 'MowgliG'
app.config['MYSQL_PASSWORD'] = 'Josuedavid01'
app.config['MYSQL_DB'] = 'TIENDA'

# configuracion
app.secret_key = "server-ca.pem"
print("Conectado a la Base de Datos")

# semilla para encriptamiento
semilla = bcrypt.gensalt()

# ruta para la clase principal
@app.route('/')
def main():
    if 'username' in session:
        return render_template('home.html')
    else:
        return render_template('inicio/login.html')

# ruta para la clase home
@app.route('/home', )
def home():
    if 'username' in session:
        return render_template('home.html')
    else:
        return render_template('inicio/login.html')

# ruta para la clase login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if (request.method == "GET"):
        if 'username' in session:
            return render_template('home.html')
        else:
            return render_template('inicio/login.html')
    else:
        if request.method == 'POST' and 'emailLogin' in request.form and 'passwordLogin' in request.form:
            correo = request.form['emailLogin']
            password = request.form['passwordLogin']
            password_encode = password.encode("utf-8")

            cursor = mysql.connection.cursor()
            sQuery = "SELECT * FROM Usuario WHERE Correo = %s"
            cursor.execute(sQuery, [correo])
            account = cursor.fetchone()
            cursor.close()

            if (account != None):
                password_encriptado_encode = account[6].encode()
                if (bcrypt.checkpw(password_encode, password_encriptado_encode)):
                    session['loggedin'] = True
                    session['username'] = account[1]
                    session['correo'] = account[4]
                    return redirect(url_for('home'))
                else:
                    flash("El Password o Correo no son correctos", "alert-warning")
                    return render_template('inicio/login.html')
            else:
                flash("El Correo no existe", "alert-warning")
                return render_template('inicio/login.html')
    return render_template('home.html')


# ruta para la clase registrar
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if (request.method == "GET"):
        if 'username' in session:
            return render_template('home.html')
        else:
            return render_template('inicio/signup.html')
    else:
        if request.method == 'POST' and 'nameRegistro' in request.form and 'surnameRegistro' in request.form and 'idRegistro' in request.form and 'emailRegistro' in request.form and 'phoneRegistro' in request.form and 'passwordRegistro' in request.form:

            nombre = request.form['nameRegistro']
            apellido = request.form['surnameRegistro']
            cedula = request.form['idRegistro']
            correo = request.form['emailRegistro']
            telefono = request.form['phoneRegistro']
            password = request.form['passwordRegistro']
            password_encode = password.encode("utf-8")
            password_encriptado = bcrypt.hashpw(password_encode, semilla)
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM Usuario WHERE Correo = %s', [correo])
            account = cursor.fetchone()

            if account:
                flash("Esta cuenta ya existe!", "alert-warning")
            elif not re.match(r'[A-Za-z]+', nombre):
                flash("El nombre debe contener solo letras", "alert-warning")
            elif not re.match(r'[A-Za-z]+', apellido):
                flash("El apellido debe contener solo letras", "alert-warning")
            elif not re.match(r'[0-9]+', cedula):
                flash("La cedula solo debe tener números", "alert-warning")
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', correo):
                flash("Correo invalido!", "alert-warning")
            elif not re.match(r'[0-9]+', telefono):
                flash("El telefono solo debe tener números", "alert-warning")
            elif not re.match(r'[A-Za-z0-9]+', password):
                flash("La contraseña solo debe tener números y letras", "alert-warning")
            else:
                sQuery = "INSERT INTO Usuario (Nombre, Apellido, Cedula, Correo, Telefono, Password) VALUES ( %s, %s, %s, %s, %s, %s)"
                cursor.execute(sQuery, [nombre, apellido, cedula, correo, telefono, password_encriptado])
                mysql.connection.commit()
                flash("Se ha registrado exitosamente!", "alert-warning")
        elif request.method == 'POST':
            flash("Por favor rellena el formulario!", "alert-warning")
        return redirect(url_for('home'))
    return render_template('inicio/login.html')


@app.route("/salir")
def salir():
    session.clear()
    return redirect(url_for('login'))


@app.route('/password')
def password():
    if 'username' in session:
        return render_template('home.html')
    else:
        return render_template('inicio/password.html')


@app.route('/terminos')
def terminos():
    return render_template('inicio/terminos.html')


@app.route('/Bloqueado')
def h401():
    return abort('401')


@app.errorhandler(401)
def access_error(error):
    return render_template('errores/h401.html'), 401


@app.route('/Prohibido')
def h403():
    return abort('403')


@app.errorhandler(403)
def access_error(error):
    return render_template('errores/h403.html'), 403


@app.route('/SinAcceso')
def h404():
    return abort('404')


@app.errorhandler(404)
def access_error(error):
    return render_template('errores/h404.html'), 404


@app.route('/InternalServerError')
def h500():
    return abort('500')


@app.errorhandler(500)
def access_error(error):
    return render_template('errores/h500.html'), 500


@app.route('/cart')
def cart():
    return render_template('pagar/cart.html')


@app.route('/teclados')
def teclados():
    return render_template('perifericos/teclados.html')


@app.route('/mouse')
def mouse():
    return render_template('perifericos/mouse.html')


@app.route('/headset')
def headset():
    return render_template('perifericos/headset.html')


@app.route('/mousepad')
def mousepad():
    return render_template('perifericos/mousepad.html')


@app.route('/controles')
def controles():
    return render_template('perifericos/controles.html')


@app.route('/parlantes')
def parlantes():
    return render_template('perifericos/parlantes.html')


@app.route('/webcam')
def webcam():
    return render_template('perifericos/webcam.html')


@app.route('/microfonos')
def microfonos():
    return render_template('perifericos/microfonos.html')


@app.route('/impresoras')
def impresoras():
    return render_template('perifericos/impresoras.html')


@app.route('/combos')
def combos():
    return render_template('computadoras/combos.html')


@app.route('/gaming')
def gaming():
    return render_template('computadoras/gaming.html')


@app.route('/hogar')
def hogar():
    return render_template('computadoras/hogar.html')


@app.route('/laptop')
def laptop():
    return render_template('computadoras/laptop.html')


@app.route('/venta')
def venta():
    return render_template('computadoras/venta.html')


@app.route('/almacenamiento')
def almacenamiento():
    return render_template('componentes/almacenamiento.html')


@app.route('/cases')
def cases():
    return render_template('componentes/cases.html')


@app.route('/enfriamiento')
def enfriamiento():
    return render_template('componentes/enfriamiento.html')


@app.route('/monitores')
def monitores():
    return render_template('componentes/monitores.html')


@app.route('/motherboard')
def motherboard():
    return render_template('componentes/motherboard.html')


@app.route('/power')
def power():
    return render_template('componentes/power.html')


@app.route('/procesadores')
def procesadores():
    return render_template('componentes/procesadores.html')


@app.route('/ram')
def ram():
    return render_template('componentes/ram.html')


@app.route('/tarjetavideo')
def tarjetavideo():
    return render_template('componentes/tarjetavideo.html')


@app.route('/cables')
def cables():
    return render_template('accesorios/cables.html')


@app.route('/encapsuladores')
def encapsuladores():
    return render_template('accesorios/encapsuladores.html')


@app.route('/extencion')
def extencion():
    return render_template('accesorios/extencion.html')


@app.route('/led')
def led():
    return render_template('accesorios/led.html')


@app.route('/pastatermica')
def pastatermica():
    return render_template('accesorios/pastatermica.html')


@app.route('/sillas')
def sillas():
    return render_template('accesorios/sillas.html')


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/template')
def template():
    return render_template('template.html')


if __name__ == '__main__':
    app.run(debug=True)
