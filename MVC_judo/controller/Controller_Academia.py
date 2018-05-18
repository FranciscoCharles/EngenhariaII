#modulo de Controller_Academia
import sys
import sqlite3
sys.path.insert(0,'../')
from model import*
class Controller_Academia(object):
	
	__academia = None
	__banco = None
	
	def __init__(self, banco='C:\\Users\\Charles\\Desktop\\aulas\\Engenharia\\MVC_judo\\banco\\banco_dados.db'):
		self.set_banco(banco)
	def criar_tabela(self):
		try:
			self.conecao = sqlite3.connect(self.get_banco())
			self.cursor = self.conecao.cursor()
			self.cursor.execute("""
				CREATE TABLE IF NOT EXISTS academia (
					nome VARCHAR(100) NOT NULL,
					data VARCHAR(10) NOT NULL,
					local VARCHAR(100) NOT NULL,
					responsavel VARCHAR(10) NOT NULL,
					PRIMARY KEY(nome),
					FOREIGN KEY (nome) REFERENCES integrantes(nome_academia)
			);""")
		except sqlite3.Error :
			print('Erro na Tabela Academia.')
	def get_banco(self):
		return self.Controller_Academia__banco
	def set_academia(self, academia):
		self.Controller_Academia__academia = academia
	def set_banco(self, banco):
		self.Controller_Academia__banco = banco
	def salvar_dados_banco(self):
		pass
		
if __name__== '__main__':
	C = Controller_Academia()
	C.criar_tabela()