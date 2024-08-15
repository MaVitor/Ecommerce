class VendaItem:
    def __init__(self, id: int, qtd: int, preco: float, id_venda: int, id_produto: int):
        self._id = id
        self._qtd = qtd
        self._preco = preco
        self._id_venda = id_venda
        self._id_produto = id_produto

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def qtd(self):
        return self._qtd

    @qtd.setter
    def qtd(self, value: int):
        self._qtd = value

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, value: float):
        self._preco = value

    @property
    def id_venda(self):
        return self._id_venda

    @id_venda.setter
    def id_venda(self, value: int):
        self._id_venda = value

    @property
    def id_produto(self):
        return self._id_produto

    @id_produto.setter
    def id_produto(self, value: int):
        self._id_produto = value

    def __str__(self):
        return f"VendaItem[ID={self._id}, Qtd={self._qtd}, Preço={self._preco}, ID Venda={self._id_venda}, ID Produto={self._id_produto}]"
