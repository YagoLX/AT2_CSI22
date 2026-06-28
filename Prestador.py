from validate_docbr import CPF, CNPJ
from abc import ABC, abstractmethod
from Endereco import Endereco, CEP_API

class Prestador: 
    def __init__(self):
        self._id = ""
        self._tipo_documento = ""
        self._documento = ""
        self._nascimento = ""
        self._contato = ""
        self.endereco = Endereco()
        self._usuario = ""
        self._senha = ""
        self._adm = False
        self._nome =""
    

    def def_adm(self, adm=False):
        try:
            self._adm = adm
        except:
            print("formato invalido na atribuicao de bool adm")
    
    def ler_adm(self, adm):
        return self._adm

    def def_usuario(self, usuario=""):
        try:
            self._usuario = usuario
        except:
            print("formato invalido na atribuicao de usuario")
    
    def ler_usuario(self):
        return self._usuario
    
    def def_senha(self, senha = ""):
        try:
            self._senha = senha
        except: 
            print("formato invalido na atribuicao de senha")

    def ler_senha(self):
        return self._senha

    def def_id(self,identificacao):
        try:
            self._id = identificacao
        except: 
            print("formato invalido na atribuicao de id")
    
    def ler_id(self):
        return self._id
    
    def def_tipo_documento(self, tipo_documento=""):
        try: 
            self._tipo_documento = tipo_documento
        except:
            print("Erro na atribuicao de tipo de documento")

    def ler_tipo_documento(self):
        return self._tipo_documento
    
    def def_documento(self, doc):
        try:    
            self._documento = doc
        except:
            print("Erro na atribuicao de documento")

    def ler_documento(self,doc):
        return self._documento

    def def_nascimento(self, nasc):
        try:
            self._nascimento = nasc
        except:
            print("Erro na atribuicao de data de nascimento")

    def ler_nascimento(self):
        return self._nascimento
    
    def def_contato(self, ctt):
        try:
            self._contato = ctt
        except:
            print("Erro na atribuicao de documento")

    def ler_contato(self):
        return self._contato
    
    def def_endereco(self, cep, complemento = "", numero = ""):
        try:
            interface = CEP_API()
            self.endereco = CEP_API.ler_endereco(cep)
            self.endereco.complemento = complemento
            self.endereco.numero = numero
        except:
            print("entrada em def_endereco invalida")
    
    def def_nome(self, nome=""):
        try:
            self._nome = nome
        except:
            print("entrada em def nome invalida")
    
    def ler_nome(self):
        return self._nome

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
    
