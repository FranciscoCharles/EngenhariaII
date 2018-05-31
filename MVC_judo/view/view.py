#modulo menu principal
from tkinter import*
from tkinter import messagebox
import tkinter as tk

import sys
sys.path.append("../")

from controller.Controller_Secretario import*
from controller.Controller_Participante import*

diretorio_imagens = 'C:\\Users\\Charles\\Desktop\\aulas\\Engenharia\\MVC_judo\\image\\'

COR_FUNDO = '#105e74'
LARGURA_PADRAO = 60
ALTURA_PADRAO = 4
TAMANHO_BORDA_BOTAO = 8
TIPO_BORDA_BOTAO = RIDGE

class Gerenciador(tk.Tk):
	def __init__(self,*args,**wargs):
		tk.Tk.__init__(self,*args,**wargs)
		tk.Tk.iconbitmap(self,default= diretorio_imagens+"icone.ico" )
		tk.Tk.wm_title(self,"JUDORAMA")
		tk.Tk.background='black'
		
		container = Frame(self)
		container.pack(side="top",fill="both",expand=True)
		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)
		
		TELAS = [LoginInicial,MenuPrincipal,Academia,CadastrarParticipante,MenuTorneio,CadastrarTorneio,
				Sobre,Secretario,CadastrarSecretario,ListarSecretario,RemoverSecretario,GerarCarteirinha,
				ExibeCarteirinha,ListarAcademia,ListarParticipante]
		
		self.frames = {}
		for tela in (TELAS):
			frame = tela(container,self)
			self.frames[tela] = frame
			frame.grid(row=0,column=0,stick="nsew")
		self.show_frame(LoginInicial)
		
	def show_frame(self,count):
		frame = self.frames[count]
		frame.tkraise()
#TELA INICIAL DE LOGIN
class LoginInicial(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		
		total_labels = 22
		
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=60)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=8,relief=RIDGE,text= "JUDORAMA",width=60,height=4)
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
		
		self.login = Label(self.frame_usuario,border=2,relief=RIDGE,text="login : ",width=int(LARGURA_PADRAO/3))
		self.senha = Label(self.frame_usuario,border=2,relief=RIDGE,text="senha : ",width=int(LARGURA_PADRAO/3))
		
		self.entrada_login = Entry(self.frame_usuario,width=80)
		self.entrada_senha = Entry(self.frame_usuario,width=80,show="*",)
		
		self.login.grid(row=0,column=0)
		self.senha.grid(row=(1*total_labels),column=0)
		
		self.entrada_login.grid(row=0,column=1)
		self.entrada_senha.grid(row=(1*total_labels),column=1)
		
		self.frame_botoes = Frame(self, bg = COR_FUNDO,pady=10)
		self.frame_botoes.pack()
		self.botao_entrar = Button(self.frame_botoes,border=8,relief=RIDGE,font=("Time News Roman",10,"bold"), text = "Entrar",width = int(LARGURA_PADRAO/3),command = lambda:self.valida_dados(controler),activebackground='green')
		self.botao_entrar.grid(row=0,column=0)
		self.botao_fechar = Button(self.frame_botoes,border=8,relief=RIDGE,font=("Time News Roman",10,"bold"), text = "Fechar",width = int(LARGURA_PADRAO/3),command = self.quit,activebackground='green')
		self.botao_fechar.grid(row=0,column=10)
		
	def valida_dados(self,controler):
		S = Controller_Secretario()
		S.set_login(self.entrada_login.get())
		S.set_senha(self.entrada_senha.get())
		
		if(S.login_vazio() and S.senha_vazia()):
			messagebox.showwarning("Aviso", "Preencha os Campos")
		elif(S.login_vazio()):
			messagebox.showwarning("Aviso", "Preencha o Campo de Login")
		elif(S.senha_vazia()):
			messagebox.showwarning("Aviso", "Preencha o Campo de Senha")
		elif(S.validar_secretario()):
			self.limpar_campos(controler)
			messagebox.showinfo("Acesso", S.get_login()+" Seja Bem Vindo ao Nosso Sistema")
			controler.show_frame(MenuPrincipal)
		else:
			self.limpar_campos(controler)
			messagebox.showerror("Erro", "Login ou Senha Invalidos")
			controler.show_frame(LoginInicial)
		
	def limpar_campos(self,controler):
		self.entrada_login.delete(0, END)
		self.entrada_senha.delete(0, END)
