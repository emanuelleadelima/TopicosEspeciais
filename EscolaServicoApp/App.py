from flask import Flask, request, jsonify
from flask_json_schema import JsonSchema, JsonValidationError
import sqlite3
import logging

app = Flask(__name__)

formatter = logging.Formatter("%(asctime)s - %(le
velname)s - %(message)s")
handler = logging.FileHandler("escolaapp.log")
handler.setFormatter(formatter)

logger = app.logger
logger.addHandler(handler)
logger.setLevel(logging.INFO)

#Validação
schema = JsonSchema()
schema.init_app(app)

escola_schema = {}

aluno_schema = {
    'required': ['nome', 'matricula', 'cpf', 'nascimento'],
    'properties': {
        'nome': {'type': 'string'},
        'matricula': {'type': 'string'},
        'cpf': {'type': 'string'},
        'nascimento': {'type': 'string'}
    }
}

curso_schema = {}

turma_schema = {}

disciplina_schema = {}

databaseName = 'IFPB.db'

@app.route("/escolas", methods=['GET'])
def getEscolas():
    logger.info("Listando escolas")

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM tb_escola;
        """)

        escolas = []
        for linha in cursor.fetchall():
            escola = {
                "id_escola":linha[0],
                "nome":linha[1],
                "logradouro":linha[2],
                "cidade":linha[3]
            }
            escolas.append(escola)

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(escolas)

@app.route("/escolas/<int:id>", methods=['GET'])
def getEscolasByID(id):
    logger.info("Listando escola pelo ID: %s" %(id))

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_escola
            WHERE id_escola = ?;
        """, (id, ))

        linha = cursor.fetchone()
        escola = {
            "id_escola":linha[0],
            "nome":linha[1],
            "logradouro":linha[2],
            "cidade":linha[3]
        }

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(escola)

@app.route("/escola", methods=['POST'])
def setEscola():
    logger.info('Cadastrando a escola')

    try:
        escola = request.get_json()
        nome = escola["nome"]
        print(nome)
        logradouro = escola["logradouro"]
        print(logradouro)
        cidade = escola["cidade"]
        print(cidade)

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_escola(nome, logradouro, cidade)
            VALUES(?, ?, ?);
        """, (nome, logradouro, cidade))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        escola['id'] = id

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(escola)

@app.route("/escola/<int:id>", methods=['PUT'])
def updateEscola(id):
    logger.info('Atualizando a escola')

    try:
        escola = request.get_json()
        nome = escola['nome']
        print(nome)
        logradouro = escola['logradouro']
        print(logradouro)
        cidade = escola['cidade']
        print(cidade)

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_escola
            WHERE id_escola = ?;
            """, (id,))

        tab = cursor.fetchone()

        if (tab is not None):
            cursor.execute("""
                UPDATE tb_escola
                SET nome=?, logradouro=?, cidade=?
                """ (nome,logradouro, cidade, id))
            conn.commit()
        else:
            print ("Escolher o recurso '/escola' :)")

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(escola)

@app.route("/alunos", methods=['GET'])
def getAlunos():
    logger.info("Listando os alunos")

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_aluno;
        """)

        alunos = []
        for linha in cursor.fetchall():
            aluno = {
                "id_aluno":linha[0],
                "nome":linha[1],
                "matricula":linha[2],
                "cpf":linha[3],
                "nascimento":linha[4]
            }
            alunos.append(aluno)

        conn.close()
    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(alunos)

@app.route("/alunos/<int:id>", methods=['GET'])
def getAlunosByID(id):
    logger.info("Listando o aluno pelo ID: %s" %(id))

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_aluno
            WHERE id_aluno = ?;
        """,(id, ))

        linha = cursor.fecthone()
        aluno = {
            "id_aluno":linha[0],
            "nome":linha[1],
            "matricula":linha[2],
            "cpf":linha[3],
            "nascimento":linha[4]
        }

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(aluno)

@app.route("/aluno", methods=['POST'])
@schema.validate(aluno_schema)
def setAluno():
    logger.info('Cadastrando o aluno')

    try:
        #Recuperando o JSON
        aluno = request.get_json()
        nome = aluno["nome"]
        print(nome)
        matricula = aluno["matricula"]
        print(matricula)
        cpf = aluno["cpf"]
        print(cpf)
        nascimento = aluno["nascimento"]
        print(nascimento)

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_aluno(nome, matricula, cpf, nascimento)
            VALUES(?, ?, ?, ?);
        """, (nome, matricula, cpf, nascimento))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        aluno['id'] = id

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(aluno)

@app.route("/aluno/<int:id>", methods=['PUT'])
def updateAluno(id):
    logger.info('Atualizando o aluno')

    try:
        aluno = request.get_json()
        nome = aluno['nome']
        print(nome)
        matricula = aluno['matricula']
        print(matricula)
        cpf = aluno['cpf']
        print(cpf)
        nascimento = aluno['nascimento']
        print(nascimento)

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_aluno
            WHERE id_aluno = ?;
            """, (id,))

        tab = cursor.fetchone()

        if (tab is not None):
            cursor.execute("""
                UPDATE tb_aluno
                SET nome=?, matricula=?, cpf=?,nascimento=?
                WHERE id_aluno = ?
                """, (nome, matricula, cpf, nascimento,id))
            conn.commit()
        else:
            print ("Escolher o recurso '/aluno' :)")

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(aluno)

