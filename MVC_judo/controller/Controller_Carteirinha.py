#modulo de Controller_Carteirinha
import sys
import sqlite3
sys.path.append('../')

from model.Model_Carteirinha import*

class Controller_Carteirinha(Model_Carteirinha):
	
	def __init__(self):
		super().__init__()
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
	def valida_dia_mes_nascimento(self):
		data = self.get_data_nascimento().split("/")
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
	def valida_dia_mes_data(self):
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
						return self.valida_dia_mes_data()
		return False
	def data_nascimento_valida(self):
		if not self.data_nascimento_vazia():
			if self.get_data_nascimento().count("/") == 2:
				data = self.get_data_nascimento().split("/")
				if len(data) == 3:
					if (len(data[0]) == 2) and (len(data[1]) == 2) and (len(data[2]) == 4):
						return self.valida_dia_mes_nascimento()
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
	
	def nome_vazio(self):
		if (self.get_nome() == None) or (len(self.get_nome()) == 0):
			return True
		return False
	def data_nascimento_vazia(self):
		if (self.get_data_nascimento() == None) or (len(self.get_data_nascimento()) == 0):
			return True
		return False
	def cpf_vazio(self):
		if (self.get_cpf() == None) or (len(self.get_cpf()) == 0):
			return True
		return False
	def data_vazia(self):
		if (self.get_data() == None) or (len(self.get_data()) == 0) :
			return True
		return False
	def academia_vazia(self):
		if (self.get_academia() == None) or (len(self.get_academia()) == 0):
			return True
		return False
	def graduacao_vazia(self):
		if (self.get_graduacao() == None) or (len(self.get_graduacao()) == 0):
			return True
		return False
	def inscricao_vazia(self):
		if (self.get_inscricao() == None) or (len(self.get_inscricao()) == 0):
			return True
		return False
	def tipo_vazio(self):
		if (self.get_tipo() == None) or (len(self.get_tipo()) == 0):
			return True
		return False
	def tipo_valido(self):
		tipos = ["ALUNO","PROFESSOR","INSTRUTOR"]
		if (self.get_tipo() != None) and (tipos.count(self.get_tipo().upper()) == 1):
			return True
		return False
	def dados_validos(self):
		if self.data_nascimento_valida():
			if not self.graduacao_vazia():
				if not self.tipo_vazio():
					if not self.data_vazia():
						if not self.data_nascimento_vazia():
							if not self.academia_vazia():
								if not self.cpf_vazio():
									if not self.inscricao_vazia():
										if not self.nome_vazio():
											return True
		return False
if __name__== '__main__':
	pass