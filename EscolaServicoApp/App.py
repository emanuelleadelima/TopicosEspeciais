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

endereco_schema = {
    'required': ['logradouro', 'complemento',  'bairro', 'cep', 'numero'],
    'properties': {
        'logradouro': {'type': 'string'},
        'complemento': {'type': 'string'},
        'bairro': {'type': 'string'},
        'cep': {'type': 'string'},
        'numero': {'type': 'integer'}
    }
}

escola_schema = {
    'required': ['nome', 'fk_id_endereco', 'fk_id_campus'],
    'properties': {
        'nome': {'type': 'string'},
        'fk_id_endereco': {'type': 'integer'},
        'fk_id_campus': {'type': 'integer'}
    }
}

aluno_schema = {
    'required': ['nome', 'matricula', 'cpf', 'nascimento', 'fk_id_endereco', 'fk_id_curso'],
    'properties': {
        'nome': {'type': 'string'},
        'matricula': {'type': 'string'},
        'cpf': {'type': 'string'},
        'nascimento': {'type': 'string'},
        'fk_id_endereco': {'type': 'integer'},
        'fk_id_curso': {'type': 'integer'}
    }
}

professor_schema = {
    'required': ['nome', 'fk_id_endereco'],
    'properties': {
        'nome': {'type': 'string'},
        'fk_id_endereco': {'type': 'integer'},
    }
}

disciplina_schema = {
    'required': ['nome', 'fk_id_professor'],
    'properties': {
        'nome': {'type': 'string'},
        'fk_id_professor': {'type': 'integer'}
    }
}

curso_schema = {
    'required': ['nome','fk_id_turno'],
    'properties': {
        'nome': {'type': 'string'},
        'fk_id_turno': {'type': 'integer'}
    }
}

campus_schema = {
    'required': ['sigla','cidade'],
    'properties': {
        'sigla': {'type': 'string'},
        'cidade': {'type': 'string'}
}

turma_schema = {
    'required': ['nome','curso'],
    'properties': {
        'nome': {'type': 'string'},
        'fk_id_curso': {'type': 'integer'}
    }
}

turno_schema = {
    'required': ['nome'],
    'properties': {
        'nome': {'type': 'string'}
    }
}

databaseName = 'EscolaApp_versao2.db'

#getEnderecos
@app.route("/enderecos", methods=['GET'])
def getEnderecos():
    logger.info("Listando endereços")

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM tb_endereco;
        """)

        enderecos = []
        for linha in cursor.fetchall():
            endereco = {
                "idtb_endereco":linha[0],
                "logradouro":linha[1],
                "complemento":linha[2],
                "bairro":linha[3],
                "cep":linha[4],
                "numero":linha[5]
            }
            enderecos.append(endereco)

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(enderecos)

#getEnderecosByID
@app.route("/enderecos/<int:id>", methods=['GET'])
def getEnderecosByID(id):
    logger.info("Listando endereço pelo ID: %s" %(id))

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_endereco
            WHERE idtb_endereco = ?;
        """, (id, ))

        linha = cursor.fetchone()
        endereco = {
            "idtb_endereco":linha[0],
            "logradouro":linha[1],
            "complemento":linha[2],
            "bairro":linha[3],
            "cep":linha[4],
            "numero":linha[5]
        }

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(endereco)

#setEndereco
@app.route("/endereco", methods=['POST'])
@schema.validate(endereco_schema)
def setEndereco():
    logger.info('Cadastrando o endereco')

    try:
        endereco = request.get_json()
        logradouro = endereco["logradouro"]
        complemento = endereco["complemento"]
        bairro = endereco["bairro"]
        cep = endereco["cep"]
        numero = endereco["numero"]

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_endereco(logradouro, complemento, bairro, cep, numero)
            VALUES(?, ?, ?, ?, ?);
        """, (logradouro, complemento, bairro, cep, numero))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        endereco['id'] = id

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(endereco)

#updateEndereco
@app.route("/endereco/<int:id>", methods=['PUT'])
@schema.validate(endereco_schema)
def updateEndereco(id):
    logger.info('Atualizando o endereço')

    try:
        endereco = request.get_json()
        logradouro = endereco["logradouro"]
        complemento = endereco["complemento"]
        bairro = endereco["bairro"]
        cep = endereco["cep"]
        numero = endereco["numero"]

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_endereco
            WHERE idtb_endereco = ?;
            """, (id,))

        tab = cursor.fetchone()

        if (tab is not None):
            cursor.execute("""
                UPDATE tb_endereco
                SET logradouro=?, complemento=?, bairro=?, cep=?, numero=?
                """ (logradouro,complemento, bairro, cep, numero, id))
            conn.commit()
        else:
            print ("Escolher o recurso '/endereco' :)")

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(endereco)

#getEscolas
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
                "fk_id_endereco":linha[2],
                "fk_id_campus":linha[3]
            }
            escolas.append(escola)

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(escolas)

#getEscolasByID
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
            "fk_id_endereco":linha[2],
            "fk_id_campus":linha[3]
        }

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(escola)

