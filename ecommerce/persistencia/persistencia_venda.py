import json
from modelos.venda import Venda

class PersistenciaVenda:
    _vendas = []

    @classmethod
    def inserir(cls, venda):
        cls._vendas.append(venda)

    @classmethod
    def listar(cls):
        return cls._vendas

    @classmethod
    def listar_id(cls, id):
        for venda in cls._vendas:
            if venda.id == id:
                return venda
        return None

    @classmethod
    def atualizar(cls, venda_atualizada):
        for idx, venda in enumerate(cls._vendas):
            if venda.id == venda_atualizada.id:
                cls._vendas[idx] = venda_atualizada
                return True
        return False

    @classmethod
    def excluir(cls, id):
        for idx, venda in enumerate(cls._vendas):
            if venda.id == id:
                del cls._vendas[idx]
                return True
        return False

    @classmethod
    def abrir(cls, arquivo):
        try:
            with open(arquivo, 'r') as f:
                data = json.load(f)
                cls._vendas = [Venda(**venda) for venda in data]
        except FileNotFoundError:
            cls._vendas = []

    @classmethod
    def salvar(cls, arquivo):
        with open(arquivo, 'w') as f:
            json.dump([venda.__dict__ for venda in cls._vendas], f)