#MENU PRINCIPAL

class MenuPrincipal(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		self.frame_menu = Frame(self, bg = COR_FUNDO,pady=100)
		self.frame_menu.pack()
		self.botao_academia = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Academia",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(Academia),activebackground='green')
		self.botao_torneio = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Torneio",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(MenuTorneio),activebackground='green')
		self.botao_secretario = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Secretario",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(Secretario),activebackground='green')
		self.botao_sobre = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Sobre",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(Sobre),activebackground='green')
		self.botao_sair = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Sair",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(LoginInicial),activebackground='green')
		self.botao_academia.pack()
		self.botao_torneio.pack()
		self.botao_secretario.pack()
		self.botao_sobre.pack()
		self.botao_sair.pack()

#MENU TORNEIO
class MenuTorneio(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		self.frame_menu = Frame(self, bg = COR_FUNDO,pady=100,padx=500,height=500,width=900)
		self.frame_menu.pack()
		self.botao_adicionar = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Adicionar Torneio",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(CadastrarTorneio),activebackground='green')
		self.botao_buscar = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Buscar Torneio",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = None,activebackground='green')
		self.botao_remover = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Remover Torneio",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = None,activebackground='green')
		self.botao_listar = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Listar Torneio",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = None,activebackground='green')
		self.botao_sair = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Voltar",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(MenuPrincipal),activebackground='green')
		self.botao_adicionar.pack()
		self.botao_buscar.pack()
		self.botao_remover.pack()
		self.botao_listar.pack()
		self.botao_sair.pack()
#MENU SECRETARIO
class Secretario(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		self.frame_menu = Frame(self, bg = COR_FUNDO,pady=100)
		self.frame_menu.pack()
		self.botao_adcionar = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Adcionar",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(CadastrarSecretario),activebackground='green')
		self.botao_editar = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Editar",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = None,activebackground='green')
		self.botao_listar = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Listar",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(ListarSecretario),activebackground='green')
		self.botao_remover = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Remover",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = None,activebackground='green')
		self.botao_sair = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Voltar",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(MenuPrincipal),activebackground='green')
		self.botao_adcionar.pack()
		self.botao_editar.pack()
		self.botao_listar.pack()
		self.botao_remover.pack()
		self.botao_sair.pack()
#MENU Participante
class CadastrarParticipante(Frame):
	def __init__(self,parent,controler):
		
		Frame.__init__(self,parent)
		self.tipo1_s = False
		self.tipo2_s = False
		self.tipo3_s = False
		
		self.sexo_m = False
		self.sexo_f = False
		self.sexo = "masculino"
		
		self.tipo = "Professor"
		
		self['bg'] = COR_FUNDO
		total_labels = 22
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=80)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=8,relief=TIPO_BORDA_BOTAO,text= "Cadastro Participante",width=60,height=4)
		self.titulo.grid(row=0,column=1)
		
		self.frame_participante = Frame(self, bg = COR_FUNDO,pady=20)
		self.frame_participante.pack()
		
		self.nome = Label(self.frame_participante,border= int(TAMANHO_BORDA_BOTAO/4),relief=TIPO_BORDA_BOTAO,text="Nome : ",width=int(LARGURA_PADRAO/3))
		self.cpf = Label(self.frame_participante,border=int(TAMANHO_BORDA_BOTAO/4),relief=TIPO_BORDA_BOTAO,text="CPF : ",width=int(LARGURA_PADRAO/3))
		self.data = Label(self.frame_participante,border=int(TAMANHO_BORDA_BOTAO/4),relief=TIPO_BORDA_BOTAO,text="Data de Nascimento : ",width=int(LARGURA_PADRAO/3))
		self.academia = Label(self.frame_participante,border=int(TAMANHO_BORDA_BOTAO/4),relief=TIPO_BORDA_BOTAO,text="Academia: ",width=int(LARGURA_PADRAO/3))
		self.faixa = Label(self.frame_participante,border=int(TAMANHO_BORDA_BOTAO/4),relief=TIPO_BORDA_BOTAO,text="Graduacao: ",width=int(LARGURA_PADRAO/3))
		self.endereco = Label(self.frame_participante,border=int(TAMANHO_BORDA_BOTAO/4),relief=TIPO_BORDA_BOTAO,text="Endereco : ",width=int(LARGURA_PADRAO/3))
		
		self.entrada_nome = Entry(self.frame_participante,width=80)
		self.entrada_cpf = Entry(self.frame_participante,width=80)
		self.entrada_data = Entry(self.frame_participante,width=80)
		self.entrada_academia = Entry(self.frame_participante,width=80)
		self.entrada_faixa = Entry(self.frame_participante,width=80)
		self.entrada_endereco = Entry(self.frame_participante,width=80)
		
		self.nome.grid(row=0,column=0)
		self.cpf.grid(row=(1*total_labels),column=0)
		self.data.grid(row=(2*total_labels),column=0)
		self.academia.grid(row=(3*total_labels),column=0)
		self.faixa.grid(row=(4*total_labels),column=0)
		self.endereco.grid(row=(5*total_labels),column=0)
		
		self.entrada_nome.grid(row=0,column=1)
		self.entrada_cpf.grid(row=(1*total_labels),column=1)
		self.entrada_data.grid(row=(2*total_labels),column=1)
		self.entrada_academia.grid(row=(3*total_labels),column=1)
		self.entrada_faixa.grid(row=(4*total_labels),column=1)
		self.entrada_endereco.grid(row=(5*total_labels),column=1)
		
		self.frame_tipo = Frame(self,pady=10)
		self.frame_tipo.pack()
		
		self.tipo1 = Checkbutton(self.frame_tipo,text="Professor",padx = 20,command=self.ativar_tipo1)
		self.tipo1.select()
		self.tipo1.pack(side = LEFT)
		self.tipo2 = Checkbutton(self.frame_tipo,text="Instrutor",padx = 20,command=self.ativar_tipo2)
		self.tipo2.pack(side = LEFT)
		self.tipo3 = Checkbutton(self.frame_tipo,text="Aluno",padx = 20,command=self.ativar_tipo3)
		self.tipo3.pack(side = LEFT)
		
		self.frame_botoes = Frame(self, bg = COR_FUNDO,pady=10)
		self.frame_botoes.pack()
		self.botao_salvar = Button(self.frame_botoes, text = "Salvar",width = LARGURA_PADRAO,command = lambda:self.limpar_campos(controler),activebackground='green')
		self.botao_salvar.grid(row=0,column=0)
		self.botao_cancel = Button(self.frame_botoes, text = "Cancelar",width = LARGURA_PADRAO,command = lambda:controler.show_frame(Academia),activebackground='green')
		self.botao_cancel.grid(row=0,column=10)
	def ativar_sexo_m(self):
		self.sexo_m = not self.sexo_m
		if self.sexo_m:
			self.sexo = "Masculino"
			self.sexo_f = False
			self.sexo_f.deselect()
	def ativar_sexo_f(self):
		self.sexo_f = not self.sexo_f
		if self.sexo_f:
			self.sexo = "Feminino"
			self.sexo_m = False
			self.sexo_m.deselect()
	def ativar_tipo1(self):
		self.tipo1_s = not self.tipo1_s
		if self.tipo1_s:
			self.tipo = "Professor"
			self.tipo2_s = False
			self.tipo2.deselect()
			self.tipo3_s = False
			self.tipo3.deselect()
	def ativar_tipo2(self):
		self.tipo2_s = not self.tipo2_s
		if self.tipo2_s:
			self.tipo = "Instrutor"
			self.tipo1_s = False
			self.tipo1.deselect()
			self.tipo3_s = False
			self.tipo3.deselect()
	def ativar_tipo3(self):
		self.tipo3_s = not self.tipo3_s
		if self.tipo3_s:
			self.tipo = "Aluno"
			self.tipo1_s = False
			self.tipo1.deselect()
			self.tipo2_s = False
			self.tipo2.deselect()
	def valida_dados(self,controler):
		P = Controller_Participante()
		P.set_nome(self.entrada_nome.get())
		P.set_cpf(self.entrada_cpf.get())
		P.set_data(self.entrada_data.get())
		P.set_academia(self.entrada_academia.get())
		P.set_graduacao(self.entrada_faixa.get())
		P.set_endereco(self.entrada_endereco.get())

		if(P.nome_vazio() and P.data_vazia() and P.cpf_vazio()):
			messagebox.showwarning("Aviso", "Preencha os Campos")
		elif(P.nome_vazio()):
			messagebox.showwarning("Aviso", "Preencha o Campo de Nome")
		elif(P.data_vazia()):
			messagebox.showwarning("Aviso", "Preencha o Campo de Data")
		elif(not P.este_participante_existe()):
			self.limpar_campos(controler)
			messagebox.showinfo("Participante Cadastrado com Sucesso!")
			controler.show_frame(MenuPrincipal)
		else:
			self.limpar_campos(controler)
			messagebox.showerror("Erro", "Nao foi Possivel Cadastrar.")
			controler.show_frame(LoginInicial)
	def limpar_campos(self,controler):
		self.tipo1_s = False
		self.tipo2_s = False
		self.tipo3_s = False
		self.tipo = "Professor"
		self.entrada_nome.delete(0, END)
		self.entrada_cpf.delete(0, END)
		self.entrada_data.delete(0, END)
		self.entrada_faixa.delete(0, END)
		self.entrada_endereco.delete(0, END)
		controler.show_frame(MenuPrincipal)
	def valida_dados(self,controler):
		pass

class CadastrarSecretario(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		total_labels = 22
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=80)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text= "Adicionar secretario",width=60,height=4)
		self.titulo.grid(row=0,column=1)
		
		self.frame_participante = Frame(self, bg = COR_FUNDO,pady=20)
		self.frame_participante.pack()
		
		self.login = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="login : ",width=int(LARGURA_PADRAO/3))
		self.senha = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="senha : ",width=int(LARGURA_PADRAO/3))
		self.rep_senha = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="repita senha : ",width=int(LARGURA_PADRAO/3))
		
		self.entrada_login = Entry(self.frame_participante,width=80)
		self.entrada_senha = Entry(self.frame_participante,width=80,show="*",)
		self.entrada_rep_senha = Entry(self.frame_participante,width=80,show="*",)
		
		self.login.grid(row=0,column=0)
		self.senha.grid(row=(1*total_labels),column=0)
		self.rep_senha.grid(row=(2*total_labels),column=0)
		
		self.entrada_login.grid(row=0,column=1)
		self.entrada_senha.grid(row=(1*total_labels),column=1)
		self.entrada_rep_senha.grid(row=(2*total_labels),column=1)
		
		self.frame_botoes = Frame(self, bg = COR_FUNDO,pady=10)
		self.frame_botoes.pack()
		self.botao_salvar = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text = "Salvar",width = int(LARGURA_PADRAO/3),command = lambda:self.valida_dados(controler),activebackground='green')
		self.botao_salvar.grid(row=0,column=0)
		self.botao_cancel = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text = "Cancelar",width = int(LARGURA_PADRAO/3),command = lambda:controler.show_frame(Secretario),activebackground='green')
		self.botao_cancel.grid(row=0,column=10)
	def limpar_campos(self,controler):
		self.entrada_login.delete(0,END)
		self.entrada_senha.delete(0,END)
		self.entrada_rep_senha.delete(0,END)
	def valida_dados(self,controler):
		S = Controller_Secretario()
		S.set_login(self.entrada_login.get())
		S.set_senha(self.entrada_senha.get())
		
		rep_senha = self.entrada_rep_senha.get()
		if(S.login_vazio() and S.senha_vazia() and rep_senha==""):
			messagebox.showwarning("Aviso", "Preencha os Campos!")
		elif(S.login_vazio()):
			messagebox.showwarning("Aviso", "Preencha o Campo de Login!")
		elif(S.senha_vazia()):
			messagebox.showwarning("Aviso", "Preencha o Campo de Senha!")
		elif(rep_senha==""):
			messagebox.showwarning("Aviso", "Preencha o Campo de rep_senha!")
		elif(not (S.get_senha() == rep_senha)):
			messagebox.showwarning("Aviso", "Senhas diferem!")
		elif(not S.este_secretario_existe()):
			self.limpar_campos(controler)
			S.salvar_secretario()
			messagebox.showinfo("Sucesso", "Usuario adcionado com sucesso")
			controler.show_frame(Secretario)
		else:
			self.limpar_campos(controler)
			messagebox.showerror("Erro", "Login ou Senha Invalidos")
			controler.show_frame(CadastrarSecretario)
