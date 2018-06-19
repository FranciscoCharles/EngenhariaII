#modulo menu principal

# PRINCIPAIS IMPORT'S
import sys
sys.path.append("../")

from tkinter import*
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from datetime import datetime

#IMPORT DAS CLASSES DE CONTROLE
from controller.Controller_Torneio import*
from controller.Controller_Academia import*
from controller.Controller_Carteirinha import*
from controller.Controller_Boleto import*
from controller.Controller_Secretario import*
from controller.Controller_Participante import*
from controller.Controller_Participante_Torneio import*

#VARIAVEL DE CAMINHO DE IMAGENS
diretorio_imagens = 'C:\\Users\\Charles\\Desktop\\aulas\\Engenharia\\MVC_judo\\image\\'

#VARIAVEIS DE CARACTERISTICAS DOS WINDGETS
ALTURA_PADRAO = 4
LARGURA_PADRAO = 60
TAMANHO_BORDA_BOTAO = 8
TIPO_BORDA_BOTAO = RIDGE
COR_FUNDO = '#105e74'
FONTE_PADRAO = ("Time News Roman",10,"bold")
#VARIAVEIS RECORRENTES
Base_Torneio = Controller_Torneio()
Base_Academia = Controller_Academia()
Base_Carteirinha = Controller_Carteirinha()
Base_Boleto = Controller_Boleto()
Base_Secretario = Controller_Secretario()
Base_Participante = Controller_Participante()
Base_Participante_Torneio = Controller_Participante_Torneio()

#CLASSE RESPONSAVEL PELO GERENCIAMENTO DE FRAMES
class Gerenciador(tk.Tk):

	def __init__(self,*args,**wargs):
	
		tk.Tk.__init__(self,*args,**wargs)
		tk.Tk.iconbitmap(self,default= diretorio_imagens+"icone.ico" )
		tk.Tk.wm_title(self,"JUDORAMA")
		tk.Tk.background='black'
		self.auto = self
		self.container = Frame(self)
		self.container.pack(side="top",fill="both",expand=True)
		self.container.grid_rowconfigure(0,weight=1)
		self.container.grid_columnconfigure(0,weight=1)
		
		self.TELAS = [LoginInicial,MenuPrincipal,
				MenuAcademia,CadastrarAcademia,ListarAcademia,RemoverAcademia,GerarCarteirinha,
				MenuParticipante,CadastrarParticipante,CadastrarParticipanteTorneio,ListarParticipante,
				MenuTorneio,CadastrarTorneio,MenuTorneioBuscas,TorneioBuscaNome,TorneioBuscaId,ListarTorneio,RemoverTorneio,
				MenuSecretario,CadastrarSecretario,ListarSecretario,RemoverSecretario,
				Sobre,ExibeCarteirinha]
		
		self.frames = {}
		
		for tela in (self.TELAS):
			frame = tela(self.container,self)
			self.frames[tela] = frame
			frame.grid(row=0,column=0,stick="nsew")
		self.show_frame(LoginInicial)
		
	def show_frame(self,count):
		self.atualizar(count)
		frame = self.frames[count]
		frame.tkraise()
	def atualizar(self,count):
		self.TELAS.remove(count)
		self.TELAS.append(count)
		del self.frames[count]
		frame = count(self.container,self)
		self.frames[count] = frame
		frame.grid(row=0,column=0,stick="nsew")
		
#CLASSE RESPONSAVEL PELA TELA INICIAL DE LOGIN
class LoginInicial(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=60)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=8,relief=RIDGE,text= "JUDORAMA",width=60,height=4,font=FONTE_PADRAO)
		self.titulo.grid(row=0,column=1)
		
		logo = PhotoImage(file=diretorio_imagens+"testejudo.png")
		self.frame_logo = Frame(self,bg=COR_FUNDO,pady=10)
		self.frame_logo.pack()
		self.logo = Label(self.frame_logo,bg=COR_FUNDO)
		self.logo["image"] = logo
		self.logo.image = logo
		self.logo.pack()
		
		self.frame_usuario = Frame(self, bg = COR_FUNDO,pady=10)
		self.frame_usuario.pack()
		
		self.login = Label(self.frame_usuario,border=2,relief=RIDGE,text="Login : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.senha = Label(self.frame_usuario,border=2,relief=RIDGE,text="Senha : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		
		self.entrada_login = Entry(self.frame_usuario,width=80)
		self.entrada_senha = Entry(self.frame_usuario,width=80,show="*",)
		
		self.login.grid(row=0,column=0)
		self.senha.grid(row=1,column=0)
		
		self.entrada_login.grid(row=0,column=1)
		self.entrada_senha.grid(row=1,column=1)
		
		self.frame_botoes = Frame(self, bg = COR_FUNDO,pady=10)
		self.frame_botoes.pack()
		self.botao_entrar = Button(self.frame_botoes,border=8,relief=RIDGE,font=("Time News Roman",10,"bold"), text = "Entrar",width = int(LARGURA_PADRAO/3),command = lambda:self.valida_dados(controler),activebackground='green')
		self.botao_entrar.grid(row=0,column=0)
		self.botao_fechar = Button(self.frame_botoes,border=8,relief=RIDGE,font=("Time News Roman",10,"bold"), text = "Fechar",width = int(LARGURA_PADRAO/3),command = self.quit,activebackground='green')
		self.botao_fechar.grid(row=0,column=10)
		
	def valida_dados(self,controler):
		global Base_Secretario
		Base_Secretario.set_login(self.entrada_login.get())
		Base_Secretario.set_senha(self.entrada_senha.get())
		
		if(Base_Secretario.login_vazio() and Base_Secretario.senha_vazia()):
			messagebox.showwarning("Aviso", "Preencha os Campos")
		elif(Base_Secretario.login_vazio()):
			messagebox.showwarning("Aviso", "Preencha o Campo Login")
		elif(Base_Secretario.senha_vazia()):
			messagebox.showwarning("Aviso", "Preencha o Campo Senha")
		elif(Base_Secretario.validar_secretario()):
			self.limpar_campos()
			messagebox.showinfo("Acesso", Base_Secretario.get_login()+" Seja bem vindo ao nosso sistema")
			Base_Secretario.inicializacao_padrao()
			controler.show_frame(MenuPrincipal)
		else:
			self.limpar_campos()
			messagebox.showerror("Erro", "Login ou Senha Invalidos")
		
	def limpar_campos(self):
		self.entrada_login.delete(0, END)
		self.entrada_senha.delete(0, END)

#CLASSE RESPONSAVEL PELE MENU PRINCIPAL
class MenuPrincipal(Frame):

	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		self.frame_menu = Frame(self, bg = COR_FUNDO,pady=75)
		self.frame_menu.pack()
		self.botao_academia = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Academia",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(MenuAcademia),activebackground='green',font=FONTE_PADRAO)
		self.botao_torneio = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Torneio",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(MenuTorneio),activebackground='green',font=FONTE_PADRAO)
		self.botao_participante = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Participante",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(MenuParticipante),activebackground='green',font=FONTE_PADRAO)
		self.botao_secretario = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Secretario",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(MenuSecretario),activebackground='green',font=FONTE_PADRAO)
		self.botao_sobre = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Sobre",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(Sobre),activebackground='green',font=FONTE_PADRAO)
		self.botao_sair = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Sair",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(LoginInicial),activebackground='green',font=FONTE_PADRAO)
		self.botao_academia.pack()
		self.botao_torneio.pack()
		self.botao_participante.pack()
		self.botao_secretario.pack()
		self.botao_sobre.pack()
		self.botao_sair.pack()
#CLASSE RESPONSAVEL PELA TELA DE MENU ACADEMIA
class MenuAcademia(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		self.frame_menu = Frame(self, bg = COR_FUNDO,pady=50)
		self.frame_menu.pack()
		self.botao_adcionar = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Adicionar Academia",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(CadastrarAcademia),activebackground='green',font=FONTE_PADRAO)
		self.botao_listar = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Listar Academia",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(ListarAcademia),activebackground='green',font=FONTE_PADRAO)
		self.botao_listar_participante = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Listar Participante",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(ListarParticipante),activebackground='green',font=FONTE_PADRAO)
		self.botao_remover = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Remover Academia",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(RemoverAcademia),activebackground='green',font=FONTE_PADRAO)
		self.botao_carteirinha = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Gerar Carteirinha",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(GerarCarteirinha),activebackground='green',font=FONTE_PADRAO)
		self.botao_sair = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Voltar",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(MenuPrincipal),activebackground='green',font=FONTE_PADRAO)
		self.botao_adcionar.pack()
		self.botao_listar.pack()
		self.botao_listar_participante.pack()
		self.botao_remover.pack()
		self.botao_carteirinha.pack()
		self.botao_sair.pack()

#CLASSE RESPONSAVEL PELO MENU TORNEIO
class MenuTorneio(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		self.frame_menu = Frame(self, bg = COR_FUNDO,pady=100,padx=500,height=500,width=900)
		self.frame_menu.pack()
		self.botao_adicionar = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Adicionar Torneio",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(CadastrarTorneio),activebackground='green',font=FONTE_PADRAO)
		self.botao_buscar = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Buscar Torneio",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(MenuTorneioBuscas),activebackground='green',font=FONTE_PADRAO)
		self.botao_remover = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Remover Torneio",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(RemoverTorneio),activebackground='green',font=FONTE_PADRAO)
		self.botao_listar = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Listar Torneio",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(ListarTorneio),activebackground='green',font=FONTE_PADRAO)
		self.botao_sair = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Voltar",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(MenuPrincipal),activebackground='green',font=FONTE_PADRAO)
		self.botao_adicionar.pack()
		self.botao_buscar.pack()
		self.botao_remover.pack()
		self.botao_listar.pack()
		self.botao_sair.pack()
#CLASSE RESPONSAVEL PELO MENU DE BUSCAS DE TORNEIO
class MenuTorneioBuscas(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		self.frame_menu = Frame(self, bg = COR_FUNDO,pady=100,padx=500,height=500,width=900)
		self.frame_menu.pack()
		self.botao_buscar_nome = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Buscar Torneio por nome",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(TorneioBuscaNome),activebackground='green',font=FONTE_PADRAO)
		self.botao_buscar_id = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Buscar Torneio por Id",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(TorneioBuscaId),activebackground='green',font=FONTE_PADRAO)
		self.botao_sair = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Voltar",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(MenuTorneio),activebackground='green',font=FONTE_PADRAO)
		self.botao_buscar_nome.pack()
		self.botao_buscar_id.pack()
		self.botao_sair.pack()
#CLASSE RESPONSAVEL PELA TELA DE BUSCA DE TORNEIO POR NOME
class TorneioBuscaNome(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)

		self['bg'] = COR_FUNDO
		
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=80)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text= "Buscar Torneio por nome",width=60,height=4,font=FONTE_PADRAO)
		self.titulo.grid(row=0,column=1)
		self.frame_participante = Frame(self, bg = COR_FUNDO,pady=20)
		self.frame_participante.pack()
		self.nome = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Nome Torneio : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.entrada_nome = Entry(self.frame_participante,width=80)
		self.nome.grid(row=0,column=0)
		self.entrada_nome.grid(row=0,column=1)
		self.frame_botoes = Frame(self, bg = COR_FUNDO,pady=10)
		self.frame_botoes.pack()
		self.botao_buscar = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text = "Buscar Torneio",width = int(LARGURA_PADRAO/3),command = None,activebackground='green',font=FONTE_PADRAO)
		self.botao_buscar.grid(row=0,column=0)
		self.botao_cancel = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text = "Cancelar",width = int(LARGURA_PADRAO/3),command = lambda:self.voltar(controler),activebackground='green',font=FONTE_PADRAO)
		self.botao_cancel.grid(row=0,column=10)
	def voltar(self,controler):
		self.entrada_nome.delete(0,END)
		controler.show_frame(MenuTorneioBuscas)
	def buscar_participante(self, controler):
		global Base_Torneio
		Base_Torneio.set_nome(self.entrada_nome.get())
		if Base_Torneio.nome_vazio():
			messagebox.showwarning("Aviso", "Preencha o campo Nome.")
		else:
			if Base_Torneio.este_torneio_existe():
				messagebox.showinfo("Sucesso", "Torneio encontrado.")
				self.limpar_campos()
				controler.show_frame(ExibeCarteirinha)
			else:
				messagebox.showerror("Erro", "Torneio nao encontrado.")
				self.limpar_campos()
	def limpar_campos(self):
		self.entrada_nome.delete(0,END)
