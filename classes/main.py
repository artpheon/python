from Classes import *

childRouter = ChildOfRouter('newrouter', '1800', '11111', '12.6', '10')
print(childRouter.portsno)
print(childRouter.model)
childRouter.printRouter('hgf')
childRouter.printNewRouter('hgf')

#print(issubclass(ChildOfRouter, MyRouter))