from refurbished import Store

store = Store('it')

products = store.get_macs()

print(len(products))

[print(product) for product in products if product.savings_price > 350]
