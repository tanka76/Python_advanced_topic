def outer(msg):


    def inner():
        print(msg)


    return inner

a=outer("hello world")
del outer #even we delete this function 
a()