#modulo de Controller_Participante_Torneio
import sys
import sqlite3
sys.path.append('../')

from model.Model_Banco_Participante_Torneio import*

class Controller_Participante_Torneio(Model_Banco_Participante_Torneio):
	
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
		data = self.get_nascimento().split("/")
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
	def data_nascimento_valida(self):
		if not self.nascimento_vazio():
			if self.get_nascimento().count("/") == 2:
				data = self.get_nascimento().split("/")
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
	
	def nome_vazio(self):
		if (self.get_nome() is None) or (len(self.get_nome()) == 0):
			return True
		return False
	def nascimento_vazio(self):
		if (self.get_nascimento() is None) or (len(self.get_nascimento()) == 0):
			return True
		return False
	def cpf_vazio(self):
		if (self.get_cpf() is None) or (len(self.get_cpf()) == 0):
			return True
		return False
	def telefone_vazio(self):
		if (self.get_telefone() is None) or (len(self.get_telefone()) == 0) :
			return True
		return False
	def academia_vazia(self):
		if (self.get_academia() is None) or (len(self.get_academia()) == 0):
			return True
		return False
	def graduacao_vazia(self):
		if (self.get_graduacao() is None) or (len(self.get_graduacao()) == 0):
			return True
		return False
	def tipo_vazio(self):
		if (self.get_tipo() is None) or (len(self.get_tipo()) == 0):
			return True
		return False
	def endereco_vazio(self):
		if (self.get_endereco() is None) or (len(self.get_endereco()) == 0):
			return True
		return False
	def torneio_vazio(self):
		if (self.get_torneio() is None) or (len(self.get_torneio()) == 0):
			return True
		return False
	def pago_vazio(self):
		if (self.get_pago() is None) or (len(self.get_pago()) == 0):
			return True
		return False
	def pago_valido(self):
		if (self.get_pago().upper() == "FALSE") or (self.get_pago().upper() == "TRUE"):
			return True
		return False
	def telefone_valido(self):
		if (self.telefone_vazio()) or (len(self.get_telefone()) < 9 ) or (len(self.get_telefone()) > 13 ) or ((self.get_telefone().count("(")>1) and (self.get_telefone().count(")")>1)):
			return False
		if (self.get_telefone().count("(")>=1 and self.get_telefone().count(")")==0) or ((self.get_telefone().count("(")==0) and (self.get_telefone().count(")")>=1)):
			return False
		return True
	def dados_validos(self):
		if self.data_nascimento_valida():
			if self.telefone_valido():
				if not self.graduacao_vazia():
					if not self.tipo_vazio():
						if not self.academia_vazia():
							if not self.endereco_vazio():
								if not self.cpf_vazio():
									if not self.nome_vazio():
										if not self.torneio_vazio():
											if not self.pago_vazio():
												return True
		return False
	def salvar_participante(self):
		if self.dados_validos():
			return super().salvar_participante()
		return False
	def remover_participante(self):
		if self.dados_validos():
			return super().remover_participante()
		return False
		
if __name__== '__main__':
	P = Controller_Participante_Torneio()
	P.criar_tabela()
	P.listar_participante()
	