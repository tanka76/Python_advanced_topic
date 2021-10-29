#concate two dictionary

dict1={'a':1,'b':2}
dict2={'c':3,'d':4}
dict3=dict2.copy()
dict3.update(dict1)
print(dict3)