#modulo de Model_Academia
class Model_Academia(object):
	
	__nome = None
	__local = None
	__data = None
	__responsavel = None
	
	def __init__(self):
		pass
	#get's
	def get_nome(self):
		return self.Model_Academia__nome
	def get_local(self):
		return self.Model_Academia__local
	def get_data(self):
		return self.Model_Academia__data
	def get_responsavel(self):
		return self.Model_Academia__responsavel
	#set's
	def set_nome(self, nome):
		self.Model_Academia__nome = nome
	def set_local(self, local):
		self.Model_Academia__local = local
	def set_data(self, data):
		self.Model_Academia__data = data
	def set_responsavel(self, responsavel):
		self.Model_Academia__responsavel = responsavel
if __name__== '__main__':
	pass