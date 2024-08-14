from persistencia.persistencia_cliente import PersistenciaCliente
from persistencia.persistencia_categoria import PersistenciaCategoria
from persistencia.persistencia_produto import PersistenciaProduto
from ui import UI

if __name__ == "__main__":
    # Carregar dados previamente salvos
    PersistenciaCliente.abrir('clientes.json')
    PersistenciaCategoria.abrir('categorias.json')
    PersistenciaProduto.abrir('produtos.json')

    # Iniciar a interface de usuário
    UI.main()

    # Salvar os dados ao finalizar
    PersistenciaCliente.salvar('clientes.json')
    PersistenciaCategoria.salvar('categorias.json')
    PersistenciaProduto.salvar('produtos.json')
