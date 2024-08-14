from persistencia.persistencia_cliente import PersistenciaCliente
from persistencia.persistencia_categoria import PersistenciaCategoria
from persistencia.persistencia_produto import PersistenciaProduto
from modelos.cliente import Cliente
from modelos.categoria import Categoria
from modelos.produto import Produto

class UI:
    @staticmethod
    def main():
        while True:
            UI.menu()
            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                UI.listar_clientes()
            elif opcao == '2':
                UI.inserir_cliente()
            elif opcao == '3':
                UI.atualizar_cliente()
            elif opcao == '4':
                UI.excluir_cliente()
            elif opcao == '5':
                UI.listar_categorias()
            elif opcao == '6':
                UI.inserir_categoria()
            elif opcao == '7':
                UI.atualizar_categoria()
            elif opcao == '8':
                UI.excluir_categoria()
            elif opcao == '9':
                UI.listar_produtos()
            elif opcao == '10':
                UI.inserir_produto()
            elif opcao == '11':
                UI.atualizar_produto()
            elif opcao == '12':
                UI.excluir_produto()
            elif opcao == '0':
                print("Encerrando o sistema...")
                break
            else:
                print("Opção inválida! Tente novamente.")

    @staticmethod
    def menu():
        print("\n--- Menu ---")
        print("1. Listar Clientes")
        print("2. Inserir Cliente")
        print("3. Atualizar Cliente")
        print("4. Excluir Cliente")
        print("5. Listar Categorias")
        print("6. Inserir Categoria")
        print("7. Atualizar Categoria")
        print("8. Excluir Categoria")
        print("9. Listar Produtos")
        print("10. Inserir Produto")
        print("11. Atualizar Produto")
        print("12. Excluir Produto")
        print("0. Finalizar")

    @staticmethod
    def listar_clientes():
        clientes = PersistenciaCliente.listar()
        for cliente in clientes:
            print(cliente)

    @staticmethod
    def inserir_cliente():
        id = int(input("ID: "))
        nome = input("Nome: ")
        email = input("Email: ")
        fone = input("Fone: ")
        cliente = Cliente(id, nome, email, fone)
        PersistenciaCliente.inserir(cliente)
        print("Cliente inserido com sucesso!")

    @staticmethod
    def atualizar_cliente():
        id = int(input("ID do cliente a ser atualizado: "))
        cliente = PersistenciaCliente.listar_id(id)
        if cliente:
            nome = input("Novo Nome: ")
            email = input("Novo Email: ")
            fone = input("Novo Fone: ")
            cliente.nome = nome
            cliente.email = email
            cliente.fone = fone
            PersistenciaCliente.atualizar(cliente)
            print("Cliente atualizado com sucesso!")
        else:
            print("Cliente não encontrado!")

    @staticmethod
    def excluir_cliente():
        id = int(input("ID do cliente a ser excluído: "))
        if PersistenciaCliente.excluir(id):
            print("Cliente excluído com sucesso!")
        else:
            print("Cliente não encontrado!")

    @staticmethod
    def listar_categorias():
        categorias = PersistenciaCategoria.listar()
        for categoria in categorias:
            print(categoria)

    @staticmethod
    def inserir_categoria():
        id = int(input("ID: "))
        descricao = input("Descrição: ")
        categoria = Categoria(id, descricao)
        PersistenciaCategoria.inserir(categoria)
        print("Categoria inserida com sucesso!")

    @staticmethod
    def atualizar_categoria():
        id = int(input("ID da categoria a ser atualizada: "))
        categoria = PersistenciaCategoria.listar_id(id)
        if categoria:
            descricao = input("Nova Descrição: ")
            categoria.descricao = descricao
            PersistenciaCategoria.atualizar(categoria)
            print("Categoria atualizada com sucesso!")
        else:
            print("Categoria não encontrada!")

    @staticmethod
    def excluir_categoria():
        id = int(input("ID da categoria a ser excluída: "))
        if PersistenciaCategoria.excluir(id):
            print("Categoria excluída com sucesso!")
        else:
            print("Categoria não encontrada!")

    @staticmethod
    def listar_produtos():
        produtos = PersistenciaProduto.listar()
        for produto in produtos:
            print(produto)

    @staticmethod
    def inserir_produto():
        id = int(input("ID: "))
        descricao = input("Descrição: ")
        preco = float(input("Preço: "))
        estoque = int(input("Estoque: "))
        id_categoria = int(input("ID da Categoria: "))
        produto = Produto(id, descricao, preco, estoque, id_categoria)
        PersistenciaProduto.inserir(produto)
        print("Produto inserido com sucesso!")

    @staticmethod
    def atualizar_produto():
        id = int(input("ID do produto a ser atualizado: "))
        produto = PersistenciaProduto.listar_id(id)
        if produto:
            descricao = input("Nova Descrição: ")
            preco = float(input("Novo Preço: "))
            estoque = int(input("Novo Estoque: "))
            id_categoria = int(input("Novo ID da Categoria: "))
            produto.descricao = descricao
            produto.preco = preco
            produto.estoque = estoque
            produto.id_categoria = id_categoria
            PersistenciaProduto.atualizar(produto)
            print("Produto atualizado com sucesso!")
        else:
            print("Produto não encontrado!")

    @staticmethod
    def excluir_produto():
        id = int(input("ID do produto a ser excluído: "))
        if PersistenciaProduto.excluir(id):
            print("Produto excluído com sucesso!")
        else:
            print("Produto não encontrado!")
