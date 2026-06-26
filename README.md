## Objetivo
Implementar um catalogo de Prestadores de Servico em TI com python e POO. 
Cada prestador deve possuir:
- CPF/CNPJ 
- Id
- Nome
- Data de Nascimento
- Endereco: rua, numero, complemento, bairro, cidade, UF, CEP
- Contato

## Requisitos
- verificar a validade do CPF/CNPJ 
- completar o endereco dado o CEP.
- CRUD
- Persistência dos dados
- Tratamento de Exceções

## Ideias de Biblioteca
- Via CEP
- sqlite3? ver qual foi usado da ultima vez
- tkinter/custom tkinter https://www.youtube.com/watch?v=yHdZvQhSRiA

## Passos
1) Implementar classes relativas ao prestador

2) Validacao de CPF e CNPJ
- docsbr implementado, falta testar

3) API CEP
- Via Cep 
- implementado, falta testar mais
 
4) Persistencia dos dados 
 - sqlite3. 
 Tutoriais: https://www.geeksforgeeks.org/python/python-sqlite-crud-operations/
 https://www.geeksforgeeks.org/python/python-sqlite/

 https://paginadoale.com.br/2025/10/crud-em-python-com-sqlite/

5) Interface Grafica
- 
-

6) Funções que preciso da DB
- verificar se é adm (buscar se adm dado documento): buscar_adm()
- login: retornar verdadeiro ou falso se o email e a senha (ambos tem que estar na mesma linha) estiverem na DB -- buscar senha dado documento: buscar_senha()
- função adicionar: temos que salvar na DB: Email, senha, documento, qual tipo de documento (baseado na entrada) (tem que ter uma coluna pra dizer se é CPF ou CNPJ), CEP, ciodade, UF, Bairro, rua, número, complemento. Não precisa verificar se é válido CPF ou CNPJ, vou fazer essa verificação antes de subir pra DB: criar_prestador() 
- função editar: Quando tiver logado, preciso conseguir editar as informações passadas com a função adicionar: atualizar_prestador()
- função verificar ADM: Retorna 0 ou 1 se o usuário for adm: buscar_adm()
- função consulta: tem que retornar um vetor/list de structs com os campos nome, email, documento, cidade, tipo_documento (cpf ou cnpj): listar_prestadores()
- dúvida na implementação da consulta: da pra puxar todos os dados da DB, organizar eles com .sort do python e lenha, mas isso com certeza é subótimo. Convém fazer uma função variável de busca? Os filtros que implementei são: CPF e CNPJ (check), caso contrário é só ordenar, daí é só usar o .sort msm, não precisa inventar moda. -- criarei listar_por_cpf listar_por_cnpj
- função apagar conta: apaga conta do DB: deletar_prestador