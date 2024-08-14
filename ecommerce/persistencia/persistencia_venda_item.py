import json
from modelos.venda_item import VendaItem

class PersistenciaVendaItem:
    _itens_venda = []

    @classmethod
    def inserir(cls, item_venda):
        cls._itens_venda.append(item_venda)

    @classmethod
    def listar(cls):
        return cls._itens_venda

    @classmethod
    def listar_id(cls, id):
        for item_venda in cls._itens_venda:
            if item_venda.id == id:
                return item_venda
        return None

    @classmethod
    def atualizar(cls, item_venda_atualizado):
        for idx, item_venda in enumerate(cls._itens_venda):
            if item_venda.id == item_venda_atualizado.id:
                cls._itens_venda[idx] = item_venda_atualizado
                return True
        return False

    @classmethod
    def excluir(cls, id):
        for idx, item_venda in enumerate(cls._itens_venda):
            if item_venda.id == id:
                del cls._itens_venda[idx]
                return True
        return False

    @classmethod
    def abrir(cls, arquivo):
        try:
            with open(arquivo, 'r') as f:
                data = json.load(f)
                cls._itens_venda = [VendaItem(**item_venda) for item_venda in data]
        except FileNotFoundError:
            cls._itens_venda = []

    @classmethod
    def salvar(cls, arquivo):
        with open(arquivo, 'w') as f:
            json.dump([item_venda.__dict__ for item_venda in cls._itens_venda], f)
