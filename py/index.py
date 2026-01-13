# # # # # 1. *args and **kwargs
# # # # def greet(name, *args, **kwargs):
# # # #     print(f"Hello, {name}!")

# # # #     if args:
# # # #         print(f"Additional arguments: {args}")

# # # #     if kwargs:
# # # #         print(f"Additional keyword arguments:")
# # # #         for key, value in kwargs.items():
# # # #             print(f"  {key}: {value}")

# # # # greet("John", "Jane", "Jim", "Jill", age=25, city="New York")
# # # # ## Output:
# # # # # Hello, John!
# # # # # Additional arguments: ('Jane', 'Jim', 'Jill')
# # # # # Additional keyword arguments:
# # # # #   age: 25
# # # # #   city: New York

# # # # 2. Python decorators
# # # def logging(func):
# # #     def wrapper(*args, **kwargs):
# # #         print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
# # #         result = func(*args, **kwargs)
# # #         print(f"Result: {result}")
# # #         return result
# # #     return wrapper

# # # @logging
# # # def add(a, b):
# # #     return a + b

# # # print(add(1, 2))
# # # ## Output:
# # # # Calling add with args: (1, 2) and kwargs: {}
# # # # Result: 3
# # # # 3

# # # is vs == in Python
# # # Topic 3: is vs == in Python

# # print("=" * 50)
# # print("TOPIC 3: is vs == in Python")
# # print("=" * 50)

# # # ========== Value Comparison (==) ==========
# # print("\n1. Value Comparison (==):")
# # a = [1, 2, 3]
# # b = [1, 2, 3]
# # print(f"a = {a}")
# # print(f"b = {b}")
# # print(f"a == b: {a == b}")      # True - same values
# # print(f"a is b: {a is b}")      # False - different objects in memory

# # # ========== Identity Comparison (is) ==========
# # print("\n2. Identity Comparison (is):")
# # c = a
# # print(f"c = a")
# # print(f"a is c: {a is c}")      # True - same object
# # print(f"id(a): {id(a)}")
# # print(f"id(c): {id(c)}")
# # print(f"Same id? {id(a) == id(c)}")

# # # ========== Integer Caching ==========
# # print("\n3. Integer Caching (Python optimization):")
# # x = 256
# # y = 256
# # print(f"x = 256, y = 256")
# # print(f"x is y: {x is y}")      # True (Python caches -5 to 256)

# # x = 257
# # y = 257
# # print(f"\nx = 257, y = 257")
# # print(f"x is y: {x is y}")      # False (or True - implementation dependent)
# # print(f"x == y: {x == y}")      # Always True

# # # ========== Always use 'is' for None, True, False ==========
# # print("\n4. Use 'is' for None, True, False:")
# # value = None

# # # Correct way
# # if value is None:
# #     print("✓ Correct: value is None")

# # # Works but not Pythonic
# # if value == None:
# #     print("✗ Works but not recommended")

# # # ========== String Interning ==========
# # print("\n5. String Interning:")
# # str1 = "hello"
# # str2 = "hello"
# # print(f"str1 = 'hello', str2 = 'hello'")
# # print(f"str1 is str2: {str1 is str2}")  # Usually True (interning)

# # str3 = "hello world"
# # str4 = "hello world"
# # print(f"\nstr3 = 'hello world', str4 = 'hello world'")
# # print(f"str3 is str4: {str3 is str4}")  # May be False (not always interned)
# # print(f"str3 == str4: {str3 == str4}")  # Always True

# # # ========== Practical Examples ==========
# # print("\n6. Practical Examples:")

# # def check_none(value):
# #     """Always use 'is' for None checks"""
# #     return value is None

# # def check_equality(a, b):
# #     """Use '==' for value comparison"""
# #     return a == b

# # print(f"check_none(None): {check_none(None)}")
# # print(f"check_equality([1,2], [1,2]): {check_equality([1,2], [1,2])}")

# # # Common mistake
# # print("\n7. Common Mistake:")
# # my_list = [1, 2, 3]
# # if my_list == None:  # Wrong! Should use 'is None'
# #     print("This won't execute")
# # else:
# #     print("List is not None, but this check is inefficient")

