import mysql.connector

self = 'self'
class ConexaoMySQL:

    def __init__(self, conexao):
        self.conexao = conexao


    def conexao(self):
        conexao = mysql.connector.connect(
                host='localhost', 
                database='crudapp', 
                user='root', 
                password='')
        return conexao