#CLASSE RESPONSAVEL PELA TELA DE BUSCA DE TORNEIO POR ID
class TorneioBuscaId(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)

		self['bg'] = COR_FUNDO
		
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=80)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text= "Buscar Torneio por ID",font=FONTE_PADRAO,width=60,height=4)
		self.titulo.grid(row=0,column=1)
		self.frame_participante = Frame(self, bg = COR_FUNDO,pady=20)
		self.frame_participante.pack()
		self.id = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="ID Torneio : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.entrada_id = Entry(self.frame_participante,width=80)
		self.id.grid(row=0,column=0)
		self.entrada_id.grid(row=0,column=1)
		self.frame_botoes = Frame(self, bg = COR_FUNDO,pady=10)
		self.frame_botoes.pack()
		self.botao_buscar = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text = "Buscar Torneio",width = int(LARGURA_PADRAO/3),command = None,activebackground='green',font=FONTE_PADRAO)
		self.botao_buscar.grid(row=0,column=0)
		self.botao_cancel = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text = "Cancelar",width = int(LARGURA_PADRAO/3),command = lambda:self.voltar(controler),activebackground='green',font=FONTE_PADRAO)
		self.botao_cancel.grid(row=0,column=10)
	def voltar(self,controler):
		self.entrada_id.delete(0,END)
		controler.show_frame(MenuTorneioBuscas)
	def buscar_participante(self, controler):
		global Base_Torneio
		Base_Torneio.set_id(self.entrada_id.get())
		if Base_Torneio.nome_vazio():
			messagebox.showwarning("Aviso", "Preencha o campo ID.")
		else:
			busca = Base_Torneio.buscar_torneio_id()
			if resultado != None:
				messagebox.showinfo("Sucesso", "Torneio encontrado.")
				self.limpar_campos()
				controler.show_frame(ExibeCarteirinha)
			else:
				messagebox.showerror("Erro", "Torneio nao encontrado.")
				self.limpar_campos()
	def limpar_campos(self):
		self.entrada_id.delete(0,END)
#CLASSE RESPONSAVEL PELO MENU PARTICIPANTE
class MenuParticipante(Frame):

	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		self.frame_menu = Frame(self, bg = COR_FUNDO,pady=100)
		self.frame_menu.pack()
		self.botao_participante_academia = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Adicionar a Academia",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(CadastrarParticipante),activebackground='green',font=FONTE_PADRAO)
		self.botao_participante_torneio = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Adicionar a Torneio",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(CadastrarParticipanteTorneio),activebackground='green',font=FONTE_PADRAO)
		self.botao_participante_remove_academia = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Remover de Academia",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command =None,activebackground='green',font=FONTE_PADRAO)
		self.botao_participante_remove_torneio = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Remover de Torneio",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command =  None,activebackground='green',font=FONTE_PADRAO)
		self.botao_sair = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Voltar",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(MenuPrincipal),activebackground='green',font=FONTE_PADRAO)
		self.botao_participante_academia.pack()
		self.botao_participante_torneio.pack()
		self.botao_participante_remove_academia.pack()
		self.botao_participante_remove_torneio.pack()
		self.botao_sair.pack()
