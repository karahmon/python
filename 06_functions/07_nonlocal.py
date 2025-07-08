def update_order():
    chai_type = "Elaichi"
    def kitchen ():
        nonlocal chai_type #non local means inside to inside function
        chai_type = "Masala"
    kitchen()
    print(f"After kitchen update : {chai_type}")

update_order()