class CadastrarTorneio(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		total_labels = 22
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=10,padx=10,height=600,width=900)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text= "Adicionar de Torneio",width=40,height=2)
		self.titulo.grid(row=0,column=1)
		
		self.frame_participante = Frame(self, bg = COR_FUNDO,pady=200,padx=0,height=300,width=900)
		self.frame_participante.pack()
		
		self.nome = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Nome do Torneio : ",width=int(LARGURA_PADRAO/3))
		self.local = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Local : ",width=int(LARGURA_PADRAO/3))
		self.data = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Data : ",width=int(LARGURA_PADRAO/3))
		self.valor = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Valor : ",width=int(LARGURA_PADRAO/3))
		
		
		self.entrada_nome = Entry(self.frame_participante,width=80)
		self.entrada_local = Entry(self.frame_participante,width=80)
		self.entrada_data = Entry(self.frame_participante,width=80)
		self.entrada_valor = Entry(self.frame_participante,width=80)
		
		self.nome.grid(row=0,column=0)
		self.local.grid(row=(1*total_labels),column=0)
		self.data.grid(row=(2*total_labels),column=0)
		self.valor.grid(row=(3*total_labels),column=0)
		
		self.entrada_nome.grid(row=0,column=1)
		self.entrada_local.grid(row=(1*total_labels),column=1)
		self.entrada_data.grid(row=(2*total_labels),column=1)
		self.entrada_valor.grid(row=(3*total_labels),column=1)
		
		self.frame_botoes = Frame(self, bg = COR_FUNDO,pady=10)
		self.frame_botoes.pack()
		self.botao_salvar = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text = "Salvar",width = int(LARGURA_PADRAO/3),command = None,activebackground='green')
		self.botao_salvar.grid(row=0,column=0)
		self.botao_cancel = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text = "Cancelar",width = int(LARGURA_PADRAO/3),command = lambda:controler.show_frame(MenuTorneio),activebackground='green')
		self.botao_cancel.grid(row=0,column=10)
	def limpar_campos(self,controler):
		self.entrada_nome.delete(0,END)
		self.entrada_local.delete(0,END)
		self.entrada_data.delete(0,END)
		self.entrada_valor.delete(0,END)
		controler.show_frame(CadastrarTorneio)
	def valida_dados(self,controler):
		pass
