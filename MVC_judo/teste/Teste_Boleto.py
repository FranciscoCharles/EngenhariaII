#modulo de Controllerl_Secretario
import sys
import unittest
sys.path.append("../")
from controller.Controller_Secretario import*

class Teste_Secretario(unittest.TestCase):
	def setUp(self):
		self.secretario = Controller_Secretario()
	def teste_salvar_dados(self):
		#self.assertEqual(funcao, saida)
		self.assertFalse(self.secretario.salvar_secretario())
	def teste_dados_validos(self):
		self.assertFalse(self.secretario.dados_validos())
	def teste_tamanho_valido_de_login(self):
		self.secretario.set_login("admin")
		self.assertTrue(self.secretario.valida_tamanho_login())
	def teste_tamanho_valido_de_senha(self):
		self.secretario.set_senha("essaeumasenha")
		self.assertTrue(self.secretario.valida_tamanho_senha())
	def teste_login_sem_caractere_especial(self):
		self.secretario.set_login("admin")
		self.assertFalse(self.secretario.login_tem_caractere_especial())
	def teste_senha_possui_espaco(self):
		self.secretario.set_senha("essa e uma senha")
		self.assertTrue(self.secretario.senha_tem_espaco())
if __name__== '__main__':
	unittest.main()
		
