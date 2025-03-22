def get_integer(prompt) :
    res = int(input(prompt))
    return res

def exchange(ep) :
    n500 = ep // 500
    ep %= 500

    n100 = ep // 100
    ep %= 100

    n50 = ep // 50
    ep %= 50

    n10 = ep // 10
    ep %= 10

    print('500원 동전의 개수:', n500)
    print('100원 동전의 개수:', n100)
    print('50원 동전의 개수:', n50)
    print('10원 동전의 개수:', n10)

n1 = int(get_integer('동전으로 교환하고자 하는 금액은? :'))
exchange(n1)
