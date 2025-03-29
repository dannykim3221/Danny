def get_fixed_price(discount_rate, discount_price):
    dr = 100 - discount_rate
    price = discount_price * 100 / dr
    return price

dr = int(input('할인율은? '))
dp1 = int(input('A 상품의 할인된 가격은? '))
dp2 = int(input('B 상품의 할인된 가격은? '))
p1 = get_fixed_price(dr, dp1)
p2 = get_fixed_price(dr, dp2)
print('A 상품의 정가는', int(p1), '원')
print('B 상품의 정가는', int(p2), '원')









    