class RemoverSecretario(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		total_labels = 22
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=80)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,text= "Remover Secretario",width=60,height=4)
		self.titulo.grid(row=0,column=1)
		
		self.frame_participante = Frame(self, bg = COR_FUNDO,pady=20)
		self.frame_participante.pack()
		
		self.login = Label(self.frame_participante,text="login : ",width=int(LARGURA_PADRAO/3))
		self.senha = Label(self.frame_participante,text="senha : ",width=int(LARGURA_PADRAO/3))
		
		self.entrada_login = Entry(self.frame_participante,width=80)
		self.entrada_senha = Entry(self.frame_participante,width=80,show="*")
		
		self.login.grid(row=0,column=0)
		self.senha.grid(row=(1*total_labels),column=0)
		
		self.entrada_login.grid(row=0,column=1)
		self.entrada_senha.grid(row=(1*total_labels),column=1)
		
		self.frame_botoes = Frame(self, bg = COR_FUNDO,pady=10)
		self.frame_botoes.pack()
		self.botao_salvar = Button(self.frame_botoes, text = "Remover",width = int(LARGURA_PADRAO/3),command = lambda:controler.show_frame(Secretario),activebackground='green')
		self.botao_salvar.grid(row=0,column=0)
		self.botao_cancel = Button(self.frame_botoes, text = "Cancelar",width = int(LARGURA_PADRAO/3),command = lambda:controler.show_frame(Secretario),activebackground='green')
		self.botao_cancel.grid(row=0,column=10)
