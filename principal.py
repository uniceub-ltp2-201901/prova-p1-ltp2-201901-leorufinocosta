from flask import Flask, request, render_template
from flaskext.mysql import MySQL
from bd import *

app = Flask(__name__)
mysql = MySQL()
mysql.init_app(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'faculdade'

@app.route('/')
def prin():
    #cursor = mysql.get_db().cursor()
    return render_template('principal.html')

@app.route('/listarprofessores')
def listarprofessores():
    cursor = mysql.get_db().cursor()
    return render_template('listarprof.html', detalhar=listar_professores(cursor))

@app.route('/exibirprofessor/<prof>')
def exibirprofessor(prof):
    cursor = mysql.get_db().cursor()
    return render_template('detalhes.html', professor= exibir_professor(cursor, nome=prof))

@app.route('/consultaportitulacao', methods=['GET', 'POST'])
def consultarportitulacao():
    if request.method == 'POST':
        parametro = request.form.get('parametro')

        cursor = mysql.get_db().cursor()

        titulacao = consultarTitulacao(cursor, parametro)

        if titulacao is None:
            return render_template('menu.html', erro='Valor incorreto')

        else:
            cursor = mysql.get_db().cursor()
            return render_template('consulta.html', consulta=consultarTitulacao(cursor, parametro))
    return

@app.route('/consultarapenascomputacao')
def consultacompu():
    cursor = mysql.get_db().cursor()
    return render_template('consultacomputacao.html', curso=consultarapenascomputacao(cursor))

if __name__ == '__main__':
    app.run(debug=True)