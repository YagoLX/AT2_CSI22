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

    def def_id(self,identificacao):
        self.id = identificacao
    def ler_id(self):
        return self.id
    
    def def_documento(self, doc):
        self.documento = doc

    def ler_documento(self,doc):
        return self.documento

    def def_nascimento(self, nasc):
        self.nascimento = nasc
    
    def ler_nascimento(self):
        return self.nascimento
    
    def def_contato(self, ctt):
        self.contato = ctt

    def ler_contato(self):
        return self.contato
    
    def def_endereco(self, cep, complemento = "", numero = ""):
        interface = CEP_API()
        self.endereco = CEP_API.ler_endereco(cep)
        self.endereco.complemento = complemento
        self.endereco.numero = numero

class validador_cpf:
    def __init__(self):
        self.cpf = CPF()
    def validar(self, documento):
        try:
            return self.cpf.validate(documento)
        except:
            print('PROBLEMA COM A FUNCAO VALIDAR CPF')

class validador(ABC):
    @abstractmethod
    def validar(self, dado):
        pass

class validador_cpf(validador):
    def validar(self, dado):
        cpf = CPF()
        return cpf.validate(dado)

class validador_cnpj(validador):
    def validar(self, dado):
        cnpj = CNPJ()
        return cnpj.validate(dado)
    
