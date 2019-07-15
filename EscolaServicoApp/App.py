from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/escolas", methods=['GET'])
def getEscolas():
    conn = sqlite3.connect('IFPB.db')
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

    return jsonify(escolas)

@app.route("/escolas/<int:id>", methods=['GET'])
def getEscolasByID(id):
    conn = sqlite3.connect('IFPB.db')
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

    return jsonify(escola)

@app.route("/escola", methods=['POST'])
def setEscola():
    print('Cadastrando a escola')
    escola = request.get_json()
    nome = escola["nome"]
    print(nome)
    logradouro = escola["logradouro"]
    print(logradouro)
    cidade = escola["cidade"]
    print(cidade)

    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tb_escola(nome, logradouro, cidade)
        VALUES(?, ?, ?);
    """, (nome, logradouro, cidade))

    conn.commit()
    conn.close()

    id = cursor.lastrowid
    escola['id'] = id

    return jsonify(escola)

@app.route("/escola/<int:id>", methods=['PUT'])
def updateEscola(id):
    print ('Atualizando a escola')
    escola = request.get_json()
    nome = escola['nome']
    print(nome)
    logradouro = escola['logradouro']
    print(logradouro)
    cidade = escola['cidade']
    print(cidade)

    conn = sqlite3.connect(database)
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

    return jsonify(escola)

@app.route("/alunos", methods=['GET'])
def getAlunos():
    conn = sqlite3.connect('IFPB.db')
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

    return jsonify(alunos)

@app.route("/alunos/<int:id>", methods=['GET'])
def getAlunosByID(id):
    conn = sqlite3.connect('IFPB.db')
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

    return jsonify(aluno)

@app.route("/aluno", methods=['POST'])
def setAluno():
    print('Cadastrando o aluno')
    aluno = request.get_json()
    nome = aluno["nome"]
    print(nome)
    matricula = aluno["matricula"]
    print(matricula)
    cpf = aluno["cpf"]
    print(cpf)
    nascimento = aluno["nascimento"]
    print(nascimento)

    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tb_aluno(nome, matricula, cpf, nascimento)
        VALUES(?, ?, ?, ?);
    """, (nome, matricula, cpf, nascimento))

    conn.commit()
    conn.close()

    id = cursor.lastrowid
    aluno['id'] = id

    return jsonify(aluno)

@app.route("/aluno/<int:id>", methods=['PUT'])
def updateAluno(id):
    print ('Atualizando o aluno')
    aluno = request.get_json()
    nome = aluno['nome']
    print(nome)
    matricula = aluno['matricula']
    print(matricula)
    cpf = aluno['cpf']
    print(cpf)
    nascimento = aluno['nascimento']
    print(nascimento)

    conn = sqlite3.connect(database)
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

    return jsonify(aluno)

@app.route("/cursos", methods=['GET'])
def getCursos():
    conn = sqlite3.connect('IFPB.db')
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

    return jsonify(cursos)

@app.route("/cursos/<int:id>", methods=['GET'])
def getCursosByID(id):
    conn = sqlite3.connect('IFPB.db')
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

    return jsonify(curso)

@app.route("/curso", methods=['POST'])
def setCurso():
    print('Cadastrando o curso')
    curso = request.get_json()
    nome = curso["nome"]
    print(nome)
    turno = curso["turno"]
    print(turno)

    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tb_curso(nome, turno)
        VALUES(?, ?);
    """, (nome, turno))

    conn.commit()
    conn.close()

    id = cursor.lastrowid
    curso['id'] = id

    return jsonify(curso)

@app.route("/curso/<int:id>", methods=['PUT'])
def updateCurso(id):
    print ("Atualizando o curso")
    curso = request.get_json()
    nome = curso['nome']
    print(nome)
    turno = curso['turno']
    print(turno)

    conn = sqlite3.connect(database)
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

    return jsonify(curso)

@app.route("/turmas", methods=['GET'])
def getTurmas():
    conn = sqlite3.connect('IFPB.db')
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

    return jsonify(turmas)

@app.route("/turmas/<int:id>", methods=['GET'])
def getTurmasByID(id):
    conn = sqlite3.connect('IFPB.db')
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

    return jsonify(turma)

@app.route("/turma", methods=['POST'])
def setTurma():
    turma = request.get_json()
    print('Cadastrando a turma')
    nome = turma["nome"]
    print(nome)
    curso = turma["curso"]
    print(curso)

    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tb_turma(nome, curso)
        VALUES(?, ?);
    """, (nome, curso))

    conn.commit()
    conn.close()

    id = cursor.lastrowid
    turma["id"] = id

    return jsonify(turma)

@app.route("/turma/<int:id>", methods=['PUT'])
def updateTurma(id):
    print ("Atualizando a turma")
    turma = request.get_json()
    nome = turma['nome']
    print(nome)
    curso = turma['curso']
    print(curso)

    conn = sqlite3.connect(database)
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

    return jsonify(turma)

@app.route("/disciplinas", methods=['GET'])
def getDisciplinas():
    conn = sqlite3.connect('IFPB.db')
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

    return jsonify(disciplinas)

@app.route("/disciplinas/<int:id>", methods=['GET'])
def getDisciplinasByID(id):
    conn = sqlite3.connect('IFPB.db')
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

    return jsonify(disciplina)

@app.route("/disciplina", methods=['POST'])
def setDisciplina():
    print('Cadastrando a disciplina')
    disciplina = request.get_json()
    nome = disciplina["nome"]
    print(nome)

    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tb_disciplina(nome)
        VALUES(?);
    """, (nome, ))

    conn.commit()
    conn.close()

    id = cursor.lastrowid
    disciplina["id"] = id

    return jsonify(disciplina)

@app.route("/disciplina/<int:id>", methods=['PUT'])
def updateDisciplina(id):
    print ("Atualizando a disciplina")
    disciplina = request.get_json()
    nome = disciplina['nome']
    print(nome)

    conn = sqlite3.connect(database)
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

    return jsonify(disciplina)

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)

