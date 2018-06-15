#modulo de Controller_Boleto
import sys
import sqlite3
sys.path.append('../')

from model.Model_Banco_Boleto import*

class Controller_Boleto(Model_Banco_Boleto):
	
	def __init__(self):
		super().__init__()
		self.criar_tabela()
	#metodos de validacao
	def valida_dia(self, dia):
		if dia<1 or dia>31:
			return False
		return True
	def valida_mes(self, mes):
		if mes<1 or mes>12:
			return False
		return True
	def valida_ano(self, ano):
		if ano<1700:
			return False
		return True
	def valida_dia_mes(self):
		if (not self.data_vazia()) and (len(self.get_data())==10):
			data = self.get_data().split("/")
			dia = int(data[0])
			mes = int(data[1])
			ano = int(data[2])
			if self.valida_dia(dia):
				if self.valida_mes(mes):
					if self.valida_ano(ano):
						if (mes == 2) and ((dia<1) or (dia>29)) :
							return False
						return True
		return False
	def nome_tem_caracteres_especiais(self):
		if self.nome_vazio():
			return False
		especiais = ".,<>;:?/\\!'\"¹²³£¢¬#$%%¨&´`§*()ç_~^+-=[]{}ªº°|@"
		nome = self.get_nome()
		for caractere in especiais:
			if nome.count(caractere) > 0:
				return True
		return False
	def inscricao_vazia(self):
		if (self.get_inscricao() == None) or (len(self.get_inscricao()) == 0):
			return True
	def nome_vazio(self):
		if (self.get_nome() == None) or (len(self.get_nome()) == 0):
			return True
		return False
	def data_vazia(self):
		if (self.get_data() == None) or (len(self.get_data()) == 0):
			return True
		return False
	def academia_vazia(self):
		if (self.get_academia() == None) or (len(self.get_academia()) == 0):
			return True
		return False
	def torneio_vazio(self):
		if (self.get_torneio() == None) or (len(self.get_torneio()) == 0):
			return True
		return False
	def status_vazio(self):
		if (self.get_status() == None) or (len(self.get_status()) == 0):
			return True
		return False
	def status_valido(self):
		if not self.status_vazio():
			if (self.get_status().upper() == "FALSE") or (self.get_status().upper() == "TRUE"):
				return True
		return False
	def valor_vazio(self):
		if (self.get_valor() == None) or (len(self.get_valor()) == 0):
			return True
		return False
	def valor_valido(self):
		try:
			if (self.get_valor() == None):
				return False
			float(self.get_valor())
		except ValueError:
			return False
		return True
	def dados_validos(self):
		if not self.valor_vazio():
			if self.valor_valido():
				if not self.nome_vazio():
					if not self.nome_tem_caracteres_especiais():
						if not self.inscricao_vazia():
							if not self.academia_vazia():
								if not self.torneio_vazio():
									if not self.status_vazio():
										if self.status_valido():
											if not self.data_vazia():
												if self.valida_dia_mes():
													return True
		return False
	def salvar_boleto(self):
		if self.dados_validos():
			return super().salvar_boleto()
		return False
	def remover_boleto(self):
		if self.dados_validos():
			return super().remover_boleto()
		return False
		
if __name__== '__main__':
	B = Controller_Boleto()
	B.set_nome("boi")
	B.set_inscricao("1")
	B.set_academia("boi")
	B.set_torneio("boi")
	B.set_status("true")
	B.set_valor("1")
	B.set_data("20/02/2010")
	print(B.dados_validos())
	print(B.este_boleto_existe())
	print(B.salvar_boleto())
	B.gerar_boletos(B.listar_boleto())
	#print(B.remover_boleto())
	