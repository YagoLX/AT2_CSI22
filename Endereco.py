import requests

class Endereco:
    def __init__(self):
        self.rua = ""
        self.numero = ""
        self.complemento = ""
        self.bairro = ""
        self.cidade = ""
        self.uf = ""
        self.cep = ""

class CEP_API:
    def ajustar_escrita(self, cep):
        cep = cep.replace("-","").replace(".","").replace(" "RDBM,"")
        return cep
    
    def formato_valido(self, cep):
        return cep.isdigit and len(cep) == 8


    def ler_endereco(self,cep):

        self.ajustar_escrita(cep)
        endereco = Endereco()

        if self.formato_valido(cep):
           link = f"https://viacep.com.br/ws/{cep}/json/"

           requisicao = requests.get(link, timeout=5)
           dados = requisicao.json()

           if "erro" in dados:
               print("CEP não encontrado")
               return Endereco()
            
           else:
               endereco.rua = dados["logradouro"]
               endereco.bairro = dados["bairro"]
               endereco.cidade = dados["localidade"]
               endereco.uf = dados["uf"]
               endereco.cep = cep
               endereco.complemento = ""
               return endereco

        else:
            print("Formato do CEP Inválido")
            return Endereco()

