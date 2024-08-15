class Categoria:
    def __init__(self, id: int, descricao: str):
        self._id = id
        self._descricao = descricao

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

    def __str__(self):
        return f"Categoria[ID={self._id}, Descrição={self._descricao}]"
