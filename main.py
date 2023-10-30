from enum import Enum

class Produto:

    total_produtos = 0

    def __init__(self, nome_produto, codigo_barras, preco, marca):
        self.nome_produto = nome_produto
        self.codigo_barras = codigo_barras
        self.preco = preco
        self.marca = marca
        Produto.total_produtos += 1
    
    def remover_produto(self):
        Produto.total_produtos = Produto.total_produtos - 1
        # Deletar o produto

    def info_produto(self):
        return {"Produto": self.nome_produto, "Código de Barras": self.codigo_barras, "Preço": self.preco, "Marca": self.marca}

class Produto_Limpeza(Produto):
    def __init__(self, nome_produto, codigo_barras, preco, marca, tipo_uso):
        super().__init__(nome_produto, codigo_barras, preco, marca)
        self.tipo_uso = tipo_uso

class Produto_Alimento(Produto):
    def __init__(self, nome_produto, codigo_barras, preco, quant_peso):
        super().__init__(nome_produto, codigo_barras, preco)
        self.quant_peso = quant_peso

class Produto_Bebida(Produto):

    def __init__(self, nome_produto, codigo_barras, preco, marca, alcoolico):
        super().__init__(nome_produto, codigo_barras, preco, marca)
        self.alcoolico = alcoolico

class Invetario():
    produtos_em_estoque = set()

