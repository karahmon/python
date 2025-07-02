is_boiling = False #Also Represented as 0
is_cold = True #Also Represented as 1
check_actions = 4
total_actions = is_cold + check_actions
print(f"Total Actions : {total_actions}") #uses upcasting to change datatype from bool to int therefore ans is 4 + 1 = 5

check_conditon = is_boiling & is_cold
print(f"Can Serve Chai : {check_conditon}")
