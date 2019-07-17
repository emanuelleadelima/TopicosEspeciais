import sqlite3

conn = sqlite3.connect('EscolaServicoApp.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE tb_escola(
        id_escola INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL,
        logradouro VARCHAR(70) NOT NULL,
        cidade VARCHAR(45) NOT NULL
    );
""")

print('table "tb_escola" created successfully =)')

cursor.execute("""
    CREATE TABLE tb_aluno(
        id_aluno INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(45) NOT NULL,
        turno VARCHAR(1) NOT NULL
    );
""")

print('table "tb_aluno" created successfully =)')

cursor.execute("""
    CREATE TABLE tb_class(
        id_turma INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        fk_id_curso INTEGER
    );
""")

print('table "tb_class" created successfully =)')

conn.close()
