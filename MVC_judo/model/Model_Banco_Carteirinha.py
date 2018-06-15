#modulo de Model_Banco_Carteirinha
import sqlite3
import sys
sys.path.append("../")
from model.Model_Carteirinha import*

class Model_Banco_Carteirinha(Model_Carteirinha):
	
	__caminho_banco = None
	
	def __init__(self):
		super().__init__()
		self.set_caminho("C:\\Users\\Charles\\Desktop\\aulas\\Engenharia\\MVC_judo\\banco\\banco_dados.db")
		self.criar_tabela()
	#get's'
	def get_caminho(self):
		return self.Model_Banco_Carteirinha__caminho_banco
	#set's
	def set_caminho(self, caminho):
		self.Model_Banco_Carteirinha__caminho_banco = caminho
	#metodos de gerenciamento de banco
	def criar_tabela(self):
		# criando a tabela (schema)
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			resultado = self.cursor.execute("""
				CREATE TABLE IF NOT EXISTS boleto (
					nome VARCHAR(100) NOT NULL,
					inscricao  INTEGER NOT NULL,
					academia VARCHAR(100) NOT NULL,,
					data VARCHAR(13) NOT NULL,
					data_nascimento VARCHAR(13) NOT NULL,
					valor VARCHAR(20) NOT NULL,
					PRIMARY KEY (inscricao),
					FOREIGN KEY (inscricao) REFERENCES participante_torneio(inscricao)
				);
			""")
			self.conecao.close()
			if resultado is not None:
				return True
		except sqlite3.Error :
			pass
		return False
	def salvar_boleto(self):
		try:
			if not self.esta_boleto_existe():
				self.conecao = sqlite3.connect(self.get_caminho())
				self.cursor = self.conecao.cursor()
				resultado = self.cursor.execute("INSERT INTO boleto (nome,inscricao,academia,torneio,status,data,valor) VALUES (?,?,?,?,?,?,?)",(self.get_nome(),self.get_inscricao(),self.get_academia(),self.get_torneio(),self.get_status(),self.get_data(),self.get_valor(),))
				self.conecao.commit()
				self.conecao.close()
				if resultado is not None:
					return True
		except sqlite3.Error :
			pass
		return False
	def listar_boleto(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			self.cursor.execute("SELECT * FROM boleto BY ORDER inscricao")
			texto = self.cursor.fetchall()
			saida = ""
			for linha in texto:
				saida += str(linha[1])+"\n"
			self.conecao.close()
			return saida
		except sqlite3.Error :
			pass
	def remover_boleto(self):	
		try:
			if self.esta_boleto_existe():
				self.conecao = sqlite3.connect(self.get_caminho())
				self.cursor = self.conecao.cursor()
				# excluindo um registro da tabela
				saida = self.cursor.execute("DELETE FROM boleto WHERE (inscricao=?)", (self.get_inscricao(),))
				self.conecao.commit()
				self.conecao.close()
				if saida is not None:
					return True
		except sqlite3.Error :
			pass
		return False
	def buscar_boleto_nome(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			saida = self.cursor.execute("SELECT * FROM boleto WHERE (inscricao=?)",(self.get_nome(),))
			saida = self.cursor.fetchone()
			self.conecao.close();
			return saida
		except sqlite3.Error :
			pass
	def buscar_boleto_id(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			saida = self.cursor.execute("SELECT * FROM boleto WHERE (inscricao=?)",(self.get_inscricao(),))
			saida = self.cursor.fetchone()
			self.conecao.close();
			return saida
		except sqlite3.Error :
			pass
	def esta_boleto_existe(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			saida = self.cursor.execute("SELECT * FROM boleto WHERE (inscricao=?)",(self.get_inscricao(),))
			saida = saida.fetchone()
			self.conecao.close();
			if saida is not None:
				return True
		except sqlite3.Error :
			pass
		return False
if __name__== '__main__':

	A = Model_Banco_Carteirinha()
	print(A.salvar_boleto())
	#print(A.remover_boleto())
	print(A.buscar_boleto_nome())