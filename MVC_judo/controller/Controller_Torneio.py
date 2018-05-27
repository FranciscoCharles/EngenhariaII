#modulo de Controller_Torneio
import sys
import sqlite3
sys.path.insert(0,'../')

from model.Model_Banco_Torneio import*

class Controller_Torneio(Model_Banco_Torneio):
	
	def __init__(self):
		super().__init__()
		self.criar_tabela()
	#metodos de validacao
	def valida_valor(self):
		if not self.valor_vazio():
			if self.get_valor().count(",")==1:
				return True
		return False
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
	def data_valida(self):
		if not self.data_vazia():
			if self.get_data().count("/") == 2:
				data = self.get_data().split("/")
				if len(data) == 3:
					if (len(data[0]) == 2) and (len(data[1]) == 2) and (len(data[2]) == 4):
						return self.valida_dia_mes()
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
	def organizador_tem_caracteres_especiais(self):
		if self.organizador_vazio():
			return False
		especiais = ".,<>;:?/\\!'\"¹²³£¢¬#$%%¨&´`§*()ç_~^+-=[]{}ªº°|@"
		organizador = self.get_organizador()
		for caractere in especiais:
			if organizador.count(caractere) > 0:
				return True
		return False
	def nome_vazio(self):
		if (self.get_nome() is None) or (len(self.get_nome()) == 0):
			return True
		return False
	def data_vazia(self):
		if (self.get_data() is None) or (len(self.get_data()) == 0):
			return True
		return False
	def contato_vazio(self):
		if (self.get_contato() is None) or (len(self.get_contato()) == 0) :
			return True
		return False
	def valor_vazio(self):
		if (self.get_valor() is None) or (len(self.get_valor()) == 0):
			return True
		return False
	def organizador_vazio(self):
		if (self.get_organizador() is None) or (len(self.get_organizador()) == 0):
			return True
		return False
	def local_vazio(self):
		if (self.get_local() is None) or (len(self.get_local()) == 0):
			return True
		return False
	def contato_valido(self):
		if (self.contato_vazio()) or (len(self.get_contato()) < 9 ) or (len(self.get_contato()) > 12 ):
			return False
		return True
	def dados_validos(self):
		if self.data_valida():
			if contato_valido():
				if not self.organizador_vazio():
					if not self.local_vazio():
						if not self.nome_vazio():
							return True
		return False
	def salvar_torneio(self):
		if self.dados_validos():
			return super().salvar_torneio()
		return False
	def remover_torneio(self):
		if self.dados_validos():
			return super().remover_torneio()
		return False
		
if __name__== '__main__':
	C = Controller_Torneio()
	C.criar_tabela()
	