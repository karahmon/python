device_status = input ("Enter if device is active or off : ").lower()
if device_status == "off":
    print(f"Device is offline")
else :
    temperature = int (input ("Enter Room Temperature : "))
    if temperature > 35 :
        print(f"High Temperature")
    else :
        print(f"Temperature is Normal")
