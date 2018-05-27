#modulo de teste Academia
import sys
import unittest
sys.path.append("../")
from controller.Controller_Academia import*

class Teste_Academia(unittest.TestCase):
	def setUp(self):
		self.academia = Controller_Academia()
	#teste de campos vazios
	def teste_nome_vazio(self):
		self.academia.set_nome("")
		self.assertTrue(self.academia.nome_vazio())
	def teste_nome_nao_vazio(self):
		self.academia.set_nome("um nome qualquer")
		self.assertFalse(self.academia.nome_vazio())
	def teste_data_vazia(self):
		self.academia.set_data("")
		self.assertTrue(self.academia.data_vazia())
	def teste_data_nao_vazia(self):
		self.academia.set_data("23/07/2011")
		self.assertFalse(self.academia.data_vazia())
	def teste_contato_vazio(self):
		self.academia.set_contato("")
		self.assertTrue(self.academia.contato_vazio())
	def teste_contato_nao_vazio(self):
		self.academia.set_contato("088999118812")
		self.assertFalse(self.academia.contato_vazio())
	def teste_email_vazio(self):
		self.academia.set_email("")
		self.assertTrue(self.academia.email_vazio())
	def teste_email_nao_vazio(self):
		self.academia.set_email("umexemplode@email.com")
		self.assertFalse(self.academia.email_vazio())
	def teste_responsavel_vazio(self):
		self.academia.set_responsavel("")
		self.assertTrue(self.academia.responsavel_vazio())
	def teste_responsavel_nao_vazio(self):
		self.academia.set_responsavel("Rafael Lima")
		self.assertFalse(self.academia.responsavel_vazio())
	def teste_local_vazio(self):
		self.academia.set_local("")
		self.assertTrue(self.academia.local_vazio())
	def teste_local_nao_vazio(self):
		self.academia.set_local("rua dos bobos numero 0")
		self.assertFalse(self.academia.local_vazio())
	#teste em relacao a validacao de dados
	def teste_dados_validos(self):
		self.academia.set_data("20/02/18")
		self.assertFalse(self.academia.dados_validos())
	#teste em relacao a data
	def teste_data_valida(self):
		self.academia.set_data("20/02/2018")
		self.assertTrue(self.academia.data_valida())
	def teste_data_invalida(self):
		self.academia.set_data("-1/02/20")
		self.assertFalse(self.academia.data_valida())
	#teste em relacao ao dia e mes
	def teste_dia_mes_valido(self):
		self.academia.set_data("02/02/2018")
		self.assertTrue(self.academia.valida_dia_mes())
	def teste_dia_mes_invalido(self):
		self.academia.set_data("31/02/2018")
		self.assertFalse(self.academia.valida_dia_mes())
	#teste em relacao a presenca de caracteres especiais no nome da academia
	def teste_nome_tem_caracteres_especiais(self):
		self.academia.set_nome("jose lima & cia")
		self.assertTrue(self.academia.nome_tem_caracteres_especiais())
	def teste_nome_nao_tem_caracteres_especiais(self):
		self.academia.set_nome("jose lima")
		self.assertFalse(self.academia.nome_tem_caracteres_especiais())
	#teste em relacao a presenca de caracteres especiais no nome do responsavel da academia
	def teste_responsavel_tem_caracteres_especiais(self):
		self.academia.set_responsavel("jose Lima & cia")
		self.assertTrue(self.academia.responsavel_tem_caracteres_especiais())
	def teste_responsavel_nao_tem_caracteres_especiais(self):
		self.academia.set_responsavel("jose Lima cia")
		self.assertFalse(self.academia.responsavel_tem_caracteres_especiais())
	#teste em realacao a ano
	def teste_ano_valido(self):
		self.assertTrue(self.academia.valida_ano(2018))
	def teste_ano_invalido(self):
		self.assertFalse(self.academia.valida_ano(99))
	#teste em relacao a dia
	def teste_dia_invalido(self):
		self.assertFalse(self.academia.valida_dia(33))
	def teste_dia_valido(self):
		self.assertTrue(self.academia.valida_dia(12))
	#teste em relacao ao email
	def teste_email_possui_um_unico_arroba(self):
		self.academia.set_email("teste@hotmail.com")
		self.assertTrue(self.academia.email_possui_arroba())
	def teste_email_nao_possui_arroba(self):
		self.academia.set_email("testehotmail.com")
		self.assertFalse(self.academia.email_possui_arroba())
	def teste_email_possui_muitos_arroba(self):
		self.academia.set_email("teste@@hotmail@.com")
		self.assertFalse(self.academia.email_possui_arroba())
	def teste_email_possui_um_unico_ponto_com(self):
		self.academia.set_email("teste@hotmail.com")
		self.assertTrue(self.academia.email_possui_ponto_com())
	def teste_email_nao_possui_ponto_com(self):
		self.academia.set_email("teste@hotmail")
		self.assertFalse(self.academia.email_possui_ponto_com())
	def teste_email_possui_muitos_ponto_com(self):
		self.academia.set_email("t.comeste@hotma.comil.com")
		self.assertFalse(self.academia.email_possui_ponto_com())
	def teste_email_valido(self):
		self.academia.set_email("teste@hotmail.com")
		self.assertTrue(self.academia.email_valido())
	#teste em relacao a contato
	def teste_contato_valido(self):
		self.academia.set_contato("08999102122")
		self.assertTrue(self.academia.contato_valido())
	def teste_contato_invalido(self):
		self.academia.set_contato("3685")
		self.assertFalse(self.academia.contato_valido())
	#teste em relacao a funcoes de gerenciamento de banco
	def teste_salvar_academia(self):
		self.assertFalse(self.academia.salvar_academia())
	def teste_esta_academia_existe(self):
		self.assertFalse(self.academia.esta_academia_existe())
if __name__== '__main__':
	unittest.main()