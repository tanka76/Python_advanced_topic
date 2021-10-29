def fun1(**kwargs):
   for key in kwargs:
       print('({0}:{1})'.format(key,kwargs[key]))


dict1={'1':"tanka",'2':"bhattarai"}
fun1(**dict1)