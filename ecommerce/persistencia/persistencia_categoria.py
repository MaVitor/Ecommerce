import json
from modelos.categoria import Categoria

class PersistenciaCategoria:
    _categorias = []

    @classmethod
    def inserir(cls, categoria):
        cls._categorias.append(categoria)

    @classmethod
    def listar(cls):
        return cls._categorias

    @classmethod
    def listar_id(cls, id):
        for categoria in cls._categorias:
            if categoria.id == id:
                return categoria
        return None

    @classmethod
    def atualizar(cls, categoria_atualizada):
        for idx, categoria in enumerate(cls._categorias):
            if categoria.id == categoria_atualizada.id:
                cls._categorias[idx] = categoria_atualizada
                return True
        return False

    @classmethod
    def excluir(cls, id):
        for idx, categoria in enumerate(cls._categorias):
            if categoria.id == id:
                del cls._categorias[idx]
                return True
        return False

    @classmethod
    def abrir(cls, arquivo):
        try:
            with open(arquivo, 'r') as f:
                data = json.load(f)
                cls._categorias = [Categoria(**categoria) for categoria in data]
        except FileNotFoundError:
            cls._categorias = []

    @classmethod
    def salvar(cls, arquivo):
        with open(arquivo, 'w') as f:
            json.dump([categoria.__dict__ for categoria in cls._categorias], f)
