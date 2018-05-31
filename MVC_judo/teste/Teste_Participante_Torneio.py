#modulo de Controllerl_Participante
import sys
import unittest
sys.path.append("../")

from controller.Controller_Participante_Torneio import*

class Teste_Participante_Torneio(unittest.TestCase):
	def setUp(self):
		self.participante = Controller_Participante_Torneio()
	def teste_dia_valido(self):
		self.assertTrue(self.participante.valida_dia(5))
	def teste_dia_invalido(self):
		self.assertFalse(self.participante.valida_dia(32))
	def teste_mes_valido(self):
		self.assertTrue(self.participante.valida_mes(10))
	def teste_mes_invalido(self):
		self.assertFalse(self.participante.valida_mes(13))
	def teste_ano_valido(self):
		self.assertTrue(self.participante.valida_ano(1997))
	def teste_ano_invalido(self):
		self.assertFalse(self.participante.valida_ano(10))
	def teste_dia_mes_valido(self):
		self.participante.set_nascimento("23/12/1997")
		self.assertTrue(self.participante.valida_dia_mes())
	def teste_dia_mes_invalido(self):
		self.participante.set_nascimento("30/02/1997")
		self.assertFalse(self.participante.valida_dia_mes())
	def teste_data_nascimento_valida(self):
		self.participante.set_nascimento("20/02/1997")
		self.assertTrue(self.participante.data_nascimento_valida())
	def teste_data_nascimento_invalida(self):
		self.participante.set_nascimento("1/2/97")
		self.assertFalse(self.participante.data_nascimento_valida())
	def teste_nome_tem_caracteres_especiais(self):
		self.participante.set_nome("lekenho#-boy")
		self.assertTrue(self.participante.nome_tem_caracteres_especiais())
	def teste_nome_nao_tem_caracteres_especiais(self):
		self.participante.set_nome("lekenho")
		self.assertFalse(self.participante.nome_tem_caracteres_especiais())
	def teste_nome_vazio(self):
		self.assertTrue(self.participante.nome_vazio())
	def teste_nome_nao_vazio(self):
		self.participante.set_nome("um nome")
		self.assertFalse(self.participante.nome_vazio())
	def teste_nascimento_vazio(self):
		self.assertTrue(self.participante.nascimento_vazio())
	def teste_nascimento_nao_vazio(self):
		self.participante.set_nascimento("24/07/2001")
		self.assertFalse(self.participante.nascimento_vazio())
	def teste_cpf_vazio(self):
		self.assertTrue(self.participante.cpf_vazio())
	def teste_cpf_nao_vazio(self):
		self.participante.set_cpf("12345678")
		self.assertFalse(self.participante.cpf_vazio())
	def teste_telefone_vazio(self):
		self.assertTrue(self.participante.telefone_vazio())
	def teste_telefone_nao_vazio(self):
		self.participante.set_telefone("(089)3685-3456")
		self.assertFalse(self.participante.telefone_vazio())
	def teste_academia_vazia(self):
		self.assertTrue(self.participante.academia_vazia())
	def teste_academia_nao_vazia(self):
		self.participante.set_academia("teste")
		self.assertFalse(self.participante.academia_vazia())
	def teste_graduacao_vazia(self):
		self.assertTrue(self.participante.graduacao_vazia())
	def teste_graduacao_nao_vazia(self):
		self.participante.set_graduacao("roxa")
		self.assertFalse(self.participante.graduacao_vazia())
	def teste_tipo_vazio(self):
		self.assertTrue(self.participante.tipo_vazio())
	def teste_tipo_nao_vazio(self):
		self.participante.set_tipo("professor")
		self.assertFalse(self.participante.tipo_vazio())
	def teste_endereco_vazio(self):
		self.assertTrue(self.participante.endereco_vazio())
	def teste_endereco_nao_vazio(self):
		self.participante.set_endereco("rua dos bobos numero zero")
		self.assertFalse(self.participante.endereco_vazio())
	def teste_torneio_nao_vazio(self):
		self.participante.set_torneio("torneio de forca")
		self.assertFalse(self.participante.torneio_vazio())
	def teste_torneio_vazio(self):
		self.assertTrue(self.participante.torneio_vazio())
	def teste_pago_nao_vazio(self):
		self.participante.set_endereco("False")
		self.assertFalse(self.participante.pago_vazio())
	def teste_pago_vazio(self):
		self.participante.set_pago("")
		self.assertTrue(self.participante.pago_vazio())
	def teste_telefone_valido(self):
		self.participante.set_telefone("(88)99923423")
		self.assertTrue(self.participante.telefone_valido())
	def teste_telefone_invalido(self):
		self.participante.set_telefone("678@")
		self.assertFalse(self.participante.telefone_valido())
	def teste_dados_invalidos(self):
		self.assertFalse(self.participante.dados_validos())
	def teste_pago_valido(self):
		self.participante.set_pago("False")
		self.assertTrue(self.participante.pago_valido())
	def teste_pago_invalido(self):
		self.participante.set_pago("issjd")
		self.assertFalse(self.participante.pago_valido())
	def teste_dados_validos(self):
		self.participante.set_nome("sei la")
		self.participante.set_academia("Cobra")
		self.participante.set_nascimento("13/10/2019")
		self.participante.set_graduacao("preta")
		self.participante.set_cpf("368599010")
		self.participante.set_tipo("Aluno")
		self.participante.set_endereco("rua dos bobos")
		self.participante.set_telefone("(89)99999999")
		self.participante.set_pago("False")
		self.participante.set_torneio("torneio de forca")
		self.assertTrue(self.participante.dados_validos())
	def teste_salvar_participante(self):
		self.assertFalse(self.participante.salvar_participante())
	def teste_remover_participante(self):
		self.assertFalse(self.participante.remover_participante())
if __name__== '__main__':
	unittest.main()
		