# # 4. Mutable vs Immutable Types
# # Topic 4: Mutable vs Immutable Types
# # How does it affect dictionary keys?

# print("=" * 60)
# print("TOPIC 4: Mutable vs Immutable Types")
# print("=" * 60)

# # ========== PART 1: Understanding Immutability ==========
# print("\n" + "─" * 60)
# print("PART 1: What are Immutable Types?")
# print("─" * 60)

# print("\nImmutable Types (CANNOT be changed after creation):")
# print("  • int, float, complex")
# print("  • str")
# print("  • tuple")
# print("  • frozenset")
# print("  • bool")
# print("  • bytes")

# # Example 1: Integers are immutable
# print("\n1. Integers (Immutable):")
# x = 10
# print(f"   x = {x}, id(x) = {id(x)}")
# x = x + 5  # This creates a NEW object, doesn't modify the old one
# print(f"   After x = x + 5:")
# print(f"   x = {x}, id(x) = {id(x)}")  # Different id!

# # Example 2: Strings are immutable
# print("\n2. Strings (Immutable):")
# name = "Python"
# print(f"   name = '{name}', id(name) = {id(name)}")
# name = name + "!"  # Creates new string object
# print(f"   After name = name + '!':")
# print(f"   name = '{name}', id(name) = {id(name)}")  # Different id!

# # Try to modify string (will error)
# # name[0] = "p"  # TypeError: 'str' object does not support item assignment

# # Example 3: Tuples are immutable
# print("\n3. Tuples (Immutable):")
# tup = (1, 2, 3)
# print(f"   tup = {tup}")
# # tup[0] = 10  # TypeError: 'tuple' object does not support item assignment
# print("   tup[0] = 10  # ERROR! Cannot modify tuple")

# # ========== PART 2: Understanding Mutability ==========
# print("\n" + "─" * 60)
# print("PART 2: What are Mutable Types?")
# print("─" * 60)

# print("\nMutable Types (CAN be changed after creation):")
# print("  • list")
# print("  • dict")
# print("  • set")
# print("  • custom classes")

# # Example 1: Lists are mutable
# print("\n1. Lists (Mutable):")
# my_list = [1, 2, 3]
# print(f"   my_list = {my_list}, id(my_list) = {id(my_list)}")
# my_list.append(4)  # Modifies the same object
# print(f"   After my_list.append(4):")
# print(f"   my_list = {my_list}, id(my_list) = {id(my_list)}")  # Same id!

# # Example 2: Reference behavior
# print("\n2. Reference Behavior (Critical!):")
# list1 = [1, 2, 3]
# list2 = list1  # Both point to the SAME object
# print(f"   list1 = {list1}, id(list1) = {id(list1)}")
# print(f"   list2 = {list2}, id(list2) = {id(list2)}")
# print(f"   list1 is list2: {list1 is list2}")  # True!
# print(f"   list1 == list2: {list1 == list2}")  # True!

# list2.append(4)
# print(f"\n   After list2.append(4):")
# print(f"   list1 = {list1}")  # list1 also changed!
# print(f"   list2 = {list2}")
# print(f"   Both reference the same object!")

# # Example 3: Dictionaries are mutable
# print("\n3. Dictionaries (Mutable):")
# my_dict = {"a": 1, "b": 2}
# print(f"   my_dict = {my_dict}")
# my_dict["c"] = 3  # Can modify
# print(f"   After my_dict['c'] = 3:")
# print(f"   my_dict = {my_dict}")

# # ========== PART 3: Dictionary Keys Must Be Immutable ==========
# print("\n" + "─" * 60)
# print("PART 3: Why Dictionary Keys Must Be Immutable")
# print("─" * 60)

# print("\nDictionary keys must be 'hashable' (immutable):")
# print("  • Dictionaries use hash tables internally")
# print("  • Hash of a key must remain constant")
# print("  • If key changes, hash changes → dictionary breaks!")

