def buy(dic):
    while True:
        print('[구입]')
        item = input('상품명? ')
        if item == '':
            return False
        count = int(input('수량은? '))
        dic[item] = count
        print(f'장바구니에 {item} {count}개가 담겼습니다.\n')

def show(dic):
        print(f'\n>>> 장바구니 보기: {dic}')

def find(dic):
    print('\n[검색]')
    n = input('장바구니에서 확인하고자 하는 상품은? ')

    if n in dic:
        print(f'{n}(는) {dic[n]}개 담겨 있습니다.')
    else:
        print(f'장바구니에 {n}은(는) 없습니다.')

shopping_bag = {}

while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
