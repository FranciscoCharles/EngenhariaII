#modulo de Model_Academia
import sys
sys.path.append("../model")

class Model_Academia(object):
	
	__id = None
	__nome = None
	__local = None
	__data = None
	__contato = None
	__responsavel = None
	__email = None
	
	def __init__(self):
		self.inicialicao_padrao()
	def inicialicao_padrao(self):
		self.set_nome(None)
		self.set_data(None)
		self.set_local(None)
		self.set_contato(None)
		self.set_email(None)
		self.set_responsavel(None)
		self.set_id(None)
	#get's
	def get_id(self):
		return self.Model_Academia__id
	def get_nome(self):
		return self.Model_Academia__nome
	def get_contato(self):
		return self.Model_Academia__contato
	def get_local(self):
		return self.Model_Academia__local
	def get_data(self):
		return self.Model_Academia__data
	def get_email(self):
		return self.Model_Academia__email
	def get_responsavel(self):
		return self.Model_Academia__responsavel
	#set's
	def set_id(self, id):
		self.Model_Academia__id = id
	def set_nome(self, nome):
		self.Model_Academia__nome = nome
	def set_contato(self, contato):
		self.Model_Academia__contato = contato
	def set_local(self, local):
		self.Model_Academia__local = local
	def set_data(self, data):
		self.Model_Academia__data = data
	def set_email(self, email):
		self.Model_Academia__email = email
	def set_responsavel(self, responsavel):
		self.Model_Academia__responsavel = responsavel
if __name__== '__main__':
	pass