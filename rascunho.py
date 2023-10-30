class Produto:
    def __init__(self, nome, preco, id_produto, estoque):
        self.nome = nome
        self.preco = preco
        self.id_produto = id_produto
        self.estoque = estoque

    def info_produto(self):
        print(f"{self.nome}, ID: {self.id_produto}, Preço: R${self.preco:.2f}, Estoque: {self.estoque} unidades")

class ProdutoEletronico(Produto):
    def __init__(self, nome, preco, estoque, id_produto, marca, modelo):
        super().__init__(nome, preco, estoque, id_produto)
        self.marca = marca
        self.modelo = modelo

    def exibir_informacoes(self):
        super().info_produto()
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Tipo: Eletrônico"

class ProdutoVestuario(Produto):
    def __init__(self, nome, preco, estoque, id_produto, tamanho, cor):
        super().__init__(nome, preco, estoque, id_produto)
        self.tamanho = tamanho
        self.cor = cor

    def exibir_informacoes(self):
        super().info_produto()
        return f"Tamanho: {self.tamanho}, Cor: {self.cor}, Tipo: Vestuário"

class ProdutoAlimento(Produto):
    def __init__(self, nome, preco, estoque, id_produto, validade):
        super().__init__(nome, preco, estoque, id_produto)
        self.validade = validade

    def exibir_informacoes(self):
        super().info_produto()
        return f"Data de Validade: {self.validade}, Tipo: Alimento"

# Exemplo de uso:
eletronico = ProdutoEletronico("Smartphone", 999.99, 10, 101,"Samsung", "Galaxy S20")
vestuario = ProdutoVestuario("Camiseta", 29.99, 50, 102,"M", "Branca")
alimento = ProdutoAlimento("Chocolate", 5.99, 100, 103,"2023-12-31")

print("Informações do Produto Eletrônico:")
print(eletronico.exibir_informacoes())

print("\nInformações do Produto de Vestuário:")
print(vestuario.exibir_informacoes())

print("\nInformações do Produto Alimentício:")
print(alimento.exibir_informacoes())


