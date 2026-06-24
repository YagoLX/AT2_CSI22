#Banco de Dados
import sqlite3
from abc import ABC, abstractmethod
from Prestador import *

class banco():

    
    def __init__(self):
        self.SQL_CRIAR_TABELA = """create table if not exists prestadores(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     nome text,
                     tipo_documento text,
                     documento text,
                     nascimento text,
                     rua text,
                     numero text,
                     complemento text,
                     bairro text,
                     cidade text,
                     uf text,
                     cep text,
                     contato text)"""
        self.caminho = "prestador.db"
        self.conexao = sqlite3.connect(self.caminho)
        self.criar_tabela()

    def criar_tabela(self):
        c = self.conexao

        c.execute(self.SQL_CRIAR_TABELA)

        self.conexao.commit()
        c.close()

class dados_prestadores():

    def __init__(self, prestador = Prestador()):
        self.id = prestador.id
        self.tipo_documento = prestador.tipo_documento
        self.documento = prestador.documento
        self.nascimento = prestador.nascimento
        self.contato = prestador.contato
        prestador.endereco.bairro
        prestador.endereco.cep
        prestador.endereco.cidade
        prestador.endereco.complemento
        prestador.endereco.numero
        prestador.endereco.rua
        prestador.endereco.uf



    
