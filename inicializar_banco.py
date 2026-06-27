from Prestador import *
from Endereco import *
from Banco import *


prestador1 = Prestador() 
prestador1._adm = True
prestador1._documento = "92553044020"
prestador1._tipo_documento = "cpf"
prestador1._endereco = CEP_API().ler_endereco("12228462")
prestador1._endereco.numero = "10"
prestador1._usuario = "Pietro"
prestador1._senha = "123"
prestador1._nascimento = "01/01/2001"
prestador1._contato = "pietrinho@gmail.com"
prestador1._endereco.complemento = "no dcta"

prestador2 = Prestador() 
prestador2._adm = False
prestador2._documento = "48355731000186"
prestador2._tipo_documento = "cnpj"
prestador2._endereco = CEP_API().ler_endereco("66640000")
prestador2._endereco.numero = "11"
prestador2._usuario = "Yago"
prestador2._senha = "321"
prestador2._nascimento = "02/02/2002"
prestador2._contato = "yaguinho@gmail.com"
prestador2._endereco.complemento = "fora do dcta"

db = banco()
#db.criar_prestador(prestador1)
db.criar_prestador(prestador2)

#lista = db.listar_prestadores()
#print(lista)
saida = db.listar_prestadores()
print(saida[0]["documento"])
#saida de exemplo: ('Yago', '321', '', 'cnpj', '48355731000186', '02/02/2002', 'Rodovia Augusto Montenegro', '11', 'fora do dcta', 'Mangueirão', 'Belém', 'PA', '66640000', 'yaguinho@gmail.com', 0)
                    # 0      1     2     3              4            5                      6                   7          8            9            10     11         12           13            14                        