class MyRouter(object):
    "This is a class that describes a router"
    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios
    def printRouter(self, manufDate):
        print("Router characteristics:", self.routername, self.model, self.serialno, self.ios)
        print("The model and date: ", self.model + "/" + manufDate)

#always type object when the class does not inherit
# defining init is like a default constructor
# the code that is executed when instanciating an obj
# seld is always the first parameter

router1 = MyRouter('R1', '2600', '123456', '14.0')
print(router1)
router1.printRouter('29.04.1997')
print(router1.serialno)

print(getattr(router1, 'model'))
setattr(router1, 'ios', '14.3')
print(getattr(router1, 'ios'))
print(hasattr(router1, 'kik'))
print(hasattr(router1, 'serialno'))
delattr(router1, 'model')
print(hasattr(router1, 'model'))

print(isinstance(router1, MyRouter))