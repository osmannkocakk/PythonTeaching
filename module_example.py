import calculator_module

calc = calculator_module.Calculator()    # create new instance of Calculator class defined in calculator module
calc.add(2)
print(calc.get_current())

import mymodule

mymodule.greeting("Osman Koçak")

#Import only the person1 dictionary from the module:
#from mymodule import person
#print (person["age"])
