#modulo de Controllerl_Boleto
import sys
import unittest
sys.path.append("../")
from controller.Controller_Boleto import*

class Teste_Boleto(unittest.TestCase):
	def setUp(self):
		self.boleto = Controller_Boleto()
	def teste_valida_dia(self):
		self.assertTrue(self.boleto.valida_dia(10))
	def teste_nao_valida_dia(self):
		self.assertFalse(self.boleto.valida_dia(-1))
	def teste_valida_mes(self):
		self.assertTrue(self.boleto.valida_mes(10))
	def teste_nao_valida_mes(self):
		self.assertFalse(self.boleto.valida_mes(88))
	def teste_valida_ano(self):
		self.assertTrue(self.boleto.valida_ano(2020))
	def teste_nao_valida_ano(self):
		self.assertFalse(self.boleto.valida_ano(1000))
	def teste_valida_dia_mes(self):
		self.boleto.set_data("10/06/2020")
		self.assertTrue(self.boleto.valida_dia_mes())
	def teste_nao_valida_dia_mes(self):
		self.boleto.set_data("10/22/2020")
		self.assertFalse(self.boleto.valida_dia_mes())
	def teste_valida_dia_mes(self):
		self.boleto.set_data("10/06/2020")
		self.assertTrue(self.boleto.valida_dia_mes())
	def teste_nao_valida_dia_mes(self):
		self.boleto.set_data("33/06/2020")
		self.assertFalse(self.boleto.valida_dia_mes())
	def teste_nome_tem_caracteres_especiais(self):
		self.boleto.set_nome("boi-")
		self.assertTrue(self.boleto.nome_tem_caracteres_especiais())
	def teste_nome_nao_tem_caracteres_especiais(self):
		self.boleto.set_nome("boi")
		self.assertFalse(self.boleto.nome_tem_caracteres_especiais())
	def teste_inscricao_vazia(self):
		self.assertTrue(self.boleto.inscricao_vazia())
	def teste_inscricao_nao_vazia(self):
		self.boleto.set_inscricao("1")
		self.assertFalse(self.boleto.inscricao_vazia())
	def teste_nome_vazio(self):
		self.assertTrue(self.boleto.nome_vazio())
	def teste_nome_nao_vazio(self):
		self.boleto.set_nome("boi")
		self.assertFalse(self.boleto.nome_vazio())
	def teste_data_vazia(self):
		self.assertTrue(self.boleto.data_vazia())
	def teste_data_nao_vazia(self):
		self.boleto.set_data("10/06/2019")
		self.assertFalse(self.boleto.data_vazia())
	def teste_academia_vazia(self):
		self.assertTrue(self.boleto.academia_vazia())
	def teste_academia_nao_vazia(self):
		self.boleto.set_academia("academia")
		self.assertFalse(self.boleto.academia_vazia())
	def teste_torneio_vazio(self):
		self.assertTrue(self.boleto.torneio_vazio())
	def teste_torneio_nao_vazio(self):
		self.boleto.set_torneio("torneio")
		self.assertFalse(self.boleto.torneio_vazio())
	def teste_status_vazio(self):
		self.assertTrue(self.boleto.status_vazio())
	def teste_status_nao_vazio(self):
		self.boleto.set_status("false")
		self.assertFalse(self.boleto.status_vazio())
	def teste_status_valido(self):
		self.boleto.set_status("true")
		self.assertTrue(self.boleto.status_valido())
	def teste_status_invalido(self):
		self.assertFalse(self.boleto.status_valido())
	def teste_valor_vazio(self):
		self.assertTrue(self.boleto.valor_vazio())
	def teste_valor_nao_vazio(self):
		self.boleto.set_valor("10.0")
		self.assertFalse(self.boleto.valor_vazio())
	def teste_valor_valido(self):
		self.boleto.set_valor("10.0")
		self.assertTrue(self.boleto.valor_valido())
	def teste_valor_invalido(self):
		self.boleto.set_valor("10..")
		self.assertFalse(self.boleto.valor_valido())
	def teste_dados_validos(self):
		self.boleto.set_nome("boi")
		self.boleto.set_inscricao("1")
		self.boleto.set_academia("boi")
		self.boleto.set_torneio("boi")
		self.boleto.set_status("true")
		self.boleto.set_valor("1.0")
		self.boleto.set_data("03/02/2010")
		self.assertTrue(self.boleto.dados_validos())
	def teste_dados_invalidos(self):
		self.assertFalse(self.boleto.dados_validos())
	def teste_salvar_boleto(self):
		self.assertFalse(self.boleto.salvar_boleto())
	def teste_remover_boleto(self):
		self.assertFalse(self.boleto.remover_boleto())
if __name__== '__main__':
	unittest.main()
		
