#print fabbiano number

def gen(limit):
    a=0
    b=1
   
    while a<=limit:
        yield a
        a,b=b,a+b
        #yield b

x=gen(5)
for i in gen(5):
    print(i)