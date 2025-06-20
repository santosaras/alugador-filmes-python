import mysql.connector

# estabelecendo conexao com banco de dados
conexao = mysql.connector.connect(host= '127.0.0.1',
                                  database = 'locadora',
                                  user = 'root',
                                  password = '')