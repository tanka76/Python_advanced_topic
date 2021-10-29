import pickle,stu
with open("student","rb") as f:
    while True:
        try:
            obj=pickle.load(f)

        except EOFError:

            print("done")
            break

obj.dis()