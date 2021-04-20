import pymongo
from bson.objectid import ObjectId
import pandas as pd

class ConexaoMongo:
    def __init__(self, nome_banco:str, nome_collection:str):
        self.nome_banco = nome_banco
        self.nome_collection = nome_collection

        self.conexao = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.conexao[self.nome_banco]
        self.collection = self.db[self.nome_collection]

    def crud_create(self, lista_de_dict_ou_dicionario):
        """
        Recebe uma lista com vários dicionários ou apenas um dicionário.
        No dicionário, a key é o nome da coluna e o value é o valor do documento.
        Um único dicionário é convertido em lista para o método rodar.
        Cada dicionário será tratado como um documento (linha) no db.

        :param lista_de_dict_ou_dicionario: list, dict
        """
        # ---> TRATAR DADOS QUE CHEGAR ERRADO
        dados = lista_de_dict_ou_dicionario
        if type(dados) == dict:
            dados = [dados]
        executa = self.collection.insert_many(dados)
        print("Ids adicionados:")
        for i in executa.inserted_ids:
            print(i)


    def crud_update_one(self, dict_filtro:dict, dict_updates:dict):
        """
        :param dict_filtro: dicionário com os items (nome_coluna:valor) que serão
        utilizados para filtrar o db.
        :param dict_updates: dicionário com os novos valores (nome_coluna:vaalor) que
        deverão ser modificados ou até criados.
        """
        # ---> TRATAR DADOS QUE CHEGAR ERRADO
        executa = self.collection.update_one(dict_filtro,{"$set": dict_updates})
        if executa.modified_count == 0:
            print("OBSERVAÇÃO: Nenhum item foi modificado.")

    def crud_update_many(self, dict_filtro:dict, dict_updates:dict):
        # ---> TRATAR DADOS QUE CHEGAR ERRADO
        executa = self.collection.update_many(dict_filtro,{"$set": dict_updates})
        if executa.modified_count == 0:
            print("OBSERVAÇÃO: Nenhum item foi modificado.")

    def crud_delete_one(self, dict_filtro:dict):
        """
        :param dict_filtro: dicionário com os items (nome_coluna:valor) que serão
        utilizados para filtrar os documentos que a serem deletados. Deleta o primeiro
        documento (linha) encontrado.
        """
        # ---> TRATAR DADOS QUE CHEGAR ERRADO
        executa = self.collection.delete_one(dict_filtro)
        if executa.deleted_count == 0:
            print("OBSERVAÇÃO: Nenhum item foi deletado.")

    def crud_delete_many(self, dict_filtro: dict):
        """
        :param dict_filtro: dicionário com os items (nome_coluna:valor) que serão
        utilizados para filtrar os documentos que a serem deletados. Deleta os documentos
        (linhas) que atendem as condições.
        """
        # ---> TRATAR DADOS QUE CHEGAR ERRADO
        executa = self.collection.delete_many(dict_filtro)
        if executa.deleted_count == 0:
            print("OBSERVAÇÃO: Nenhum item foi deletado.")

    def crud_read(self, dict_filtro:dict):
        """
        :param dict_filtro: dicionário com os items (nome_coluna:valor) que serão
        utilizados para filtrar os documentos que serão printados.
        Quando há mais de um item no dict, a filtragem é por 'and'.
        """
        # ---> TRATAR DADOS QUE CHEGAR ERRADO
        dados = self.collection.find(dict_filtro)
        print(pd.DataFrame(dados))

    def crud_read_min_max(self, param:str, min:float, max:float):
        """
        A partir de um valor mínimo e máximo de uma coluna com valores numéricos,
        filtra os dados a serem apresentados.
        :param param: str: nome da coluna que será utilizada para filtrar.
        :param min: valor mínimo. Irá retornar todos os valores maiores
        :param max: valor máximo. Ira retornar todos os valores menores.
        """
        # ---> TRATAR DADOS QUE CHEGAR ERRADO
        dados = self.collection.find({"$and":[{param:{"$gt":min}},{param:{"$lt": max}}]})
        print(pd.DataFrame(dados))

cnx = ConexaoMongo("novo_db_teste", "usuarios")
#cnx.crud_create([dict(nome="Luana Bittencourt", idade=55), dict(nome="juliana", idade=49)])
#cnx.crud_update_many(dict(nome="Gustavo"),dict(idade=55, curso="Completo"))
#cnx.crud_delete_many(dict(nome="Ana Furtado", curso="Completo"))
#cnx.crud_read(dict(nome="Gustavo", curso="Completo"))
#cnx.crud_read_min_max("idade",20,30)