#MENU ACADEMIA
class Academia(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		self.frame_menu = Frame(self, bg = COR_FUNDO,pady=50)
		self.frame_menu.pack()
		self.botao_adcionar = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Adicionar Academia",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = None,activebackground='green')
		self.botao_editar = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Adicionar Integrante",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(CadastrarParticipante),activebackground='green')
		self.botao_listar = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Listar Academia",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = None,activebackground='green')
		self.botao_listar_participante = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Listar Participante",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = None,activebackground='green')
		self.botao_remover = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Remover Academia",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = None,activebackground='green')
		self.botao_carteirinha = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Gerar Carteirinha",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(GerarCarteirinha),activebackground='green')
		self.botao_sair = Button(self.frame_menu,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO, text = "Voltar",width = LARGURA_PADRAO,height=ALTURA_PADRAO,command = lambda:controler.show_frame(MenuPrincipal),activebackground='green')
		self.botao_adcionar.pack()
		self.botao_editar.pack()
		self.botao_listar.pack()
		self.botao_listar_participante.pack()
		self.botao_remover.pack()
		self.botao_carteirinha.pack()
		self.botao_sair.pack()
class ListarAcademia(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		
		self['bg'] = COR_FUNDO
		total_labels = 22
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=10,padx=10,height=600,width=900)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,text= "Listando Academias",width=40,height=2)
		self.titulo.grid(row=0,column=1)
		self.frame_texto = Frame(self, bg = COR_FUNDO,pady=10,padx=10,height=100,width=100)
		self.frame_texto.pack()
		barra_rolagem = Scrollbar(self.frame_texto)
		barra_rolagem.pack(side=RIGHT, fill=Y)
		texto = "TEXTO"
		mensagem = Listbox(self.frame_texto, yscrollcommand = barra_rolagem.set,width=50,height=20)
		for linha in str(texto).split():
			mensagem.insert(END,linha)
		mensagem.pack()
		barra_rolagem.config(command=mensagem.yview)
		botao = Button(self,text="fechar",border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,width= 10, command= lambda: controler.show_frame(Academia))
		botao.pack()
