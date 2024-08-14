import json
from modelos.produto import Produto

class PersistenciaProduto:
    _produtos = []

    @classmethod
    def inserir(cls, produto):
        cls._produtos.append(produto)

    @classmethod
    def listar(cls):
        return cls._produtos

    @classmethod
    def listar_id(cls, id):
        for produto in cls._produtos:
            if produto.id == id:
                return produto
        return None

    @classmethod
    def atualizar(cls, produto_atualizado):
        for idx, produto in enumerate(cls._produtos):
            if produto.id == produto_atualizado.id:
                cls._produtos[idx] = produto_atualizado
                return True
        return False

    @classmethod
    def excluir(cls, id):
        for idx, produto in enumerate(cls._produtos):
            if produto.id == id:
                del cls._produtos[idx]
                return True
        return False

    @classmethod
    def abrir(cls, arquivo):
        try:
            with open(arquivo, 'r') as f:
                data = json.load(f)
                cls._produtos = [Produto(**produto) for produto in data]
        except FileNotFoundError:
            cls._produtos = []

    @classmethod
    def salvar(cls, arquivo):
        with open(arquivo, 'w') as f:
            json.dump([produto.__dict__ for produto in cls._produtos], f)
