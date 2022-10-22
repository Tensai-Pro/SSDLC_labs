import os
import json
import product as p


file = 'allFiles/myJsonFile.json'

def encode_product(product):
    if isinstance(product, p.Product):
        return (product.name, product.amount, product.price)
    else:
        type_name = product.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")

def decode_product(product):
    if "__product__" in product:
            return p.Product(product["Name"], product["Amount"], product["Price"])
    else:
        return product


product1 = p.Product("Milk", 100, 58)
product2 = p.Product("Juice", 77, 82)
product3 = p.Product("Eggs", 261, 110)
product4 = p.Product("Fish", 73, 118)
product5 = p.Product("Bread", 112, 25)
stock = [ product1, product2, product3, product4, product5 ]

with open(file, "w") as file_handler:
    json_file = []
    i = 0
    for product in stock:
        json_element = {}
        json_element["__product__"] = True
        json_element["Name"] = product.name
        json_element["Amount"] = product.amount
        json_element["Price"] = product.price

        json_file.append(json_element)

    json.dump(json_file, file_handler, default=encode_product, indent=4)


with open(file, "r") as file_handler:
    data = file_handler.read()
    stock_from_json = json.loads(data, object_hook=decode_product)
    
    for product in stock_from_json:
        print(product.name, product.amount, product.price, sep=', ', end='\n')


answer = input("Do you want to delete the file? [y/n]: ")
if answer == 'y':
    if os.path.isfile(file):
        os.remove(file)
    else:
        print(f"Error: {file} file not found" )