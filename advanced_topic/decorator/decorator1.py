def fun1(fum):
    def inner():
        print("*"*5)
        fum()
        print("*"*5)
    return inner
#@fun1
def show():
    print("hello world")
    

a=fun1(show)
a()

#show   decorator ko sign use garako vaya yati lakhya pugcha