#modulo de Model_Banco_Participante
import sys
import sqlite3
sys.path.append('../')

from model.Model_Participante import*

class Model_Banco_Participante(Model_Participante):
	
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
				CREATE TABLE IF NOT EXISTS participante (
					nome VARCHAR(100) NOT NULL,
					academia VARCHAR(120) NOT NULL,
					nascimento VARCHAR(10) NOT NULL,
					endereco VARCHAR(100) NOT NULL,
					cpf VARCHAR(20) NOT NULL,
					tipo VARCHAR(20) NOT NULL,
					graduacao VARCHAR(20) NOT NULL,
					telefone VARCHAR(12) NOT NULL,
					PRIMARY KEY(nome)
				);
			""")
			self.conecao.close()
			if resultado is not None:
				return True
		except sqlite3.Error :
			pass
		return False
	def salvar_participante(self):
		try:
			if not self.esta_participante_existe():
				self.conecao = sqlite3.connect(self.get_caminho())
				self.cursor = self.conecao.cursor()
				resultado = self.cursor.execute("INSERT INTO participante (nome,academia,nascimento,endereco,cpf,tipo,graduacao,telefone) VALUES (?,?,?,?,?,?,?,?)",(self.get_nome(),self.get_academia(),self.get_nascimento(),self.get_endereco(),self.get_cpf(),self.get_tipo(),self.get_graduacao(),self.get_telefone(),))
				self.conecao.commit()
				self.conecao.close()
				if resultado is not None:
					return True
		except sqlite3.Error :
			pass
		return False
	def listar_participante(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			self.cursor.execute("SELECT * FROM participante;")
			texto = self.cursor.fetchall()
			saida = ""
			for linha in texto:
				#texto+= str(linha[0])+"\n"
				print(linha)
			self.conecao.close()
			return saida
		except sqlite3.Error :
			pass
	def remover_participante(self):	
		try:
			if self.este_secretario_existe():
				self.conecao = sqlite3.connect(self.get_caminho())
				self.cursor = self.conecao.cursor()
				# excluindo um registro da tabela
				saida = self.cursor.execute("DELETE FROM participante WHERE (nome=?) AND (academia=?)", (self.get_nome(),self.get_academia(),))
				self.conecao.commit()
				self.conecao.close()
				if saida is not None:
					return True
		except sqlite3.Error :
			pass
		return False
	def buscar_participante(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			saida = self.cursor.execute("SELECT * FROM participante WHERE (nome=?)(nome=?) AND (academia=?)", (self.get_nome(),self.get_academia(),))
			saida = self.cursor.fetchone()
			self.conecao.close();
			return saida
		except sqlite3.Error :
			pass
	def esta_participante_existe(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			saida = self.cursor.execute("SELECT * FROM participante WHERE (nome=?) AND (academia=?)", (self.get_nome(),self.get_academia(),))
			saida = saida.fetchone()
			self.conecao.close();
			if saida is not None:
				return True
		except sqlite3.Error :
			pass
		return False
if __name__== '__main__':
	P = Model_Banco_Participante()
	P.criar_tabela()
	
	P.set_nome("sei la")
	P.set_academia("Cobra")
	P.set_nascimento("13/10/2019")
	P.set_graduacao("preta")
	P.set_cpf("368599010")
	P.set_tipo("Aluno")
	P.set_endereco("rua dos bobos")
	P.set_telefone("(89)99999999")
	
	print(P.esta_participante_existe())
	print(P.salvar_participante())
	P.listar_participante()