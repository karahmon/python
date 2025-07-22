class ChaiOrder :
    def __init__(self,tea_type,sweetness,size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size
    
    @classmethod
    def from_dict(cls,order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"]
        )
    @classmethod
    def from_string (cls,order_string):
        tea_type,sweetness,size = order_string.split("-")
        return cls(tea_type,sweetness,size)

class ChaiUtils:
    @staticmethod
    def is_valid_Size(size):
        return size in ["Small","Medium","Large"]
    
print(ChaiUtils.is_valid_Size("Medium"))

order1 = ChaiOrder.from_dict({"tea_type":"Masala","sweetness":"Medium","size":"Small"})
print(order1.__dict__)
order2 = ChaiOrder.from_string("Ginger-Low-Small")
print(order2.__dict__)