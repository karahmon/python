from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before Function Runs")
        func()
        print("After Function Runs")
    return wrapper

@my_decorator
def greet():
    print("Hello from Decorators")

greet()
print(greet.__name__)