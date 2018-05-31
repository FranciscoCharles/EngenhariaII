#modulo de Model_Participante_Torneio
import sys
sys.path.append("../model")

class Model_Participante_Torneio(object):
	
	__nome = None
	__nascimento = None
	__cpf = None
	__graduacao = None
	__academia = None
	__telefone = None
	__tipo = None
	__inscricao = None
	__torneio = None
	__endereco = None
	__pago = False
	
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
		self.set_torneio(None)
		self.set_pago("False")
		
	def get_nome(self):
		return self.Model_Participante_Torneio__nome
	def get_nascimento(self):
		return self.Model_Participante_Torneio__nascimento
	def get_cpf(self):
		return self.Model_Participante_Torneio__cpf
	def get_graduacao(self):
		return self.Model_Participante_Torneio__graduacao
	def get_tipo(self):
		return self.Model_Participante_Torneio__tipo
	def get_telefone(self):
		return self.Model_Participante_Torneio__telefone
	def get_academia(self):
		return self.Model_Participante_Torneio__academia
	def get_inscricao(self):
		return self.Model_Participante_Torneio__inscricao
	def get_endereco(self):
		return self.Model_Participante_Torneio__endereco
	def get_torneio(self):
		return self.Model_Participante_Torneio__torneio
	def get_pago(self):
		return self.Model_Participante_Torneio__pago
	#set's
	def set_nome(self, nome):
		self.Model_Participante_Torneio__nome = nome
	def set_nascimento(self, nascimento):
		self.Model_Participante_Torneio__nascimento = nascimento
	def set_cpf(self, cpf):
		self.Model_Participante_Torneio__cpf = cpf
	def set_graduacao(self, graduacao):
		self.Model_Participante_Torneio__graduacao = graduacao
	def set_tipo(self, tipo):
		self.Model_Participante_Torneio__tipo = tipo
	def set_telefone(self , telefone):
		self.Model_Participante_Torneio__telefone = telefone
	def set_academia(self, academia):
		self.Model_Participante_Torneio__academia = academia
	def set_endereco(self, endereco):
		self.Model_Participante_Torneio__endereco = endereco
	def set_inscricao(self, inscricao):
		self.Model_Participante_Torneio__inscricao = inscricao
	def set_torneio(self, torneio):
		self.Model_Participante_Torneio__torneio = torneio
	def set_pago(self, pago):
		self.Model_Participante_Torneio__pago = pago
	
if __name__== '__main__':
	pass