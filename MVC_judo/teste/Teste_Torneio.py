#modulo de Controllerl_Torneio
import sys
import unittest
sys.path.append("../")

from controller.Controller_Torneio import*

class Teste_Torneio(unittest.TestCase):
	def setUp(self):
		self.torneio = Controller_Torneio()
	#teste de campos vazios
	def teste_horario_vazio(self):
		self.torneio.set_horario("")
		self.assertTrue(self.torneio.horario_vazio())
	def teste_horario_nao_vazio(self):
		self.torneio.set_horario("03:56")
		self.assertFalse(self.torneio.horario_vazio())
	def teste_hora_valida(self):
		self.assertTrue(self.torneio.hora_valida(10))
	def teste_hora_invalida(self):
		self.assertFalse(self.torneio.hora_valida(67))
	def teste_minutos_valido(self):
		self.assertTrue(self.torneio.minutos_valido(10))
	def teste_minutos_invalido(self):
		self.assertFalse(self.torneio.minutos_valido(-1))
	def teste_separa_horario_valido(self):
		self.torneio.set_horario("03:45")
		self.assertTrue(self.torneio.separa_horario())
	def teste_separa_horario_invalido(self):
		self.torneio.set_horario("03:45/")
		self.assertFalse(self.torneio.separa_horario())
	def teste_horario_possui_caractere_invalido(self):
		self.torneio.set_horario("03:45/")
		self.assertTrue(self.torneio.horario_possui_caractere_invalido())
	def teste_horario_nao_possui_caractere_invalido(self):
		self.torneio.set_horario("03:45")
		self.assertFalse(self.torneio.horario_possui_caractere_invalido())
	def teste_nome_vazio(self):
		self.torneio.set_nome("")
		self.assertTrue(self.torneio.nome_vazio())
	def teste_nome_nao_vazio(self):
		self.torneio.set_nome("um nome qualquer")
		self.assertFalse(self.torneio.nome_vazio())
	def teste_data_vazia(self):
		self.torneio.set_data("")
		self.assertTrue(self.torneio.data_vazia())
	def teste_data_nao_vazia(self):
		self.torneio.set_data("23/07/2011")
		self.assertFalse(self.torneio.data_vazia())
	def teste_valor_vazio(self):
		self.torneio.set_valor("")
		self.assertTrue(self.torneio.valor_vazio())
	def teste_valor_nao_vazio(self):
		self.torneio.set_valor("12,00")
		self.assertFalse(self.torneio.valor_vazio())
	def teste_contato_vazio(self):
		self.torneio.set_contato("")
		self.assertTrue(self.torneio.contato_vazio())
	def teste_contato_nao_vazio(self):
		self.torneio.set_contato("088999118812")
		self.assertFalse(self.torneio.contato_vazio())
	def teste_organizador_vazio(self):
		self.torneio.set_organizador("")
		self.assertTrue(self.torneio.organizador_vazio())
	def teste_organizador_nao_vazio(self):
		self.torneio.set_organizador("Rafael Lima")
		self.assertFalse(self.torneio.organizador_vazio())
	def teste_local_vazio(self):
		self.torneio.set_local("")
		self.assertTrue(self.torneio.local_vazio())
	def teste_local_nao_vazio(self):
		self.torneio.set_local("rua dos bobos numero 0")
		self.assertFalse(self.torneio.local_vazio())
	#teste em relacao a validacao de dados
	def teste_dados_validos(self):
		self.torneio.set_data("20/02/18")
		self.assertFalse(self.torneio.dados_validos())
	#teste em relacao a data
	def teste_data_valida(self):
		self.torneio.set_data("20/02/2018")
		self.assertTrue(self.torneio.data_valida())
	def teste_data_invalida(self):
		self.torneio.set_data("-1/02/20")
		self.assertFalse(self.torneio.data_valida())
	#teste em relacao ao dia e mes
	def teste_dia_mes_valido(self):
		self.torneio.set_data("02/02/2018")
		self.assertTrue(self.torneio.valida_dia_mes())
	def teste_dia_mes_invalido(self):
		self.torneio.set_data("31/02/2018")
		self.assertFalse(self.torneio.valida_dia_mes())
	#teste em realacao a ano
	def teste_ano_valido(self):
		self.assertTrue(self.torneio.valida_ano(2018))
	def teste_ano_invalido(self):
		self.assertFalse(self.torneio.valida_ano(99))
	#teste em relacao a dia
	def teste_dia_invalido(self):
		self.assertFalse(self.torneio.valida_dia(33))
	def teste_dia_valido(self):
		self.assertTrue(self.torneio.valida_dia(12))
	#teste em relacao ao valor
	def teste_valor_valido(self):
		self.torneio.set_valor("50,00")
		self.assertTrue(self.torneio.valida_valor())
	def teste_valor_invalido(self):
		self.torneio.set_valor("50.00")
		self.assertFalse(self.torneio.valida_valor())
	#teste em relacao a presenca de caracteres especiais no nome do torneio
	def teste_nome_tem_caracteres_especiais(self):
		self.torneio.set_nome("jose lima & cia")
		self.assertTrue(self.torneio.nome_tem_caracteres_especiais())
	def teste_nome_nao_tem_caracteres_especiais(self):
		self.torneio.set_nome("jose lima")
		self.assertFalse(self.torneio.nome_tem_caracteres_especiais())
	#teste em relacao a presenca de caracteres especiais no nome do organizador do torneio
	def teste_organizador_tem_caracteres_especiais(self):
		self.torneio.set_organizador("jose Lima & cia")
		self.assertTrue(self.torneio.organizador_tem_caracteres_especiais())
	def teste_organizador_nao_tem_caracteres_especiais(self):
		self.torneio.set_organizador("jose Lima cia")
		self.assertFalse(self.torneio.organizador_tem_caracteres_especiais())
	#teste em relacao a contato
	def teste_contato_valido(self):
		self.torneio.set_contato("08999102122")
		self.assertTrue(self.torneio.contato_valido())
	def teste_contato_invalido(self):
		self.torneio.set_contato("3685")
		self.assertFalse(self.torneio.contato_valido())
	#teste em relacao a funcoes de gerenciamento de banco
	def teste_salvar_torneio(self):
		self.assertFalse(self.torneio.salvar_torneio())
	def teste_este_torneio_existe(self):
		self.assertFalse(self.torneio.este_torneio_existe())
if __name__== '__main__':
	unittest.main()