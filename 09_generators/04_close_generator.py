def local_chai ():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha Tea"
    yield "Oolang Tea"

def full_menu ():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

def chai_stall():
    try:
        while True :
            order = yield "Waiting for Chai Order"

    except:
        print("Stall Closed, No more chai")

stall = chai_stall()
print(next(stall))
stall.close() #closes generator and clean up 