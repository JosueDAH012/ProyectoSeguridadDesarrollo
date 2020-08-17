# importaciones de la libreria de Flask para la base de datos y web
from flask import Flask, render_template, request, flash, redirect, url_for, session, abort
from flask_mysqldb import MySQL
import bcrypt

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

# @app.route('/')
# def Index():
#    cur = mysql.connection.cursor()
#    cur.execute('SELECT * FROM contacts')
#    data = cur.fetchall()
#    cur.close()
#    return render_template('index.html', contacts = data)

# @app.route('/add_contact', methods=['POST'])
# def add_contact():
#    if request.method == 'POST':
#        fullname = request.form['fullname']
#        phone = request.form['phone']
#        email = request.form['email']
#        cur = mysql.connection.cursor()
#        cur.execute("INSERT INTO contacts (fullname, phone, email) VALUES (%s,%s,%s)", (fullname, phone, email))
#        mysql.connection.commit()
#        flash('Contact Added successfully')
#        return redirect(url_for('Index'))

# @app.route('/edit/<id>', methods = ['POST', 'GET'])
# def get_contact(id):
#    cur = mysql.connection.cursor()
#    cur.execute('SELECT * FROM contacts WHERE id = %s', (id))
#    data = cur.fetchall()
#    cur.close()
#    print(data[0])
#    return render_template('edit-contact.html', contact = data[0])

# @app.route('/update/<id>', methods=['POST'])
# def update_contact(id):
#    if request.method == 'POST':
#        fullname = request.form['fullname']
#        phone = request.form['phone']
#        email = request.form['email']
#        cur = mysql.connection.cursor()
#        cur.execute("""
#            UPDATE contacts
#            SET fullname = %s,
#                email = %s,
#                phone = %s
#            WHERE id = %s
#        """, (fullname, email, phone, id))
#        flash('Contact Updated Successfully')
#        mysql.connection.commit()
#        return redirect(url_for('Index'))

# @app.route('/delete/<string:id>', methods = ['POST','GET'])
# def delete_contact(id):
#    cur = mysql.connection.cursor()
#    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
#    mysql.connection.commit()
#    flash('Contact Removed Successfully')
#    return redirect(url_for('Index'))


# conexion a base de datos
app.config['MYSQL_HOST'] = '35.235.106.218'
app.config['MYSQL_USER'] = 'MowgliG'
app.config['MYSQL_PASSWORD'] = 'Josuedavid01'
app.config['MYSQL_DB'] = 'TIENDA'

# configuracion
app.secret_key = "server-ca.pem"

print("Conectado a la Base de Datos")

# rutas


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login',)
def login():

    return render_template('inicio/login.html')


@app.route('/signup')
def signup():
    return render_template('inicio/signup.html')


@app.route('/ccsignup')
def ccsignup():
    return render_template('inicio/ccsignup.html')


@app.route('/password')
def password():
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
