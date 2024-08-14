class Produto:
    def __init__(self, id, descricao, preco, estoque, id_categoria):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.id_categoria = id_categoria

    def __str__(self):
        return f"Produto[ID={self.id}, Descrição={self.descricao}, Preço={self.preco}, Estoque={self.estoque}, IDCategoria={self.id_categoria}]"