class ListarSecretario(Frame):
	def __init__(self,parent,controler):
		
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		total_labels = 22
		self.Secretario = Controller_Secretario()
		
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=10,padx=10,height=600,width=900)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text= "Listando Secretarios",width=40,height=2)
		self.titulo.grid(row=0,column=1)
		self.frame_texto = Frame(self, bg = COR_FUNDO,pady=10,padx=10,height=100,width=100)
		self.frame_texto.pack()
		self.barra_rolagem = Scrollbar(self.frame_texto)
		self.barra_rolagem.pack(side=RIGHT, fill=Y)
		
		self.mensagem = Listbox(self.frame_texto, yscrollcommand = self.barra_rolagem.set,width=50,height=20)
		self.atualizar_texto(controler)
		self.mensagem.pack()
		self.botao = Button(self,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text="fechar",width= 10, command=lambda:self.atualizar_texto(controler))
		self.barra_rolagem.config(command=self.mensagem.yview)
		self.botao.pack()
	
	def atualizar_texto(self, controler):
		self.texto = ""
		self.texto = self.Secretario.listar_secretario()
		self.limpar_mensagem()
		for linha in self.texto.split('\n'):
			self.mensagem.insert(END,linha)
		controler.show_frame(Secretario)
	def limpar_mensagem(self):
		self.mensagem.delete(0,self.mensagem.size())
class ListarParticipante(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		total_labels = 22
		self.Participante = Controller_Participante()
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=10,padx=10,height=600,width=900)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,text= "Listando Participantes",width=40,height=2)
		self.titulo.grid(row=0,column=1)
		self.frame_texto = Frame(self, bg = COR_FUNDO,pady=10,padx=10,height=100,width=100)
		self.frame_texto.pack()
		self.barra_rolagem = Scrollbar(self.frame_texto)
		self.barra_rolagem.pack(side=RIGHT, fill=Y)
		self.mensagem = Listbox(self.frame_texto, yscrollcommand = self.barra_rolagem.set,width=50,height=20)
		self.mensagem.pack()
		self.barra_rolagem.config(command=self.mensagem.yview)
		self.botao = Button(self,text="fechar",width= 10, command= lambda: self.atualizar_texto(controler))
		self.botao.pack()
	def atualizar_texto(self, controler):
		self.texto = ""
		self.texto = self.Participante.listar_participante()
		self.limpar_mensagem()
		for linha in self.texto.split('\n'):
			self.mensagem.insert(END,linha)
		controler.show_frame(CadastrarParticipante)
	def limpar_mensagem(self):
		self.mensagem.delete(0,self.mensagem.size())
