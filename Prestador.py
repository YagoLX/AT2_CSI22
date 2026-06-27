from validate_docbr import CPF, CNPJ
from abc import ABC, abstractmethod
from Endereco import Endereco, CEP_API

class Prestador: 
    def __init__(self):
        self.id = ""
        self.tipo_documento = ""
        self.documento = ""
        self.nascimento = ""
        self.contato = ""
        self.endereco = Endereco()
        self.usuario = ""
        self.senha = ""
        self.adm = False
        self.nome =""
    
    def def_adm(self, adm=False):
        try:
            self.adm = adm
        except:
            print("formato invalido na atribuicao de bool adm")
    
    def ler_adm(self, adm):
        return self.adm

    def def_usuario(self, usuario=""):
        try:
            self.usuario = usuario
        except:
            print("formato invalido na atribuicao de usuario")
    
    def ler_usuario(self):
        return self.usuario
    
    def def_senha(self, senha = ""):
        try:
            self.senha = senha
        except: 
            print("formato invalido na atribuicao de senha")

    def ler_senha(self):
        return self.senha

    def def_id(self,identificacao):
        try:
            self.id = identificacao
        except: 
            print("formato invalido na atribuicao de id")
    
    def ler_id(self):
        return self.id
    
    def def_documento(self, doc):
        try:    
            self.documento = doc
        except:
            print("Erro na atribuicao de documento")

    def ler_documento(self,doc):
        return self.documento

    def def_nascimento(self, nasc):
        try:
            self.nascimento = nasc
        except:
            print("Erro na atribuicao de data de nascimento")

    def ler_nascimento(self):
        return self.nascimento
    
    def def_contato(self, ctt):
        try:
            self.contato = ctt
        except:
            print("Erro na atribuicao de documento")

    def ler_contato(self):
        return self.contato
    
    def def_endereco(self, cep, complemento = "", numero = ""):
        try:
            interface = CEP_API()
            self.endereco = CEP_API.ler_endereco(cep)
            self.endereco.complemento = complemento
            self.endereco.numero = numero
        except:
            print("entrada em def_endereco invalida")

class validador(ABC):
    @abstractmethod
    def validar(self, dado):
        pass

class validador_cpf(ABC):
    def __init__(self):
        self.cpf = CPF()
    def validar(self, documento):
        try:
            return self.cpf.validate(documento)
        except:
            print('erro na validacao do cpf')

class validador_cnpj(validador):
    def validar(self, dado):
        try:
            cnpj = CNPJ()
            return cnpj.validate(dado)
        except:
            print('erro na validacao do cnpj')
    
