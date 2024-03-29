def get_fixed_price(won):
    global discount
    return won / (1 - discount/100)


discount = int(input("할인율은? "))
discount_priceA = int(input("A 상품의 할인된 가격은? "))
discount_priceB = int(input("B 상품의 할인된 가격은? "))

con1 = get_fixed_price(discount_priceA)
con2 = get_fixed_price(discount_priceB)

print("A 상품의 정가는", con1,"원")
print("B 상품의 정가는", con2,"원")
