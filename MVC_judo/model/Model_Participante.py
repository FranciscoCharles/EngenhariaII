#modulo de Model_Participante
import sys
sys.path.append("../model")

class Model_Participante(object):
	
	__nome = None
	__nascimento = None
	__cpf = None
	__graduacao = None
	__academia = None
	__telefone = None
	__tipo = None
	__inscricao = None
	__endereco = None
	
	def __init__(self):
		self.inicializacao_padrao()
		
	def inicializacao_padrao(self):
		self.set_nome(None)
		self.set_academia(None)
		self.set_cpf(None)
		self.set_graduacao(None)
		self.set_inscricao(None)
		self.set_nascimento(None)
		self.set_endereco(None)
		self.set_telefone(None)
		self.set_tipo(None)
		
	def get_nome(self):
		return self.Model_Participante__nome
	def get_nascimento(self):
		return self.Model_Participante__nascimento
	def get_cpf(self):
		return self.Model_Participante__cpf
	def get_graduacao(self):
		return self.Model__Participante__graduacao
	def get_tipo(self):
		return self.Model__Participante__tipo
	def get_telefone(self):
		return self.Model__Participante__telefone
	def get_academia(self):
		return self.Model__Participante__academia
	def get_inscricao(self):
		return self.Model__Participante__inscricao
	def get_endereco(self):
		return self.Model__Participante__endereco
	#set's
	def set_nome(self, nome):
		self.Model_Participante__nome = nome
	def set_nascimento(self, nascimento):
		self.Model_Participante__nascimento = nascimento
	def set_cpf(self, cpf):
		self.Model_Participante__cpf = cpf
	def set_graduacao(self, graduacao):
		self.Model__Participante__graduacao = graduacao
	def set_tipo(self, tipo):
		self.Model__Participante__tipo = tipo
	def set_telefone(self , telefone):
		self.Model__Participante__telefone = telefone
	def set_academia(self, academia):
		self.Model__Participante__academia = academia
	def set_endereco(self, endereco):
		self.Model__Participante__endereco = endereco
	def set_inscricao(self, inscricao):
		self.Model__Participante__inscricao = inscricao
	
if __name__== '__main__':
	pass