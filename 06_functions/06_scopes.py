def serve_chai():
    chai_type = "Masala Chai" #Local Scope
    print(f"Inside Function : {chai_type}")

chai_type = "Lemon"
serve_chai()
print(f"Outside Function : {chai_type}")

def chai_counter():
    chai_order = "lemon" #enclosing scope
    def print_order():
        print(chai_order) #this will have access to above function objects

chai_order = "tulsi"
print(chai_order) # global scope