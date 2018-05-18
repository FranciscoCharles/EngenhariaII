#modulo de Model_Carteirinha

class Model_Carteirinha(object):

	__nome = None
	__data = None
	__academia = None
	__tipo = None
	__graduacao = None
	__inscricao = None
	
	def __init__(self):
		pass
	#get's
	def get_nome(self):
		return self.Model_Carteirinha__nome
	def get_data(self):
		return self.Model_Carteirinha__data
	def get_academia(self):
		return self.Model_Carteirinha__academia
	def get_tipo(self):
		return self.Model_Carteirinha__tipo
	def get_graduacao(self):
		return self.Model_Carteirinha__graduacao
	def get_inscricao(self):
		return self.Model_Carteirinha__inscricao
	#set's
	def set_nome(self, nome):
		self.Model_Carteirinha__nome = nome
	def set_data(self, data):
		self.Model_Carteirinha__data = data
	def set_academia(self, academia):
		self.Model_Carteirinha__academia = academia
	def set_tipo(self, tipo):
		self.Model_Carteirinha__tipo = tipo
	def set_graduacao(self, graduacao):
		self.Model_Carteirinha__graduacao = graduacao
	def set_inscricao(self, inscricao):
		self.Model_Carteirinha__inscricao = inscricao
		
if __name__== '__main__':
	pass