#setEscola
@app.route("/escola", methods=['POST'])
@schema.validate(escola_schema)
def setEscola():
    logger.info('Cadastrando a escola')

    try:
        escola = request.get_json()
        nome = escola["nome"]
        fk_id_endereco = escola["fk_id_endereco"]
        fk_id_campus = escola["fk_id_campus"]

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_escola(nome, fk_id_endereco, fk_id_campus)
            VALUES(?, ?, ?);
        """, (nome, fk_id_endereco, fk_id_campus))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        escola['id'] = id

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(escola)

#updateEscola
@app.route("/escola/<int:id>", methods=['PUT'])
@schema.validate(escola_schema)
def updateEscola(id):
    logger.info('Atualizando a escola')

    try:
        escola = request.get_json()
        nome = escola["nome"]
        fk_id_endereco = escola["fk_id_endereco"]
        fk_id_campus = escola["fk_id_campus"]

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
                SET nome=?, fk_id_endereco=?, fk_id_campus=?
                """ (nome, fk_id_endereco, fk_id_campus, id))
            conn.commit()
        else:
            print ("Escolher o recurso '/escola' :)")

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(escola)

#getAlunos
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
                "nascimento":linha[4],
                "fk_id_endereco":linha[5],
                "fk_id_curso":linha[6]
            }
            alunos.append(aluno)

        conn.close()
    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(alunos)

#getAlunosByID
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
            "nascimento":linha[4],
            "fk_id_endereco":linha[5],
            "fk_id_curso":linha[6]
        }

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(aluno)

#setAluno
@app.route("/aluno", methods=['POST'])
@schema.validate(aluno_schema)
def setAluno():
    logger.info('Cadastrando o aluno')

    try:
        #Recuperando o JSON
        aluno = request.get_json()
        nome = aluno["nome"]
        matricula = aluno["matricula"]
        cpf = aluno["cpf"]
        nascimento = aluno["nascimento"]
        fk_id_endereco = aluno["fk_id_endereco"]
        fk_id_curso = aluno["fk_id_curso"]

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_aluno(nome, matricula, cpf, nascimento, fk_id_endereco, fk_id_curso)
            VALUES(?, ?, ?, ?);
        """, (nome, matricula, cpf, nascimento, fk_id_endereco, fk_id_curso))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        aluno['id'] = id

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(aluno)

#updateAluno
@app.route("/aluno/<int:id>", methods=['PUT'])
@schema.validate(aluno_schema)
def updateAluno(id):
    logger.info('Atualizando o aluno')

    try:
        aluno = request.get_json()
        nome = aluno["nome"]
        matricula = aluno["matricula"]
        cpf = aluno["cpf"]
        nascimento = aluno["nascimento"]
        fk_id_endereco = aluno["fk_id_endereco"]
        fk_id_curso = aluno["fk_id_curso"]

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
                SET nome=?, matricula=?, cpf=?,nascimento=?, fk_id_endereco=?, fk_id_curso=?
                WHERE id_aluno = ?
                """, (nome, matricula, cpf, nascimento, fk_id_endereco, fk_id_curso, id))
            conn.commit()
        else:
            print ("Escolher o recurso '/aluno' :)")

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(aluno)

#getProfessores
@app.route("/professores", methods=['GET'])
def getProfessores():
    logger.info("Listando os professores")

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_professor;
        """)

        professores = []
        for linha in cursor.fetchall():
            professor = {
                "id_professor":linha[0],
                "nome":linha[1],
                "fk_id_endereco":linha[2]
            }
            professores.append(professor)

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(disciplinas)

#getProfessoresByID
@app.route("/professores/<int:id>", methods=['GET'])
def getProfessoresByID(id):
    logger.info("Listando o professor pelo id: %s" %(id))

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_professor
            WHERE id_professor = ?
        """, (id, ))

        linha = cursor.fetchone()
        professor = {
            "id_professor":linha[0],
            "nome":linha[1],
            "fk_id_endereco":linha[2]
        }

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(professor)

#setProfessor
@app.route("/professor", methods=['POST'])
@schema.validate(professor_schema)
def setProfessor():
    logger.info('Cadastrando o professor')

    try:
        professor = request.get_json()
        nome = professor["nome"]
        fk_id_endereco = professor["fk_id_endereco"]

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_professor(nome, fk_id_endereco)
            VALUES(?, ?);
        """, (nome, fk_id_endereco))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        professor["id"] = id

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(professor)

#updateProfessor
@app.route("/professor/<int:id>", methods=['PUT'])
@schema.validate(professor_schema)
def updateProfessor(id):
    logger.info('Atualizando o professor')

    try:
        professor = request.get_json()
        nome = professor["nome"]
        fk_id_endereco = professor["fk_id_endereco"]

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_professor
            WHERE id_professor = ?;
            """, (id,))

        tab = cursor.fetchone()

        if (tab is not None):
            cursor.execute("""
                UPDATE tb_professor
                SET nome=?, fk_id_endereco=?
                WHERE id_professor= ?
                """, (nome, fk_id_endereco, id))
            conn.commit()
        else:
            print ("Escolher o recurso '/professor' :)")

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(professor)

