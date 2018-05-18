#modulo menu principal
from tkinter import*
from tkinter import messagebox
import tkinter as tk

diretorio_imagens = 'C:\\Users\\Charles\\Desktop\\aulas\\Engenharia\\MVC_judo\\image\\'

class Geral(tk.Tk):
	def __init__(self,*args,**wargs):
		cor_fundo = '#105e74'
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
				Exibe_Carteira,ListarAcademia,ListarParticipante]
		
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
		largura = 60
		altura = 4
		self.cor_fundo = '#105e74'
		self['bg'] = self.cor_fundo
		largura = 20
		total_labels = 22
		
		self.frame_titulo = Frame(self, bg = self.cor_fundo,pady=60)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=8,relief=RIDGE,text= "JUDORAMA",width=60,height=4)
		self.titulo.grid(row=0,column=1)
		
		logo = PhotoImage(file=diretorio_imagens+"testejudo.png")
		self.frame_logo = Frame(self,bg=self.cor_fundo,pady=10)
		self.frame_logo.pack()
		self.logo = Label(self.frame_logo,bg=self.cor_fundo)
		self.logo["image"] = logo
		self.logo.image = logo
		self.logo.pack()
		
		self.frame_usuario = Frame(self, bg = self.cor_fundo,pady=10)
		self.frame_usuario.pack()
		
		self.login = Label(self.frame_usuario,border=2,relief=RIDGE,text="login : ",width=largura)
		self.senha = Label(self.frame_usuario,border=2,relief=RIDGE,text="senha : ",width=largura)
		
		self.entrada_login = Entry(self.frame_usuario,width=80)
		self.entrada_senha = Entry(self.frame_usuario,width=80,show="*",)
		
		self.login.grid(row=0,column=0)
		self.senha.grid(row=(1*total_labels),column=0)
		
		self.entrada_login.grid(row=0,column=1)
		self.entrada_senha.grid(row=(1*total_labels),column=1)
		
		self.frame_botoes = Frame(self, bg = self.cor_fundo,pady=10)
		self.frame_botoes.pack()
		self.botao_entrar = Button(self.frame_botoes,border=8,relief=RIDGE,font=("Time News Roman",10,"bold"), text = "Entrar",width = largura,command = lambda:self.valida_dados(controler),activebackground='green')
		self.botao_entrar.grid(row=0,column=0)
		self.botao_fechar = Button(self.frame_botoes,border=8,relief=RIDGE,font=("Time News Roman",10,"bold"), text = "Fechar",width = largura,command = self.quit,activebackground='green')
		self.botao_fechar.grid(row=0,column=10)
		
	def valida_dados(self,controler):
		controler.show_frame(MenuPrincipal)
	def limpar_campos(self,controler):
		self.entrada_login.delete(0, END)
		self.entrada_senha.delete(0, END)
#MENU PRINCIPAL

