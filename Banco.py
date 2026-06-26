#Banco de Dados
import sqlite3
from abc import ABC, abstractmethod
from Prestador import *

class banco():

    
    def __init__(self):
        self.SQL_CRIAR_TABELA = """create table if not exists prestadores(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     usuario text,
                     senha text,
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
                     contato text,
                     adm text)"""
        self.caminho = "prestador.db"
        self.conexao = sqlite3.connect(self.caminho)
        self.criar_tabela()

    def criar_tabela(self):
        c = self.conexao

        c.execute(self.SQL_CRIAR_TABELA)

        self.conexao.commit()
        c.close()
    


    def criar_prestador(self, prestador = Prestador(), adm = False):
        con = sqlite3.connect(self.caminho)
        cur = con.cursor()
        if prestador.def_documento != "" and prestador.nome != "" :
            cur.execute("""INSERT INTO prestadores (usuario, senha, 
                        nome, tipo_documento, documento,
                        nascimento, rua, numero, complemento,
                        bairro, cidade, uf, cep, contato, adm) 
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"""
                        (prestador.usuario, prestador.senha,
                         prestador.nome, prestador.tipo_documento,
                         prestador.documento,
                         prestador.nascimento, prestador.rua,
                         prestador.endereco.numero,
                         prestador.endereco.complemento,
                         prestador.endereco.bairro,
                         prestador.endereco.cidade,
                         prestador.endereco.uf,
                         prestador.endereco.cep,
                         prestador.contato,
                         prestador.adm))
            
    def listar_prestadores(self):
        con = sqlite3.connect(self.caminho)
        cur = con.cursor()
        cur.execute("""SELECT usuario, senha, 
                        nome, tipo_documento, documento,
                        nascimento, rua, numero, complemento,
                        bairro, cidade, uf, cep, contato, adm FROM prestadores ORDER BY cidade""")
        
    def buscar_prestador(self,documento):
        con = sqlite3.connect(self.caminho)
        cur = con.cursor()
        cur.execute("""SELECT usuario, senha, 
                        nome, tipo_documento, documento,
                        nascimento, rua, numero, complemento,
                        bairro, cidade, uf, cep, contato, adm 
                    FROM prestadores WHERE documento = ?""", 
                    (documento))
        linha = cur.fetchonte()
        con.close()
        return linha
    
    def buscar_senha(self, usuario=""):
        con = sqlite3.connect(self.caminho)
        cur = con.cursor()
        cur.execute("""SELECT senha FROM prestadores WHERE usuario = ?""", (usuario))
        senha = cur.fetchone()
        con.close()
        return senha

    def atualizar_prestador(self, cpf, prestador = Prestador()):
        con = sqlite3.connect(self.caminho)
        cur = con.cursor()
        cur.execute("""UPDATE prestadores SET usuario, senha, nome, tipo_documento, documento, nascimento
                    rua, numero, complemento, bairro, cidade, uf, cep, contato, adm = ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?""",
                    (prestador.usuario, prestador.senha, prestador.nome, prestador.tipo_documento, prestador.documento,
                     prestador.nascimento, prestador.endereco.rua, prestador.endereco.numero,
                     prestador.endereco.complemento, prestador.endereco.bairro, prestador.endereco.cidade,
                     prestador.endereco.uf, prestador.endereco.uf, prestador.endereco.cep, 
                     prestador.endereco.contato, prestador.endereco.adm))
        modificado = cur.rowcount()
        con.commit()
        con.close()
        return modificado
    
    def deletar_prestador(self, documento =""):
        con = sqlite3.connect(self.caminho)
        cur = con.cursor()
        cur.execute("DELETE FROM prestadores WHERE documento = ?", (documento))
        deletado = cur.rowcount
        con.commit()
        con.close()
        return deletado



        




    