# # Valid dictionary keys (all immutable)
# valid_dict = {
#     "string": "value",           # String is immutable ✓
#     123: "integer",              # Integer is immutable ✓
#     (1, 2, 3): "tuple",         # Tuple is immutable ✓
#     frozenset([1, 2]): "frozen", # Frozenset is immutable ✓
#     True: "boolean",             # Bool is immutable ✓
# }

# print("\n✓ Valid dictionary keys:")
# for key, value in valid_dict.items():
#     print(f"   {key} ({type(key).__name__}): {value}")

# # Invalid dictionary keys (mutable)
# print("\n✗ Invalid dictionary keys (will cause TypeError):")
# print("   [1, 2, 3]  # List is mutable")
# print("   {1, 2, 3}  # Set is mutable")
# print("   {'a': 1}   # Dict is mutable") 

# # Uncomment to see the error:
# # invalid_dict = {
# #     [1, 2, 3]: "list"  # TypeError: unhashable type: 'list'
# # }

# # Why this matters
# print("\nWhy this matters:")
# print("  If a list could be a key:")
# print("    key = [1, 2]")
# print("    d[key] = 'value'")
# print("    key.append(3)  # Key changed!")
# print("    # Now d[key] is broken - hash changed!")

# # ========== PART 4: Mutable Default Argument Bug ==========
# print("\n" + "─" * 60)
# print("PART 4: The Mutable Default Argument Bug (COMMON INTERVIEW QUESTION!)")
# print("─" * 60)

# print("\n⚠️  THE BUG:")
# def add_item_bad(item, target_list=[]):  # DANGER: Mutable default!
#     """This function has a bug!"""
#     target_list.append(item)
#     return target_list

# print("   Bad function:")
# result1 = add_item_bad(1)
# print(f"   add_item_bad(1) → {result1}")  # [1]

# result2 = add_item_bad(2)
# print(f"   add_item_bad(2) → {result2}")  # [1, 2] ← Bug! Previous items still there!

# result3 = add_item_bad(3)
# print(f"   add_item_bad(3) → {result3}")  # [1, 2, 3] ← Keeps growing!

# print("\n   Why this happens:")
# print("   • Default arguments are evaluated ONCE when function is defined")
# print("   • The same list object is reused across all function calls")
# print("   • Modifications persist between calls!")

# print("\n✅ THE FIX:")
# def add_item_good(item, target_list=None):
#     """Correct: Use None as default, create new list inside."""
#     if target_list is None:
#         target_list = []
#     target_list.append(item)
#     return target_list

# print("   Good function:")
# result1 = add_item_good(1)
# print(f"   add_item_good(1) → {result1}")  # [1]

# result2 = add_item_good(2)
# print(f"   add_item_good(2) → {result2}")  # [2] ← Correct!

# result3 = add_item_good(3)
# print(f"   add_item_good(3) → {result3}")  # [3] ← Correct!

# # ========== PART 5: Function Arguments Behavior ==========
# print("\n" + "─" * 60)
# print("PART 5: How Mutability Affects Function Arguments")
# print("─" * 60)

# def modify_immutable(x):
#     """Immutable arguments: changes don't affect original"""
#     x = x + 10
#     print(f"   Inside function: x = {x}")

# def modify_mutable(lst):
#     """Mutable arguments: changes affect original!"""
#     lst.append(100)
#     print(f"   Inside function: lst = {lst}")

# # Immutable argument
# print("\n1. Immutable argument (int):")
# num = 5
# print(f"   Before: num = {num}")
# modify_immutable(num)
# print(f"   After: num = {num}")  # Unchanged!

# # Mutable argument
# print("\n2. Mutable argument (list):")
# my_list = [1, 2, 3]
# print(f"   Before: my_list = {my_list}")
# modify_mutable(my_list)
# print(f"   After: my_list = {my_list}")  # Changed!

# print("\n   Key takeaway:")
# print("   • Immutable: Function gets a copy (sort of)")
# print("   • Mutable: Function gets a reference to the same object")

# # ========== PART 6: Copying Mutable Objects ==========
# print("\n" + "─" * 60)
# print("PART 6: Shallow Copy vs Deep Copy")
# print("─" * 60)

# import copy

