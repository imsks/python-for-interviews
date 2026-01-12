# # # 1. *args and **kwargs
# # def greet(name, *args, **kwargs):
# #     print(f"Hello, {name}!")

# #     if args:
# #         print(f"Additional arguments: {args}")

# #     if kwargs:
# #         print(f"Additional keyword arguments:")
# #         for key, value in kwargs.items():
# #             print(f"  {key}: {value}")

# # greet("John", "Jane", "Jim", "Jill", age=25, city="New York")
# # ## Output:
# # # Hello, John!
# # # Additional arguments: ('Jane', 'Jim', 'Jill')
# # # Additional keyword arguments:
# # #   age: 25
# # #   city: New York

# # 2. Python decorators
# def logging(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Result: {result}")
#         return result
#     return wrapper

# @logging
# def add(a, b):
#     return a + b

# print(add(1, 2))
# ## Output:
# # Calling add with args: (1, 2) and kwargs: {}
# # Result: 3
# # 3

# is vs == in Python
# Topic 3: is vs == in Python

print("=" * 50)
print("TOPIC 3: is vs == in Python")
print("=" * 50)

# ========== Value Comparison (==) ==========
print("\n1. Value Comparison (==):")
a = [1, 2, 3]
b = [1, 2, 3]
print(f"a = {a}")
print(f"b = {b}")
print(f"a == b: {a == b}")      # True - same values
print(f"a is b: {a is b}")      # False - different objects in memory

# ========== Identity Comparison (is) ==========
print("\n2. Identity Comparison (is):")
c = a
print(f"c = a")
print(f"a is c: {a is c}")      # True - same object
print(f"id(a): {id(a)}")
print(f"id(c): {id(c)}")
print(f"Same id? {id(a) == id(c)}")

# ========== Integer Caching ==========
print("\n3. Integer Caching (Python optimization):")
x = 256
y = 256
print(f"x = 256, y = 256")
print(f"x is y: {x is y}")      # True (Python caches -5 to 256)

x = 257
y = 257
print(f"\nx = 257, y = 257")
print(f"x is y: {x is y}")      # False (or True - implementation dependent)
print(f"x == y: {x == y}")      # Always True

# ========== Always use 'is' for None, True, False ==========
print("\n4. Use 'is' for None, True, False:")
value = None

# Correct way
if value is None:
    print("✓ Correct: value is None")

# Works but not Pythonic
if value == None:
    print("✗ Works but not recommended")

# ========== String Interning ==========
print("\n5. String Interning:")
str1 = "hello"
str2 = "hello"
print(f"str1 = 'hello', str2 = 'hello'")
print(f"str1 is str2: {str1 is str2}")  # Usually True (interning)

str3 = "hello world"
str4 = "hello world"
print(f"\nstr3 = 'hello world', str4 = 'hello world'")
print(f"str3 is str4: {str3 is str4}")  # May be False (not always interned)
print(f"str3 == str4: {str3 == str4}")  # Always True

# ========== Practical Examples ==========
print("\n6. Practical Examples:")

def check_none(value):
    """Always use 'is' for None checks"""
    return value is None

def check_equality(a, b):
    """Use '==' for value comparison"""
    return a == b

print(f"check_none(None): {check_none(None)}")
print(f"check_equality([1,2], [1,2]): {check_equality([1,2], [1,2])}")

# Common mistake
print("\n7. Common Mistake:")
my_list = [1, 2, 3]
if my_list == None:  # Wrong! Should use 'is None'
    print("This won't execute")
else:
    print("List is not None, but this check is inefficient")