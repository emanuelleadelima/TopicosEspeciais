import sqlite3

conn = sqlite3.connect('shallownowschool.db')

cursor = conn.cursor()

newname = 'João da Silva'
newaddress = 'Rua da Palha'
newbirth = '1977-06-15'
newregistration = '201713710022'

cursor.execute("""
    UPDATE tb_student
    SET name=?, address=?, birth=?, registration=?
    WHERE id=3
""", (newname, newaddress, newbirth, newregistration))

conn.commit()

print('values updated successfully')

conn.close()
