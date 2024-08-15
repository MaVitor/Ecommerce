class Cliente:
    def __init__(self, id: int, nome: str, email: str, fone: str):
        self._id = id
        self._nome = nome
        self._email = email
        self._fone = fone

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value: str):
        self._nome = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value: str):
        self._email = value

    @property
    def fone(self):
        return self._fone

    @fone.setter
    def fone(self, value: str):
        self._fone = value

    def __str__(self):
        return f"Cliente[ID={self._id}, Nome={self._nome}, Email={self._email}, Fone={self._fone}]"
