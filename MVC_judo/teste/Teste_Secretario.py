#modulo Teste_Secretario
import sys
import unittest
sys.path.append("../")
from controller.Controller_Secretario import*

class Teste_Secretario(unittest.TestCase):
	def setUp(self):
		self.secretario = Controller_Secretario()
	#teste em relacao a presenca de caracteres especiais no login
	def teste_login_sem_caractere_especial(self):
		self.secretario.set_login("admin")
		self.assertFalse(self.secretario.login_tem_caractere_especial())
	def teste_login_possui_caractere_especial(self):
		self.secretario.set_login("admin.#!")
		self.assertTrue(self.secretario.login_tem_caractere_especial())
	#teste em relacao a campos vazios
	def teste_login_vazio(self):
		self.secretario.set_login("")
		self.assertTrue(self.secretario.login_vazio())
	def teste_login_nao_vazio(self):
		self.secretario.set_login("login")
		self.assertFalse(self.secretario.login_vazio())
	def teste_senha_vazia(self):
		self.secretario.set_senha("")
		self.assertTrue(self.secretario.senha_vazia())
	def teste_senha_nao_vazia(self):
		self.secretario.set_senha("essaeumasenha")
		self.assertFalse(self.secretario.senha_vazia())
	#testes em relacao ao tamanho do login
	def teste_tamanho_menor_de_login(self):
		self.secretario.set_login("ad")
		self.assertFalse(self.secretario.valida_tamanho_login())
	def teste_tamanho_maior_de_login(self):
		self.secretario.set_login("esseeumnomedeloginmuitolongoecansativo")
		self.assertFalse(self.secretario.valida_tamanho_login())
	def teste_tamanho_valido_de_login(self):
		self.secretario.set_login("admin")
		self.assertTrue(self.secretario.valida_tamanho_login())
	#testes em relacao ao tamanho de senha
	def teste_tamanho_valido_de_senha(self):
		self.secretario.set_senha("essaeumasenha")
		self.assertTrue(self.secretario.valida_tamanho_senha())
	def teste_tamanho_menor_de_senha(self):
		self.secretario.set_senha("es")
		self.assertFalse(self.secretario.valida_tamanho_senha())
	def teste_tamanho_maior_de_senha(self):
		self.secretario.set_senha("esseeumnomedesenhamuitolongoecansativo")
		self.assertFalse(self.secretario.valida_tamanho_senha())
	#teste em relacao a presenca de espaco na senha
	def teste_senha_possui_espaco(self):
		self.secretario.set_senha("essa e uma senha")
		self.assertTrue(self.secretario.senha_tem_espaco())
	def teste_senha_nao_possui_espaco(self):
		self.secretario.set_senha("essaeumasenha")
		self.assertFalse(self.secretario.senha_tem_espaco())
	def teste_senha_possui_muitos_espacos(self):
		self.secretario.set_senha("essae   uma senha")
		self.assertTrue(self.secretario.senha_tem_espaco())
	#teste em relacaoa metodos de gerenciamento do banco de dados
	def teste_salvar_dados(self):
		self.assertFalse(self.secretario.salvar_secretario())
	def teste_dados_validos(self):
		self.assertFalse(self.secretario.dados_validos())
	#teste em relacao a existencia de um determinado secretario
	def teste_nao_este_secretario_existe(self):
		self.assertFalse(self.secretario.este_secretario_existe())
if __name__== '__main__':
	unittest.main()
		
