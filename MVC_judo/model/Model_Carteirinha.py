#modulo de Model_Carteirinha

class Model_Carteirinha(object):
	__nome = None
	__data = None
	__data_nascimento = None
	__academia = None
	__tipo = None
	__graduacao = None
	__cpf = None
	__inscricao = None
	
	def __init__(self):
		self.inicializacao_padrao()
	def inicializacao_padrao(self):
		self.set_nome(None)
		self.set_data(None)
		self.set_data_nascimento(None)
		self.set_academia(None)
		self.set_tipo(None)
		self.set_graduacao(None)
		self.set_inscricao(None)
		self.set_cpf(None)
	#get's
	def get_cpf(self):
		return self.Model_Carteirinha__cpf
	def get_nome(self):
		return self.Model_Carteirinha__nome
	def get_data(self):
		return self.Model_Carteirinha__data
	def get_data_nascimento(self):
		return self.Model_Carteirinha__data_nascimento
	def get_academia(self):
		return self.Model_Carteirinha__academia
	def get_tipo(self):
		return self.Model_Carteirinha__tipo
	def get_graduacao(self):
		return self.Model_Carteirinha__graduacao
	def get_inscricao(self):
		return self.Model_Carteirinha__inscricao
	#set's
	def set_carteirinha(self,lista_carteirinha):
		lista = []
		objeto_carteirinha = Model_Carteirinha()
		for objeto in lista_carteirinha:
			objeto_carteirinha.set_nome(objeto[0])
			objeto_carteirinha.set_data(objeto[1])
			objeto_carteirinha.set_academia(objeto[2])
			objeto_carteirinha.set_tipo(objeto[3])
			objeto_carteirinha.set_graduacao(objeto[4])
			objeto_carteirinha.set_inscricao(objeto[5])
			objeto_carteirinha.set_cpf(objeto[6])
		return objeto_carteirinha	
	def set_nome(self, nome):
		self.Model_Carteirinha__nome = nome
	def set_cpf(self, cpf):
		self.Model_Carteirinha__cpf = cpf
	def set_data(self, data):
		self.Model_Carteirinha__data = data
	def set_data_nascimento(self, data_nascimento):
		self.Model_Carteirinha__data_nascimento = data_nascimento
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