# # Shallow copy
# print("\n1. Shallow Copy (copy.copy() or list.copy()):")
# original = [1, 2, [3, 4]]
# shallow = original.copy()  # or copy.copy(original) or list(original) or original[:]

# print(f"   original = {original}")
# print(f"   shallow = {shallow}")

# # Modify top-level
# shallow[0] = 100
# print(f"\n   After shallow[0] = 100:")
# print(f"   original = {original}")  # [1, 2, [3, 4]] - unchanged
# print(f"   shallow = {shallow}")     # [100, 2, [3, 4]] - changed

# # Modify nested object
# shallow[2].append(5)
# print(f"\n   After shallow[2].append(5):")
# print(f"   original = {original}")  # [1, 2, [3, 4, 5]] - nested list changed!
# print(f"   shallow = {shallow}")    # [100, 2, [3, 4, 5]] - nested list changed!

# print("\n   Shallow copy:")
# print("   • Creates new top-level object")
# print("   • But nested objects are still references")

# # Deep copy
# print("\n2. Deep Copy (copy.deepcopy()):")
# original2 = [1, 2, [3, 4]]
# deep = copy.deepcopy(original2)

# print(f"   original2 = {original2}")
# print(f"   deep = {deep}")

# # Modify nested object
# deep[2].append(5)
# print(f"\n   After deep[2].append(5):")
# print(f"   original2 = {original2}")  # [1, 2, [3, 4]] - unchanged!
# print(f"   deep = {deep}")            # [1, 2, [3, 4, 5]] - changed

# print("\n   Deep copy:")
# print("   • Creates completely independent copy")
# print("   • All nested objects are also copied")

# # ========== PART 7: Interview Scenarios ==========
# print("\n" + "─" * 60)
# print("PART 7: Common Interview Scenarios")
# print("─" * 60)

# # Scenario 1: Tuple with mutable elements
# print("\n1. Tuple with Mutable Elements:")
# tup = ([1, 2], [3, 4])
# print(f"   tup = {tup}")
# # tup[0] = [5, 6]  # ERROR! Can't modify tuple
# tup[0].append(5)   # But can modify the list inside!
# print(f"   After tup[0].append(5):")
# print(f"   tup = {tup}")  # ([1, 2, 5], [3, 4])

# print("   • Tuple is immutable, but its contents can be mutable")
# print("   • You can't reassign tuple elements")
# print("   • But you can modify mutable elements inside")

# # Scenario 2: Set with immutable elements
# print("\n2. Set Requirements:")
# # Sets can only contain immutable (hashable) elements
# valid_set = {1, 2, 3, "hello", (4, 5)}
# print(f"   valid_set = {valid_set}")

# # Uncomment to see error:
# # invalid_set = {[1, 2], [3, 4]}  # TypeError: unhashable type: 'list'

# print("   • Sets can only contain immutable elements")
# print("   • Same reason as dictionary keys: must be hashable")

# # ========== SUMMARY ==========
# print("\n" + "=" * 60)
# print("SUMMARY - Key Takeaways for Interviews")
# print("=" * 60)

# print("""
# 1. IMMUTABLE TYPES:
#    • int, float, str, tuple, frozenset, bool, bytes
#    • Cannot be changed after creation
#    • Operations create new objects

# 2. MUTABLE TYPES:
#    • list, dict, set, custom classes
#    • Can be changed after creation
#    • Operations modify the same object

# 3. DICTIONARY KEYS:
#    • Must be immutable (hashable)
#    • Ensures hash remains constant
#    • Lists, sets, dicts cannot be keys

# 4. MUTABLE DEFAULT ARGUMENTS:
#    • NEVER use mutable defaults: def func(x=[])
#    • Use None instead: def func(x=None)
#    • Create new object inside function

# 5. COPYING:
#    • Shallow copy: copy.copy() - nested objects still referenced
#    • Deep copy: copy.deepcopy() - completely independent

# 6. FUNCTION ARGUMENTS:
#    • Immutable: Changes don't affect original
#    • Mutable: Changes affect original (pass by reference)
# """)

# print("=" * 60)