#getDisciplinas
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
                "nome":linha[1],
                "fk_id_professor":linha[2]
            }
            disciplinas.append(disciplina)

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(disciplinas)

#getDisciplinasByID
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
            "nome":linha[1],
            "fk_id_professor":linha[2]
        }

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(disciplina)

#setDisciplina
@app.route("/disciplina", methods=['POST'])
@schema.validate(disciplina_schema)
def setDisciplina():
    logger.info('Cadastrando a disciplina')

    try:
        disciplina = request.get_json()
        nome = disciplina["nome"]
        fk_id_professor = disciplina["fk_id_professor"]
        print(nome)

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_disciplina(nome, fk_id_professor)
            VALUES(?, ?);
        """, (nome, fk_id_professor))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        disciplina["id"] = id

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(disciplina)

#updateDisciplina
@app.route("/disciplina/<int:id>", methods=['PUT'])
@schema.validate(disciplina_schema)
def updateDisciplina(id):
    logger.info("Atualizando a disciplina")

    try:
        disciplina = request.get_json()
        nome = disciplina['nome']
        fk_id_professor = disciplina['fk_id_professor']

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
                SET nome=?, fk_id_professor=?
                WHERE id_disciplina = ?
                """, (nome, fk_id_professor, id))
            conn.commit()
        else:
            print ("Escolher o recurso '/disciplina' :)")

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(disciplina)

#getCursos
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
                "fk_id_turno":linha[2]
            }
            cursos.append(curso)

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(cursos)

#getCursosByID
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
            "fk_id_turno":linha[2]
        }

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(curso)

#setCurso
@app.route("/curso", methods=['POST'])
@schema.validate(curso_schema)
def setCurso():
    logger.info('Cadastrando o curso')

    try:
        curso = request.get_json()
        nome = curso["nome"]
        fk_id_turno = curso["fk_id_turno"]

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_curso(nome, fk_id_turno)
            VALUES(?, ?);
        """, (nome, fk_id_turno))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        curso['id'] = id

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(curso)

#updateCurso
@app.route("/curso/<int:id>", methods=['PUT'])
@schema.validate(curso_schema)
def updateCurso(id):
    logger.info("Atualizando o curso")

    try:
        curso = request.get_json()
        nome = curso['nome']
        fk_id_turno = curso['fk_id_turno']

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
                SET nome=?, fk_id_turno=?
                WHERE id_curso = ?
                """, (nome, fk_id_turno, id))
            conn.commit()
        else:
            print ("Escolher o recurso '/curso' :)")

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(curso)

#getCampi
@app.route("/campi", methods=['GET'])
def getCampi():
    logger.info("Listando os campi")

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_campus;
        """)

        campi = []
        for linha in cursor.fetchall():
            campus = {
                "id_campus":linha[0],
                "sigla":linha[1],
                "cidade":linha[2]
            }
            campi.append(campus)

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(campi)

#getCampiByID
@app.route("/campi/<int:id>", methods=['GET'])
def getCampiByID(id):
    logger.info("Listando o campus pelo ID: %s" %(id))

    try:
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM tb_campus
            WHERE id_campus = ?
        """, (id, ))

        linha = cursor.fetchone()
        campus = {
            "id_campus":linha[0],
            "sigla":linha[1],
            "cidade":linha[2]
        }

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(campus)

#setCampus
#updateCampus

#getTurmas
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
                "fk_id_curso":linha[2]
            }
            turmas.append(turma)

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(turmas)

#getTurmasByID
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
            "fk_id_curso":linha[2]
        }

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(turma)

#setTurma
@app.route("/turma", methods=['POST'])
@schema.validate(turma_schema)
def setTurma():
    logger.info('Cadastrando a turma')

    try:
        turma = request.get_json()
        nome = turma["nome"]
        fk_id_curso = turma["curso"]

        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_turma(nome, fk_id_curso)
            VALUES(?, ?);
        """, (nome, fk_id_curso))

        conn.commit()
        conn.close()

        id = cursor.lastrowid
        turma["id"] = id

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(turma)

#updateTurma
@app.route("/turma/<int:id>", methods=['PUT'])
@schema.validate(turma_schema)
def updateTurma(id):
    logger.info("Atualizando a turma")

    try:
        turma = request.get_json()
        nome = turma['nome']
        fk_id_curso = turma['curso']

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
                SET nome=?, fk_id_curso=?
                WHERE id_disciplina = ?
                """, (nome,fk_id_curso, id))
            conn.commit()
        else:
            print ("Escolher o recurso '/turma' :)")

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(turma)

#getTurno
#getTurnosByID
#setTurno
#updateTurno

@app.errorhandler(JsonValidationError)
def validation_error(e):
    return jsonify({ 'error': e.message, 'errors': [validation_error.message for validation_error  in e.errors]})

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
