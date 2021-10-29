class Myexception(Exception):
    pass


def balance():
    total_balance=10000
    withdrawl=5000
    balance=total_balance-withdrawl

    try:
        if(balance<2000):
            raise Myexception('balance not suffient')
    except Myexception as ep:
        print(ep)


balance()