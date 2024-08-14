class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone

    def __str__(self):
        return f"Cliente[ID={self.id}, Nome={self.nome}, Email={self.email}, Fone={self.fone}]"
