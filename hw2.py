def exchange(coin):
    n500 = coin // 500
    amount = coin % 500
    n100 = amount // 100
    amount = amount % 100
    n50 = amount // 50
    amount = amount % 50
    n10 = amount // 10
    print("500원 동전의 개수: ", n500);
    print("100원 동전의 개수: ", n100);
    print("50원 동전의 개수: ", n50);
    print("10원 동전의 개수: ", n10);

def get_interger(prompt):
    res = int(input(prompt));
    return res

coin = get_interger("동전으로 교환하고자 하는 금액은? ");
exchange(coin);
