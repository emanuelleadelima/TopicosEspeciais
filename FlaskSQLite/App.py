from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/alunos", methods=['GET'])
def getAlunos():
    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_student;
    """)

    for linha in cursor.fetchall():
        print(linha)

    conn.close()

    return("Executado!", 200)

@app.route("/alunos/<int:id>", methods=['GET'])
def getAlunosByID(id):
    pass

@app.route("/aluno", methods=['POST'])
def setAluno():
    print('Cadastrando o aluno')
    nome = request.form["nome"]
    print(nome)
    nascimento = request.form["nascimento"]
    print(nascimento)
    matricula = request.form["matricula"]
    print(matricula)
    cpf = request.form["cpf"]
    print(cpf)
    return ('Cadastrado com sucesso', 200)

    conn = sqlite3.connect('escola.db')
    cursor = conn.cursor()
    cursor.execute("""
        insert into tb_aluno(id_aluno, nome, matricula, cpf, nascimento)
        values(1, ?, ?, ?, ?);
    """, (nome, matricula, cpf, nascimento))

    conn.commit()
    conn.close()

@app.route("/cursos", methods=['GET'])
def getCursos():
    pass

@app.route("/cursos/<int:id>", methods=['GET'])
def getCursosByID():
    pass

@app.route("/turmas", methods=['GET'])
def getTurmas():
    pass

@app.route("/turmas/<int:id>", methods=['GET'])
def getTurmasByID():
    pass

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
