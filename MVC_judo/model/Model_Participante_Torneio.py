#modulo de Model_Participante
class Model_Participante(object):
	
	__nome = None
	__data = None
	__cpf = None
	__graduacao = None
	__academia = None
	__tipo = None
	__inscricao = None
	
	def __init__(self):
		pass
	def get_nome(self):
		return self.Model_Participante__nome
	def get_data(self):
		return self.Model_Participante__data
	def get_cpf(self):
		return self.Model_Participante__cpf
	def get_graduacao(self):
		return self.Model__Participante__graduacao
	def get_tipo(self):
		return self.Model__Participante__tipo
	def get_academia(self):
		return self.Model__Participante__academia
	def get_inscricao(self):
		return self.Model__Participante__inscricao
	#set's
	def set_nome(self, nome):
		self.Model_Participante__nome = nome
	def set_data(self, data):
		self.Model_Participante__data = data
	def set_cpf(self, cpf):
		self.Model_Participante__cpf = cpf
	def set_graduacao(self, graduacao):
		self.Model__Participante__graduacao = graduacao
	def set_tipo(self, tipo):
		self.Model__Participante__tipo = tipo
	def set_academia(self, academia):
		self.Model__Participante__academia = academia
	def set_inscricao(self, inscricao):
		self.Model__Participante__inscricao = inscricao
	
if __name__== '__main__':
	pass