#GERAR CARTEIRINHA
class GerarCarteirinha(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)

		self['bg'] = COR_FUNDO
		total_labels = 22
		
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=80)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text= "Carterinha",width=60,height=4)
		self.titulo.grid(row=0,column=1)
		
		self.frame_participante = Frame(self, bg = COR_FUNDO,pady=20)
		self.frame_participante.pack()
		
		self.nome = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Nome Integrante : ",width=int(LARGURA_PADRAO/3))
		self.cpf = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="CPF : ",width=int(LARGURA_PADRAO/3))
		self.academia = Label(self.frame_participante,border=2,relief=TIPO_BORDA_BOTAO,text="Academia : ",width=int(LARGURA_PADRAO/3))
		
		self.entrada_nome = Entry(self.frame_participante,width=80)
		self.entrada_cpf = Entry(self.frame_participante,width=80)
		self.entrada_academia = Entry(self.frame_participante,width=80)
		
		self.nome.grid(row=0,column=0)
		self.cpf.grid(row=(1*total_labels),column=0)
		self.academia.grid(row=(2*total_labels),column=0)
		
		self.entrada_nome.grid(row=0,column=1)
		self.entrada_cpf.grid(row=(1*total_labels),column=1)
		self.entrada_academia.grid(row=(2*total_labels),column=1)
		
		self.frame_botoes = Frame(self, bg = COR_FUNDO,pady=10)
		self.frame_botoes.pack()
		self.botao_gerar = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text = "Gerar Carteirinha",width = int(LARGURA_PADRAO/3),command = None,activebackground='green')
		self.botao_gerar.grid(row=0,column=0)
		self.botao_cancel = Button(self.frame_botoes,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text = "Cancelar",width = int(LARGURA_PADRAO/3),command = lambda:controler.show_frame(Academia),activebackground='green')
		self.botao_cancel.grid(row=0,column=10)
class ExibeCarteirinha(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		
		self['bg'] = COR_FUNDO
		total_labels = 22
		
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=80)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,text= "CARTEIRINHA",width=60,height=4)
		self.titulo.grid(row=0,column=1)
		
		self.frame_carteira = Frame(self, bg = COR_FUNDO,pady=20)
		self.frame_carteira.pack()
		
		self.nome = Label(self.frame_carteira,text="Nome Integrante : ",width=int(LARGURA_PADRAO/3))
		self.nome_academia = Label(self.frame_carteira,text="Nome Academia : ",width=int(LARGURA_PADRAO/3))
		self.cpf = Label(self.frame_carteira,text="CPF : ",width=int(LARGURA_PADRAO/3))
		self.id = Label(self.frame_carteira,text="Id : ",width=int(LARGURA_PADRAO/3))
		self.vencimento = Label(self.frame_carteira,text="Vencimento : ",width=int(LARGURA_PADRAO/3))
		
		self.nome.pack()
		self.nome_academia.pack()
		self.cpf.pack()
		self.id.pack()
		self.vencimento.pack()
		self.frame_botoes = Frame(self, bg = COR_FUNDO,pady=20)
		self.botao_cancel = Button(self.frame_botoes, text = "Cancelar",width = int(LARGURA_PADRAO/3),command = lambda:controler.show_frame(Academia),activebackground='green')
		self.botao_cancel.pack()		
#MENU SOBRE
class Sobre(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self['bg'] = COR_FUNDO
		total_labels = 22
		
		self.frame_titulo = Frame(self, bg = COR_FUNDO,pady=10,padx=10,height=600,width=900)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text= "Sobre",width=40,height=2)
		self.titulo.grid(row=0,column=1)
		self.frame_texto = Frame(self, bg = COR_FUNDO,pady=10,padx=10,height=4,width=10)
		self.frame_texto.pack()
		texto = "O sistema judorama foi desenvolvido para gerenciar a Federacao de judo\n"
		texto += "Uma Confederação qualquer de Judô pode usar nossa Plataforma para facilitar sua organizacao.\n"
		mensagem = Label(self.frame_texto,text=texto,font=('times','18'))
		mensagem.pack()
		botao = Button(self,border=TAMANHO_BORDA_BOTAO,relief=TIPO_BORDA_BOTAO,text="voltar",width= 10, command= lambda: controler.show_frame(MenuPrincipal))
		botao.pack()
def init_view():
	app = Gerenciador()
	app.mainloop()
if __name__ == '__main__':
	init_view()