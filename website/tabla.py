import sqlite3


conexion = sqlite3.connect('database.db')
cursor = conexion.cursor()
sentenciaSQL = cursor.execute("SELECT email FROM user")
tabla_email_user = cursor.fetchall()
for tupl_email_user in tabla_email_user:
    for email_user in tupl_email_user:
        print(email_user)
conexion = sqlite3.connect('database.db')
cursor = conexion.cursor()
sentenciaSQL = cursor.execute('SELECT * FROM user')
todos_clientes = cursor.fetchall()
cliente_lista = []
for x in todos_clientes:
    pass

