#modulo de Model_Boleto
class Model_Boleto(object):
	__nome = None
	__inscricao = None
	__data = None
	__valor = None
	#get's
	def __init__(self):
		pass
	def get_nome(self):
		return self.Model_Boleto__nome
	def get_inscricao(self):
		return self.Model_Boleto__inscricao
	def get_data(self):
		return self.Model_Boleto__data
	def get_valor(self):
		return self.Model_Boleto__valor
	#set's
	def set_nome(self, nome):
		self.Model_Boleto__nome = nome
	def set_inscricao(self, inscricao):
		self.Model_Boleto__inscricao = inscricao
	def set_data(self, data):
		self.Model_Boleto__data = data
	def set_valor(self, valor):
		self.Model_Boleto__valor = valor
		
if __name__== '__main__':
	pass