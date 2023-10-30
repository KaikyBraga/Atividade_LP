from enum import Enum

class Company(Enum):
    COCACOLA = 1
    PEPSICO = 2
    APPLE = 3
    MICROSOFT = 4
    SAMSUNG = 5
    GUARANA = 6

class Product:
    def __init__(self, name_product: str, barcode: str, price: float, id_company: int, category: str):
        self.name_product = name_product
        self.barcode = barcode
        self.price = price
        self.id_company = id_company
        self.category = category

    def get_info_product(self):
        return {"Product Name": self.name_product, 
                "Barcode": self.barcode, 
                "Price": self.price, 
                "Company ID": Company(self.id_company).value,
                "Company Name": Company(self.id_company).name,
                "Category": self.category}
    
    def update_name(self, _name_product):
        self.name_product = _name_product

    def update_barcode(self, _barcode):
        self.barcode = _barcode

    def update_price(self, _price):
        self.price = _price

    def update_id_company(self, _id_company):
        self.id_company = _id_company

    def update_category(self, _category):
        self.category = _category
    
class ClothingProduct(Product):
    def __init__(self, name_product, barcode, price, id_company, category, size, style):
        super().__init__(name_product, barcode, price, id_company, category)
        self.size = size
        self.style = style

class EletronicProduct(Product):
    def __init__(self, name_product, barcode, price, id_company, category, warranty):
        super().__init__(name_product, barcode, price, id_company, category)
        self.warranty = warranty

class FoodProduct(Product):
    def __init__(self, name_product, barcode, price, id_company, category, expiration_date):
        super().__init__(name_product, barcode, price, id_company, category)
        self.expiration_date = expiration_date

class Invetory():
    def __init__(self):        
        self.products_list = [] # [[obj1, qnt1], [obj2, qnt2], [obj3, qnt]]

    def get_products_list(self):
        return self.products_list

    def add_product(self, product, qnt: int):
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
        for prod in self.products_list:
            print(prod[0].get_info_product(), prod[1])

    def rmv_product(self, product, qnt: int):
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

    
guarana_lata = FoodProduct("Guarana Lata", "3128939120381", 3.70, 6, "Refrigerante", "24-12-05")
coca_lata = FoodProduct("Coca-cola Lata", "31289392320381", 3.50, 1, "Refrigerante", "24-10-30")
iphone20 = FoodProduct("Iphone 20s", "31243250949085", 15000, 3, "Smartphone", 2)

estoque = Invetory()
estoque.add_product(guarana_lata, 100)
estoque.add_product(coca_lata, 180)
estoque.add_product(coca_lata, 50)
estoque.add_product(guarana_lata, 10)

estoque.rmv_product(coca_lata, 50)
estoque.rmv_product(coca_lata, 130)
#estoque.rmv_product(iphone20, 50)

estoque.rmv_product(coca_lata, 50)
estoque.show_invetory()