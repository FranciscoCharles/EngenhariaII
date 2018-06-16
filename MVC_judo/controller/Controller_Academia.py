#modulo de Controller_Academia
import sys
import sqlite3
sys.path.append('../')

from model.Model_Banco_Academia import*

class Controller_Academia(Model_Banco_Academia):
	
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
	def responsavel_tem_caracteres_especiais(self):
		if self.responsavel_vazio():
			return False
		especiais = ".,<>;:?/\\!'\"¹²³£¢¬#$%%¨&´`§*()ç_~^+-=[]{}ªº°|@"
		responsavel = self.get_responsavel()
		for caractere in especiais:
			if responsavel.count(caractere) > 0:
				return True
		return False
	def nome_vazio(self):
		if (self.get_nome() == None) or (len(self.get_nome()) == 0):
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
	def email_vazio(self):
		if (self.get_email() == None) or (len(self.get_email()) == 0):
			return True
		return False
	def responsavel_vazio(self):
		if (self.get_responsavel() == None) or (len(self.get_responsavel()) == 0):
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
	def id_valido(self):
		try:
			if (self.get_id() == None):
				return False
			int(self.get_id())
		except ValueError:
			return False
		return True
	def contato_valido(self):
		if (self.contato_vazio()) or (len(self.get_contato()) < 9 ) or (len(self.get_contato()) > 12 ):
			return False
		return True
	def dados_validos(self):
		if self.data_valida():
			if self.email_valido():
				if self.contato_valido():
					if not self.responsavel_vazio():
						if not self.local_vazio():
							if not self.nome_vazio():
								return True
		return False
	def email_possui_arroba(self):
		if self.get_email().count("@")!=1:
			return False
		return True
	def email_possui_ponto_com(self):
		if self.get_email().count(".com")!=1 :
				return False
		return True
	def email_valido(self):
		if not self.email_vazio():
			if self.email_possui_arroba():
				if self.email_possui_ponto_com():
					especiais = ".,<>;:?/\\!'\"¹²³£¢¬#$%%¨&´`§*()ç_~^+-=[]{}ªº°|"
					arroba = self.get_email().find("@")
					if arroba == 0:
						return False
					lado1 = self.get_email()[0:arroba]
					com = self.get_email().find(".com")
					resto_email = self.get_email()[com+4:len(self.get_email())]
					if len(resto_email)!=0:
						return False
					if com == (arroba+1):
						return False
					lado2 = self.get_email()[arroba+1:com]
					for letra in especiais:
						if lado1.count(letra)!=0 or lado2.count(letra)!=0:
							return False
					return True
		return False
		
	def salvar_academia(self):
		if self.dados_validos():
			return super().salvar_academia()
		return False
	def remover_academia(self):
		if self.dados_validos():
			return super().remover_academia()
		return False
		
if __name__== '__main__':
	C = Controller_Academia()
	C.criar_tabela()
	C.set_nome("cobra")
	C.set_data("10/07/1990")
	C.set_local("Picos-PI")
	C.set_contato("(89)2412344")
	C.set_responsavel("Manoel")
	C.set_email("menu@hotmail.com")
	print(C.dados_validos())
	print(C.salvar_academia())
	print(C.buscar_academia())