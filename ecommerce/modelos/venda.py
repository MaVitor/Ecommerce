from datetime import datetime

class Venda:
    def __init__(self, id, data, carrinho, total, id_cliente):
        self.id = id
        self.data = data
        self.carrinho = carrinho
        self.total = total
        self.id_cliente = id_cliente

    def __str__(self):
        return f"Venda[ID={self.id}, Data={self.data}, Carrinho={self.carrinho}, Total={self.total}, IDCliente={self.id_cliente}]"
