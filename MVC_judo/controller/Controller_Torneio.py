#modulo de Model_Torneio
class Model_Torneio(object):
	
	__nome = None
	__local = None
	__data = None
	__valor = None
	__organizador = None
	
	def __init__(self):
		pass
	#get's
	def get_nome(self):
		return self.Model_Torneio__nome
	def get_local(self):
		return self.Model_Torneio__local
	def get_data(self):
		return self.Model_Torneio__data
	def get_valor(self):
		return self.Model_Torneio__valor
	def get_organizador(self):
		return self.Model_Torneio__organizador
	#set's
	def set_nome(self, nome):
		self.Model_Torneio__nome = nome
	def set_local(self, local):
		self.Model_Torneio__local = local
	def set_data(self, data):
		self.Model_Torneio__data = data
	def set_valor(self, valor):
		self.Model_Torneio__valor = valor
	def set_organizador(self, organizador):
		self.Model_Torneio__organizador = organizador

if __name__== '__main__':
	pass
		