#CLASSE RESPONSAVEL PELO MENU SECRETARIO
class MenuSecretario(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		self.frame_menu = Frame(self, bg = COR_FUNDO,pady=100)
		self.frame_menu.pack()
		self.botao_adcionar = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Adcionar Secretario",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(CadastrarSecretario),activebackground='green',font=FONTE_PADRAO)
		self.botao_listar = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Listar Secretario",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(ListarSecretario),activebackground='green',font=FONTE_PADRAO)
		self.botao_remover = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Remover Secretario",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(RemoverSecretario),activebackground='green',font=FONTE_PADRAO)
		self.botao_sair = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Voltar Secretario",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(MenuPrincipal),activebackground='green',font=FONTE_PADRAO)
		self.botao_adcionar.pack()
		self.botao_listar.pack()
		self.botao_remover.pack()
		self.botao_sair.pack()
#CLASSE RESPONSAVEL PELO CADASTRO DE PARTICIPANTE
class CadastrarParticipante(Frame):
	def __init__(self,parent,controler):
		
		Frame.__init__(self,parent)
		
		self.sexo = "Masculino"
		self.tipo = "Professor"
		
		self.sexo_aux = IntVar()
		self.tipo_aux = IntVar()
		
		self['bg'] = COR_FUNDO
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=80)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=8,relief=TIPO_BORDA_BOTAO,text= "Cadastro Participante",font=FONTE_PADRAO,width=60,height=4)
		self.titulo.grid(row=0,column=1)
		
		self.frame_participante = Frame(self, bg = COR_FUNDO,pady=20)
		self.frame_participante.pack()
		
		self.nome = Label(self.frame_participante,border= int(TAMANHO_BORDA_BOTAO/4),relief=TIPO_BORDA_BOTAO,text="Nome : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.nascimento = Label(self.frame_participante,border=int(TAMANHO_BORDA_BOTAO/4),relief=TIPO_BORDA_BOTAO,text="Data de Nascimento : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.academia = Label(self.frame_participante,border=int(TAMANHO_BORDA_BOTAO/4),relief=TIPO_BORDA_BOTAO,text="Academia: ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.graduacao = Label(self.frame_participante,border=int(TAMANHO_BORDA_BOTAO/4),relief=TIPO_BORDA_BOTAO,text="Graduacao: ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.combo_graduacao = ttk.Combobox(self.frame_participante,text="Graduacao: ",width=66,font=FONTE_PADRAO)
		self.combo_graduacao['values'] = ["Branca","Cinza","Amarela","Laranja","Verde","Roxa","Marrom","Preta","Vermelha"]
		self.telefone = Label(self.frame_participante,border=int(TAMANHO_BORDA_BOTAO/4),relief=TIPO_BORDA_BOTAO,text="Telefone: ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.cpf = Label(self.frame_participante,border=int(TAMANHO_BORDA_BOTAO/4),relief=TIPO_BORDA_BOTAO,text="CPF : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.endereco = Label(self.frame_participante,border=int(TAMANHO_BORDA_BOTAO/4),relief=TIPO_BORDA_BOTAO,text="Endereco : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		
		self.entrada_nome = Entry(self.frame_participante,width=80)
		self.entrada_nascimento = Entry(self.frame_participante,width=80)
		self.entrada_academia = Entry(self.frame_participante,width=80)
		self.entrada_graduacao = Entry(self.frame_participante,width=80)
		self.entrada_telefone = Entry(self.frame_participante,width=80)
		self.entrada_cpf = Entry(self.frame_participante,width=80)
		self.entrada_endereco = Entry(self.frame_participante,width=80)
		
		self.nome.grid(row=0,column=0)
		self.nascimento.grid(row=1,column=0)
		self.academia.grid(row=2,column=0)
		self.graduacao.grid(row=3,column=0)
		self.telefone.grid(row=4,column=0)
		self.cpf.grid(row=5,column=0)
		self.endereco.grid(row=6,column=0)
		
		self.entrada_nome.grid(row=0,column=1)
		self.entrada_nascimento.grid(row=1,column=1)
		self.entrada_academia.grid(row=2,column=1)
		self.combo_graduacao.grid(row=3,column=1)
		self.entrada_telefone.grid(row=4,column=1)
		self.entrada_cpf.grid(row=5,column=1)
		self.entrada_endereco.grid(row=6,column=1)
		
		self.frame_tipo = Frame(self,pady=10)
		self.frame_tipo.pack()
		
		self.tipo1 = Radiobutton(self.frame_tipo,text="Professor",padx = 20,value=1,variable=self.tipo_aux)
		self.tipo1.select()
		self.tipo1.pack(side = LEFT)
		self.tipo2 = Radiobutton(self.frame_tipo,text="Instrutor",padx = 20,value=2,variable=self.tipo_aux)
		self.tipo2.pack(side = LEFT)
		self.tipo3 = Radiobutton(self.frame_tipo,text="Aluno",padx = 20,value=3,variable=self.tipo_aux)
		self.tipo3.pack(side = LEFT)
		
		self.frame_sexo = Frame(self,pady=10)
		self.frame_sexo.pack()
		
		self.sexo1 = Radiobutton(self.frame_sexo,text="Masculino",padx = 20,value=1,variable=self.sexo_aux)
		self.sexo1.select()
		self.sexo1.pack(side = LEFT)
		self.sexo2 = Radiobutton(self.frame_sexo,text="Feminino",padx = 20,value=2,variable=self.sexo_aux)
		self.sexo2.pack(side = LEFT)
		
		self.frame_botoes = Frame(self, bg = COR_FUNDO,pady=10)
		self.frame_botoes.pack()
		self.botao_salvar = Button(self.frame_botoes, text = "Salvar",width = int(LARGURA_PADRAO/3),command = lambda:self.valida_dados(controler),activebackground='green',font=FONTE_PADRAO)
		self.botao_salvar.grid(row=0,column=0)
		self.botao_cancel = Button(self.frame_botoes, text = "Cancelar",width = int(LARGURA_PADRAO/3),command = lambda:self.voltar(controler),activebackground='green',font=FONTE_PADRAO)
		self.botao_cancel.grid(row=0,column=10)		
		
	def voltar(self,controler):
		global Base_Participante
		Base_Participante.inicializacao_padrao()
		controler.show_frame(MenuParticipante)
	def tipo_sexo(self):
		if self.sexo_aux.get() == 1:
			self.sexo = "Masculino"
		else:
			self.sexo = "Feminino"
	def tipo_participante(self):
		if self.tipo_aux.get() == 1:
			self.tipo = "Professor"
		if self.tipo_aux == 2:
			self.tipo = "Instrutor"
		else:
			self.tipo = "Aluno"
	def valida_dados(self,controler):
		global Base_Participante
		
		self.tipo_sexo()
		self.tipo_participante()
		
		Base_Participante.set_nome(self.entrada_nome.get())
		Base_Participante.set_cpf(self.entrada_cpf.get())
		Base_Participante.set_nascimento(self.entrada_nascimento.get())
		Base_Participante.set_academia(self.entrada_academia.get())
		Base_Participante.set_graduacao(self.combo_graduacao.get())
		Base_Participante.set_tipo(self.tipo)
		Base_Participante.set_sexo(self.sexo)
		Base_Participante.set_telefone(self.entrada_telefone.get())
		Base_Participante.set_endereco(self.entrada_endereco.get())

		if Base_Participante.nome_vazio() and Base_Participante.nascimento_vazio() and Base_Participante.cpf_vazio() and Base_Participante.academia_vazia() and Base_Participante.graduacao_vazia() and Base_Participante.telefone_vazio() and Base_Participante.endereco_vazio() and Base_Participante.tipo_vazio():
			messagebox.showwarning("Aviso", "Preencha os Campos.")
		elif(Base_Participante.nome_vazio()):
			messagebox.showwarning("Aviso", "Preencha o Campo Nome.")
		elif(Base_Participante.nascimento_vazio()):
			messagebox.showwarning("Aviso", "Preencha o Campo Nascimento.")
		elif(Base_Participante.cpf_vazio()):
			messagebox.showwarning("Aviso", "Preencha o Campo Cpf.")
		elif(Base_Participante.academia_vazia()):
			messagebox.showwarning("Aviso", "Preencha o Campo Academia.")
		elif(Base_Participante.graduacao_vazia()):
			messagebox.showwarning("Aviso", "Preencha o Campo Graduacao.")
		elif(Base_Participante.telefone_vazio()):
			messagebox.showwarning("Aviso", "Preencha o Campo Telefone.")
		elif(Base_Participante.endereco_vazio()):
			messagebox.showwarning("Aviso", "Preencha o Campo Endereco.")
		elif not Base_Participante.data_nascimento_valida():
			messagebox.showwarning("Aviso", "Data Nascimento invalida!")
		elif Base_Participante.nome_tem_caracteres_especiais():
			messagebox.showwarning("Aviso", "Nome invalido!")
		elif Base_Participante.graduacao_valida():
			messagebox.showwarning("Aviso", "Graduacao invalida!")	
		elif(not Base_Participante.este_participante_existe()):
			if Base_Participante.salvar_participante():
				self.limpar_campos()
				messagebox.showinfo("Sucesso","Participante cadastrado com sucesso!")
			else:
				messagebox.showerror("Erro", "Ocorreu um erro!")
		else:
			self.limpar_campos()
			messagebox.showerror("Erro", "Participante ja cadastrado!")
			
	def limpar_campos(self):
		self.tipo = "Professor"
		self.sexo = "Masculino"
		self.entrada_nome.delete(0, END)
		self.entrada_academia.delete(0, END)
		self.entrada_cpf.delete(0, END)
		self.entrada_nascimento.delete(0, END)
		self.entrada_graduacao.delete(0, END)
		self.entrada_telefone.delete(0, END)
		self.entrada_endereco.delete(0, END)
#CLASSE RESPONSAVEL PELO CADASTRO DE PARTICIPANTE TORNEIO
class CadastrarParticipanteTorneio(Frame):
	def __init__(self,parent,controler):
		
		Frame.__init__(self,parent)
		self.sexo = "Masculino"
		self.tipo = "Professor"
		self.sexo_aux = IntVar()
		self.tipo_aux = IntVar()
		self['bg'] = COR_FUNDO
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=80)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=8,relief=TIPO_BORDA_BOTAO,text= "Cadastro Participante Torneio",font=FONTE_PADRAO,width=60,height=4)
		self.titulo.grid(row=0,column=1)
		
		self.frame_participante = Frame(self, bg = COR_FUNDO,pady=20)
		self.frame_participante.pack()
		
		self.nome = Label(self.frame_participante,border= int(TAMANHO_BORDA_BOTAO/4),relief=TIPO_BORDA_BOTAO,text="Nome : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.nascimento = Label(self.frame_participante,border=int(TAMANHO_BORDA_BOTAO/4),relief=TIPO_BORDA_BOTAO,text="Data de Nascimento : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.academia = Label(self.frame_participante,border=int(TAMANHO_BORDA_BOTAO/4),relief=TIPO_BORDA_BOTAO,text="Academia: ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.graduacao = Label(self.frame_participante,border=int(TAMANHO_BORDA_BOTAO/4),relief=TIPO_BORDA_BOTAO,text="Graduacao: ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.combo_graduacao = ttk.Combobox(self.frame_participante,text="Graduacao: ",width=66,font=FONTE_PADRAO)
		self.combo_graduacao['values'] = ["Branca","Cinza","Amarela","Laranja","Verde","Roxa","Marrom","Preta","Vermelha"]
		self.telefone = Label(self.frame_participante,border=int(TAMANHO_BORDA_BOTAO/4),relief=TIPO_BORDA_BOTAO,text="Telefone: ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.cpf = Label(self.frame_participante,border=int(TAMANHO_BORDA_BOTAO/4),relief=TIPO_BORDA_BOTAO,text="CPF : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.endereco = Label(self.frame_participante,border=int(TAMANHO_BORDA_BOTAO/4),relief=TIPO_BORDA_BOTAO,text="Endereco : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.torneio = Label(self.frame_participante,border=int(TAMANHO_BORDA_BOTAO/4),relief=TIPO_BORDA_BOTAO,text="Torneio : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		
		self.entrada_nome = Entry(self.frame_participante,width=80)
		self.entrada_nascimento = Entry(self.frame_participante,width=80)
		self.entrada_academia = Entry(self.frame_participante,width=80)
		self.entrada_telefone = Entry(self.frame_participante,width=80)
		self.entrada_cpf = Entry(self.frame_participante,width=80)
		self.entrada_endereco = Entry(self.frame_participante,width=80)
		self.entrada_torneio = Entry(self.frame_participante,width=80)
		
		self.nome.grid(row=0,column=0)
		self.nascimento.grid(row=1,column=0)
		self.academia.grid(row=2,column=0)
		self.graduacao.grid(row=3,column=0)
		self.telefone.grid(row=4,column=0)
		self.cpf.grid(row=5,column=0)
		self.endereco.grid(row=6,column=0)
		self.torneio.grid(row=7,column=0)
		
		self.entrada_nome.grid(row=0,column=1)
		self.entrada_nascimento.grid(row=1,column=1)
		self.entrada_academia.grid(row=2,column=1)
		self.combo_graduacao.grid(row=3,column=1)
		self.entrada_telefone.grid(row=4,column=1)
		self.entrada_cpf.grid(row=5,column=1)
		self.entrada_endereco.grid(row=6,column=1)
		self.entrada_torneio.grid(row=7,column=1)

		self.frame_tipo = Frame(self,pady=10)
		self.frame_tipo.pack()
		
		self.tipo1 = Radiobutton(self.frame_tipo,text="Professor",padx = 20,value=1,variable=self.tipo_aux)
		self.tipo1.select()
		self.tipo1.pack(side = LEFT)
		self.tipo2 = Radiobutton(self.frame_tipo,text="Instrutor",padx = 20,value=2,variable=self.tipo_aux)
		self.tipo2.pack(side = LEFT)
		self.tipo3 = Radiobutton(self.frame_tipo,text="Aluno",padx = 20,value=3,variable=self.tipo_aux)
		self.tipo3.pack(side = LEFT)
		
		self.frame_sexo = Frame(self,pady=10)
		self.frame_sexo.pack()
		
		self.sexo1 = Radiobutton(self.frame_sexo,text="Masculino",padx = 20,value=1,variable=self.sexo_aux)
		self.sexo1.select()
		self.sexo1.pack(side = LEFT)
		self.sexo2 = Radiobutton(self.frame_sexo,text="Feminino",padx = 20,value=2,variable=self.sexo_aux)
		self.sexo2.pack(side = LEFT)
		
		self.frame_botoes = Frame(self, bg = COR_FUNDO,pady=10)
		self.frame_botoes.pack()
		self.botao_salvar = Button(self.frame_botoes, text = "Salvar",border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,width = int(LARGURA_PADRAO/3),command = self.valida_dados,activebackground='green',font=FONTE_PADRAO)
		self.botao_salvar.grid(row=0,column=0)
		self.botao_cancel = Button(self.frame_botoes, text = "Cancelar",border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,width = int(LARGURA_PADRAO/3),command = lambda:self.voltar(controler),activebackground='green',font=FONTE_PADRAO)
		self.botao_cancel.grid(row=0,column=10)		
	def voltar(self,controler):
		global Base_Participante_Torneio
		Base_Participante_Torneio.inicializacao_padrao()
		controler.show_frame(MenuParticipante)
	def tipo_sexo(self):
		if self.sexo_aux.get() == 1:
			self.sexo = "Masculino"
		else:
			self.sexo = "Feminino"
	def tipo_participante(self):
		if self.tipo_aux.get() == 1:
			self.tipo = "Professor"
		if self.tipo_aux == 2:
			self.tipo = "Instrutor"
		else:
			self.tipo = "Aluno"
	def valida_dados(self):
		global Base_Participante_Torneio
		self.tipo_sexo()
		self.tipo_participante()
		Base_Participante_Torneio.set_nome(self.entrada_nome.get())
		Base_Participante_Torneio.set_cpf(self.entrada_cpf.get())
		Base_Participante_Torneio.set_nascimento(self.entrada_nascimento.get())
		Base_Participante_Torneio.set_academia(self.entrada_academia.get())
		Base_Participante_Torneio.set_graduacao(self.combo_graduacao.get())
		Base_Participante_Torneio.set_tipo(self.tipo)
		Base_Participante_Torneio.set_sexo(self.sexo)
		Base_Participante_Torneio.set_telefone(self.entrada_telefone.get())
		Base_Participante_Torneio.set_endereco(self.entrada_endereco.get())

		if Base_Participante_Torneio.nome_vazio() and Base_Participante_Torneio.nascimento_vazio() and Base_Participante_Torneio.cpf_vazio() and Base_Participante_Torneio.academia_vazia() and Base_Participante_Torneio.graduacao_vazia() and Base_Participante_Torneio.telefone_vazio() and Base_Participante_Torneio.endereco_vazio() and Base_Participante_Torneio.tipo_vazio() and Base_Participante_Torneio.torneio_vazio():
			messagebox.showwarning("Aviso", "Preencha os Campos.")
		elif(Base_Participante_Torneio.nome_vazio()):
			messagebox.showwarning("Aviso", "Preencha o Campo Nome.")
		elif(Base_Participante_Torneio.nascimento_vazio()):
			messagebox.showwarning("Aviso", "Preencha o Campo Nascimento.")
		elif(Base_Participante_Torneio.cpf_vazio()):
			messagebox.showwarning("Aviso", "Preencha o Campo Cpf.")
		elif(Base_Participante_Torneio.academia_vazia()):
			messagebox.showwarning("Aviso", "Preencha o Campo Academia.")
		elif(Base_Participante_Torneio.graduacao_vazia()):
			messagebox.showwarning("Aviso", "Preencha o Campo Graduacao.")
		elif(Base_Participante_Torneio.telefone_vazio()):
			messagebox.showwarning("Aviso", "Preencha o Campo Telefone.")
		elif(Base_Participante_Torneio.endereco_vazio()):
			messagebox.showwarning("Aviso", "Preencha o Campo Endereco.")
		elif(Base_Participante_Torneio.torneio_vazio()):
			messagebox.showwarning("Aviso", "Preencha o Campo Torneio.")
		elif(not Base_Participante_Torneio.data_nascimento_valida()):
			messagebox.showerror("Aviso", "Data Nascimento invalida!")
		elif(not Base_Participante_Torneio.graduacao_valida()):
			messagebox.showerror("Aviso", "Graduacao invalida!")
		elif(not Base_Participante_Torneio.este_participante_existe()):
			if Base_Participante_Torneio.salvar_participante():
				self.limpar_campos()
				messagebox.showinfo("Sucesso","Participante cadastrado com sucesso!")
			else:
				messagebox.showerror("Erro", "Ocorreu um erro!")
		else:
			self.limpar_campos()
			messagebox.showerror("Erro", "Participante ja cadastrado!")
			
	def limpar_campos(self):
		self.tipo = "Professor"
		self.sexo = "Masculino"
		self.ativar_sexo_m()
		self.ativar_tipo1()
		self.entrada_nome.delete(0, END)
		self.entrada_academia.delete(0, END)
		self.entrada_cpf.delete(0, END)
		self.entrada_nascimento.delete(0, END)
		self.entrada_graduacao.delete(0, END)
		self.entrada_telefone.delete(0, END)
		self.entrada_endereco.delete(0, END)
		self.entrada_torneio.delete(0, END)
		
#CLASSE RESPONSAVEL PELO CADASTRO DE SECRETARIO
class CadastrarSecretario(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=80)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text= "Adicionar Secretario",font=FONTE_PADRAO,width=60,height=4)
		self.titulo.grid(row=0,column=1)
		
		self.frame_participante = Frame(self, bg = COR_FUNDO,pady=20)
		self.frame_participante.pack()
		
		self.login = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Login : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.senha = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Senha : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.rep_senha = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Repita a senha : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		
		self.entrada_login = Entry(self.frame_participante,width=80)
		self.entrada_senha = Entry(self.frame_participante,width=80,show="*",)
		self.entrada_rep_senha = Entry(self.frame_participante,width=80,show="*",)
		
		self.login.grid(row=0,column=0)
		self.senha.grid(row=1,column=0)
		self.rep_senha.grid(row=2,column=0)
		
		self.entrada_login.grid(row=0,column=1)
		self.entrada_senha.grid(row=1,column=1)
		self.entrada_rep_senha.grid(row=2,column=1)
		
		self.frame_botoes = Frame(self, bg = COR_FUNDO,pady=10)
		self.frame_botoes.pack()
		self.botao_salvar = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text = "Salvar",width = int(LARGURA_PADRAO/3),command = lambda:self.valida_dados(controler),activebackground='green',font=FONTE_PADRAO)
		self.botao_salvar.grid(row=0,column=0)
		self.botao_cancel = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text = "Cancelar",width = int(LARGURA_PADRAO/3),command = lambda:self.voltar(controler),activebackground='green',font=FONTE_PADRAO)
		self.botao_cancel.grid(row=0,column=10)
	def voltar(self, controler):
		global Base_Secretario
		Base_Secretario.inicializacao_padrao()
		controler.show_frame(MenuSecretario)
	def limpar_campos(self,controler):
		self.entrada_login.delete(0,END)
		self.entrada_senha.delete(0,END)
		self.entrada_rep_senha.delete(0,END)
	def valida_dados(self,controler):
	
		global Base_Secretario
		
		Base_Secretario.set_login(self.entrada_login.get())
		Base_Secretario.set_senha(self.entrada_senha.get())
		
		rep_senha = self.entrada_rep_senha.get()
		if(Base_Secretario.login_vazio() and Base_Secretario.senha_vazia() and rep_senha==""):
			messagebox.showwarning("Aviso", "Preencha os Campos!")
		elif(Base_Secretario.login_vazio()):
			messagebox.showwarning("Aviso", "Preencha o Campo Login!")
		elif(Base_Secretario.senha_vazia()):
			messagebox.showwarning("Aviso", "Preencha o Campo Senha!")
		elif(rep_senha==""):
			messagebox.showwarning("Aviso", "Preencha o Campo Rep_senha!")
		elif(not (Base_Secretario.get_senha() == rep_senha)):
			messagebox.showwarning("Aviso", "Senhas diferem!")
		else:
			if(not Base_Secretario.este_secretario_existe()):			
				if Base_Secretario.salvar_secretario():
					messagebox.showinfo("Sucesso", "Usuario adcionado com sucesso")
					Base_Secretario.inicializacao_padrao()
				else:
					messagebox.showerror("Erro", "Nao foi possivel cadastrar")
			else:
				messagebox.showerror("Erro", "Secretario ja cadastrado!")
			self.limpar_campos(controler)
#CLASSE RESPONSAVEL PELO CADASTRO DE TORNEIO
class CadastrarAcademia(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=100,padx=10,height=600,width=900)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text= "Adicionar Academia",font=FONTE_PADRAO,width=40,height=2)
		self.titulo.grid(row=0,column=1)
		
		self.frame_participante = Frame(self, bg = COR_FUNDO,pady=90,padx=0,height=300,width=900)
		self.frame_participante.pack()
		
		self.nome = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Nome da Academia : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.local = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Endereco : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.data = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Data : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.contato = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Contato : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.email = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Email : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.responsavel = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Responsavel : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		
		self.entrada_nome = Entry(self.frame_participante,width=80)
		self.entrada_local = Entry(self.frame_participante,width=80)
		self.entrada_data = Entry(self.frame_participante,width=80)
		self.entrada_contato = Entry(self.frame_participante,width=80)
		self.entrada_email = Entry(self.frame_participante,width=80)
		self.entrada_responsavel = Entry(self.frame_participante,width=80)
		
		self.nome.grid(row=0,column=0)
		self.local.grid(row=1,column=0)
		self.data.grid(row=2,column=0)
		self.contato.grid(row=3,column=0)
		self.email.grid(row=4,column=0)
		self.responsavel.grid(row=5,column=0)
		
		self.entrada_nome.grid(row=0,column=1)
		self.entrada_local.grid(row=1,column=1)
		self.entrada_data.grid(row=2,column=1)
		self.entrada_contato.grid(row=3,column=1)
		self.entrada_email.grid(row=4,column=1)
		self.entrada_responsavel.grid(row=5,column=1)
	
		self.frame_botoes = Frame(self, bg = COR_FUNDO,pady=10)
		self.frame_botoes.pack()
		self.botao_salvar = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text = "Salvar",width = int(LARGURA_PADRAO/3),command = lambda:self.salvar_dados(),activebackground='green',font=FONTE_PADRAO)
		self.botao_salvar.grid(row=0,column=0)
		self.botao_cancel = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text = "Cancelar",width = int(LARGURA_PADRAO/3),command = lambda:self.voltar(controler),activebackground='green',font=FONTE_PADRAO)
		self.botao_cancel.grid(row=0,column=10)
	def voltar(self,controler):
		self.limpar_campos()
		controler.show_frame(MenuAcademia)
	def limpar_campos(self):
		self.entrada_nome.delete(0,END)
		self.entrada_local.delete(0,END)
		self.entrada_data.delete(0,END)
		self.entrada_contato.delete(0,END)
		self.entrada_email.delete(0,END)
		self.entrada_responsavel.delete(0,END)
	def salvar_dados(self):
		global Base_Academia
		Base_Academia.set_nome(self.entrada_nome.get())
		Base_Academia.set_local(self.entrada_local.get())
		Base_Academia.set_data(self.entrada_data.get())
		Base_Academia.set_contato(self.entrada_contato.get())
		Base_Academia.set_email(self.entrada_email.get())
		Base_Academia.set_responsavel(self.entrada_responsavel.get())
		if Base_Academia.nome_vazio() and Base_Academia.local_vazio() and Base_Academia.data_vazia() and Base_Academia.contato_vazio() and Base_Academia.email_vazio() and Base_Academia.responsavel_vazio():
			messagebox.showwarning("Aviso", "Preencha os campos.")
		elif Base_Academia.nome_vazio():
			messagebox.showwarning("Aviso", "Preencha o campo Nome.")
		elif Base_Academia.local_vazio():
			messagebox.showwarning("Aviso", "Preencha o campo Endereco.")
		elif Base_Academia.data_vazia():
			messagebox.showwarning("Aviso", "Preencha o campo Data.")
		elif Base_Academia.contato_vazio():
			messagebox.showwarning("Aviso", "Preencha o campo Contato.")
		elif Base_Academia.email_vazio():
			messagebox.showwarning("Aviso", "Preencha o campo Email.")
		elif Base_Academia.responsavel_vazio():
			messagebox.showwarning("Aviso", "Preencha o campo Responsavel.")
		elif not Base_Academia.contato_valido():
			messagebox.showwarning("Aviso", "Contato invalido!")
		elif not Base_Academia.data_valida():
			messagebox.showwarning("Aviso", "Data invalida!")
		elif not Base_Academia.email_valido():
			messagebox.showwarning("Aviso", "Email invalido!")
		else:
			if not Base_Academia.esta_academia_existe():
				if Base_Academia.salvar_academia():
					messagebox.showinfo("Sucesso", "Academia cadastrada com sucesso.")
					self.limpar_campos()
				else:
					messagebox.showerror("Erro", "Ocorreu um erro!")
			else:
				messagebox.showerror("Erro", "Esta Academia ja esta cadastrada!")
				self.limpar_campos()
