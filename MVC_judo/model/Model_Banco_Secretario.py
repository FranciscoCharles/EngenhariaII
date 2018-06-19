#modulo de Model_Banco_Secretario
import sqlite3
import sys
sys.path.append("../")

from model.Model_Secretario import*

class Model_Banco_Secretario(Model_Secretario):
	
	__caminho_banco = None
	
	def __init__(self):
		super().__init__()
		self.set_caminho("C:\\Users\\Charles\\Desktop\\aulas\\Engenharia\\MVC_judo\\banco\\banco_dados.db")
		self.criar_tabela()
	#get's'
	def get_caminho(self):
		return self.Model_Banco_Secretario__caminho_banco
	#set's
	def set_caminho(self, caminho):
		self.Model_Banco_Secretario__caminho_banco = caminho
	#metodos de gerenciamento de banco
	def criar_tabela(self):
		# criando a tabela (schema)
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			resultado = self.cursor.execute("""
				CREATE TABLE IF NOT EXISTS secretario (
					login TEXT NOT NULL,
					senha TEXT NOT NULL
			);
			""")
			self.conecao.close()
			if resultado is not None:
				return True
		except sqlite3.Error :
			pass
		return False
	def salvar_secretario(self):
		try:
			if not self.este_secretario_existe():
				self.conecao = sqlite3.connect(self.get_caminho())
				self.cursor = self.conecao.cursor()
				resultado = self.cursor.execute("INSERT INTO secretario (login,senha) VALUES (?,?)",(self.get_login(),self.get_senha(),))
				self.conecao.commit()
				self.conecao.close()
				if resultado is not None:
					return True
		except sqlite3.Error :
			pass
		return False
	def listar_secretario(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			self.cursor.execute("SELECT * FROM secretario ORDER BY login")
			texto = self.cursor.fetchall()
			saida = []
			for linha in texto:
				saida.append(linha)
			self.conecao.close()
			return saida
		except sqlite3.Error :
			pass
	def remover_secretario(self):	
		try:
			if self.este_secretario_existe():
				self.conecao = sqlite3.connect(self.get_caminho())
				self.cursor = self.conecao.cursor()
				# excluindo um registro da tabela
				saida = self.cursor.execute("DELETE FROM secretario WHERE (login=?)", (self.get_login(),))
				self.conecao.commit()
				self.conecao.close()
				if saida is not None:
					return True
		except sqlite3.Error :
			pass
		return False
	def buscar_secretario(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			saida = self.cursor.execute("SELECT * FROM secretario WHERE (login=?)",(self.get_login(),))
			saida = self.cursor.fetchone()
			self.conecao.close();
			return saida
		except sqlite3.Error :
			pass
	def validar_secretario(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			saida = self.cursor.execute("SELECT * FROM secretario WHERE (login=?)AND(senha=?)",(self.get_login(),self.get_senha(),))
			saida = saida.fetchone()
			self.conecao.close();
			if saida is not None:
				return True
		except sqlite3.Error :
			pass
		return False
	def este_secretario_existe(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			saida = self.cursor.execute("SELECT * FROM secretario WHERE (login=?)",(self.get_login(),))
			saida = saida.fetchone()
			self.conecao.close();
			if saida is not None:
				return True
		except sqlite3.Error :
			pass
		return False
if __name__== '__main__':

	S = Model_Banco_Secretario()
	S.criar_tabela()
	S.set_login("admin")
	S.set_senha("1234")
	print(S.este_secretario_existe())
	print(S.salvar_secretario())
	#print(S.validar_secretario())
	print(S.listar_secretario())