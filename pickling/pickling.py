import pickle,stu
n=int(input("enter the number of student"))


with open('student','wb') as f:

    for i in range(n):
        name=input("enter your name")
        roll=int(input("enter your name"))
        address=input("enter your name")
        stu1=stu.Student(name,roll,address)
        pickle.dump(stu1,f)
    
print("pickling done")