#CLASSE RESPONSAVEL PELO CADASTRO DE TORNEIO
class CadastrarTorneio(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=100,padx=10,height=600,width=900)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text= "Adicionar Torneio",font=FONTE_PADRAO,width=40,height=2)
		self.titulo.grid(row=0,column=1)
		
		self.frame_participante = Frame(self, bg = COR_FUNDO,pady=90,padx=0,height=300,width=900)
		self.frame_participante.pack()
		
		self.nome = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Nome do Torneio : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.local = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Local : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.data = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Data : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.horario = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Horario : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.valor = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Valor : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.organizador = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Organizador : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.contato = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Contato : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		
		self.entrada_nome = Entry(self.frame_participante,width=80)
		self.entrada_local = Entry(self.frame_participante,width=80)
		self.entrada_data = Entry(self.frame_participante,width=80)
		self.entrada_horario = Entry(self.frame_participante,width=80)
		self.entrada_valor = Entry(self.frame_participante,width=80)
		self.entrada_organizador = Entry(self.frame_participante,width=80)
		self.entrada_contato = Entry(self.frame_participante,width=80)
		
		self.nome.grid(row=0,column=0)
		self.local.grid(row=1,column=0)
		self.data.grid(row=2,column=0)
		self.horario.grid(row=3,column=0)
		self.valor.grid(row=4,column=0)
		self.organizador.grid(row=5,column=0)
		self.contato.grid(row=6,column=0)
		
		self.entrada_nome.grid(row=0,column=1)
		self.entrada_local.grid(row=1,column=1)
		self.entrada_data.grid(row=2,column=1)
		self.entrada_horario.grid(row=3,column=1)
		self.entrada_valor.grid(row=4,column=1)
		self.entrada_organizador.grid(row=5,column=1)
		self.entrada_contato.grid(row=6,column=1)
		
		self.frame_botoes = Frame(self, bg = COR_FUNDO,pady=10)
		self.frame_botoes.pack()
		self.botao_salvar = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text = "Salvar",width = int(LARGURA_PADRAO/3),command = lambda:self.salvar_dados(),activebackground='green',font=FONTE_PADRAO)
		self.botao_salvar.grid(row=0,column=0)
		self.botao_cancel = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text = "Cancelar",width = int(LARGURA_PADRAO/3),command = lambda:self.voltar(controler),activebackground='green',font=FONTE_PADRAO)
		self.botao_cancel.grid(row=0,column=10)
	def voltar(self,controler):
		controler.show_frame(MenuTorneio)
	def limpar_campos(self):
		self.entrada_nome.delete(0,END)
		self.entrada_local.delete(0,END)
		self.entrada_data.delete(0,END)
		self.entrada_valor.delete(0,END)
		self.entrada_horario.delete(0,END)
		self.entrada_organizador.delete(0,END)
		self.entrada_contato.delete(0,END)
	def salvar_dados(self):
		global Base_Torneio
		Base_Torneio.set_nome(self.entrada_nome.get())
		Base_Torneio.set_local(self.entrada_local.get())
		Base_Torneio.set_data(self.entrada_data.get())
		Base_Torneio.set_valor(self.entrada_valor.get())
		Base_Torneio.set_horario(self.entrada_horario.get())
		Base_Torneio.set_organizador(self.entrada_organizador.get())
		Base_Torneio.set_contato(self.entrada_contato.get())
		if Base_Torneio.nome_vazio() and Base_Torneio.local_vazio() and Base_Torneio.data_vazia() and Base_Torneio.valor_vazio() and Base_Torneio.organizador_vazio() and Base_Torneio.contato_vazio():
			messagebox.showwarning("Aviso", "Preencha os campos.")
		elif Base_Torneio.nome_vazio():
			messagebox.showwarning("Aviso", "Preencha o campo Nome.")
		elif Base_Torneio.local_vazio():
			messagebox.showwarning("Aviso", "Preencha o campo Local.")
		elif Base_Torneio.data_vazia():
			messagebox.showwarning("Aviso", "Preencha o campo Data.")
		elif Base_Torneio.valor_vazio():
			messagebox.showwarning("Aviso", "Preencha o campo Valor.")
		elif Base_Torneio.organizador_vazio():
			messagebox.showwarning("Aviso", "Preencha o campo Organizador.")
		elif Base_Torneio.contato_vazio():
			messagebox.showwarning("Aviso", "Preencha o campo Contato.")
		elif not Base_Torneio.este_torneio_existe():
			if Base_Torneio.salvar_torneio():
				messagebox.showinfo("Sucesso", "Torneio cadastrado com sucesso.")
				self.limpar_campos()
			else:
				messagebox.showerror("Erro", "Ocorreu um erro!")
		else:
			messagebox.showerror("Erro", "Este Torneio ja esta cadastrado!")
			self.limpar_campos()

