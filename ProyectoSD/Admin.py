# importaciones de la libreria de Flask para la base de datos y web
from flask import Flask, render_template
from flask_mysqldb import MySQL

# inicializacion
app = Flask(__name__ , static_url_path='/assets')

# conexion a base de datos
app.config['MYSQL_HOST'] = '35.235.106.218'
app.config['MYSQL_USER'] = 'MowgliG'
app.config['MYSQL_PASSWORD'] = 'Josuedavid01'
app.config['MYSQL_DB'] = 'TIENDA'
mysql = MySQL(app)

# configuracion
app.secret_key = "server-ca.pem"

print("Conectado a la Base de Datos")

# rutas
@app.route('/', methods= ['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/ccsignup')
def ccsignup():
    return render_template('ccsignup.html')

@app.route('/h404')
def h404():
    return render_template('h404.html')

@app.route('/h401')
def h401():
    return render_template('h401.html')

@app.route('/h500')
def h500():
    return render_template('h500.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/password')
def password():
    return render_template('password.html')


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


if __name__ == '__main__':
    app.run(debug=True)
