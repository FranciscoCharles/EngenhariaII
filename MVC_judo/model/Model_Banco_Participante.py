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
		self.criar_tabela()
	#get's'
	def get_caminho(self):
		return self.Model_Banco_Participante__caminho_banco
	#set's
	def set_caminho(self, caminho):
		self.Model_Banco_Participante__caminho_banco = caminho
	#metodos de gerenciamento de banco
	def criar_tabela(self):
		# criando a tabela (schema)
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			resultado = self.cursor.execute("""
				CREATE TABLE IF NOT EXISTS participante (
					inscricao INTEGER AUTOINCREMENT,
					nome VARCHAR(100) NOT NULL,
					academia VARCHAR(120) NOT NULL,
					nascimento VARCHAR(10) NOT NULL,
					endereco VARCHAR(100) NOT NULL,
					cpf VARCHAR(20) NOT NULL,
					tipo VARCHAR(20) NOT NULL,
					sexo VARCHAR(10) NOT NULL,
					graduacao VARCHAR(20) NOT NULL,
					telefone VARCHAR(12) NOT NULL,
					PRIMARY KEY (inscricao)
				);
			""")
			self.conecao.close()
			if resultado is not None:
				return True
		except sqlite3.Error :
			pass
		return False
	def conta_participantes(self):
		pass
	def salvar_participante(self):
		try:
			if not self.este_participante_existe():
				self.conecao = sqlite3.connect(self.get_caminho())
				self.cursor = self.conecao.cursor()
				resultado = self.cursor.execute("INSERT INTO participante (nome,academia,nascimento,endereco,cpf,tipo,sexo,graduacao,telefone) VALUES (?,?,?,?,?,?,?,?,?)",(self.get_nome(),self.get_academia(),self.get_nascimento(),self.get_endereco(),self.get_cpf(),self.get_tipo(),self.get_sexo(),self.get_graduacao(),self.get_telefone(),))
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
				saida += str(linha)+"\n"
			self.conecao.close()
			return saida
		except sqlite3.Error :
			pass
	def remover_participante(self):	
		try:
			if self.este_participante_existe():
				self.conecao = sqlite3.connect(self.get_caminho())
				self.cursor = self.conecao.cursor()
				# excluindo um registro da tabela
				saida = self.cursor.execute("DELETE FROM participante WHERE (nome=?) AND (academia=?) AND (inscricao=?)", (self.get_nome(),self.get_academia(),self.get_inscricao(),))
				self.conecao.commit()
				self.conecao.close()
				if saida is not None:
					return True
		except sqlite3.Error :
			pass
		return False
	def buscar_participante_por_inscricao(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			saida = self.cursor.execute("SELECT * FROM participante WHERE (id=?)", (self.get_inscricao(),))
			saida = self.cursor.fetchone()
			self.conecao.close();
			return saida
		except sqlite3.Error :
			pass
	def buscar_participante_por_cpf(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			saida = self.cursor.execute("SELECT * FROM participante WHERE (cpf=?) AND (academia=?)", (self.get_cpf(),self.get_academia(),))
			saida = self.cursor.fetchone()
			self.conecao.close();
			return saida
		except sqlite3.Error :
			pass
	def buscar_participante_por_nome(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			saida = self.cursor.execute("SELECT * FROM participante WHERE (nome=?) AND (academia=?)", (self.get_nome(),self.get_academia(),))
			saida = self.cursor.fetchone()
			self.conecao.close();
			return saida
		except sqlite3.Error :
			pass
	def get_participante(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			saida = self.cursor.execute("SELECT * FROM participante WHERE (academia=?) AND (cpf=?)", (self.get_academia(),self.get_cpf(),))
			saida = self.cursor.fetchone()
			self.conecao.close();
			if saida is not None:
				P = Model_Participante()
				P.set_inscricao(saida[0])
				P.set_nome(saida[1])
				P.set_academia(saida[2])
				P.set_nascimento(saida[3])
				P.set_endereco(saida[4])
				P.set_cpf(saida[5])
				P.set_tipo(saida[6])
				P.set_graduacao(saida[7])
				P.set_telefone(saida[8])
				return P
			else:
				return None
		except sqlite3.Error :
			pass
	def este_participante_existe(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			saida = self.cursor.execute("SELECT * FROM participante WHERE (nome=?) AND (academia=?) AND (cpf=?)", (self.get_nome(),self.get_academia(),self.get_cpf(),))
			saida = saida.fetchone()
			self.conecao.close();
			if saida is not None:
				return True
		except sqlite3.Error :
			pass
		return False
		
if __name__== '__main__':
	P = Model_Banco_Participante()
	print(P.criar_tabela())
	P.set_nome("Boi")
	P.set_academia("Cobra")
	P.set_nascimento("13/10/2019")
	P.set_graduacao("preta")
	P.set_cpf("666668")
	P.set_tipo("Aluno")
	P.set_endereco("rua dos bobos")
	P.set_telefone("(89)9999999")
	
	
	print(P.este_participante_existe())
	print("salvou "+str(P.salvar_participante()))
	#P.remover_participante()
	print(P.listar_participante())