#CLASSE RESPONSAVEL PELA TELA DE REMOCAO DE ACADEMIA
class RemoverAcademia(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=80)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text= "Remover Academia",font=FONTE_PADRAO,width=60,height=4)
		self.titulo.grid(row=0,column=1)
		
		self.frame_academia = Frame(self, bg = COR_FUNDO,pady=20)
		self.frame_academia.pack()
		
		self.academia = Label(self.frame_academia,border=2,relief=TIPO_BORDA_BOTAO,text="Nome : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.id = Label(self.frame_academia,border=2,relief=TIPO_BORDA_BOTAO,text="ID : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		
		self.entrada_academia = Entry(self.frame_academia,width=80)
		self.entrada_id = Entry(self.frame_academia,width=80)
		
		self.academia.grid(row=0,column=0)
		self.id.grid(row=1,column=0)
		
		self.entrada_academia.grid(row=0,column=1)
		self.entrada_id.grid(row=1,column=1)
		
		self.frame_botoes = Frame(self, bg = COR_FUNDO,pady=10)
		self.frame_botoes.pack()
		self.botao_salvar = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Remover",width = int(LARGURA_PADRAO/3),command = self.remover_academia,activebackground='green',font=FONTE_PADRAO)
		self.botao_salvar.grid(row=0,column=0)
		self.botao_cancel = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Cancelar",width = int(LARGURA_PADRAO/3),command = lambda:self.voltar(controler),activebackground='green',font=FONTE_PADRAO)
		self.botao_cancel.grid(row=0,column=10)
	def remover_academia(self):
		global Base_Academia
		Base_Academia.set_nome(self.entrada_academia.get())
		Base_Academia.set_id(self.entrada_id.get())
		if Base_Academia.nome_vazio() and Base_Academia.id_vazio():
			messagebox.showwarning("Aviso", "Preencha os campos!")
		elif(Base_Academia.nome_vazio()):
			messagebox.showwarning("Aviso", "Preencha o campo Academia!")
		elif(Base_Academia.id_vazio()):
			messagebox.showwarning("Aviso", "Preencha o campo ID!")
		elif(Base_Academia.esta_academia_existe()):
			Base_Academia.remover_academia()
			self.limpar_campos()
			messagebox.showinfo("Sucesso", "Academia removido com sucesso")
		else:
			self.limpar_campos()
			messagebox.showerror("Erro", "Academia nao encontrada!")
	def limpar_campos(self):
		self.entrada_academia.delete(0,END)
		self.entrada_id.delete(0,END)
	def voltar(self,controler):
		Base_Academia.inicializacao_padrao()
		controler.show_frame(MenuAcademia)
#CLASSE RESPONSAVEL PELA TELA DE REMOCAO DE TORNEIO
class RemoverTorneio(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=80)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text= "Remover Torneio",font=FONTE_PADRAO,width=60,height=4)
		self.titulo.grid(row=0,column=1)
		
		self.frame_torneio = Frame(self, bg = COR_FUNDO,pady=20)
		self.frame_torneio.pack()
		
		self.torneio = Label(self.frame_torneio,border=2,relief=TIPO_BORDA_BOTAO,text="Nome : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.id = Label(self.frame_torneio,border=2,relief=TIPO_BORDA_BOTAO,text="ID : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		
		self.entrada_torneio = Entry(self.frame_torneio,width=80)
		self.entrada_id = Entry(self.frame_torneio,width=80)
		
		self.torneio.grid(row=0,column=0)
		self.id.grid(row=1,column=0)
		
		self.entrada_torneio.grid(row=0,column=1)
		self.entrada_id.grid(row=1,column=1)
		
		self.frame_botoes = Frame(self, bg = COR_FUNDO,pady=10)
		self.frame_botoes.pack()
		self.botao_salvar = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Remover",width = int(LARGURA_PADRAO/3),command = self.remover_torneio,activebackground='green',font=FONTE_PADRAO)
		self.botao_salvar.grid(row=0,column=0)
		self.botao_cancel = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Cancelar",width = int(LARGURA_PADRAO/3),command = lambda:self.voltar(controler),activebackground='green',font=FONTE_PADRAO)
		self.botao_cancel.grid(row=0,column=10)
	def remover_torneio(self):
		global Base_Torneio
		Base_Torneio.set_nome(self.entrada_torneio.get())
		Base_Torneio.set_id(self.entrada_id.get())
		if Base_Torneio.nome_vazio() and Base_Torneio.id_vazio():
			messagebox.showwarning("Aviso", "Preencha os campos!")
		elif(Base_Torneio.nome_vazio()):
			messagebox.showwarning("Aviso", "Preencha o campo Torneio!")
		elif(Base_Torneio.id_vazio()):
			messagebox.showwarning("Aviso", "Preencha o campo ID!")
		elif(Base_Torneio.este_torneio_existe()):
			if Base_Torneio.remover_torneio_id_nome():
				self.limpar_campos()
				messagebox.showinfo("Sucesso", "Torneio removido com sucesso")
			else:
				messagebox.showerror("Erro", "Ocorreu um Erro!")
		else:
			self.limpar_campos()
			messagebox.showerror("Erro", "Torneio nao encontrado!")
	def limpar_campos(self):
		self.entrada_torneio.delete(0,END)
		self.entrada_id.delete(0,END)
	def voltar(self,controler):
		Base_Torneio.inicializacao_padrao()
		controler.show_frame(MenuTorneio)
#CLASSE RESPONSAVEL PELA TELA DE REMOCAO DE SECRETARIO
class RemoverSecretario(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=80)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text= "Remover Secretario",font=FONTE_PADRAO,width=60,height=4)
		self.titulo.grid(row=0,column=1)
		
		self.frame_participante = Frame(self, bg = COR_FUNDO,pady=20)
		self.frame_participante.pack()
		
		self.login = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="login : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.senha = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="senha : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		
		self.entrada_login = Entry(self.frame_participante,width=80)
		self.entrada_senha = Entry(self.frame_participante,width=80)
		
		self.login.grid(row=0,column=0)
		self.senha.grid(row=1,column=0)
		
		self.entrada_login.grid(row=0,column=1)
		self.entrada_senha.grid(row=1,column=1)
		
		self.frame_botoes = Frame(self, bg = COR_FUNDO,pady=10)
		self.frame_botoes.pack()
		self.botao_salvar = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Remover",width = int(LARGURA_PADRAO/3),command = self.remover_secretario,activebackground='green',font=FONTE_PADRAO)
		self.botao_salvar.grid(row=0,column=0)
		self.botao_cancel = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Cancelar",width = int(LARGURA_PADRAO/3),command = lambda:self.voltar(controler),activebackground='green',font=FONTE_PADRAO)
		self.botao_cancel.grid(row=0,column=10)
	def remover_secretario(self):
		global Base_Secretario
		Base_Secretario.set_login(self.entrada_login.get())
		Base_Secretario.set_senha(self.entrada_senha.get())
		if Base_Secretario.login_vazio() and Base_Secretario.senha_vazia():
			messagebox.showwarning("Aviso", "Preencha os Campos!")
		elif(Base_Secretario.login_vazio()):
			messagebox.showwarning("Aviso", "Preencha o Campo Login!")
		elif(Base_Secretario.senha_vazia()):
			messagebox.showwarning("Aviso", "Preencha o Campo Senha!")
		elif(Base_Secretario.este_secretario_existe()):
			Base_Secretario.remover_secretario()
			self.limpar_campos()
			messagebox.showinfo("Sucesso", "Secretario removido com sucesso")
			Base_Secretario.inicializacao_padrao()
		else:
			messagebox.showerror("Erro", "Secretario nao encontrado!")
	def limpar_campos(self):
		self.entrada_login.delete(0,END)
		self.entrada_senha.delete(0,END)
	def voltar(self,controler):
		Base_Secretario.inicializacao_padrao()
		controler.show_frame(MenuSecretario)
