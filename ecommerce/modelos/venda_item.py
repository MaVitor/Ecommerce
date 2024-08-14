class VendaItem:
    def __init__(self, id, qtd, preco, id_venda, id_produto):
        self.id = id
        self.qtd = qtd
        self.preco = preco
        self.id_venda = id_venda
        self.id_produto = id_produto

    def __str__(self):
        return f"VendaItem[ID={self.id}, Qtd={self.qtd}, Preço={self.preco}, IDVenda={self.id_venda}, IDProduto={self.id_produto}]"
