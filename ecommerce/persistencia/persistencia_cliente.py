import json
from modelos.cliente import Cliente

class PersistenciaCliente:
    _clientes = []

    @classmethod
    def inserir(cls, cliente):
        cls._clientes.append(cliente)

    @classmethod
    def listar(cls):
        return cls._clientes

    @classmethod
    def listar_id(cls, id):
        for cliente in cls._clientes:
            if cliente.id == id:
                return cliente
        return None

    @classmethod
    def atualizar(cls, cliente_atualizado):
        for idx, cliente in enumerate(cls._clientes):
            if cliente.id == cliente_atualizado.id:
                cls._clientes[idx] = cliente_atualizado
                return True
        return False

    @classmethod
    def excluir(cls, id):
        for idx, cliente in enumerate(cls._clientes):
            if cliente.id == id:
                del cls._clientes[idx]
                return True
        return False

    @classmethod
    def abrir(cls, arquivo):
        try:
            with open(arquivo, 'r') as f:
                data = json.load(f)
                cls._clientes = [Cliente(**cliente) for cliente in data]
        except FileNotFoundError:
            cls._clientes = []

    @classmethod
    def salvar(cls, arquivo):
        with open(arquivo, 'w') as f:
            json.dump([cliente.__dict__ for cliente in cls._clientes], f)
