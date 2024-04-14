def read_single_digit(num):
    single = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    if 0 <= num <= 9:
        return single[num]

def read_number(num):
    if num < 10 :
        return read_single_digit(num)
    elif num < 100 :
        n10 = num // 10
        n1 = num % 10
        return read_single_digit(n10) + read_single_digit(n1)
    else :
        n100 = num // 100
        n10 = (num // 10) % 10
        n1 = num % 10
        return read_single_digit(n100) + read_single_digit(n10) + read_single_digit(n1)

digit = int(input('세 자리 정수 입력: '))
res = read_number(digit)
print(res)
