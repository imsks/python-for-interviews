# # 1. *args and **kwargs
# def greet(name, *args, **kwargs):
#     print(f"Hello, {name}!")

#     if args:
#         print(f"Additional arguments: {args}")

#     if kwargs:
#         print(f"Additional keyword arguments:")
#         for key, value in kwargs.items():
#             print(f"  {key}: {value}")

# greet("John", "Jane", "Jim", "Jill", age=25, city="New York")
# ## Output:
# # Hello, John!
# # Additional arguments: ('Jane', 'Jim', 'Jill')
# # Additional keyword arguments:
# #   age: 25
# #   city: New York

# 2. Python decorators
def logging(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@logging
def add(a, b):
    return a + b

print(add(1, 2))
## Output:
# Calling add with args: (1, 2) and kwargs: {}
# Result: 3
# 3