class age(Exception):
    def __init__(self,message):
        Exception.__init__(self,message)

class student:
    def __init__(self,age):
        if(age>=0 and age<=100):
            self.age=age

        else:
            raise age("in-valid age")

    def get_age(self):
        return self.age

try:
    s=student(int(input("enter your age")))
    print("your age",s.get_age())
except Exception as e:
    print(e)
