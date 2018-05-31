#modulo de Model_Banco_Torneio
import sqlite3
import sys
sys.path.append("../")

from model.Model_Torneio import*
"""
obter data do sistema

from datetime import datetime
now = datetime.now()
print now.year
print now.month
print now.day
print now.hour
print now.minute
print now.second

"""
class Model_Banco_Torneio(Model_Torneio):
	
	__caminho_banco = None
	
	def __init__(self):
		super().__init__()
		self.set_caminho("C:\\Users\\Charles\\Desktop\\aulas\\Engenharia\\MVC_judo\\banco\\banco_dados.db")
	#get's'
	def get_caminho(self):
		return self.Model_Banco_Torneio__caminho_banco
	#set's
	def set_caminho(self, caminho):
		self.Model_Banco_Torneio__caminho_banco = caminho
	#metodos de gerenciamento de banco
	def criar_tabela(self):
		# criando a tabela (schema)
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			resultado = self.cursor.execute("""
				CREATE TABLE IF NOT EXISTS torneio (
					id INT AUTO_INCREMENT DEFAULT 1,
					nome VARCHAR(100) NOT NULL,
					data VARCHAR(10) NOT NULL,
					local VARCHAR(10) NOT NULL,
					contato VARCHAR(12) NOT NULL,
					horario VARCHAR(7) NOT NULL,
					organizador VARCHAR(10) NOT NULL,
					PRIMARY KEY(nome),
					FOREIGN KEY (nome) REFERENCES participante_torneio(torneio)
					);
			""")
			self.conecao.close()
			if resultado is not None:
				return True
		except sqlite3.Error :
			pass
		return False
	def salvar_torneio(self):
		try:
			if not self.este_torneio_existe():
				self.conecao = sqlite3.connect(self.get_caminho())
				self.cursor = self.conecao.cursor()
				resultado = self.cursor.execute("INSERT INTO torneio (nome,data,local,horario,contato,organizador) VALUES (?,?,?,?,?,?)",(self.get_nome(),self.get_data(),self.get_local(),self.get_horario(),self.get_contato(),self.get_organizador(),))
				self.conecao.commit()
				self.conecao.close()
				if resultado is not None:
					return True
		except sqlite3.Error :
			pass
		return False
	def listar_torneio(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			self.cursor.execute("SELECT * FROM torneio;")
			texto = self.cursor.fetchall()
			saida = ""
			for linha in texto:
				saida += str(linha[1])+"\n"
			self.conecao.close()
			return saida
		except sqlite3.Error :
			pass
	def remover_torneio_nome(self):	
		try:
			if self.este_secretario_existe():
				self.conecao = sqlite3.connect(self.get_caminho())
				self.cursor = self.conecao.cursor()
				# excluindo um registro da tabela
				saida = self.cursor.execute("DELETE FROM torneio WHERE (nome=?)", (self.get_nome(),))
				self.conecao.commit()
				self.conecao.close()
				if saida is not None:
					return True
		except sqlite3.Error :
			pass
		return False
	def remover_torneio_id(self):	
		try:
			if self.este_secretario_existe():
				self.conecao = sqlite3.connect(self.get_caminho())
				self.cursor = self.conecao.cursor()
				# excluindo um registro da tabela
				saida = self.cursor.execute("DELETE FROM torneio WHERE (id=?)", (self.get_id(),))
				self.conecao.commit()
				self.conecao.close()
				if saida is not None:
					return True
		except sqlite3.Error :
			pass
		return False
	def buscar_torneio_nome(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			saida = self.cursor.execute("SELECT * FROM torneio WHERE (nome=?)",(self.get_nome(),))
			saida = self.cursor.fetchone()
			self.conecao.close();
			return saida
		except sqlite3.Error :
			pass
	def buscar_torneio_id(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			saida = self.cursor.execute("SELECT * FROM torneio WHERE (id=?)",(self.get_id(),))
			saida = self.cursor.fetchone()
			self.conecao.close();
			return saida
		except sqlite3.Error :
			pass
	def este_torneio_existe(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			saida = self.cursor.execute("SELECT * FROM torneio WHERE (nome=?)",(self.get_nome(),))
			saida = saida.fetchone()
			self.conecao.close();
			if saida is not None:
				return True
		except sqlite3.Error :
			pass
		return False
if __name__== '__main__':
	A = Model_Banco_Torneio()