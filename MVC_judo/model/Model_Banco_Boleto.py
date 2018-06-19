#modulo de Model_Banco_Boleto
import sqlite3
import sys
sys.path.append("../")
from model.Model_Boleto import*

class Model_Banco_Boleto(Model_Boleto):
	
	__caminho_banco = None
	
	def __init__(self):
		super().__init__()
		self.set_caminho("C:\\Users\\Charles\\Desktop\\aulas\\Engenharia\\MVC_judo\\banco\\banco_dados.db")
		self.criar_tabela()
	#get's'
	def get_caminho(self):
		return self.Model_Banco_Boleto__caminho_banco
	#set's
	def set_caminho(self, caminho):
		self.Model_Banco_Boleto__caminho_banco = caminho
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
					academia VARCHAR(100) NOT NULL,
					torneio VARCHAR(100) NOT NULL,
					status VARCHAR(4) NOT NULL,
					data VARCHAR(13) NOT NULL,
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
	def gerar_boletos(self,lista_boleto):
		for objeto in lista_boleto:
			print("nome: "+str(objeto.get_nome()))
			print("academia: "+str(objeto.get_academia()))
			print("inscricao: "+str(objeto.get_inscricao()))
			print("torneio: "+str(objeto.get_torneio()))
			print("status: "+str(objeto.get_status()))
			print("data: "+str(objeto.get_data()))
			print("valor: "+str(objeto.get_valor()))
	def salvar_boleto(self):
		try:
			if not self.este_boleto_existe():
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
			self.cursor.execute("SELECT * FROM boleto ORDER BY inscricao;")
			texto = self.cursor.fetchall()
			saida = []
			for linha in texto:
				saida.append(linha)
			self.conecao.close()
			return lista
		except sqlite3.Error :
			pass
	def remover_boleto(self):	
		try:
			if self.este_boleto_existe():
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
	def buscar_boleto_nome_torneio(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			saida = self.cursor.execute("SELECT * FROM boleto WHERE (nome=?) AND (torneio=?)",(self.get_nome(),self.get_torneio(),))
			saida = self.cursor.fetchone()
			self.conecao.close();
			return saida
		except sqlite3.Error :
			pass
	def buscar_boleto_inscricao(self):
		try:
			self.conecao = sqlite3.connect(self.get_caminho())
			self.cursor = self.conecao.cursor()
			saida = self.cursor.execute("SELECT * FROM boleto WHERE (inscricao=?)",(self.get_inscricao(),))
			saida = self.cursor.fetchone()
			self.conecao.close();
			return saida
		except sqlite3.Error :
			pass
	def este_boleto_existe(self):
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

	A = Model_Banco_Boleto()