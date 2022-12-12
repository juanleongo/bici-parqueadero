import sqlite3

def conexion():
	conn = sqlite3.connect("parqueaderoDB.db")
	print("todo ok")
	return conn
	



