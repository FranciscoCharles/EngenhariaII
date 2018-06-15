#modulo de Model_Boleto
class Model_Boleto(object):

	__nome = None
	__inscricao = None
	__academia = None
	__torneio = None
	__status = None
	__data = None
	__valor = None
	
	#get's
	def __init__(self):
		self.inicializacao_padrao()
	def inicializacao_padrao(self):
		self.set_academia(None)
		self.set_status(None)
		self.set_torneio(None)
		self.set_nome(None)
		self.set_inscricao(None)
		self.set_data(None)
		self.set_valor(None)
	def get_academia(self):
		return self.Model_Boleto__academia
	def get_status(self):
		return self.Model_Boleto__status
	def get_torneio(self):
		return self.Model_Boleto__torneio
	def get_nome(self):
		return self.Model_Boleto__nome
	def get_inscricao(self):
		return self.Model_Boleto__inscricao
	def get_data(self):
		return self.Model_Boleto__data
	def get_valor(self):
		return self.Model_Boleto__valor
	#set's
	def set_boleto(self,lista_boleto):
		lista = []
		objeto_boleto = Model_Boleto()
		for objeto in lista_boleto:
			print(objeto)
			objeto_boleto.set_nome(objeto[0])
			objeto_boleto.set_academia(objeto[1])
			objeto_boleto.set_inscricao(objeto[2])
			objeto_boleto.set_torneio(objeto[3])
			objeto_boleto.set_status(objeto[4])
			objeto_boleto.set_data(objeto[5])
			objeto_boleto.set_valor(objeto[6])
			lista.append(objeto_boleto)
		return lista
	def set_academia(self, academia):
		self.Model_Boleto__academia = academia
	def set_status(self, status):
		self.Model_Boleto__status = status
	def set_torneio(self, torneio):
		self.Model_Boleto__torneio = torneio
	def set_nome(self, nome):
		self.Model_Boleto__nome = nome
	def set_inscricao(self, inscricao):
		self.Model_Boleto__inscricao = inscricao
	def set_data(self, data):
		self.Model_Boleto__data = data
	def set_valor(self, valor):
		self.Model_Boleto__valor = valor
		
		
if __name__== '__main__':
	B = Model_Boleto()