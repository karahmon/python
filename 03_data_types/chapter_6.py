chai_type = "Ginger Chai"
customer_name = "Monil Karania"

print(f"Order for {chai_type} by {customer_name} is ready for pickup")

chai_description = "Hot and Classy"
print(f"First Word of Description : {chai_description[0:4:2]}") #0 to 4, skip 2 place
print(f"First Word of Description : {chai_description[::-1]}") # to reverse a string

label_text = "Chai Spéciale"
encoded_label = label_text.encode("utf-8")
print(f"Nonencoded Label : {label_text}")
print(f"Encoded Label : {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded Label : {decoded_label}")