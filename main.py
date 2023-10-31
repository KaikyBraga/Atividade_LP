from enum import Enum

class Company(Enum):
    """
    Representa empresas disponíveis no sistema.

    Esta enumeração permite associar um nome a uma empresa por meio de um valor numérico.
    """
    COCACOLA = 1
    PEPSICO = 2
    APPLE = 3
    MICROSOFT = 4
    SAMSUNG = 5
    GUARANA = 6
    NIKE = 7
    ADIDAS = 8

class Product:
    """
    Representa um produto genérico.

    Esta classe contém atributos comuns a todos os produtos e métodos.
    """
    def __init__(self, name_product: str, barcode: str, price: float, id_company: int, category: str):
        """
        Inicializa um novo produto.

        Args:
            name_product (str): Nome do produto.
            barcode (str): Código de barras do produto.
            price (float): Preço do produto.
            id_company (int): ID da empresa que fabrica o produto.
            category (str): Categoria do produto.
        """
        self.name_product = name_product
        self.barcode = barcode
        self.price = price
        self.id_company = id_company
        self.category = category

    def get_info_product(self):
        """
        Retorna informações detalhadas sobre o produto.

        Returns:
            dict: Um dicionário com informações do produto, incluindo nome, código de barras, preço, empresa e categoria.
        """
        return {"Product Name": self.name_product, 
                "Barcode": self.barcode, 
                "Price": self.price, 
                "Company ID": Company(self.id_company).value,
                "Company Name": Company(self.id_company).name,
                "Category": self.category}
    
    def update_name(self, _name_product):
        """
        Atualiza o nome do produto.

        Args:
            _name_product (str): Novo nome do produto.
        """
        self.name_product = _name_product

    def update_barcode(self, _barcode):
        """
        Atualiza o código de barras do produto.

        Args:
            _barcode (str): Novo código de barras.
        """
        self.barcode = _barcode

    def update_price(self, _price):
        """
        Atualiza o preço do produto.

        Args:
            _price (float): Novo preço do produto.
        """
        self.price = _price

    def update_id_company(self, _id_company):
        """
        Atualiza o ID da empresa que fabrica o produto.

        Args:
            _id_company (int): Novo ID da empresa.
        """
        self.id_company = _id_company

    def update_category(self, _category):
        """
        Atualiza a categoria do produto.

        Args:
            _category (str): Nova categoria do produto.
        """
        self.category = _category
    
class ClothingProduct(Product):
    """
    Representa um produto de roupas.

    Esta classe herda os atributos e métodos da classe 'Product' e adiciona atributos específicos para roupas.
    """
    def __init__(self, name_product, barcode, price, id_company, category, size, style):
        """
        Inicializa um novo produto de roupas.

        Args:
            name_product (str): Nome do produto.
            barcode (str): Código de barras do produto.
            price (float): Preço do produto.
            id_company (int): ID da empresa que fabrica o produto.
            category (str): Categoria do produto.
            size (str): Tamanho das roupas.
            style (str): Estilo das roupas.
        """
        super().__init__(name_product, barcode, price, id_company, category)
        self.size = size
        self.style = style

class EletronicProduct(Product):
    """
    Representa um produto eletrônico.

    Esta classe herda os atributos e métodos da classe 'Product' e adiciona atributos específicos para produtos eletrônicos.
    """
    def __init__(self, name_product, barcode, price, id_company, category, warranty):
        """
        Inicializa um novo produto eletrônico.

        Args:
            name_product (str): Nome do produto.
            barcode (str): Código de barras do produto.
            price (float): Preço do produto.
            id_company (int): ID da empresa que fabrica o produto.
            category (str): Categoria do produto.
            warranty (str): Informações sobre a garantia do produto eletrônico.
        """
        super().__init__(name_product, barcode, price, id_company, category)
        self.warranty = warranty

class FoodProduct(Product):
    """
    Representa um produto alimentício.

    Esta classe herda os atributos e métodos da classe 'Product' e adiciona atributos específicos para produtos alimentícios.
    """
    def __init__(self, name_product, barcode, price, id_company, category, expiration_date):
        """
        Inicializa um novo produto alimentício.

        Args:
            name_product (str): Nome do produto.
            barcode (str): Código de barras do produto.
            price (float): Preço do produto.
            id_company (int): ID da empresa que fabrica o produto.
            category (str): Categoria do produto.
            expiration_date (str): Data de validade do produto alimentício.
        """
        super().__init__(name_product, barcode, price, id_company, category)
        self.expiration_date = expiration_date

class Invetory():
    """
    Representa um inventário de produtos.

    Esta classe permite adicionar, remover e listar produtos no inventário.
    """
    def __init__(self):        
        """Inicializa o inventário vazio."""
        self.products_list = [] 

    def get_products_list(self):
        """
        Retorna a lista de produtos no inventário.

        Returns:
            list: Uma lista de produtos no inventário.
        """
        return self.products_list

    def add_product(self, product, qnt: int):
        """
        Adiciona uma quantidade específica de um produto ao inventário.

        Esta função permite adicionar uma quantidade específica de um produto ao inventário. Ela verifica se o tipo de produto
        é válido (FoodProduct, ClothingProduct ou EletronicProduct) e, em seguida, procura o produto na lista do inventário.
        Se o produto já estiver no inventário, a quantidade disponível é incrementada. Caso contrário, um novo item é adicionado.

        Args:
            product (Product): O produto a ser adicionado.
            qnt (int): A quantidade a ser adicionada.
        """
        if(type(product)!=FoodProduct and type(product)!=ClothingProduct and type(product)!=EletronicProduct):
            raise TypeError("Objeto invalido")

        flag = 1

        for i in range(len(self.products_list)):
            if self.products_list[i][0]==product:
                self.products_list[i][1] += qnt
                flag = 0
                break
        
        if flag:
            self.products_list.append([product, qnt])

    def show_invetory(self):
        """
        Exibe a lista de produtos no inventário com suas informações.

        Esta função imprime as informações de todos os produtos no inventário, incluindo nome, código de barras, preço,
        quantidade em estoque, empresa e categoria. Cada produto é listado com a quantidade disponível.
        """
        for prod in self.products_list:
            print(prod[0].get_info_product(), prod[1])

    def rmv_product(self, product, qnt: int):
        """
        Remove uma quantidade específica de um produto do inventário.

        Esta função permite remover uma quantidade específica de um produto do inventário. O tipo de produto é verificado
        e a quantidade disponível é atualizada. Se a quantidade especificada for maior do que a disponível, uma exceção
        é gerada.

        Args:
            product (Product): O produto a ser removido.
            qnt (int): A quantidade a ser removida.
        """
        if(type(product)!=FoodProduct and type(product)!=ClothingProduct and type(product)!=EletronicProduct):
            raise TypeError("Objeto invalido")

        flag = 1

        for i in range(len(self.products_list)):
            if self.products_list[i][0]==product:

                if(self.products_list[i][1]<qnt):
                    raise Exception("quantidade invalida")

                self.products_list[i][1] -= qnt
                flag = 0

                if self.products_list[i][1]==0:
                    self.products_list.remove(self.products_list[i])
                break
        
        if flag:
            raise Exception("Objeto nao encontrado")
        
