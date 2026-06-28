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
                     adm BOOLEAN)"""
        self.caminho = "prestador.db"
        self.conexao = sqlite3.connect(self.caminho)
        self.criar_tabela()

    def criar_tabela(self):
        try:
            c = self.conexao
            c.execute(self.SQL_CRIAR_TABELA)
            self.conexao.commit()
            c.close()
        except:
            print("Erro ao criar tabela")


    def criar_prestador(self, prestador = Prestador()):
        try:
            con = sqlite3.connect(self.caminho)
            cur = con.cursor()
            usuario = prestador.ler_usuario()
            senha = prestador.ler_senha()
            nome = prestador.ler_nome()
            tipo_documento = prestador.ler_tipo_documento()
            documento = prestador.ler_documento()
            nascimento = prestador.ler_nascimento()
            contato = prestador.ler_contato()
            adm = prestador.ler_adm()

            cur.execute("""
            INSERT INTO prestadores (
            usuario, senha, nome, tipo_documento, documento,
            nascimento, rua, numero, complemento,
            bairro, cidade, uf, cep, contato, adm
            )
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """, (
            usuario,
            senha,
            nome,
            tipo_documento,
            documento,
            nascimento,
            prestador.endereco.rua,
            prestador.endereco.numero,
            prestador.endereco.complemento,
            prestador.endereco.bairro,
            prestador.endereco.cidade,
            prestador.endereco.uf,
            prestador.endereco.cep,
            contato,
            adm
            ))
            con.commit()
            con.close()
        except: 
            print("Erro ao criar prestador")

    def listar_prestadores(self):
        try:
            con = sqlite3.connect(self.caminho)
            cur = con.cursor()
            cur.execute("""SELECT * FROM prestadores ORDER BY cidade""")
            linhas = cur.fetchall()
            con.close()
            return linhas
        except:
            print("Erro ao listar prestadores")
    
    def listar_por_cpf(self):
        try:
            con = sqlite3.connect(self.caminho)
            cur = con.cursor()
            cur.execute("""SELECT * FROM prestadores WHERE tipo_documento = 'cpf'""")
            linhas = cur.fetchall()
            con.close()
            return linhas
        except:
            print("Erro ao listar por cpf")
    
    def listar_por_cnpj(self):
        try:
            con = sqlite3.connect(self.caminho)
            cur = con.cursor()
            cur.execute("""SELECT * FROM prestadores WHERE tipo_documento = 'cnpj'""")
            linhas = cur.fetchall()
            con.close()
            return linhas
        except:
            print("Erro ao listar por CNPJ")

        
    def buscar_prestador(self,documento):
        try:
            con = sqlite3.connect(self.caminho)
            cur = con.cursor()
            cur.execute("""SELECT usuario, senha, 
                        nome, tipo_documento, documento,
                        nascimento, rua, numero, complemento,
                        bairro, cidade, uf, cep, contato, adm 
                    FROM prestadores WHERE documento = ?""", 
                    (documento,))
            linha = cur.fetchone()
            con.close()
            return linha
        except:
            print("Erro ao buscar prestador")
    
    def buscar_senha(self, doc=""):
        try:
            con = sqlite3.connect(self.caminho)
            cur = con.cursor()
            cur.execute("""SELECT senha FROM prestadores WHERE documento = ?""", (doc,))
            senha = cur.fetchone()
            con.close()
            return senha
        except:
            print("Erro ao buscar senha")
    
    def buscar_adm(self, doc = ""):
        try:
            con = sqlite3.connect(self.caminho)
            cur = con.cursor()
            cur.execute("""SELECT adm FROM prestadores WHERE documento = ?""", (doc,))
            status_adm = cur.fetchone()
            con.close()
            return status_adm
        except:
            print("Erro ao buscar bool adm")

    def atualizar_prestador(self, doc, novos_dados=Prestador()):
        try:
            con = sqlite3.connect(self.caminho)
            cur = con.cursor()
            usuario = novos_dados.ler_usuario()
            senha = novos_dados.ler_senha()
            nome = novos_dados.ler_nome()
            tipo_documento = novos_dados.ler_tipo_documento()
            documento = novos_dados.ler_documento()
            nascimento = novos_dados.ler_nascimento()
            contato = novos_dados.ler_contato()
            adm = novos_dados.ler_adm()
            cur.execute("""
            UPDATE prestadores SET
                usuario = ?,
                senha = ?,
                nome = ?,
                tipo_documento = ?,
                documento = ?,
                nascimento = ?,
                rua = ?,
                numero = ?,
                complemento = ?,
                bairro = ?,
                cidade = ?,
                uf = ?,
                cep = ?,
                contato = ?,
                adm = ?
            WHERE documento = ?
            """, (
            usuario,
            senha,
            nome,
            tipo_documento,
            documento,
            nascimento,
            novos_dados.endereco.rua,
            novos_dados.endereco.numero,
            novos_dados.endereco.complemento,
            novos_dados.endereco.bairro,
            novos_dados.endereco.cidade,
            novos_dados.endereco.uf,
            novos_dados.endereco.cep,
            contato,
            adm,
            doc
            ))

            modificado = cur.rowcount
            con.commit()
            con.close()
            return modificado
        except:
            print("Erro ao atulizar prestador")

    def deletar_prestador(self, documento =""):
        try:
            con = sqlite3.connect(self.caminho)
            cur = con.cursor()
            cur.execute("DELETE FROM prestadores WHERE documento = ?", (documento,))
            deletado = cur.rowcount
            con.commit()
            con.close()
            return deletado
        
        except: 
            print("Erro ao deletar prestador")


        




    
