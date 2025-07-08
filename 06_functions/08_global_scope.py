chai_type ="Plain"

def front_desk():
    def kitchen():
        global chai_type # allows to edit global variables
        chai_type = "Masala"
    kitchen()
front_desk()

print(chai_type)