@app.route("/cursos", methods=['GET'])
def getCursos():
    logger.info("Listando os cursos")

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_curso;
        """)

        cursos = []
        for linha in cursor.fetchall():
            curso = {
                "id_curso":linha[0],
                "nome":linha[1],
                "turno":linha[2]
            }
            cursos.append(curso)

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(cursos)

@app.route("/cursos/<int:id>", methods=['GET'])
def getCursosByID(id):
    logger.info("Listando o curso pelo id: %s" %(id))

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_curso
            WHERE id_curso = ?;
        """, (id, ))

        linha = cursor.fecthone()
        curso = {
            "id_curso":linha[0],
            "nome":linha[1],
            "turno":linha[2]
        }

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(curso)

@app.route("/curso", methods=['POST'])
def setCurso():
    logger.info('Cadastrando o curso')

    try:
        curso = request.get_json()
        nome = curso["nome"]
        print(nome)
        turno = curso["turno"]
        print(turno)

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_curso(nome, turno)
            VALUES(?, ?);
        """, (nome, turno))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        curso['id'] = id

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(curso)

@app.route("/curso/<int:id>", methods=['PUT'])
def updateCurso(id):
    logger.info("Atualizando o curso")

    try:
        curso = request.get_json()
        nome = curso['nome']
        print(nome)
        turno = curso['turno']
        print(turno)

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_curso
            WHERE id_curso = ?;
            """, (id,))

        tab = cursor.fetchone()

        if (tab is not None):
            cursor.execute("""
                UPDATE tb_curso
                SET nome=?, turno=?
                WHERE id_curso = ?
                """, (nome, turno, id))
            conn.commit()
        else:
            print ("Escolher o recurso '/curso' :)")

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(curso)

@app.route("/turmas", methods=['GET'])
def getTurmas():
    logger.info("Listando as turmas")

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_turma;
        """)

        turmas = []
        for linha in cursor.fetchall():
            turma = {
                "id_turma":linha[0],
                "nome":linha[1],
                "curso":linha[2]
            }
            turmas.append(turma)

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(turmas)

@app.route("/turmas/<int:id>", methods=['GET'])
def getTurmasByID(id):
    logger.info("Listando a turma pelo ID: %s" %(id))

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_turma
            WHERE id_turma = ?
        """, (id, ))

        linha = cursor.fetchone()
        turma = {
            "id_turma":linha[0],
            "nome":linha[1],
            "curso":linha[2]
        }

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(turma)

@app.route("/turma", methods=['POST'])
def setTurma():
    logger.info('Cadastrando a turma')

    try:
        turma = request.get_json()
        nome = turma["nome"]
        print(nome)
        curso = turma["curso"]
        print(curso)

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_turma(nome, curso)
            VALUES(?, ?);
        """, (nome, curso))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        turma["id"] = id

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(turma)

@app.route("/turma/<int:id>", methods=['PUT'])
def updateTurma(id):
    logger.info("Atualizando a turma")

    try:
        turma = request.get_json()
        nome = turma['nome']
        print(nome)
        curso = turma['curso']
        print(curso)

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_turma
            WHERE id_turma = ?;
            """, (id,))

        tab = cursor.fetchone()

        if (tab is not None):
            cursor.execute("""
                UPDATE tb_turma
                SET nome=?, curso=?
                WHERE id_disciplina = ?
                """, (nome,curso, id))
            conn.commit()
        else:
            print ("Escolher o recurso '/turma' :)")

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(turma)

@app.route("/disciplinas", methods=['GET'])
def getDisciplinas():
    logger.info("Listando as disciplinas")

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_disciplina;
        """)

        disciplinas = []
        for linha in cursor.fetchall():
            disciplina = {
                "id_disciplina":linha[0],
                "nome":linha[1]
            }
            disciplinas.append(disciplina)

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(disciplinas)

@app.route("/disciplinas/<int:id>", methods=['GET'])
def getDisciplinasByID(id):
    logger.info("Listando a disciplina pelo id: %s" %(id))

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_disciplina
            WHERE id_disciplina = ?
        """, (id, ))

        linha = cursor.fetchone()
        disciplina = {
            "id_disciplina":linha[0],
            "nome":linha[1]
        }

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(disciplina)

@app.route("/disciplina", methods=['POST'])
def setDisciplina():
    logger.info('Cadastrando a disciplina')

    try:
        disciplina = request.get_json()
        nome = disciplina["nome"]
        print(nome)

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_disciplina(nome)
            VALUES(?);
        """, (nome, ))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        disciplina["id"] = id

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(disciplina)

@app.route("/disciplina/<int:id>", methods=['PUT'])
def updateDisciplina(id):
    logger.info("Atualizando a disciplina")

    try:
        disciplina = request.get_json()
        nome = disciplina['nome']
        print(nome)

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_disciplina
            WHERE id_disciplina = ?;
            """, (id,))

        tab = cursor.fetchone()
        if (tab is not None):
            cursor.execute("""
                UPDATE tb_disciplina
                SET nome=?
                WHERE id_disciplina = ?
                """, (nome, id))
            conn.commit()
        else:
            print ("Escolher o recurso '/disciplina' :)")

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(disciplina)

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
