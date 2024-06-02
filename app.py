from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.exc import ProgrammingError


# Creamos la aplicación:
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'RELLENAR'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)

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
    return render_template('consultas.html', attributes=attributes,
                            conditions=where, table=table, result=result)
        

# Ejecutamos la aplicación:
if __name__ == '__main__':
    app.run(debug=False, port=8070)