#modulo de Controller_Torneio
import sys
import sqlite3
sys.path.append('../')
from model.Model_Banco_Torneio import*

class Controller_Torneio(Model_Banco_Torneio):
	
	def __init__(self):
		super().__init__()
		self.criar_tabela()
		
	#metodos de validacao
	def hora_valida(self, hora):
		if hora<0 or hora>24:
			return False
		return True
	def minutos_valido(self, minutos):
		if minutos<0 or minutos>59:
			return False
		return True
	def separa_horario(self):
		if (not self.horario_vazio()) and (not self.horario_possui_caractere_invalido()):
			if self.get_horario().find(":") == 2:
				horario = self.get_horario().split(":")
				hora = int(horario[0])
				minutos = int(horario[1])
				if self.hora_valida(hora) and self.minutos_valido(minutos):
					return True
		return False
	def horario_possui_caractere_invalido(self):
		invalidos = "\\|,.;?/°]º}[ª{+=§_-)(*!¹²³£¢¬@#%$¨&'\""
		for caractere in invalidos:
			if self.get_horario().count(caractere)!=0:
				return True
		return False
	def horario_esta_no_padrao(self):
		if (not self.horario_vazio()) and (not self.horario_possui_caractere_invalido()):
			if self.get_horario().count(":") == 1:
				if len(self.get_horario()) == 5:
					return self.separa_horario()
		return False
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
		if (self.get_nome() == None) or (len(self.get_nome()) == 0):
			return True
		return False
	def horario_vazio(self):
		if (self.get_horario() == None) or (len(self.get_horario()) == 0):
			return True
		return False
	def data_vazia(self):
		if (self.get_data() == None) or (len(self.get_data()) == 0):
			return True
		return False
	def contato_vazio(self):
		if (self.get_contato() == None) or (len(self.get_contato()) == 0) :
			return True
		return False
	def valor_vazio(self):
		if (self.get_valor() == None) or (len(self.get_valor()) == 0):
			return True
		return False
	def organizador_vazio(self):
		if (self.get_organizador() == None) or (len(self.get_organizador()) == 0):
			return True
		return False
	def local_vazio(self):
		if (self.get_local() == None) or (len(self.get_local()) == 0):
			return True
		return False
	def id_vazio(self):
		if (self.get_id() == None) or (len(self.get_id()) == 0):
			return True
		return False
	def contato_valido(self):
		if (self.contato_vazio()) or (len(self.get_contato()) < 9 ) or (len(self.get_contato()) > 13 ):
			return False
		return True
	def dados_validos(self):
		if self.data_valida():
			if self.contato_valido():
				if not self.organizador_vazio():
					if not self.local_vazio():
						if not self.nome_vazio():
							if self.horario_esta_no_padrao():
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
	T = Controller_Torneio()
	print(T.criar_tabela())
	T.set_data("13/12/2019")
	T.set_horario("02:45")
	T.set_nome("Teste")
	T.set_valor("3,44")
	T.set_local("Picos")
	T.set_organizador("pipoca")
	T.set_contato("(089)10101101")
	print(T.salvar_torneio())
	T.listar_torneio()