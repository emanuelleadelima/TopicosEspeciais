import sqlite3

conn = sqlite3.connect('escola.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE tb_aluno(
        id_aluno INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL,
        matricula VARCHAR(12) NOT NULL,
        cpf VARCHAR(11) NOT NULL,
        nascimento DATE NOT NULL
    );
""")

print('table "tb_student" created successfully =)')

cursor.execute("""
    CREATE TABLE tb_course(
        id_curso INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL,
        turno VARCHAR(1) NOT NULL
    );
""")

print('table "tb_course" created successfully =)')

cursor.execute("""
    CREATE TABLE tb_class(
        id_turma INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        fk_id_curso INTEGER
    );
""")

print('table "tb_class" created successfully =)')

conn.close()
