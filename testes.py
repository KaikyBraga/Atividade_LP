from atividade import *

# Instâncias da classe FoodProduct
guarana_lata = FoodProduct("Guarana Lata", "3128939120381", 3.70, 6, "Refrigerante", "24-12-05")
coca_lata = FoodProduct("Coca-cola Lata", "31289392320381", 3.50, 1, "Refrigerante", "24-10-30")

# Instâncias da classe ClothingProduct
camiseta = ClothingProduct("Camiseta Oversized", "3128939310387", 50, 8, "Camiseta", "M", "Black")
air_max = ClothingProduct("Air Max","3128931320387", 500, 7, "Tênis", 42, "Fluorescente")

# Instâncias da classe EletronicProduct
iphone = EletronicProduct("Iphone XR", "3128935210387", 2000, 3, "Celular", 1)
televisao = EletronicProduct("Smart TV", "3128935213187", 2700, 5, "Televisão", 2)

# Métodos da classe produto
coca_lata.get_info_product()
iphone.update_name("Iphone 15")
iphone.update_price(10000)
camiseta.update_barcode("3120939320387")
iphone.update_category("Smartphone")
televisao.update_id_company(4)

# Adição de produtos cadastrados no Inventário
estoque = Invetory()
estoque.add_product(guarana_lata, 100)
estoque.add_product(coca_lata, 180)
estoque.add_product(coca_lata, 50)
estoque.add_product(guarana_lata, 10)
estoque.add_product(camiseta, 90)
estoque.add_product(air_max, 120)
estoque.add_product(iphone, 130)
estoque.add_product(televisao, 75)

# Remoção de produtos
estoque.rmv_product(coca_lata, 50)
estoque.rmv_product(coca_lata, 130)
estoque.rmv_product(coca_lata, 50)

# Amostragem do Inventário
estoque.show_invetory()
