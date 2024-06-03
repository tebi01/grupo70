from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.exc import ProgrammingError
import psycopg2

# Creamos la aplicación:
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'RELLENAR'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)

# Conexión a la base de datos:
def connection():
    connect = psycopg2.connect(
        dbname = 'grupo70e2',
        user = 'grupo70',
        password = 'ramodemierda',
        host = 'localhost'
    )
    return connect

# Rutas:
# Home
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consultas_predefinidas')
def consultas_predefinidas():
    return render_template('consultas_predefinidas.html')



# Consultas:
@app.route('/consultas', methods=['GET', 'POST'])
def consultas():
    # Si el método es POST, se ejecuta la consulta
    if request.method == 'POST':
        table = request.form['table']
        attributes = request.form['attributes']
        where = request.form['where']

        # Definimos la consulta como:
        query = f"SELECT {attributes} FROM grupo70e2.{table}"

        if where:
            query += f" WHERE {where}" # Si hay un WHERE, se añade.
        
        # Ejecutamos la consulta:
        try:
            query = text(query)
            result = db.session.execute(query)
            result = [dict(row._mapping) for row in result]

        except ProgrammingError as e:
            result = ''
    else:
        attributes = ''
        where = ''
        table = ''
        result = ''
    return render_template('consultas.html', attributes=attributes,
                            conditions=where, table=table, result=result)
        
###############################################################################
##################### Consultas Predefinidas ##################################
###############################################################################

def consulta1(plate):
    con = connection()
    # Creamos el cursor:
    cur = con.cursor()
    # Creamos la consulta
    query_1 = f"RELLENAR"
    # Ejecutamos la consulta:
    cur.execute(query_1)
    # Obtenemos el resultado:
    results = cur.fetchall()
    # Cerramos la conexión:
    con.close()
    return results

###############################################################################
#####################       Consulta 1       ##################################
###############################################################################

@app.route('/1', methods=['POST'])
def q1():
    plate = request.form['plate']
    result = consulta1(plate.lower())
    if result:
        return render_template('consultas_predefinidas.html', result=result)
    else:
        return render_template('consultas_predefinidas.html', result='No se encontraron resultados')

###############################################################################
#####################       Consulta 2       ##################################
###############################################################################

def consulta2(mail):
    con = connection()
    # Creamos el cursor:
    cur = con.cursor()
    # Creamos la consulta
    query_2 = f"RELLENAR"
    # Ejecutamos la consulta:
    cur.execute(query_2)
    # Obtenemos el resultado:
    results = cur.fetchall()
    # Cerramos la conexión:
    con.close()
    return results

@app.route('/2', methods=['POST'])
def q2():
    mail = request.form['mail']
    result = consulta2(mail)
    return render_template('consultas_predefinidas.html', result=result)

###############################################################################
#####################       Consulta 3       ##################################
###############################################################################

def consulta3():
    con = connection()
    # Creamos el cursor:
    cur = con.cursor()
    # Creamos la consulta
    query_3 = f"RELLENAR"
    # Ejecutamos la consulta:
    cur.execute(query_3)
    # Obtenemos el resultado:
    results = cur.fetchall()
    # Cerramos la conexión:
    con.close()
    return results

@app.route('/3', methods=['POST'])
def q3():
    result = consulta3()
    return render_template('consultas_predefinidas.html', result=result)

###############################################################################
#####################       Consulta 4       ##################################
###############################################################################

def consulta4(style):
    con = connection()
    # Creamos el cursor:
    cur = con.cursor()
    # Creamos la consulta
    query_4 = f"RELLENAR"
    # Ejecutamos la consulta:
    cur.execute(query_4)
    # Obtenemos el resultado:
    results = cur.fetchall()
    # Cerramos la conexión:
    con.close()
    return results

@app.route('/4', methods=['POST'])
def q4():
    style = request.form['style']
    result = consulta4(style)
    return render_template('consultas_predefinidas.html', result=result)

###############################################################################
#####################       Consulta 5       ##################################
###############################################################################

def consulta5(style):
    con = connection()
    # Creamos el cursor:
    cur = con.cursor()
    # Creamos la consulta
    query_5 = f"RELLENAR"
    # Ejecutamos la consulta:
    cur.execute(query_5)
    # Obtenemos el resultado:
    results = cur.fetchall()
    # Cerramos la conexión:
    con.close()
    return results

@app.route('/5', methods=['POST'])
def q5():
    style = request.form['style'].lower()
    result = consulta5(style)
    return render_template('consultas_predefinidas.html', result=result)

###############################################################################
#####################       Consulta 6       ##################################
###############################################################################

def consulta6(mail):
    con = connection()
    # Creamos el cursor:
    cur = con.cursor()
    # Creamos la consulta
    query_6 = f"RELLENAR"
    # Ejecutamos la consulta:
    cur.execute(query_6)
    # Obtenemos el resultado:
    results = cur.fetchall()
    # Cerramos la conexión:
    con.close()
    return results

@app.route('/6', methods=['POST'])
def q6():
    mail = request.form['mail']
    result = consulta6(mail)
    return render_template('consultas_predefinidas.html', result=result)


###############################################################################
#####################       Consulta 7       ##################################
###############################################################################

def consulta7():
    con = connection()
    # Creamos el cursor:
    cur = con.cursor()
    # Creamos la consulta
    query_7 = f"RELLENAR"
    # Ejecutamos la consulta:
    cur.execute(query_7)
    # Obtenemos el resultado:
    results = cur.fetchall()
    # Cerramos la conexión:
    con.close()
    return results

@app.route('/7', methods=['POST'])
def q7():
    result = consulta7()
    return render_template('consultas_predefinidas.html', result=result)


###############################################################################
#####################       Consulta 8       ##################################
###############################################################################

def consulta8():
    con = connection()
    # Creamos el cursor:
    cur = con.cursor()
    # Creamos la consulta
    query_8 = f"RELLENAR"
    # Ejecutamos la consulta:
    cur.execute(query_8)
    # Obtenemos el resultado:
    results = cur.fetchall()
    # Cerramos la conexión:
    con.close()
    return results

@app.route('/8', methods=['POST'])
def q8():
    result = consulta8()
    return render_template('consultas_predefinidas.html', result=result)

###############################################################################
#####################       Consulta 9       ##################################
###############################################################################

def consulta9(calification):
    con = connection()
    # Creamos el cursor:
    cur = con.cursor()
    # Creamos la consulta
    query_9 = f"RELLENAR"
    # Ejecutamos la consulta:
    cur.execute(query_9)
    # Obtenemos el resultado:
    results = cur.fetchall()
    # Cerramos la conexión:
    con.close()
    return results

@app.route('/9', methods=['POST'])
def q9():
    calification = request.form['calification']
    result = consulta9(calification)
    return render_template('consultas_predefinidas.html', result=result)

###############################################################################
#####################       Consulta 10      ##################################
###############################################################################

def consulta10(alergeno):
    con = connection()
    # Creamos el cursor:
    cur = con.cursor()
    # Creamos la consulta
    query_10 = f"RELLENAR"
    # Ejecutamos la consulta:
    cur.execute(query_10)
    # Obtenemos el resultado:
    results = cur.fetchall()
    # Cerramos la conexión:
    con.close()
    return results

@app.route('/10', methods=['POST'])
def q10():
    alergeno = request.form['alergeno']
    result = consulta10(alergeno)
    return render_template('consultas_predefinidas.html', result=result)


# Ejecutamos la aplicación:
if __name__ == '__main__':
    app.run(debug=False, port=8070)