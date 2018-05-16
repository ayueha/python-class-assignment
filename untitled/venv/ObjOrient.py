class MyClass:
    '''Class Discription is here'''
#    def f(self):
#        print('Hello world')

#obj = MyClass()
#print(type(obj))
#obj.f()

    def __init__(self,name,age):
        self.age =age
        self.name=name
    #obj.__doc__ -> class description
    #obj.__main__ ->

    def getname(self):
        return "{} is my name".format(self.name)

    def getage(self):
        return {0}


class Parrot(MyClass):
    def __init__(self):
        super().__init__()
        self.age = age
        self.name = name
        print("Parrot is ready")



p = Parrot()
isinstance(p,Parrot)