#modulo de Model_Banco_Academia
import sqlite3
import sys
sys.path.append("../")
from model.Model_Academia import*

class Model_Banco_Academia(Model_Academia):
	
	__caminho_banco = None
	
	def __init__(self):
		super().__init__()
		self.set_caminho("C:\\Users\\Charles\\Desktop\\aulas\\Engenharia\\MVC_judo\\banco\\banco_dados.db")
	#get's'
	def get_caminho(self):
		return self.Model_Banco_Academia__caminho_banco
	#set's
	def set_caminho(self, caminho):
		self.Model_Banco_Academia__caminho_banco = caminho
	#metodos de gerenciamento de banco
	def criar_tabela(self):
		# criando a tabela (schema)
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			resultado = self.cursor.execute("""
				CREATE TABLE IF NOT EXISTS academia (
					nome VARCHAR(100) NOT NULL,
					data VARCHAR(10) NOT NULL,
					local VARCHAR(10) NOT NULL,
					contato VARCHAR(12) NOT NULL,
					email TEXT NOT NULL,
					responsavel VARCHAR(10) NOT NULL,
					PRIMARY KEY(nome),
					FOREIGN KEY (nome) REFERENCES participante(academia)
				);
			""")
			self.conecao.close()
			if resultado is not None:
				return True
		except sqlite3.Error :
			pass
		return False
	def salvar_academia(self):
		try:
			if not self.esta_academia_existe():
				self.conecao = sqlite3.connect(self.get_caminho())
				self.cursor = self.conecao.cursor()
				resultado = self.cursor.execute("INSERT INTO academia (nome,data,local,contato,email,responsavel) VALUES (?,?,?,?,?,?)",(self.get_nome(),self.get_data(),self.get_local(),self.get_contato(),self.get_email(),self.get_responsavel(),))
				self.conecao.commit()
				self.conecao.close()
				if resultado is not None:
					return True
		except sqlite3.Error :
			pass
		return False
	def listar_academia(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			self.cursor.execute("SELECT * FROM academia;")
			texto = self.cursor.fetchall()
			for linha in texto:
				#texto+= str(linha[0])+"\n"
				print(linha)
			self.conecao.close()
			return texto
		except sqlite3.Error :
			pass
	def remover_academia(self):	
		try:
			if self.esta_academia_existe():
				self.conecao = sqlite3.connect(self.get_caminho())
				self.cursor = self.conecao.cursor()
				# excluindo um registro da tabela
				saida = self.cursor.execute("DELETE FROM academia WHERE (nome=?)", (self.get_nome(),))
				self.conecao.commit()
				self.conecao.close()
				if saida is not None:
					return True
		except sqlite3.Error :
			pass
		return False
	def buscar_academia(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			saida = self.cursor.execute("SELECT * FROM academia WHERE (nome=?)",(self.get_nome(),))
			saida = self.cursor.fetchone()
			self.conecao.close();
			return saida
		except sqlite3.Error :
			pass
	def esta_academia_existe(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			saida = self.cursor.execute("SELECT * FROM academia WHERE (nome=?)",(self.get_nome(),))
			saida = saida.fetchone()
			self.conecao.close();
			if saida is not None:
				return True
		except sqlite3.Error :
			pass
		return False
if __name__== '__main__':

	A = Model_Banco_Academia()
	A.criar_tabela()
	A.set_nome("cobra")
	A.set_data("10/07/1990")
	A.set_local("Picos-PI")
	A.set_contato("(89)2412344")
	A.set_email("ttt@hotmail.com")
	A.set_responsavel("Manoel")
	print(A.salvar_academia())
	#print(A.remover_academia())
	print(A.buscar_academia())