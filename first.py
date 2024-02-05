p1_code = int(input())
p1_unit_product = int(input())
p1_unit_price = float(input())

p2_code = int(input())
p2_unit_product = int(input())
p2_unit_price = float(input())

print("VALOR A PAGAR: R$ {:.2f}".format(p1_unit_price*p1_unit_product + p2_unit_price*p2_unit_product))