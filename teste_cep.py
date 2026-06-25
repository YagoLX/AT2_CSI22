#AQUI FOI SO UM TESTE E PRA ILUSTRAR COMO FUNCIONA 
#APAGAR NA VERSAO FINAL

import requests
#queremos o cep no formato de 8 numeros tipo: "00000000"
cep = "1228900"
cep = cep.replace("-","").replace(".","").replace(" ","")

if cep.isdigit and len(cep) == 8:
    #podemos consultar
    link = f"https://viacep.com.br/ws/{cep}/json/"

    requisicao = requests.get(link, timeout=5)
    
    dados = requisicao.json()
    if isinstance(dados, dict) and dados.get("erro"):
        print("CEP não encontrado")
    else:
        print("CEP:", dados["cep"])
        print("Logradouro:", dados["logradouro"])
        print("Complemento:")
        print("Bairro:", dados["bairro"])
        print("Localidade:", dados["localidade"])
        print("UF:", dados["uf"])

