chai = "Gineger Chai"

def prepare_chai(order):
    print(f"Preparing : {order}")

prepare_chai(chai)

list_of_orders = [1,2,3]

def edit_order(cup):
    cup[1] = 10  #lists value will change as it is mutable

edit_order(list_of_orders)
print(list_of_orders)

def make_chai(tea,milk,sugar):
    print(tea,milk,sugar)

make_chai("Assam","Yes","Low") #positional as we need what value will be assigned to parameters
make_chai(tea="Green",sugar="Medium",milk="Yes") #keywords ensures if there is change in position same value goes

def special_chai(*ingredients , **extras): #if you are not providing names you use single astrik *, if you provide names then double astricks **
    print(ingredients)
    print(extras)

special_chai("Cinnamon","Elaichi",sweetner ="Honey",foam ="yes")

def chai_orders(order = None):
   if order is None :
    order = []
    print(order)

chai_orders()
chai_orders()