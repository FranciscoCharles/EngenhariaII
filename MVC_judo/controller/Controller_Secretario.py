#modulo de Controllerl_Secretario
import sys
sys.path.append("../")
from model.Model_Banco_Secretario import*

class Controller_Secretario(Model_Banco_Secretario):
	def __init__(self):
		super().__init__()
		self.criar_tabela()
	#metodos de validacao de dados
	def valida_tamanho_login(self):
		if self.login_vazio():
			return False
		len_login = len(self.get_login())
		if  (len_login < self.get_min_login()) or (len_login > self.get_max_login()):
			return False
		return True
	def valida_tamanho_senha(self):
		if self.senha_vazia():
			return False
		len_senha = len(self.get_senha())
		if  len_senha < self.get_min_senha() or len_senha > self.get_max_senha():
			return False
		return True
	def login_vazio(self):
		if (self.get_login() == None) or (len(self.get_login())==0):
			return True
		return False
	def senha_vazia(self):
		if (self.get_senha() == None) or (len(self.get_senha())==0):
			return True
		return False
	def login_tem_caractere_especial(self):
		if self.login_vazio():
			return False
		especiais = ".,<>;:?/\\!'\"¹²³£¢¬#$%%¨&´`§*()ç~^+-=[]{}ªº°|@"
		login = self.get_login()
		for caractere in especiais:
			if login.count(caractere) > 0:
				return True
		return False
	def senha_tem_espaco(self):
		if self.senha_vazia():
			return False
		senha = self.get_senha()
		if senha.count(' ') != 0:
			return True
		return False
	def dados_validos(self):
		if not self.login_vazio():
			if not self.login_vazio():
				if self.valida_tamanho_login():
					if not self.login_tem_caractere_especial():
						if not self.senha_vazia():
							if self.valida_tamanho_senha():
								if not self.senha_tem_espaco():
									return True
		return False
	#metodos de gerenciamento de dados
	def salvar_secretario(self):
		if self.dados_validos():
			return super().salvar_secretario()
		return False
	def remover_secretario(self):
		if self.dados_validos():
			return super().remover_secretario()
		return False
	def buscar_secretario(self):
		if self.dados_validos():
			return super().buscar_secretario()
		return None
		
if __name__== '__main__':
	C = Controller_Secretario()
	C.set_login("big big")
	C.set_senha("1234")
	print(C.remover_secretario())
	#print(C.buscar_secretario())
	#print(C.login_tem_caractere_especial())
	#C.listar_secretario()
		
