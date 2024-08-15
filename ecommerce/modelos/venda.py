from datetime import datetime

class Venda:
    def __init__(self, id: int, data: datetime, carrinho: bool, total: float, id_cliente: int):
        self._id = id
        self._data = data
        self._carrinho = carrinho
        self._total = total
        self._id_cliente = id_cliente

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value: datetime):
        self._data = value

    @property
    def carrinho(self):
        return self._carrinho

    @carrinho.setter
    def carrinho(self, value: bool):
        self._carrinho = value

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value: float):
        self._total = value

    @property
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, value: int):
        self._id_cliente = value

    def __str__(self):
        return f"Venda[ID={self._id}, Data={self._data}, Carrinho={self._carrinho}, Total={self._total}, ID Cliente={self._id_cliente}]"
