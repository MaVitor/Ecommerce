class Produto:
    def __init__(self, id: int, descricao: str, preco: float, estoque: int, id_categoria: int):
        self._id = id
        self._descricao = descricao
        self._preco = preco
        self._estoque = estoque
        self._id_categoria = id_categoria

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value: str):
        self._descricao = value

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, value: float):
        self._preco = value

    @property
    def estoque(self):
        return self._estoque

    @estoque.setter
    def estoque(self, value: int):
        self._estoque = value

    @property
    def id_categoria(self):
        return self._id_categoria

    @id_categoria.setter
    def id_categoria(self, value: int):
        self._id_categoria = value

    def __str__(self):
        return f"Produto[ID={self._id}, Descrição={self._descricao}, Preço={self._preco}, Estoque={self._estoque}, ID Categoria={self._id_categoria}]"
