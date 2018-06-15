#modulo de Controllerl_Secretario
import sys
import unittest
sys.path.append("../")
from controller.Controller_Carteirinha import*

class Teste_Carteirinha(unittest.TestCase):
	def setUp(self):
		self.carteirinha = Controller_Carteirinha()
	def teste_valida_dia(self):
		self.assertTrue(self.carteirinha.valida_dia(11))
	def teste_nao_valida_dia(self):
		self.assertFalse(self.carteirinha.valida_dia(51))
	def teste_valida_mes(self):
		self.assertTrue(self.carteirinha.valida_mes(2))
	def teste_nao_valida_mes(self):
		self.assertFalse(self.carteirinha.valida_mes(13))
	def teste_valida_ano(self):
		self.assertTrue(self.carteirinha.valida_ano(1998))
	def teste_nao_valida_ano(self):
		self.assertFalse(self.carteirinha.valida_ano(1000))
	def teste_valida_dia_mes_nascimento(self):
		self.carteirinha.set_data_nascimento("12/08/1998")
		self.assertTrue(self.carteirinha.valida_dia_mes_nascimento())
	def teste_nao_valida_dia_mes_nascimento(self):
		self.carteirinha.set_data_nascimento("-1/08/1998")
		self.assertFalse(self.carteirinha.valida_dia_mes_nascimento())
	def teste_data_nascimento_valida(self):
		self.carteirinha.set_data_nascimento("12/08/1998")
		self.assertTrue(self.carteirinha.data_nascimento_valida())
	def teste_data_nascimento_invalida(self):
		self.carteirinha.set_data_nascimento("30/02/1998")
		self.assertFalse(self.carteirinha.data_nascimento_valida())
	def teste_valida_dia_mes_data(self):
		self.carteirinha.set_data("12/08/1998")
		self.assertTrue(self.carteirinha.valida_dia_mes_data())
	def teste_nao_valida_dia_mes_data(self):
		self.carteirinha.set_data("-1/08/1998")
		self.assertFalse(self.carteirinha.valida_dia_mes_data())
	def teste_data_valida(self):
		self.carteirinha.set_data("12/08/1998")
		self.assertTrue(self.carteirinha.data_valida())
	def teste_data_invalida(self):
		self.carteirinha.set_data("30/02/1998")
		self.assertFalse(self.carteirinha.data_valida())
	def teste_nome_tem_caracteres_especiais(self):
		self.carteirinha.set_nome("teste.")
		self.assertTrue(self.carteirinha.nome_tem_caracteres_especiais())
	def teste_nome_nao_tem_caracteres_especiais(self):
		self.carteirinha.set_nome("teste")
		self.assertFalse(self.carteirinha.nome_tem_caracteres_especiais())
	def teste_nome_vazio(self):
		self.assertTrue(self.carteirinha.nome_vazio())
	def teste_nome_nao_vazio(self):
		self.carteirinha.set_nome("teste")
		self.assertFalse(self.carteirinha.nome_vazio())
	def teste_data_nascimento_vazia(self):
		self.assertTrue(self.carteirinha.data_nascimento_vazia())
	def teste_data_nascimento_nao_vazia(self):
		self.carteirinha.set_data_nascimento("12/08/1998")
		self.assertFalse(self.carteirinha.data_nascimento_vazia())
	def teste_cpf_vazio(self):
		self.assertTrue(self.carteirinha.cpf_vazio())
	def teste_cpf_nao_vazio(self):
		self.carteirinha.set_cpf("222222222222222")
		self.assertFalse(self.carteirinha.cpf_vazio())
	def teste_data_vazia(self):
		self.assertTrue(self.carteirinha.data_vazia())
	def teste_data_nao_vazia(self):
		self.carteirinha.set_data("12/08/1998")
		self.assertFalse(self.carteirinha.data_vazia())
	def teste_academia_vazia(self):
		self.assertTrue(self.carteirinha.academia_vazia())
	def teste_academia_nao_vazia(self):
		self.carteirinha.set_academia("Teste")
		self.assertFalse(self.carteirinha.academia_vazia())
	def teste_inscricao_vazia(self):
		self.assertTrue(self.carteirinha.inscricao_vazia())
	def teste_inscricao_nao_vazia(self):
		self.carteirinha.set_inscricao("222222")
		self.assertFalse(self.carteirinha.inscricao_vazia())
	def teste_tipo_nao_vazio(self):
		self.carteirinha.set_tipo("aluno")
		self.assertFalse(self.carteirinha.tipo_vazio())
	def teste_tipo_vazio(self):
		self.assertTrue(self.carteirinha.tipo_vazio())
	def teste_tipo_valido(self):
		self.carteirinha.set_tipo("aluno")
		self.assertTrue(self.carteirinha.tipo_valido())
	def teste_tipo_invalido(self):
		self.assertFalse(self.carteirinha.tipo_valido())
	def teste_dados_validos(self):
		self.carteirinha.set_nome("teste")
		self.carteirinha.set_data("12/08/1998")
		self.carteirinha.set_data_nascimento("12/08/1998")
		self.carteirinha.set_academia("Teste")
		self.carteirinha.set_tipo("aluno")
		self.carteirinha.set_graduacao("preta")
		self.carteirinha.set_inscricao("12")
		self.carteirinha.set_cpf("12368519278")
		self.assertTrue(self.carteirinha.dados_validos())
if __name__== '__main__':
	unittest.main()
		