#CLASSE RESPONSAVEL PELA TELA DE REMOCAO DE PARTICIPANTE
class RemoverParticipante(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=80)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text= "Remover Participante",font=FONTE_PADRAO,width=60,height=4)
		self.titulo.grid(row=0,column=1)
		
		self.frame_participante = Frame(self, bg = COR_FUNDO,pady=20)
		self.frame_participante.pack()
		self.id = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="inscricao/ID : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.entrada_id = Entry(self.frame_participante,width=80)
		self.id.grid(row=0,column=0)
		self.entrada_id.grid(row=0,column=1)
		self.frame_botoes = Frame(self, bg = COR_FUNDO,pady=10)
		self.frame_botoes.pack()
		self.botao_salvar = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Remover",width = int(LARGURA_PADRAO/3),command = lambda:self.remover_secretario(controler),activebackground='green',font=FONTE_PADRAO)
		self.botao_salvar.grid(row=0,column=0)
		self.botao_cancel = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Cancelar",width = int(LARGURA_PADRAO/3),command = lambda:controler.show_frame(MenuSecretario),activebackground='green',font=FONTE_PADRAO)
		self.botao_cancel.grid(row=0,column=10)
		
	def remover_participante(self, controler):
		global Base_Participante
		Base_Participante.set_inscricao(self.entrada_id.get())
		if(Base_Participante.inscricao_vazio()):
			messagebox.showwarning("Aviso", "Preencha o campo inscricao/ID!")
		elif(Base_Participante.este_participante_existe()):
			if Base_Participante.remover_participante():
				self.limpar_campos()
				messagebox.showinfo("Sucesso", "Participante removido com sucesso")
				Base_Secretario.inicializacao_padrao()
			else:
				messagebox.showerror("Erro", "Ocorreu um erro!")
		else:
			messagebox.showerror("Erro", "Participante nao encontrado!")
		controler.show_frame(RemoverSecretario)
	def limpar_campos(self):
		self.entrada_login.delete(0,END)
		self.entrada_senha.delete(0,END)
