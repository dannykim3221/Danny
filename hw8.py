def buy(dic) :
    item = input('상품명? ')
    if item == '' :
        return False
    num = input('수량은? ')
    dic[item] = num
    print(f'장바구니에 {item}이(가) 담겼습니다.\n')

def show(dic) :
    print(f'>>> 장바구니 보기: {shopping_bag}\n')

def find(dic) :
    print('[검색]')
    product = input('장바구니에서 확인하고자 하는 상품은? ')
    
    if product in dic :
        print(f'{product}은(는) {shopping_bag[product]}개 담겨 있습니다.')
    else :
        print(f'장바구니에 {product}은(는) 없습니다.')

shopping_bag = {}
print('[구입]')
while True :
    if buy(shopping_bag) == False :
        break
show(shopping_bag)
find(shopping_bag)
