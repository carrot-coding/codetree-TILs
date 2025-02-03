product_name1, product_code1 = input().split()
product_code1 = int(product_code1)

# Write your code here!
class Product:
    def __init__(self, name='codetree', code=50):
        self.name = name
        self.code = code
prd2 = Product()
prd1 = Product(product_name1, product_code1)

print(f"product {prd2.code} is {prd2.name}")
print(f"product {prd1.code} is {prd1.name}")
