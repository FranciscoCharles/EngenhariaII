#banco de dados de academia
import sqlite3
	
class BancoAcademia(object):
	def __init__(self):
		pass
	def criar_tabela(self):
		# criando a tabela (schema)
		try:
			self.conecao = sqlite3.connect('BancoDados\\banco_dados.db')
			self.cursor = self.conecao.cursor()
			self.cursor.execute("""
				CREATE TABLE IF NOT EXISTS academia (
					nome VARCHAR(100) NOT NULL,
					data VARCHAR(10) NOT NULL,
					PRIMARY KEY(nome),
					FOREIGN KEY (nome) REFERENCES integrantes(nome_academia)
			);""")
		except sqlite3.Error :
			print('Erro na Tabela Integrantes.')
	def inserir_dados(self):
		self.nome = input("insira nome Academia: ")
		self.data = input("insira data: ")
		print("dados inseridos com sucesso")
	def inserir_academia(self):
		try:
			self.conecao = sqlite3.connect('BancoDados\\banco_dados.db')
			self.cursor = self.conecao.cursor()
			self.cursor.execute("""
				INSERT INTO academia (nome,data)
				VALUES (?,?)
			""",(self.nome,self.data))
			self.conecao.commit()
			print('Dados inseridos com sucesso.')
		except sqlite3.Error:
			print('Ocorreu um erro.')
			
		self.conecao.close()
	def listar_academias(self):
		try:
			self.conecao = sqlite3.connect('BancoDados\\banco_dados.db')
			self.cursor = self.conecao.cursor()
			self.cursor.execute("""
				SELECT * FROM academia;
			""")
			texto = ""
			for linha in self.cursor.fetchall():
				texto+="academia: "+str(linha[0])+"\n"
			self.conecao.close()
			return texto
		except sqlite3.Error:
			print('Ocorreu um erro.')
		return ""
	def buscar_academia(self,nome):
		try:
			self.conecao = sqlite3.connect("BancoDados\\banco_dados.db")
			self.cursor = self.conecao.cursor()
			saida = self.cursor.execute("SELECT * FROM academia WHERE (nome=?)",[nome])
			saida = saida.fetchone()
			self.conecao.close();
			return saida
		except sqlite3.Error:
			print('Ocorreu um erro.')
		return ""
	def remover_academia(self,nome):
		try:
			self.conecao = sqlite3.connect("BancoDados\\banco_dados.db")
			self.cursor = self.conecao.cursor()
			self.cursor.execute("DELETE FROM academia WHERE nome=?",[nome])
			self.conecao.commit()
			self.conecao.close();
		except sqlite3.Error:
			print('Ocorreu um erro.')
	def validar_academia(self):
		pass
if __name__ == '__main__':
	banco = BancoAcademia()
	banco.criar_tabela()
	banco.inserir_dados()
	banco.inserir_academia()
	print(banco.remover_academia("NewAcademy"))
	print(banco.listar_academias())