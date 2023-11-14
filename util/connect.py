import mysql.connector

from mysql.connector import errorcode

try:
    db_connection = mysql.connector.connect(host='localhost', user='leonardo', password='q1w2e3r4t5',
                                            database='DB_EMPRESA')
    print("Conexão com Banco de Dados realizada!")
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print('O banco de dados não existe')
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Usuário e/ou senha estão incorretos')
    else:
        print(error)
else:
    db_connection.close()
