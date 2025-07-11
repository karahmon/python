#pure functions - never enters any variable globally

def pure_chai(cups):
    return cups * 10

# impure function - uses global variables (not recommended)
total_chai = 0

def impure_chai(cups):
    global total_chai
    total_chai += cups
    return total_chai

impure_chai(2)
print(total_chai)

#recursive function
def pour_Chai(n):
    if n == 0:
        return "All cups poured"
    return pour_Chai(n-1)
print(pour_Chai(3))

#lambdas- anonymous function to give logic without function name
chai_types = ["light","kadak","ginger","kadak"]

strong_chai = list(filter(lambda chai : chai=="kadak",chai_types))
print(strong_chai)