class stu:
    def __init__(self,age):
        if age>=1 and age<=100:
            self.age=age

        else:
            raise Exception("invalid age")

    def get_age(self):
        return self.age

try:
    a=stu(int(input("enter age")))
    print("age",a.get_age)
except Exception as e:
    print(e)
