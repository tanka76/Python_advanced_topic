from time import time,ctime,localtime
epoch=time()
print(epoch)
print(ctime(epoch))
print(ctime())

obj=localtime()
print(obj.tm_year)