#CLASSE RESPONSAVEL PELA TELA DE LISIAGEM DE ACADEMIA
class ListarAcademia(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		self.windgets(controler)
	def windgets(self,controler):
		# Inicia o Treeview com as seguintes colunas:
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=10,padx=10,height=600,width=900)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,text= "Listando Academias",border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,font=FONTE_PADRAO,width=40,height=2)
		self.titulo.grid(row=0,column=1)
		self.frame_texto = Frame(self, bg = COR_FUNDO,pady=10,padx=10,height=100,width=100)
		self.frame_texto.pack()
		self.dataCols = ['ID','Nome','Data','Local','Contato','Email','Responsavel']
		self.tree = ttk.Treeview(self.frame_texto,columns=self.dataCols, show='headings')
		self.tree.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
		#diminue a largura da coluna
		self.tree.column("ID",minwidth=30,width=30)
		self.tree.column("Nome",minwidth=100,width=100)
		self.tree.column("Data",minwidth=60,width=60)
		self.tree.column("Local",minwidth=90,width=90)
		self.tree.column("Contato",minwidth=60,width=60)
		self.tree.column("Email",minwidth=90,width=90)
		self.tree.column("Responsavel",minwidth=100,width=100)
		
		# Barras de rolagem
		ysb = ttk.Scrollbar(self.frame_texto,orient=VERTICAL, command=self.tree.yview)
		xsb = ttk.Scrollbar(self.frame_texto,orient=HORIZONTAL, command=self.tree.xview)
		self.tree['yscroll'] = ysb.set
		self.tree['xscroll'] = xsb.set
		ysb.grid(row=0, column=1, sticky=tk.N + tk.S)
		xsb.grid(row=1, column=0, sticky=tk.E + tk.W)
		# Define o textos do cabeçalho (nome em maiúsculas)
		for c in self.dataCols:
			self.tree.heading(c, text=c.title())
		# Dados:
		self.data = Base_Academia.listar_academia()
		# Insere cada item dos dados
		for item in self.data:
			self.tree.insert('', 'end', values=item)
		self.botao = Button(self,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text="Fechar",width= 10, command=lambda:self.voltar(controler),font=FONTE_PADRAO)
		self.botao.pack()
	def voltar(self, controler):
		controler.show_frame(MenuAcademia)
#CLASSE RESPONSAVEL PELA TELA DE LISIAGEM DE TORNEIO
class ListarTorneio(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		self.windgets(controler)
	def windgets(self,controler):
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=10,padx=10,height=600,width=900)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,text= "Listando Torneio",font=FONTE_PADRAO,width=40,height=2)
		self.titulo.grid(row=0,column=1)
		self.frame_texto = Frame(self, bg = COR_FUNDO,pady=10,padx=10,height=100,width=100)
		self.frame_texto.pack()
		self.dataCols = ['ID','Nome','Data','Local','Contato','Horario','Organizador']
		self.tree = ttk.Treeview(self.frame_texto,columns=self.dataCols, show='headings')
		self.tree.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
		#diminue a largura da coluna
		self.tree.column("ID",minwidth=30,width=30)
		self.tree.column("Nome",minwidth=100,width=100)
		self.tree.column("Data",minwidth=60,width=60)
		self.tree.column("Local",minwidth=90,width=90)
		self.tree.column("Contato",minwidth=60,width=60)
		self.tree.column("Horario",minwidth=90,width=90)
		self.tree.column("Organizador",minwidth=100,width=100)
		# Barras de rolagem
		ysb = ttk.Scrollbar(self.frame_texto,orient=VERTICAL, command=self.tree.yview)
		xsb = ttk.Scrollbar(self.frame_texto,orient=HORIZONTAL, command=self.tree.xview)
		self.tree['yscroll'] = ysb.set
		self.tree['xscroll'] = xsb.set
		ysb.grid(row=0, column=1, sticky=tk.N + tk.S)
		xsb.grid(row=1, column=0, sticky=tk.E + tk.W)
		# Define o textos do cabeçalho (nome em maiúsculas)
		for c in self.dataCols:
			self.tree.heading(c, text=c.title())
		# Dados:
		self.data = Base_Torneio.listar_torneio()
		# Insere cada item dos dados
		for item in self.data:
			self.tree.insert('', 'end', values=item)
		self.botao = Button(self,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text="Fechar",width= 10, command=lambda:self.voltar(controler),font=FONTE_PADRAO)
		self.botao.pack()
	def voltar(self, controler):
		controler.show_frame(MenuTorneio)
#CLASSE RESPONSAVEL PELA TELA LISIAGEM DE SECRETARIO
class ListarSecretario(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		self.windgets(controler)
	def windgets(self,controler):
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=10,padx=10,height=600,width=900)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text= "Listando Secretarios",font=FONTE_PADRAO,width=40,height=2)
		self.titulo.grid(row=0,column=1)
		self.frame_texto = Frame(self, bg = COR_FUNDO,pady=10,padx=10,height=100,width=100)
		self.frame_texto.pack()
		
		# Inicia o Treeview com as seguintes colunas:
		self.frame_texto.pack()
		self.dataCols = ['Usuario']
		self.tree = ttk.Treeview(self.frame_texto,columns=self.dataCols, show='headings')
		self.tree.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
		# Barras de rolagem
		ysb = ttk.Scrollbar(self.frame_texto,orient=VERTICAL, command=self.tree.yview)
		xsb = ttk.Scrollbar(self.frame_texto,orient=HORIZONTAL, command=self.tree.xview)
		self.tree['yscroll'] = ysb.set
		self.tree['xscroll'] = xsb.set
		ysb.grid(row=0, column=1, sticky=tk.N + tk.S)
		xsb.grid(row=1, column=0, sticky=tk.E + tk.W)
		# Define o textos do cabeçalho (nome em maiúsculas)
		for c in self.dataCols:
			self.tree.heading(c, text=c.title())
		# Dados:
		self.data = Base_Secretario.listar_secretario()
		# Insere cada item dos dados
		for item in self.data:
			self.tree.insert('', 'end', values=item)
		self.botao = Button(self,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text="Fechar",width= 10, command=lambda:self.voltar(controler),font=FONTE_PADRAO)
		self.botao.pack()
	def voltar(self,controler):
		controler.show_frame(MenuSecretario)
