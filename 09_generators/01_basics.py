def serve_chai():
    yield "Cup 1 : Masala Chai"
    yield "Cup 2 : Elaichi Chai"
    yield "Cup 3 : Ginger Chai"

stall = serve_chai()

for cup in stall:
    print(cup)

def get_chai_list():
    return ["Cup 1", "Cup 2","Cup 3"]

#generator function
def get_chai_get():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

print(get_chai_list())
print(get_chai_get())
print(next(get_chai_get())) # will print next value if constantly printed
