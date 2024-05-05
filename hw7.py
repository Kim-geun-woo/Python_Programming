shopping_bag = {}

print('[구입]')
while True:
    item = input('상품명? ')
    if item == '':
        break
    count = int(input('수량은? '))
    shopping_bag[item] = count
    print(f'장바구니에 {item} {count}개가 담겼습니다.\n')

print(f'\n>>> 장바구니 보기:{shopping_bag}')

print(f'\n[검색]')
th = input('장바구니에서 확인하고자 하는 상품은? ')

if th in shopping_bag :
    print(f'{th}는 {shopping_bag[th]}개 담겨있습니다.')
else:
    print(f'장바구니에 {th}는 없습니다.')
