from Prestador import *
from Endereco import *
from Banco import *


prestador1 = Prestador() 
prestador1.adm = True
prestador1.documento = "92553044020"
prestador1.tipo_documento = "cpf"
prestador1.endereco = CEP_API().ler_endereco("12228462")
prestador1.endereco.numero = "10"
prestador1.usuario = "Pietro"
prestador1.senha = "123"
prestador1.nascimento = "01/01/2001"
prestador1.contato = "pietrinho@gmail.com"
prestador1.endereco.complemento = "no dcta"

prestador2 = Prestador() 
prestador2.adm = False
prestador2.documento = "48355731000186"
prestador2.tipo_documento = "cnpj"
prestador2.endereco = CEP_API().ler_endereco("66640000")
prestador2.endereco.numero = "11"
prestador2.usuario = "Yago"
prestador2.senha = "321"
prestador2.nascimento = "02/02/2002"
prestador2.contato = "yaguinho@gmail.com"
prestador2.endereco.complemento = "fora do dcta"

db = banco()
#db.criar_prestador(prestador1)
#db.criar_prestador(prestador2)

#lista = db.listar_prestadores()
#print(lista)
saida = db.listar_prestadores()
print(saida[0]["documento"])
#saida de exemplo: ('Yago', '321', '', 'cnpj', '48355731000186', '02/02/2002', 'Rodovia Augusto Montenegro', '11', 'fora do dcta', 'Mangueirão', 'Belém', 'PA', '66640000', 'yaguinho@gmail.com', 0)
