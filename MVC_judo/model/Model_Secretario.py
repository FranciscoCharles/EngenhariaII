#modulo de Model_Secretario
import sys
sys.path.append("../model")

class Model_Secretario(object):
	
	__login = None
	__senha = None
	
	__MIN_LOGIN = None
	__MIN_SENHA = None
	
	__MAX_LOGIN = None
	__MAX_SENHA = None
	
	def __init__(self):
		self.inicializacao_padrao()
		
	#get's
	def get_login(self):
		return self.Model_Secretario__login
	def get_senha(self):
		return self.Model_Secretario__senha
	def get_min_login(self):
		return self.Model_Secretario__MIN_LOGIN
	def get_min_senha(self):
		return self.Model_Secretario__MIN_SENHA
	def get_max_login(self):
		return self.Model_Secretario__MAX_LOGIN
	def get_max_senha(self):
		return self.Model_Secretario__MAX_SENHA
	
	#set's
	def set_login(self, login):
		self.Model_Secretario__login = login
	def set_senha(self, senha):
		self.Model_Secretario__senha = senha
	def set_max_login(self, max):
		self.Model_Secretario__MAX_LOGIN = max
	def set_max_senha(self, max):
		self.Model_Secretario__MAX_SENHA = max
	def set_min_login(self, min):
		self.Model_Secretario__MIN_LOGIN = min
	def set_min_senha(self, min):
		self.Model_Secretario__MIN_SENHA = min
		
	#metodos de validacao
	def inicializacao_padrao(self):
		self.set_max_login(30)
		self.set_max_senha(30)
		self.set_min_login(4)
		self.set_min_senha(4)
		self.set_login(None)
		self.set_senha(None)
	
if __name__== '__main__':
	M = Model_Secretario()
