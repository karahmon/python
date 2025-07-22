class Chai_Utils:
    @staticmethod
    def clean_ingredients(text):
       return [item.strip()for item in text.split(",")]

raw = "water , milk , tea , coffee"

cleaned = Chai_Utils.clean_ingredients(raw)
print(cleaned)

