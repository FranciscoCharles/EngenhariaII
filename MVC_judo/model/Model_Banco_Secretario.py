#modulo de Model_Banco_Secretario
import sqlite3
from model.Model_Secretario import*

class Model_Banco_Secretario(Model_Secretario):
	
	__caminho_banco = None
	
	def __init__(self):
		super().__init__()
		self.set_caminho("C:\\Users\\Charles\\Desktop\\aulas\\Engenharia\\MVC_judo\\banco\\banco_dados.db")
	#get's'
	def get_caminho(self):
		return self.Model_Banco_Secretario__caminho
	#set's
	def set_caminho(self, caminho):
		self.Model_Banco_Secretario__caminho = caminho
	#metodos de gerenciamento de banco
	def criar_tabela(self):
		# criando a tabela (schema)
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			self.cursor.execute("CREATE TABLE IF NOT EXISTS secretario (login TEXT NOT NULL,senha TEXT NOT NULL);")
			print("Tabela criada com sucesso.")
			self.conecao.close()
		except sqlite3.Error :
			pass
	def salvar_secretario(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			self.cursor.execute("INSERT INTO secretario (login,senha) VALUES (?,?)",(self.get_login(),self.get_senha()))
			self.conecao.commit()
			print("Dados inseridos com sucesso.")
			self.conecao.close()
		except sqlite3.Error :
			pass
	def listar_secretario(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			self.cursor.execute("SELECT * FROM secretario;")
			texto = ""
			for linha in self.cursor.fetchall():
				#texto+= str(linha[0])+"\n"
				print(linha)
			self.conecao.close()
			return texto
		except sqlite3.Error :
			pass
	def remover_secretario(self):	
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			# excluindo um registro da tabela
			self.cursor.execute("DELETE FROM secretario WHERE login = ?", (self.get_login,))
			saida = self.cursor.fetchall()
			self.conecao.commit()
			print("Registro excluido com sucesso.")
			self.conecao.close()
			return True
		except sqlite3.Error :
			pass
	def buscar_secretario(self,login):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			saida = self.cursor.execute("SELECT * FROM secretario WHERE (login=?)",(login))
			saida = self.cursor.fetchall()
			self.conecao.close();
			return saida
		except sqlite3.Error :
			pass
	def validar_secretario(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			saida = self.cursor.execute("SELECT * FROM secretario WHERE (login=?)AND(senha=?)",(self.get_login(),self.get_senha()))
			saida = saida.fetchone()
			self.conecao.close();
			return saida
		except sqlite3.Error :
			pass
if __name__== '__main__':
	
	S = Model_Banco_Secretario()
	S.listar_secretario()
	