#CLASSE RESPONSAVEL PELA TELA LISIAGEM DE PARTICIPANTE
class ListarParticipante(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		self.windgets(controler)
	def windgets(self,controler):
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=10,padx=10,height=600,width=900)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text= "Listando Participante",font=FONTE_PADRAO,width=40,height=2)
		self.titulo.grid(row=0,column=1)
		self.frame_texto = Frame(self, bg = COR_FUNDO,pady=10,padx=10,height=100,width=100)
		self.frame_texto.pack()
		
		# Inicia o Treeview com as seguintes colunas:
		self.frame_texto.pack()
		self.dataCols = ['ID','Nome','Academia','Nascimento','Endereco','Cpf','Tipo','Sexo','Graduacao','Telefone']
		self.tree = ttk.Treeview(self.frame_texto,columns=self.dataCols, show='headings')
		self.tree.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
		#diminue a largura da coluna
		self.tree.column("ID",minwidth=30,width=30)
		self.tree.column("Nome",minwidth=100,width=100)
		self.tree.column("Academia",minwidth=90,width=90)
		self.tree.column("Nascimento",minwidth=60,width=60)
		self.tree.column("Endereco",minwidth=90,width=90)
		self.tree.column("Cpf",minwidth=40,width=40)
		self.tree.column("Tipo",minwidth=60,width=60)
		self.tree.column("Sexo",minwidth=40,width=40)
		self.tree.column("Graduacao",minwidth=80,width=80)
		self.tree.column("Telefone",minwidth=60,width=60)
		# Barras de rolagem
		ysb = ttk.Scrollbar(self.frame_texto,orient=VERTICAL, command=self.tree.yview)
		xsb = ttk.Scrollbar(self.frame_texto,orient=HORIZONTAL, command=self.tree.xview)
		self.tree['yscroll'] = ysb.set
		self.tree['xscroll'] = xsb.set
		ysb.grid(row=0, column=1, sticky=tk.N + tk.S)
		xsb.grid(row=1, column=0, sticky=tk.E + tk.W)
		# Define o textos do cabeçalho (nome em maiúsculas)
		for c in self.dataCols:
			self.tree.heading(c, text=c.title())
		# Dados:
		self.data = Base_Participante.listar_participante()
		# Insere cada item dos dados
		for item in self.data:
			self.tree.insert('', 'end', values=item)
		self.botao = Button(self,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text="Fechar",width= 10, command=lambda:self.voltar(controler),font=FONTE_PADRAO)
		self.botao.pack()
	def voltar(self,controler):
		controler.show_frame(MenuAcademia)
		
#CLASSE RESPONSAVEL PELA TELA DE GERACAO GERAR CARTEIRINHA
class GerarCarteirinha(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)

		self['bg'] = COR_FUNDO
		
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=80)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=int(TAMANHO_BORDA_BOTAO/4),relief=TIPO_BORDA_BOTAO,text= "Carterinha",font=FONTE_PADRAO,width=60,height=4)
		self.titulo.grid(row=0,column=1)
		
		self.frame_participante = Frame(self, bg = COR_FUNDO,pady=20)
		self.frame_participante.pack()
		
		self.nome = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Nome Integrante : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.cpf = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="CPF : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		self.academia = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Academia : ",width=int(LARGURA_PADRAO/3),font=FONTE_PADRAO)
		
		self.entrada_nome = Entry(self.frame_participante,width=80)
		self.entrada_cpf = Entry(self.frame_participante,width=80)
		self.entrada_academia = Entry(self.frame_participante,width=80)
		
		self.nome.grid(row=0,column=0)
		self.cpf.grid(row=1,column=0)
		self.academia.grid(row=2,column=0)
		
		self.entrada_nome.grid(row=0,column=1)
		self.entrada_cpf.grid(row=1,column=1)
		self.entrada_academia.grid(row=2,column=1)
		
		self.frame_botoes = Frame(self, bg = COR_FUNDO,pady=10)
		self.frame_botoes.pack()
		self.botao_gerar = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text = "Gerar Carteirinha",width = int(LARGURA_PADRAO/3),command = lambda: self.buscar_participante(controler),activebackground='green',font=FONTE_PADRAO)
		self.botao_gerar.grid(row=0,column=0)
		self.botao_cancel = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text = "Cancelar",width = int(LARGURA_PADRAO/3),command = lambda:controler.show_frame(MenuAcademia),activebackground='green',font=FONTE_PADRAO)
		self.botao_cancel.grid(row=0,column=10)
		
	def buscar_participante(self, controler):
		global Base_Participante
		Base_Participante.set_nome(self.entrada_nome.get())
		Base_Participante.set_academia(self.entrada_academia.get())
		Base_Participante.set_cpf(self.entrada_cpf.get())
		if Base_Participante.nome_vazio() and Base_Participante.academia_vazia() and Base_Participante.cpf_vazio():
			messagebox.showwarning("Aviso", "Preencha os campos.")
			controler.show_frame(GerarCarteirinha)
		elif Base_Participante.nome_vazio():
			messagebox.showwarning("Aviso", "Preencha o campo Nome.")
			controler.show_frame(GerarCarteirinha)
		elif Base_Participante.academia_vazia():
			messagebox.showwarning("Aviso", "Preencha o campo Academia.")
			controler.show_frame(GerarCarteirinha)
		elif Base_Participante.cpf_vazio():
			messagebox.showwarning("Aviso", "Preencha o campo Cpf.")
			controler.show_frame(GerarCarteirinha)
		else:
			if Base_Participante.este_participante_existe():
				messagebox.showinfo("Gerando", "Participante encontrado.")
				self.limpar_campos()
				controler.show_frame(ExibeCarteirinha)
			else:
				messagebox.showerror("Erro", "Participante nao encontrado.")
				self.limpar_campos()
				controler.show_frame(GerarCarteirinha)
	def limpar_campos(self):
		self.entrada_nome.delete(0,END)
		self.entrada_academia.delete(0,END)
		self.entrada_cpf.delete(0,END)
#CLASSE RESPONSAVEL PELA TELA EXIBICAO DE CARTEIRINHA
class ExibeCarteirinha(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		
		self['bg'] = COR_FUNDO
		
		global Base_Participante
		self.data = datetime.now()
		
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=80)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=int(TAMANHO_BORDA_BOTAO/4),relief=TIPO_BORDA_BOTAO,text= "Carteirinha",font=FONTE_PADRAO,width=60,height=4)
		self.titulo.grid(row=0,column=0)
		
		self.frame_carteira = Frame(self, bg = COR_FUNDO,pady=20)
		self.frame_carteira.pack()
		
		self.nome = Label(self.frame_carteira,text="Nome Participante : "+str(Base_Participante.get_nome()),width=100,font=FONTE_PADRAO)
		self.nome_academia = Label(self.frame_carteira,text="Nome Academia : "+str(Base_Participante.get_academia()),width=100,font=FONTE_PADRAO)
		self.cpf = Label(self.frame_carteira,text="CPF : "+str(Base_Participante.get_cpf()),width=100,font=FONTE_PADRAO)
		self.id = Label(self.frame_carteira,text="Id : "+str(Base_Participante.get_inscricao()),width=100,font=FONTE_PADRAO)
		self.vencimento = Label(self.frame_carteira,text="Vencimento : "+str(self.data.day)+"/"+str(self.data.month)+"/"+str(self.data.year),width=100,font=FONTE_PADRAO)
		
		self.nome.grid(row=0,column=0)
		self.nome_academia.grid(row=1,column=0)
		self.cpf.grid(row=2,column=0)
		self.id.grid(row=3,column=0)
		self.vencimento.grid(row=4,column=0)
		
		self.frame_botoes = Frame(self, bg = COR_FUNDO,pady=200)
		self.frame_botoes.pack()
		self.botao_cancel = Button(self.frame_botoes,border=int(TAMANHO_BORDA_BOTAO/4),relief=TIPO_BORDA_BOTAO, text = "Cancelar",width = int(LARGURA_PADRAO/3),command = lambda:controler.show_frame(MenuAcademia),activebackground='green',font=FONTE_PADRAO)
		self.botao_cancel.grid(row=0,column=10)

		
#CLASSE RESPONSAVEL PELA TELA DE SOBRE
class Sobre(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=10,padx=10,height=600,width=900)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text= "Sobre",font=FONTE_PADRAO,width=40,height=2)
		self.titulo.grid(row=0,column=1)
		self.frame_texto = Frame(self, bg = COR_FUNDO,pady=10,padx=10,height=4,width=10)
		self.frame_texto.pack()
		texto = "\t\t\tSobre o JUDORAMA\n"
		texto += "O Sistema judorama foi desenvolvido para gerenciar a Federacao de judo,"
		texto += "uma Confederação\nqualquer de Judô pode usar nossa plataforma para facilitar sua organizacao.\n"
		texto += "O sistema disponibliza as seguintes funcionalidades:\n"
		texto += "\t1 - Gerenciamento de atletas(Participantes).\n"
		texto += "\t2 - Gerenciamento de instituicoes de artes marciais(Academias).\n"
		texto += "\t3 - Gerenciamento de campeonatos(Torneios).\n"
		texto += "\t4 - Gerenciamento de usuarios do sistema(Secretarios).\n"
		texto += "\t5 - Gerenciamento de pagamentos(Boletos).\n"
		texto += "\t6 - Gerenciamento de dados exclusivos de cada atleta(Carteirinhas).\n"
		texto += "Projeto concebido na Discplina de Engenharia de Software II na instuicao de ensino CSHN-UFPI.\n"
		texto += "Curso de sistemas de informacao - 4 periodo.\n"
		texto += "Esse projeto foi implemetado em linguaguem Python 3.2.\n"
		texto += "Iniciou no comeco de Abril de 2018.\n"
		texto += "Versao: 01.19.06.2018-pt-br\n"
		texto += "Desenvolvedores:\n"
		texto += "\tFrancisco Charles\n"
		texto += "\tJose Mayke\n"
		mensagem = Label(self.frame_texto,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text=texto,justify=LEFT,font=('Time News Roman','18','bold'))
		mensagem.pack(side=LEFT)
		botao = Button(self,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text="voltar",width= 10, command= lambda: controler.show_frame(MenuPrincipal),font=FONTE_PADRAO)
		botao.pack()
		
#FUNCAO MAIN
def main():
	app = Gerenciador()
	app.mainloop()
if __name__ == '__main__':
	main()