class MenuPrincipal(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		largura = 60
		altura = 4
		self.cor_fundo = '#105e74'
		tipo_botao = RIDGE
		tamanho_borda_botao = 8
		self['bg'] = self.cor_fundo
		self.frame_menu = Frame(self, bg = self.cor_fundo,pady=100)
		self.frame_menu.pack()
		self.botao_academia = Button(self.frame_menu,border=tamanho_borda_botao,relief=tipo_botao, text = "Academia",width = largura,height=altura,command = lambda:controler.show_frame(Academia),activebackground='green')
		self.botao_torneio = Button(self.frame_menu,border=tamanho_borda_botao,relief=tipo_botao, text = "Torneio",width = largura,height=altura,command = lambda:controler.show_frame(MenuTorneio),activebackground='green')
		self.botao_secretario = Button(self.frame_menu,border=tamanho_borda_botao,relief=tipo_botao, text = "Secretario",width = largura,height=altura,command = lambda:controler.show_frame(Secretario),activebackground='green')
		self.botao_sobre = Button(self.frame_menu,border=tamanho_borda_botao,relief=tipo_botao, text = "Sobre",width = largura,height=altura,command = lambda:controler.show_frame(Sobre),activebackground='green')
		self.botao_sair = Button(self.frame_menu,border=tamanho_borda_botao,relief=tipo_botao, text = "Sair",width = largura,height=altura,command = lambda:controler.show_frame(LoginInicial),activebackground='green')
		self.botao_academia.pack()
		self.botao_torneio.pack()
		self.botao_secretario.pack()
		self.botao_sobre.pack()
		self.botao_sair.pack()

#MENU TORNEIO
class MenuTorneio(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		largura = 60
		altura = 4
		self.cor_fundo = '#105e74'
		tipo_botao = RIDGE
		tamanho_borda_botao = 8
		self['bg'] = self.cor_fundo
		self.frame_menu = Frame(self, bg = self.cor_fundo,pady=100,padx=500,height=500,width=900)
		self.frame_menu.pack()
		self.botao_adicionar = Button(self.frame_menu,border=tamanho_borda_botao,relief=tipo_botao, text = "Adicionar Torneio",width = largura,height=altura,command = lambda:controler.show_frame(CadastrarTorneio),activebackground='green')
		self.botao_buscar = Button(self.frame_menu,border=tamanho_borda_botao,relief=tipo_botao, text = "Buscar Torneio",width = largura,height=altura,command = None,activebackground='green')
		self.botao_remover = Button(self.frame_menu,border=tamanho_borda_botao,relief=tipo_botao, text = "Remover Torneio",width = largura,height=altura,command = None,activebackground='green')
		self.botao_listar = Button(self.frame_menu,border=tamanho_borda_botao,relief=tipo_botao, text = "Listar Torneio",width = largura,height=altura,command = None,activebackground='green')
		self.botao_sair = Button(self.frame_menu,border=tamanho_borda_botao,relief=tipo_botao, text = "Sair",width = largura,height=altura,command = lambda:controler.show_frame(MenuPrincipal),activebackground='green')
		self.botao_adicionar.pack()
		self.botao_buscar.pack()
		self.botao_remover.pack()
		self.botao_listar.pack()
		self.botao_sair.pack()
class CadastrarTorneio(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self.cor_fundo = '#105e74'
		self['bg'] = self.cor_fundo
		largura = 20
		total_labels = 22
		tipo_botao = RIDGE
		tamanho_borda_botao = 8
		self.frame_titulo = Frame(self, bg = self.cor_fundo,pady=10,padx=10,height=600,width=900)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=tamanho_borda_botao,relief=tipo_botao,text= "Adicionar de Torneio",width=40,height=2)
		self.titulo.grid(row=0,column=1)
		
		self.frame_participante = Frame(self, bg = self.cor_fundo,pady=200,padx=0,height=300,width=900)
		self.frame_participante.pack()
		
		self.nome = Label(self.frame_participante,border=2,relief=tipo_botao,text="Nome do Torneio : ",width=largura)
		self.local = Label(self.frame_participante,border=2,relief=tipo_botao,text="Local : ",width=largura)
		self.data = Label(self.frame_participante,border=2,relief=tipo_botao,text="Data : ",width=largura)
		self.valor = Label(self.frame_participante,border=2,relief=tipo_botao,text="Valor : ",width=largura)
		
		
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
		
		self.frame_botoes = Frame(self, bg = self.cor_fundo,pady=10)
		self.frame_botoes.pack()
		self.botao_salvar = Button(self.frame_botoes,border=tamanho_borda_botao,relief=tipo_botao,text = "Salvar",width = largura,command = None,activebackground='green')
		self.botao_salvar.grid(row=0,column=0)
		self.botao_cancel = Button(self.frame_botoes,border=tamanho_borda_botao,relief=tipo_botao,text = "Cancelar",width = largura,command = lambda:controler.show_frame(MenuTorneio),activebackground='green')
		self.botao_cancel.grid(row=0,column=10)
	def limpar_campos(self,controler):
		self.entrada_nome.delete(0,END)
		self.entrada_local.delete(0,END)
		self.entrada_data.delete(0,END)
		self.entrada_valor.delete(0,END)
		controler.show_frame(CadastrarTorneio)
	def valida_dados(self,controler):
		pass
#MENU SECRETARIO
class Secretario(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		largura = 60
		altura = 4
		tipo_botao = RIDGE
		tamanho_borda_botao = 8
		self.cor_fundo = '#105e74'
		self['bg'] = self.cor_fundo
		self.frame_menu = Frame(self, bg = self.cor_fundo,pady=100)
		self.frame_menu.pack()
		self.botao_adcionar = Button(self.frame_menu,border=tamanho_borda_botao,relief=tipo_botao, text = "Adcionar",width = largura,height=altura,command = lambda:controler.show_frame(CadastrarSecretario),activebackground='green')
		self.botao_editar = Button(self.frame_menu,border=tamanho_borda_botao,relief=tipo_botao, text = "Editar",width = largura,height=altura,command = None,activebackground='green')
		self.botao_listar = Button(self.frame_menu,border=tamanho_borda_botao,relief=tipo_botao, text = "Listar",width = largura,height=altura,command = lambda:controler.show_frame(ListarSecretario),activebackground='green')
		self.botao_remover = Button(self.frame_menu,border=tamanho_borda_botao,relief=tipo_botao, text = "Remover",width = largura,height=altura,command = None,activebackground='green')
		self.botao_sair = Button(self.frame_menu,border=tamanho_borda_botao,relief=tipo_botao, text = "Sair",width = largura,height=altura,command = lambda:controler.show_frame(MenuPrincipal),activebackground='green')
		self.botao_adcionar.pack()
		self.botao_editar.pack()
		self.botao_listar.pack()
		self.botao_remover.pack()
		self.botao_sair.pack()
class CadastrarSecretario(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		largura = 60
		altura = 4
		self.cor_fundo = '#105e74'
		self['bg'] = self.cor_fundo
		largura = 20
		total_labels = 22
		tipo_botao = RIDGE
		tamanho_borda_botao = 8
		self.frame_titulo = Frame(self, bg = self.cor_fundo,pady=80)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=tamanho_borda_botao,relief=tipo_botao,text= "Adicionar secretario",width=60,height=4)
		self.titulo.grid(row=0,column=1)
		
		self.frame_participante = Frame(self, bg = self.cor_fundo,pady=20)
		self.frame_participante.pack()
		
		self.login = Label(self.frame_participante,border=2,relief=tipo_botao,text="login : ",width=largura)
		self.senha = Label(self.frame_participante,border=2,relief=tipo_botao,text="senha : ",width=largura)
		self.rep_senha = Label(self.frame_participante,border=2,relief=tipo_botao,text="repita senha : ",width=largura)
		
		self.entrada_login = Entry(self.frame_participante,width=80)
		self.entrada_senha = Entry(self.frame_participante,width=80,show="*",)
		self.entrada_rep_senha = Entry(self.frame_participante,width=80,show="*",)
		
		self.login.grid(row=0,column=0)
		self.senha.grid(row=(1*total_labels),column=0)
		self.rep_senha.grid(row=(2*total_labels),column=0)
		
		self.entrada_login.grid(row=0,column=1)
		self.entrada_senha.grid(row=(1*total_labels),column=1)
		self.entrada_rep_senha.grid(row=(2*total_labels),column=1)
		
		self.frame_botoes = Frame(self, bg = self.cor_fundo,pady=10)
		self.frame_botoes.pack()
		self.botao_salvar = Button(self.frame_botoes,border=tamanho_borda_botao,relief=tipo_botao,text = "Salvar",width = largura,command = lambda:self.valida_dados(controler),activebackground='green')
		self.botao_salvar.grid(row=0,column=0)
		self.botao_cancel = Button(self.frame_botoes,border=tamanho_borda_botao,relief=tipo_botao,text = "Cancelar",width = largura,command = lambda:controler.show_frame(Secretario),activebackground='green')
		self.botao_cancel.grid(row=0,column=10)
	def limpar_campos(self,controler):
		self.entrada_login.delete(0,END)
		self.entrada_senha.delete(0,END)
		self.entrada_rep_senha.delete(0,END)
	def valida_dados(self,controler):
		pass
class ListarSecretario(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self.cor_fundo = '#105e74'
		self['bg'] = self.cor_fundo
		largura = 20
		total_labels = 22
		tipo_botao = RIDGE
		tamanho_borda_botao = 8
		
		self.frame_titulo = Frame(self, bg = self.cor_fundo,pady=10,padx=10,height=600,width=900)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=tamanho_borda_botao,relief=tipo_botao,text= "Listando Secretarios",width=40,height=2)
		self.titulo.grid(row=0,column=1)
		self.frame_texto = Frame(self, bg = self.cor_fundo,pady=10,padx=10,height=100,width=100)
		self.frame_texto.pack()
		barra_rolagem = Scrollbar(self.frame_texto)
		barra_rolagem.pack(side=RIGHT, fill=Y)
		texto = "TEXTO"
		mensagem = Listbox(self.frame_texto, yscrollcommand = barra_rolagem.set,width=50,height=20)
		for linha in str(texto).split():
			mensagem.insert(END,linha)
		mensagem.pack()
		barra_rolagem.config(command=mensagem.yview)
		botao = Button(self,border=tamanho_borda_botao,relief=tipo_botao,text="fechar",width= 10, command= lambda: controler.show_frame(Secretario))
		botao.pack()
class RemoverSecretario(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		largura = 60
		altura = 4
		self.cor_fundo = '#105e74'
		self['bg'] = self.cor_fundo
		largura = 20
		total_labels = 22
		self.frame_titulo = Frame(self, bg = self.cor_fundo,pady=80)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,text= "Remover Secretario",width=60,height=4)
		self.titulo.grid(row=0,column=1)
		
		self.frame_participante = Frame(self, bg = self.cor_fundo,pady=20)
		self.frame_participante.pack()
		
		self.login = Label(self.frame_participante,text="login : ",width=largura)
		self.senha = Label(self.frame_participante,text="senha : ",width=largura)
		
		self.entrada_login = Entry(self.frame_participante,width=80)
		self.entrada_senha = Entry(self.frame_participante,width=80,show="*")
		
		self.login.grid(row=0,column=0)
		self.senha.grid(row=(1*total_labels),column=0)
		
		self.entrada_login.grid(row=0,column=1)
		self.entrada_senha.grid(row=(1*total_labels),column=1)
		
		self.frame_botoes = Frame(self, bg = self.cor_fundo,pady=10)
		self.frame_botoes.pack()
		self.botao_salvar = Button(self.frame_botoes, text = "Remover",width = largura,command = lambda:controler.show_frame(Secretario),activebackground='green')
		self.botao_salvar.grid(row=0,column=0)
		self.botao_cancel = Button(self.frame_botoes, text = "Cancelar",width = largura,command = lambda:controler.show_frame(Secretario),activebackground='green')
		self.botao_cancel.grid(row=0,column=10)
#MENU ACADEMIA
class Academia(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		largura = 60
		altura = 4
		self.cor_fundo = '#105e74'
		tipo_botao = RIDGE
		tamanho_borda_botao = 8
		self['bg'] = self.cor_fundo
		self.frame_menu = Frame(self, bg = self.cor_fundo,pady=50)
		self.frame_menu.pack()
		self.botao_adcionar = Button(self.frame_menu,border=tamanho_borda_botao,relief=tipo_botao, text = "Adicionar Academia",width = largura,height=altura,command = None,activebackground='green')
		self.botao_editar = Button(self.frame_menu,border=tamanho_borda_botao,relief=tipo_botao, text = "Adicionar Integrante",width = largura,height=altura,command = lambda:controler.show_frame(CadastrarParticipante),activebackground='green')
		self.botao_listar = Button(self.frame_menu,border=tamanho_borda_botao,relief=tipo_botao, text = "Listar Academia",width = largura,height=altura,command = None,activebackground='green')
		self.botao_listar_participante = Button(self.frame_menu,border=tamanho_borda_botao,relief=tipo_botao, text = "Listar Participante",width = largura,height=altura,command = None,activebackground='green')
		self.botao_remover = Button(self.frame_menu,border=tamanho_borda_botao,relief=tipo_botao, text = "Remover Academia",width = largura,height=altura,command = None,activebackground='green')
		self.botao_carteirinha = Button(self.frame_menu,border=tamanho_borda_botao,relief=tipo_botao, text = "Gerar Carteirinha",width = largura,height=altura,command = lambda:controler.show_frame(GerarCarteirinha),activebackground='green')
		self.botao_sair = Button(self.frame_menu,border=tamanho_borda_botao,relief=tipo_botao, text = "Sair",width = largura,height=altura,command = lambda:controler.show_frame(MenuPrincipal),activebackground='green')
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
		
		self.cor_fundo = '#105e74'
		self['bg'] = self.cor_fundo
		largura = 20
		total_labels = 22
		tipo_botao = RIDGE
		tamanho_borda_botao = 8
		
		self.frame_titulo = Frame(self, bg = self.cor_fundo,pady=10,padx=10,height=600,width=900)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,text= "Listando Academias",width=40,height=2)
		self.titulo.grid(row=0,column=1)
		self.frame_texto = Frame(self, bg = self.cor_fundo,pady=10,padx=10,height=100,width=100)
		self.frame_texto.pack()
		barra_rolagem = Scrollbar(self.frame_texto)
		barra_rolagem.pack(side=RIGHT, fill=Y)
		texto = "TEXTO"
		mensagem = Listbox(self.frame_texto, yscrollcommand = barra_rolagem.set,width=50,height=20)
		for linha in str(texto).split():
			mensagem.insert(END,linha)
		mensagem.pack()
		barra_rolagem.config(command=mensagem.yview)
		botao = Button(self,text="fechar",border=tamanho_borda_botao,relief=tipo_botao,width= 10, command= lambda: controler.show_frame(Academia))
		botao.pack()
#MENU PARTICIAPNTE
class CadastrarParticipante(Frame):
	def __init__(self,parent,controler):
		
		tipo_botao = RIDGE
		tamanho_borda_botao = 2
		
		self.tipo1_s = False
		self.tipo2_s = False
		self.tipo3_s = False
		self.tipo = "Professor"
		
		Frame.__init__(self,parent)
		largura = 60
		altura = 4
		self.cor_fundo = '#105e74'
		self['bg'] = self.cor_fundo
		largura = 20
		total_labels = 22
		self.frame_titulo = Frame(self, bg = self.cor_fundo,pady=80)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=8,relief=tipo_botao,text= "Cadastro Participante",width=60,height=4)
		self.titulo.grid(row=0,column=1)
		
		self.frame_participante = Frame(self, bg = self.cor_fundo,pady=20)
		self.frame_participante.pack()
		
		self.nome = Label(self.frame_participante,border=tamanho_borda_botao,relief=tipo_botao,text="Nome : ",width=largura)
		self.cpf = Label(self.frame_participante,border=tamanho_borda_botao,relief=tipo_botao,text="CPF : ",width=largura)
		self.data = Label(self.frame_participante,border=tamanho_borda_botao,relief=tipo_botao,text="Data de Nascimento : ",width=largura)
		self.academia = Label(self.frame_participante,border=tamanho_borda_botao,relief=tipo_botao,text="Academia: ",width=largura)
		self.faixa = Label(self.frame_participante,border=tamanho_borda_botao,relief=tipo_botao,text="Faixa: ",width=largura)
		self.endereco = Label(self.frame_participante,border=tamanho_borda_botao,relief=tipo_botao,text="Endereco : ",width=largura)
		
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
		
		self.frame_botoes = Frame(self, bg = self.cor_fundo,pady=10)
		self.frame_botoes.pack()
		self.botao_salvar = Button(self.frame_botoes, text = "Salvar",width = largura,command = lambda:self.limpar_campos(controler),activebackground='green')
		self.botao_salvar.grid(row=0,column=0)
		self.botao_cancel = Button(self.frame_botoes, text = "Cancelar",width = largura,command = lambda:controler.show_frame(Academia),activebackground='green')
		self.botao_cancel.grid(row=0,column=10)
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
class ListarParticipante(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self.cor_fundo = '#105e74'
		self['bg'] = self.cor_fundo
		largura = 20
		total_labels = 22
		self.frame_titulo = Frame(self, bg = self.cor_fundo,pady=10,padx=10,height=600,width=900)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,text= "Listando Secretarios",width=40,height=2)
		self.titulo.grid(row=0,column=1)
		self.frame_texto = Frame(self, bg = self.cor_fundo,pady=10,padx=10,height=100,width=100)
		self.frame_texto.pack()
		barra_rolagem = Scrollbar(self.frame_texto)
		barra_rolagem.pack(side=RIGHT, fill=Y)
		texto = "Texto"
		mensagem = Listbox(self.frame_texto, yscrollcommand = barra_rolagem.set,width=50,height=20)
		for linha in str(texto).split():
			mensagem.insert(END,linha)
		mensagem.pack()
		barra_rolagem.config(command=mensagem.yview)
		botao = Button(self,text="fechar",width= 10, command= lambda: controler.show_frame(Academia))
		botao.pack()

#GERAR CARTEIRINHA
class GerarCarteirinha(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		largura = 60
		altura = 4
		
		self.cor_fundo = '#105e74'
		self['bg'] = self.cor_fundo
		largura = 20
		total_labels = 22
		
		tipo_botao = RIDGE
		tamanho_borda_botao = 8
		
		self.frame_titulo = Frame(self, bg = self.cor_fundo,pady=80)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=tamanho_borda_botao,relief=tipo_botao,text= "Carterinha",width=60,height=4)
		self.titulo.grid(row=0,column=1)
		
		self.frame_participante = Frame(self, bg = self.cor_fundo,pady=20)
		self.frame_participante.pack()
		
		self.nome = Label(self.frame_participante,border=2,relief=tipo_botao,text="Nome Integrante : ",width=largura)
		self.cpf = Label(self.frame_participante,border=2,relief=tipo_botao,text="CPF : ",width=largura)
		self.academia = Label(self.frame_participante,border=2,relief=tipo_botao,text="Academia : ",width=largura)
		
		self.entrada_nome = Entry(self.frame_participante,width=80)
		self.entrada_cpf = Entry(self.frame_participante,width=80)
		self.entrada_academia = Entry(self.frame_participante,width=80)
		
		self.nome.grid(row=0,column=0)
		self.cpf.grid(row=(1*total_labels),column=0)
		self.academia.grid(row=(2*total_labels),column=0)
		
		self.entrada_nome.grid(row=0,column=1)
		self.entrada_cpf.grid(row=(1*total_labels),column=1)
		self.entrada_academia.grid(row=(2*total_labels),column=1)
		
		self.frame_botoes = Frame(self, bg = self.cor_fundo,pady=10)
		self.frame_botoes.pack()
		self.botao_gerar = Button(self.frame_botoes,border=tamanho_borda_botao,relief=tipo_botao,text = "Gerar Carteirinha",width = largura,command = None,activebackground='green')
		self.botao_gerar.grid(row=0,column=0)
		self.botao_cancel = Button(self.frame_botoes,border=tamanho_borda_botao,relief=tipo_botao,text = "Cancelar",width = largura,command = lambda:controler.show_frame(Academia),activebackground='green')
		self.botao_cancel.grid(row=0,column=10)
class Exibe_Carteira(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		largura = 60
		altura = 4
	
		
		self.cor_fundo = '#105e74'
		self['bg'] = self.cor_fundo
		largura = 20
		total_labels = 22
		
		self.frame_titulo = Frame(self, bg = self.cor_fundo,pady=80)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,text= "CARTEIRINHA",width=60,height=4)
		self.titulo.grid(row=0,column=1)
		
		self.frame_carteira = Frame(self, bg = self.cor_fundo,pady=20)
		self.frame_carteira.pack()
		
		self.nome = Label(self.frame_carteira,text="Nome Integrante : ",width=largura)
		self.nome_academia = Label(self.frame_carteira,text="Nome Academia : ",width=largura)
		self.cpf = Label(self.frame_carteira,text="CPF : ",width=largura)
		self.id = Label(self.frame_carteira,text="Id : ",width=largura)
		self.vencimento = Label(self.frame_carteira,text="Vencimento : ",width=largura)
		
		self.nome.pack()
		self.nome_academia.pack()
		self.cpf.pack()
		self.id.pack()
		self.vencimento.pack()
		self.frame_botoes = Frame(self, bg = self.cor_fundo,pady=20)
		self.botao_cancel = Button(self.frame_botoes, text = "Cancelar",width = largura,command = lambda:controler.show_frame(Academia),activebackground='green')
		self.botao_cancel.pack()		
#MENU SOBRE
class Sobre(Frame):
	def __init__(self,parent,controler):
		Frame.__init__(self,parent)
		self.cor_fundo = '#105e74'
		self['bg'] = self.cor_fundo
		largura = 20
		total_labels = 22
		tamanho_borda_botao = 8
		tipo_botao = RIDGE
		self.frame_titulo = Frame(self, bg = self.cor_fundo,pady=10,padx=10,height=600,width=900)
		self.frame_titulo.pack()
		self.titulo = Label(self.frame_titulo,border=tamanho_borda_botao,relief=tipo_botao,text= "Sobre",width=40,height=2)
		self.titulo.grid(row=0,column=1)
		self.frame_texto = Frame(self, bg = self.cor_fundo,pady=10,padx=10,height=4,width=10)
		self.frame_texto.pack()
		texto = "O sistema judorama foi desenvolvido para gerenciar a Federacao de judo\n"
		texto += "Uma Confederação qualquer de Judô pode usar nossa Plataforma para facilitar sua organizacao.\n"
		mensagem = Label(self.frame_texto,text=texto,font=('times','18'))
		mensagem.pack()
		botao = Button(self,border=tamanho_borda_botao,relief=tipo_botao,text="fechar",width= 10, command= lambda: controler.show_frame(MenuPrincipal))
		botao.pack()
def init_view():
	app = Geral()
	app.mainloop()
if __name__ == '__main__':
	init_view()