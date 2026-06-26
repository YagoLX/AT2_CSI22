import customtkinter as ctk
from tkcalendar import DateEntry
from datetime import date
from Endereco import CEP_API, Endereco

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

class Aplicativo(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Catálogo de Prestadores")
        self.geometry("1080x720")

        #configurando a grade
        self.grid_columnconfigure(1 , weight=1)
        self.grid_rowconfigure(0, weight=1)

        #lateral
        self.barra_lateral = ctk.CTkFrame(self,200)
        self.barra_lateral.grid(row=0, column = 0, sticky = "nsew")

        #principal
        self.principal = ctk.CTkFrame(self,400)
        self.principal.grid(row=0, column = 1, sticky = "nsew", padx = 10)

        self.Deslogado()
        self.deslogado()

        self.admin = False

    def limpar_tela(self, tela):
        for widget in list(tela.winfo_children()):
            widget.destroy()
    
    def sair(self):
        self.Deslogado()
        self.deslogado()
        self.admin = False

    def Deslogado(self):
        self.limpar_tela(self.barra_lateral)
        self.titulo = ctk.CTkLabel(self.barra_lateral,
                                    text = "Catálogo de Prestadores",
                                    font = ctk.CTkFont(size = 18, weight="bold"))
        self.titulo.pack(pady=(30,10), padx = (20,20))


        self.botao_cadastro = ctk.CTkButton(self.barra_lateral,
                                            text = "Cadastre-se", command = self.cadastro)
        self.botao_cadastro.pack(pady = (10,10), padx = (20,20), side = "bottom")

        self.botao_login = ctk.CTkButton(self.barra_lateral,
                                         text = "Login", command = self.login)
        self.botao_login.pack(pady = (10,10), padx = (20,20), side = "bottom")
        
    def Logado(self):
        self.limpar_tela(self.barra_lateral)
        self.nome = ctk.CTkLabel(self.barra_lateral,
                                 text = "Olá  + retorno da funcao de busca da DB",
                                 font = ctk.CTkFont(size = 18, weight= "bold"))
        self.nome.pack(pady=(30,10), padx = (20,20))       
        self.disponivel = ctk.CTkCheckBox(self.barra_lateral,
                                          text = "Disponível para trabalho!")
        self.disponivel.pack(pady=(30,30), padx = (20,20))
        
        self.botao_sair = ctk.CTkButton(self.barra_lateral,
                                         text = "Sair", command = self.sair)
        
        self.botao_sair.pack(pady = (10,10), padx = (20,20), side = "bottom", command = self.sair)

        self.botao_editar = ctk.CTkButton(self.barra_lateral,
                                         text = "Editar dados")
        
        self.botao_editar.pack(pady = (10,10), padx = (20,20), side = "bottom")

    def LogadoAdm(self):
        self.limpar_tela(self.barra_lateral)
        self.nome = ctk.CTkLabel(self.barra_lateral,
                                 text = "Olá ADM + retorno da funcao de busca da DB",
                                 font = ctk.CTkFont(size = 18, weight= "bold"))
        self.nome.pack(pady=(30,10), padx = (20,20))       
        self.botao_sair = ctk.CTkButton(self.barra_lateral,
                                         text = "Sair", command = self.sair)
        
        self.botao_sair.pack(pady = (10,10), padx = (20,20), side = "bottom")

    def deslogado(self):
        self.limpar_tela(self.principal)
        aviso = ctk.CTkLabel(self.principal, text = "Faça login para ver os prestadores.")
        aviso.place(relx = 0.5, rely = 0.5, anchor = "center")

    def login(self):
        self.limpar_tela(self.principal)
        self.campo_email = ctk.CTkEntry(self.principal,
                                  placeholder_text="Digite seu email",
                                  width = 300)
        self.campo_email.pack(pady = (200,20), padx = 100)

        self.campo_senha = ctk.CTkEntry(self.principal,
                                  placeholder_text="Digite sua senha",
                                  width = 300,
                                  show = "*")
        self.campo_senha.pack(pady=(0,0),padx= 100)

        botao_entrar = ctk.CTkButton(self.principal,
                                         text = "Entrar", command = self.fazer_login)
        botao_entrar.pack(pady = (10,10), padx = (20,20))

        ###o que fazer aqui????
        esqueceu_senha = ctk.CTkButton(self.principal,
                                         text = "Esqueceu sua senha?", command = self.esqueceu_senha)
        esqueceu_senha.pack(pady = (0,10), padx = (20,20))

    def cadastro(self):
        self.limpar_tela(self.principal)
        self.principal.columnconfigure(4, weight = 1)
        self.principal.rowconfigure(10, weight = 1) 

        email_label = ctk.CTkLabel(self.principal, text = "Email:")
        email_label.grid(row = 0, column = 0, pady = 20, padx = 10, sticky = "e")
        self.campo_email2 = ctk.CTkEntry(self.principal, placeholder_text="Digite seu email", width = 300)
        self.campo_email2.grid(row = 0, column = 1, pady = 20, padx = 10)

        senha_label = ctk.CTkLabel(self.principal, text = "Senha:")
        senha_label.grid(row = 1, column = 0, pady = (20,20), padx = 10, sticky = "e")
        self.campo_senha2 = ctk.CTkEntry(self.principal, placeholder_text="Digite sua senha", width = 300)
        self.campo_senha2.grid(row = 1, column = 1, pady = (20,20), padx = 10)

        doc_label = ctk.CTkLabel(self.principal, text = "Documento:")
        doc_label.grid(row = 2, column = 0, pady = (20,20), padx = 10, sticky = "e")
        self.campo_doc = ctk.CTkEntry(self.principal, placeholder_text="Digite seu CPF/CNPJ", width = 300)
        self.campo_doc.grid(row = 2, column = 1, pady = (20,20), padx = 10)

        data_nasc = ctk.CTkLabel(self.principal, text = "Data de nascimento:")
        data_nasc.grid(row = 3, column = 0, pady = (20,20), padx = 10, sticky = "e")
        self.campo_data = DateEntry(self.principal, date_pattern = "dd/mm/yyyy")
        self.campo_data.grid(row = 3, column = 1, pady = (20,20), padx = 10)

        CEP_label = ctk.CTkLabel(self.principal, text = "CEP:")
        CEP_label.grid(row = 4, column = 0, pady = (20,20), padx = 10, sticky = "e")
        self.campo_CEP = ctk.CTkEntry(self.principal, placeholder_text="Digite seu CEP", width = 300)
        self.campo_CEP.grid(row = 4, column = 1, pady = (20,20), padx = 10)
        self.buscar_cep = ctk.CTkButton(self.principal, text = "Buscar", command = self.buscar_CEP)
        self.buscar_cep.grid(row = 4, column = 2, pady = (20,20))

        cidade_label = ctk.CTkLabel(self.principal, text = "Cidade:")
        cidade_label.grid(row = 5, column = 0, pady = (20,20), padx = 10, sticky = "e")
        self.cidade_entry = ctk.CTkEntry(self.principal, placeholder_text= "Cidade", width = 300)
        self.cidade_entry.grid(row = 5, column = 1, pady = (20,20), padx = 10, sticky = "e")
        self.cidade_entry.configure(state = "normal")

        self.UF_entry = ctk.CTkEntry(self.principal, placeholder_text= "UF", width = 50)
        self.UF_entry.grid(row = 5, column = 2, pady = (20,20), padx = 0, sticky = "w")
        self.UF_entry.configure(state = "normal")

        bairro_label = ctk.CTkLabel(self.principal, text = "Bairro:")
        bairro_label.grid(row = 7, column = 0, pady = (20,20), padx = 10, sticky = "e")
        self.bairro_entry = ctk.CTkEntry(self.principal, placeholder_text= "Bairro", width = 300)
        self.bairro_entry.grid(row = 7, column = 1, pady = (20,20), padx = 10, sticky = "e")
        self.bairro_entry.configure(state = "normal")

        rua_label = ctk.CTkLabel(self.principal, text = "Rua:")
        rua_label.grid(row = 8, column = 0, pady = (20,20), padx = 10, sticky = "e")
        self.rua_entry = ctk.CTkEntry(self.principal, placeholder_text= "Rua", width = 300)
        self.rua_entry.grid(row = 8, column = 1, pady = (20,20), padx = 10, sticky = "e")
        self.rua_entry.configure(state = "normal")

        self.numero_entry = ctk.CTkEntry(self.principal, placeholder_text= "N°", width = 50)
        self.numero_entry.grid(row = 8, column = 2, pady = (20,20), padx = 0, sticky = "w")

        complemento_label = ctk.CTkLabel(self.principal, text = "Complemento:")
        complemento_label.grid(row = 9, column = 0, pady = (20,20), padx = 10, sticky = "e")
        self.complemento_entry = ctk.CTkEntry(self.principal, placeholder_text= "Complemento", width = 300)
        self.complemento_entry.grid(row = 9, column = 1, pady = (20,20), padx = 10, sticky = "e")
        
        botao_criar = ctk.CTkButton(self.principal, text = "Criar conta")
        botao_criar.grid(row = 10, column = 1)

    def logado(self):
        self.limpar_tela(self.principal)

        self.filtros = ctk.CTkFrame(self.principal, height = 50)
        self.filtros.pack(fill = "x")

        self.enable_cpf = ctk.CTkCheckBox(self.filtros, text = "CPF")
        self.enable_cpf.pack(side = "right", padx = 10)

        self.enable_cnpj = ctk.CTkCheckBox(self.filtros, text = "CNPJ")
        self.enable_cnpj.pack(side = "right", padx = 5)

        label_ordenacao = ctk.CTkLabel(self.filtros, text = "Filtros:")
        label_ordenacao.pack(side = "right", padx = (230, 10))

        self.menu_ordenacao = ctk.CTkOptionMenu(self.filtros, values = ["Nome(A-Z)", "Cidade"])
        self.menu_ordenacao.pack(side = "right", padx = 10)

       
        label_ordenacao2 = ctk.CTkLabel(self.filtros, text = "Ordenar por:")
        label_ordenacao2.pack(side = "right", padx = (50, 10))

        self.rolagem = ctk.CTkScrollableFrame(self.principal, label_text="Prestadores Disponíveis")
        self.rolagem.pack(fill = "both", expand = True, padx = 10, pady = 5)

    def habilitar_cpf(self):
        self.cpf = self.enable_cpf.get()
        self.atualizar_lista()
        pass

    def habilitar_cnpj(self):
        self.cnpj = self.enable_cnpj.get()
        self.atualizar_lista()
        pass

    def atualizar_lista(self):
        ordem = self.menu_ordenacao.get()
        if ordem == "Nome(A-Z)":
            pass
        else:
            pass
        
        #usar as funcoes anteriores para pegar os dados PF ou PJ
        #produto = coluna/linha dos dados por isso estamos iterando sobre ele. Verificar!
        for produto in dados:
            card = cardPrestadores(self.rolagem, produto, self.admin)
            card.pack(fill = "x", padx = 10, pady = 5)
        pass   
         
    def fazer_login(self):
        email = self.campo_email.get()
        senha = self.campo_senha.get()

        #usar esses dados para fazer validacao no DB
        validacao = False
        self.admin = False ##VERIFICAR NA DB SE É ADMIN TB

        if validacao and self.admin:
            self.LogadoAdm()
            self.logado()
        elif not self.admin and validacao:
            self.Logado()
            self.logado()
        else:
            mensagem_erro = ctk.CTkLabel(self.principal, text= "Usuário ou senha incorretos", text_color= "red")
            mensagem_erro.pack(pady = 50)

    def salvar_dados(self):
        pass

    def editar(self):
        #copiar o cadastro, usar funcao do banco de dados pra atualizar alguma coisa
        pass

    def editarADM(self):
        #pesquisar como alterar a classe pra quando eu tiver esse acesso aparecer um botao apagar
        pass
    
    def esqueceu_senha(self):
        aviso_senha = ctk.CTkLabel(self.principal, text = "Entre em contato com os desenvolvedores no email: desenvolvedores@emailfake.com")
        aviso_senha.pack(pady=10)

    def buscar_CEP(self):

        numero_CEP = self.campo_CEP.get()
        CEP = CEP_API()
        endereco = CEP.ler_endereco(numero_CEP)
        self.erroCEP = ctk.CTkLabel(self.principal)

        if(endereco.cidade == ""):
            self.erroCEP.configure(text = "Erro na busca, verifique o CEP")
            self.erroCEP.grid(row = 4, column = 3, padx=5 )
            self.cidade_entry.configure(state ="normal")
            self.UF_entry.configure(state ="normal")
            self.bairro_entry.configure(state ="normal")
            self.rua_entry.configure(state ="normal")

        else:
            self.erroCEP.configure(text = "Busca bem sucedida!")
            self.cidade_entry.configure(state ="normal")
            self.cidade_entry.delete(0, "end")
            self.cidade_entry.insert(0, endereco.cidade)
            self.cidade_entry.configure(state ="disabled")
            self.UF_entry.configure(state ="normal")
            self.UF_entry.delete(0, "end")
            self.UF_entry.insert(0, endereco.uf)
            self.UF_entry.configure(state ="disabled")
            self.bairro_entry.configure(state ="normal")
            self.bairro_entry.delete(0, "end")
            self.bairro_entry.insert(0, endereco.bairro)
            self.bairro_entry.configure(state ="disabled")
            self.rua_entry.configure(state ="normal")
            self.rua_entry.delete(0, "end")
            self.rua_entry.insert(0, endereco.rua)
            self.rua_entry.configure(state ="disabled")

class cardPrestadores(ctk.CTkFrame):
    def __init__(self, master, dados_prestadores, admin):
        super().__init__(master)

        self.configure(fg_color=("#F5F102", "#000657"), height=50)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(3, weight = 1)

        self.nome = ctk.CTkLabel(master, text = dados_prestadores.nome, font = ctk.CTkFont(size = 20, weight= "bold"))
        self.nome.grid(column = 0, row = 0, padx = 10, pady = 5)

        if(admin):
            self.deletar = ctk.CTkButton(master, text = "X", color = "red")
            self.deletar.grid(column =0 , row = 1, sticky = "e")

        self.contato = ctk.CTkLabel(master, text = dados_prestadores.email, font= ctk.CTkFont(size = 12))
        self.contato.grid(column = 0, row = 1, padx = 10, pady = 5)

        self.documento = ctk.CTkLabel(master, text = dados_prestadores.documento, font= ctk.CTkFont(size = 12))
        self.documento.grid(column = 0, row = 2, padx = 10, pady = 5)

        self.endereco = ctk.CTkLabel(master, text = dados_prestadores.cidade, font= ctk.CTkFont(size = 12))
        self.endereco.grid(column = 0, row = 3, padx = 10, pady = 5)

janela = Aplicativo()
janela.mainloop()