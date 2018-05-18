#modulo de Controllerl_Secretario
import sys

sys.path.insert(0,'../')
from model.Model_Banco_Secretario import*

class Controller_Secretario(Model_Banco_Secretario):
	def __init__(self):
		super().__init__()
		self.criar_tabela()
	def salvar_secretario(self):
		if self.valida_tamanho_login():
			if self.valida_tamanho_senha():
				if not self.possui_caractere_especial():
					super().salvar_secretario()
				else:
					pass
			else:
				pass
		else:
			pass
if __name__== '__main__':
	C = Controller_Secretario()
	C.listar_secretario()
		
