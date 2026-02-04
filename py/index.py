# # # # # # # # # # # # # # 1. *args and **kwargs
# # # # # # # # # # # # # def greet(name, *args, **kwargs):
# # # # # # # # # # # # #     print(f"Hello, {name}!")

# # # # # # # # # # # # #     if args:
# # # # # # # # # # # # #         print(f"Additional arguments: {args}")

# # # # # # # # # # # # #     if kwargs:
# # # # # # # # # # # # #         print(f"Additional keyword arguments:")
# # # # # # # # # # # # #         for key, value in kwargs.items():
# # # # # # # # # # # # #             print(f"  {key}: {value}")

# # # # # # # # # # # # # greet("John", "Jane", "Jim", "Jill", age=25, city="New York")
# # # # # # # # # # # # # ## Output:
# # # # # # # # # # # # # # Hello, John!
# # # # # # # # # # # # # # Additional arguments: ('Jane', 'Jim', 'Jill')
# # # # # # # # # # # # # # Additional keyword arguments:
# # # # # # # # # # # # # #   age: 25
# # # # # # # # # # # # # #   city: New York

# # # # # # # # # # # # # 2. Python decorators
# # # # # # # # # # # # def logging(func):
# # # # # # # # # # # #     def wrapper(*args, **kwargs):
# # # # # # # # # # # #         print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
# # # # # # # # # # # #         result = func(*args, **kwargs)
# # # # # # # # # # # #         print(f"Result: {result}")
# # # # # # # # # # # #         return result
# # # # # # # # # # # #     return wrapper

# # # # # # # # # # # # @logging
# # # # # # # # # # # # def add(a, b):
# # # # # # # # # # # #     return a + b

# # # # # # # # # # # # print(add(1, 2))
# # # # # # # # # # # # ## Output:
# # # # # # # # # # # # # Calling add with args: (1, 2) and kwargs: {}
# # # # # # # # # # # # # Result: 3
# # # # # # # # # # # # # 3

# # # # # # # # # # # # is vs == in Python
# # # # # # # # # # # # Topic 3: is vs == in Python

# # # # # # # # # # # print("=" * 50)
# # # # # # # # # # # print("TOPIC 3: is vs == in Python")
# # # # # # # # # # # print("=" * 50)

# # # # # # # # # # # # ========== Value Comparison (==) ==========
# # # # # # # # # # # print("\n1. Value Comparison (==):")
# # # # # # # # # # # a = [1, 2, 3]
# # # # # # # # # # # b = [1, 2, 3]
# # # # # # # # # # # print(f"a = {a}")
# # # # # # # # # # # print(f"b = {b}")
# # # # # # # # # # # print(f"a == b: {a == b}")      # True - same values
# # # # # # # # # # # print(f"a is b: {a is b}")      # False - different objects in memory

# # # # # # # # # # # # ========== Identity Comparison (is) ==========
# # # # # # # # # # # print("\n2. Identity Comparison (is):")
# # # # # # # # # # # c = a
# # # # # # # # # # # print(f"c = a")
# # # # # # # # # # # print(f"a is c: {a is c}")      # True - same object
# # # # # # # # # # # print(f"id(a): {id(a)}")
# # # # # # # # # # # print(f"id(c): {id(c)}")
# # # # # # # # # # # print(f"Same id? {id(a) == id(c)}")

# # # # # # # # # # # # ========== Integer Caching ==========
# # # # # # # # # # # print("\n3. Integer Caching (Python optimization):")
# # # # # # # # # # # x = 256
# # # # # # # # # # # y = 256
# # # # # # # # # # # print(f"x = 256, y = 256")
# # # # # # # # # # # print(f"x is y: {x is y}")      # True (Python caches -5 to 256)

# # # # # # # # # # # x = 257
# # # # # # # # # # # y = 257
# # # # # # # # # # # print(f"\nx = 257, y = 257")
# # # # # # # # # # # print(f"x is y: {x is y}")      # False (or True - implementation dependent)
# # # # # # # # # # # print(f"x == y: {x == y}")      # Always True

# # # # # # # # # # # # ========== Always use 'is' for None, True, False ==========
# # # # # # # # # # # print("\n4. Use 'is' for None, True, False:")
# # # # # # # # # # # value = None

# # # # # # # # # # # # Correct way
# # # # # # # # # # # if value is None:
# # # # # # # # # # #     print("✓ Correct: value is None")

# # # # # # # # # # # # Works but not Pythonic
# # # # # # # # # # # if value == None:
# # # # # # # # # # #     print("✗ Works but not recommended")

# # # # # # # # # # # # ========== String Interning ==========
# # # # # # # # # # # print("\n5. String Interning:")
# # # # # # # # # # # str1 = "hello"
# # # # # # # # # # # str2 = "hello"
# # # # # # # # # # # print(f"str1 = 'hello', str2 = 'hello'")
# # # # # # # # # # # print(f"str1 is str2: {str1 is str2}")  # Usually True (interning)

# # # # # # # # # # # str3 = "hello world"
# # # # # # # # # # # str4 = "hello world"
# # # # # # # # # # # print(f"\nstr3 = 'hello world', str4 = 'hello world'")
# # # # # # # # # # # print(f"str3 is str4: {str3 is str4}")  # May be False (not always interned)
# # # # # # # # # # # print(f"str3 == str4: {str3 == str4}")  # Always True

# # # # # # # # # # # # ========== Practical Examples ==========
# # # # # # # # # # # print("\n6. Practical Examples:")

# # # # # # # # # # # def check_none(value):
# # # # # # # # # # #     """Always use 'is' for None checks"""
# # # # # # # # # # #     return value is None

# # # # # # # # # # # def check_equality(a, b):
# # # # # # # # # # #     """Use '==' for value comparison"""
# # # # # # # # # # #     return a == b

# # # # # # # # # # # print(f"check_none(None): {check_none(None)}")
# # # # # # # # # # # print(f"check_equality([1,2], [1,2]): {check_equality([1,2], [1,2])}")

# # # # # # # # # # # # Common mistake
# # # # # # # # # # # print("\n7. Common Mistake:")
# # # # # # # # # # # my_list = [1, 2, 3]
# # # # # # # # # # # if my_list == None:  # Wrong! Should use 'is None'
# # # # # # # # # # #     print("This won't execute")
# # # # # # # # # # # else:
# # # # # # # # # # #     print("List is not None, but this check is inefficient")

# # # # # # # # # # # 4. Mutable vs Immutable Types
# # # # # # # # # # # Topic 4: Mutable vs Immutable Types
# # # # # # # # # # # How does it affect dictionary keys?

# # # # # # # # # # print("=" * 60)
# # # # # # # # # # print("TOPIC 4: Mutable vs Immutable Types")
# # # # # # # # # # print("=" * 60)

# # # # # # # # # # # ========== PART 1: Understanding Immutability ==========
# # # # # # # # # # print("\n" + "─" * 60)
# # # # # # # # # # print("PART 1: What are Immutable Types?")
# # # # # # # # # # print("─" * 60)

# # # # # # # # # # print("\nImmutable Types (CANNOT be changed after creation):")
# # # # # # # # # # print("  • int, float, complex")
# # # # # # # # # # print("  • str")
# # # # # # # # # # print("  • tuple")
# # # # # # # # # # print("  • frozenset")
# # # # # # # # # # print("  • bool")
# # # # # # # # # # print("  • bytes")

# # # # # # # # # # # Example 1: Integers are immutable
# # # # # # # # # # print("\n1. Integers (Immutable):")
# # # # # # # # # # x = 10
# # # # # # # # # # print(f"   x = {x}, id(x) = {id(x)}")
# # # # # # # # # # x = x + 5  # This creates a NEW object, doesn't modify the old one
# # # # # # # # # # print(f"   After x = x + 5:")
# # # # # # # # # # print(f"   x = {x}, id(x) = {id(x)}")  # Different id!

# # # # # # # # # # # Example 2: Strings are immutable
# # # # # # # # # # print("\n2. Strings (Immutable):")
# # # # # # # # # # name = "Python"
# # # # # # # # # # print(f"   name = '{name}', id(name) = {id(name)}")
# # # # # # # # # # name = name + "!"  # Creates new string object
# # # # # # # # # # print(f"   After name = name + '!':")
# # # # # # # # # # print(f"   name = '{name}', id(name) = {id(name)}")  # Different id!

# # # # # # # # # # # Try to modify string (will error)
# # # # # # # # # # # name[0] = "p"  # TypeError: 'str' object does not support item assignment

# # # # # # # # # # # Example 3: Tuples are immutable
# # # # # # # # # # print("\n3. Tuples (Immutable):")
# # # # # # # # # # tup = (1, 2, 3)
# # # # # # # # # # print(f"   tup = {tup}")
# # # # # # # # # # # tup[0] = 10  # TypeError: 'tuple' object does not support item assignment
# # # # # # # # # # print("   tup[0] = 10  # ERROR! Cannot modify tuple")

# # # # # # # # # # # ========== PART 2: Understanding Mutability ==========
# # # # # # # # # # print("\n" + "─" * 60)
# # # # # # # # # # print("PART 2: What are Mutable Types?")
# # # # # # # # # # print("─" * 60)

# # # # # # # # # # print("\nMutable Types (CAN be changed after creation):")
# # # # # # # # # # print("  • list")
# # # # # # # # # # print("  • dict")
# # # # # # # # # # print("  • set")
# # # # # # # # # # print("  • custom classes")

# # # # # # # # # # # Example 1: Lists are mutable
# # # # # # # # # # print("\n1. Lists (Mutable):")
# # # # # # # # # # my_list = [1, 2, 3]
# # # # # # # # # # print(f"   my_list = {my_list}, id(my_list) = {id(my_list)}")
# # # # # # # # # # my_list.append(4)  # Modifies the same object
# # # # # # # # # # print(f"   After my_list.append(4):")
# # # # # # # # # # print(f"   my_list = {my_list}, id(my_list) = {id(my_list)}")  # Same id!

# # # # # # # # # # # Example 2: Reference behavior
# # # # # # # # # # print("\n2. Reference Behavior (Critical!):")
# # # # # # # # # # list1 = [1, 2, 3]
# # # # # # # # # # list2 = list1  # Both point to the SAME object
# # # # # # # # # # print(f"   list1 = {list1}, id(list1) = {id(list1)}")
# # # # # # # # # # print(f"   list2 = {list2}, id(list2) = {id(list2)}")
# # # # # # # # # # print(f"   list1 is list2: {list1 is list2}")  # True!
# # # # # # # # # # print(f"   list1 == list2: {list1 == list2}")  # True!

# # # # # # # # # # list2.append(4)
# # # # # # # # # # print(f"\n   After list2.append(4):")
# # # # # # # # # # print(f"   list1 = {list1}")  # list1 also changed!
# # # # # # # # # # print(f"   list2 = {list2}")
# # # # # # # # # # print(f"   Both reference the same object!")

# # # # # # # # # # # Example 3: Dictionaries are mutable
# # # # # # # # # # print("\n3. Dictionaries (Mutable):")
# # # # # # # # # # my_dict = {"a": 1, "b": 2}
# # # # # # # # # # print(f"   my_dict = {my_dict}")
# # # # # # # # # # my_dict["c"] = 3  # Can modify
# # # # # # # # # # print(f"   After my_dict['c'] = 3:")
# # # # # # # # # # print(f"   my_dict = {my_dict}")

# # # # # # # # # # # ========== PART 3: Dictionary Keys Must Be Immutable ==========
# # # # # # # # # # print("\n" + "─" * 60)
# # # # # # # # # # print("PART 3: Why Dictionary Keys Must Be Immutable")
# # # # # # # # # # print("─" * 60)

# # # # # # # # # # print("\nDictionary keys must be 'hashable' (immutable):")
# # # # # # # # # # print("  • Dictionaries use hash tables internally")
# # # # # # # # # # print("  • Hash of a key must remain constant")
# # # # # # # # # # print("  • If key changes, hash changes → dictionary breaks!")

# # # # # # # # # # # Valid dictionary keys (all immutable)
# # # # # # # # # # valid_dict = {
# # # # # # # # # #     "string": "value",           # String is immutable ✓
# # # # # # # # # #     123: "integer",              # Integer is immutable ✓
# # # # # # # # # #     (1, 2, 3): "tuple",         # Tuple is immutable ✓
# # # # # # # # # #     frozenset([1, 2]): "frozen", # Frozenset is immutable ✓
# # # # # # # # # #     True: "boolean",             # Bool is immutable ✓
# # # # # # # # # # }

# # # # # # # # # # print("\n✓ Valid dictionary keys:")
# # # # # # # # # # for key, value in valid_dict.items():
# # # # # # # # # #     print(f"   {key} ({type(key).__name__}): {value}")

# # # # # # # # # # # Invalid dictionary keys (mutable)
# # # # # # # # # # print("\n✗ Invalid dictionary keys (will cause TypeError):")
# # # # # # # # # # print("   [1, 2, 3]  # List is mutable")
# # # # # # # # # # print("   {1, 2, 3}  # Set is mutable")
# # # # # # # # # # print("   {'a': 1}   # Dict is mutable") 

# # # # # # # # # # # Uncomment to see the error:
# # # # # # # # # # # invalid_dict = {
# # # # # # # # # # #     [1, 2, 3]: "list"  # TypeError: unhashable type: 'list'
# # # # # # # # # # # }

# # # # # # # # # # # Why this matters
# # # # # # # # # # print("\nWhy this matters:")
# # # # # # # # # # print("  If a list could be a key:")
# # # # # # # # # # print("    key = [1, 2]")
# # # # # # # # # # print("    d[key] = 'value'")
# # # # # # # # # # print("    key.append(3)  # Key changed!")
# # # # # # # # # # print("    # Now d[key] is broken - hash changed!")

# # # # # # # # # # # ========== PART 4: Mutable Default Argument Bug ==========
# # # # # # # # # # print("\n" + "─" * 60)
# # # # # # # # # # print("PART 4: The Mutable Default Argument Bug (COMMON INTERVIEW QUESTION!)")
# # # # # # # # # # print("─" * 60)

# # # # # # # # # # print("\n⚠️  THE BUG:")
# # # # # # # # # # def add_item_bad(item, target_list=[]):  # DANGER: Mutable default!
# # # # # # # # # #     """This function has a bug!"""
# # # # # # # # # #     target_list.append(item)
# # # # # # # # # #     return target_list

# # # # # # # # # # print("   Bad function:")
# # # # # # # # # # result1 = add_item_bad(1)
# # # # # # # # # # print(f"   add_item_bad(1) → {result1}")  # [1]

# # # # # # # # # # result2 = add_item_bad(2)
# # # # # # # # # # print(f"   add_item_bad(2) → {result2}")  # [1, 2] ← Bug! Previous items still there!

# # # # # # # # # # result3 = add_item_bad(3)
# # # # # # # # # # print(f"   add_item_bad(3) → {result3}")  # [1, 2, 3] ← Keeps growing!

# # # # # # # # # # print("\n   Why this happens:")
# # # # # # # # # # print("   • Default arguments are evaluated ONCE when function is defined")
# # # # # # # # # # print("   • The same list object is reused across all function calls")
# # # # # # # # # # print("   • Modifications persist between calls!")

# # # # # # # # # # print("\n✅ THE FIX:")
# # # # # # # # # # def add_item_good(item, target_list=None):
# # # # # # # # # #     """Correct: Use None as default, create new list inside."""
# # # # # # # # # #     if target_list is None:
# # # # # # # # # #         target_list = []
# # # # # # # # # #     target_list.append(item)
# # # # # # # # # #     return target_list

# # # # # # # # # # print("   Good function:")
# # # # # # # # # # result1 = add_item_good(1)
# # # # # # # # # # print(f"   add_item_good(1) → {result1}")  # [1]

# # # # # # # # # # result2 = add_item_good(2)
# # # # # # # # # # print(f"   add_item_good(2) → {result2}")  # [2] ← Correct!

# # # # # # # # # # result3 = add_item_good(3)
# # # # # # # # # # print(f"   add_item_good(3) → {result3}")  # [3] ← Correct!

# # # # # # # # # # # ========== PART 5: Function Arguments Behavior ==========
# # # # # # # # # # print("\n" + "─" * 60)
# # # # # # # # # # print("PART 5: How Mutability Affects Function Arguments")
# # # # # # # # # # print("─" * 60)

# # # # # # # # # # def modify_immutable(x):
# # # # # # # # # #     """Immutable arguments: changes don't affect original"""
# # # # # # # # # #     x = x + 10
# # # # # # # # # #     print(f"   Inside function: x = {x}")

# # # # # # # # # # def modify_mutable(lst):
# # # # # # # # # #     """Mutable arguments: changes affect original!"""
# # # # # # # # # #     lst.append(100)
# # # # # # # # # #     print(f"   Inside function: lst = {lst}")

# # # # # # # # # # # Immutable argument
# # # # # # # # # # print("\n1. Immutable argument (int):")
# # # # # # # # # # num = 5
# # # # # # # # # # print(f"   Before: num = {num}")
# # # # # # # # # # modify_immutable(num)
# # # # # # # # # # print(f"   After: num = {num}")  # Unchanged!

# # # # # # # # # # # Mutable argument
# # # # # # # # # # print("\n2. Mutable argument (list):")
# # # # # # # # # # my_list = [1, 2, 3]
# # # # # # # # # # print(f"   Before: my_list = {my_list}")
# # # # # # # # # # modify_mutable(my_list)
# # # # # # # # # # print(f"   After: my_list = {my_list}")  # Changed!

# # # # # # # # # # print("\n   Key takeaway:")
# # # # # # # # # # print("   • Immutable: Function gets a copy (sort of)")
# # # # # # # # # # print("   • Mutable: Function gets a reference to the same object")

# # # # # # # # # # # ========== PART 6: Copying Mutable Objects ==========
# # # # # # # # # # print("\n" + "─" * 60)
# # # # # # # # # # print("PART 6: Shallow Copy vs Deep Copy")
# # # # # # # # # # print("─" * 60)

# # # # # # # # # # import copy

# # # # # # # # # # # Shallow copy
# # # # # # # # # # print("\n1. Shallow Copy (copy.copy() or list.copy()):")
# # # # # # # # # # original = [1, 2, [3, 4]]
# # # # # # # # # # shallow = original.copy()  # or copy.copy(original) or list(original) or original[:]

# # # # # # # # # # print(f"   original = {original}")
# # # # # # # # # # print(f"   shallow = {shallow}")

# # # # # # # # # # # Modify top-level
# # # # # # # # # # shallow[0] = 100
# # # # # # # # # # print(f"\n   After shallow[0] = 100:")
# # # # # # # # # # print(f"   original = {original}")  # [1, 2, [3, 4]] - unchanged
# # # # # # # # # # print(f"   shallow = {shallow}")     # [100, 2, [3, 4]] - changed

# # # # # # # # # # # Modify nested object
# # # # # # # # # # shallow[2].append(5)
# # # # # # # # # # print(f"\n   After shallow[2].append(5):")
# # # # # # # # # # print(f"   original = {original}")  # [1, 2, [3, 4, 5]] - nested list changed!
# # # # # # # # # # print(f"   shallow = {shallow}")    # [100, 2, [3, 4, 5]] - nested list changed!

# # # # # # # # # # print("\n   Shallow copy:")
# # # # # # # # # # print("   • Creates new top-level object")
# # # # # # # # # # print("   • But nested objects are still references")

# # # # # # # # # # # Deep copy
# # # # # # # # # # print("\n2. Deep Copy (copy.deepcopy()):")
# # # # # # # # # # original2 = [1, 2, [3, 4]]
# # # # # # # # # # deep = copy.deepcopy(original2)

# # # # # # # # # # print(f"   original2 = {original2}")
# # # # # # # # # # print(f"   deep = {deep}")

# # # # # # # # # # # Modify nested object
# # # # # # # # # # deep[2].append(5)
# # # # # # # # # # print(f"\n   After deep[2].append(5):")
# # # # # # # # # # print(f"   original2 = {original2}")  # [1, 2, [3, 4]] - unchanged!
# # # # # # # # # # print(f"   deep = {deep}")            # [1, 2, [3, 4, 5]] - changed

# # # # # # # # # # print("\n   Deep copy:")
# # # # # # # # # # print("   • Creates completely independent copy")
# # # # # # # # # # print("   • All nested objects are also copied")

# # # # # # # # # # # ========== PART 7: Interview Scenarios ==========
# # # # # # # # # # print("\n" + "─" * 60)
# # # # # # # # # # print("PART 7: Common Interview Scenarios")
# # # # # # # # # # print("─" * 60)

# # # # # # # # # # # Scenario 1: Tuple with mutable elements
# # # # # # # # # # print("\n1. Tuple with Mutable Elements:")
# # # # # # # # # # tup = ([1, 2], [3, 4])
# # # # # # # # # # print(f"   tup = {tup}")
# # # # # # # # # # # tup[0] = [5, 6]  # ERROR! Can't modify tuple
# # # # # # # # # # tup[0].append(5)   # But can modify the list inside!
# # # # # # # # # # print(f"   After tup[0].append(5):")
# # # # # # # # # # print(f"   tup = {tup}")  # ([1, 2, 5], [3, 4])

# # # # # # # # # # print("   • Tuple is immutable, but its contents can be mutable")
# # # # # # # # # # print("   • You can't reassign tuple elements")
# # # # # # # # # # print("   • But you can modify mutable elements inside")

# # # # # # # # # # # Scenario 2: Set with immutable elements
# # # # # # # # # # print("\n2. Set Requirements:")
# # # # # # # # # # # Sets can only contain immutable (hashable) elements
# # # # # # # # # # valid_set = {1, 2, 3, "hello", (4, 5)}
# # # # # # # # # # print(f"   valid_set = {valid_set}")

# # # # # # # # # # # Uncomment to see error:
# # # # # # # # # # # invalid_set = {[1, 2], [3, 4]}  # TypeError: unhashable type: 'list'

# # # # # # # # # # print("   • Sets can only contain immutable elements")
# # # # # # # # # # print("   • Same reason as dictionary keys: must be hashable")

# # # # # # # # # # # ========== SUMMARY ==========
# # # # # # # # # # print("\n" + "=" * 60)
# # # # # # # # # # print("SUMMARY - Key Takeaways for Interviews")
# # # # # # # # # # print("=" * 60)

# # # # # # # # # # print("""
# # # # # # # # # # 1. IMMUTABLE TYPES:
# # # # # # # # # #    • int, float, str, tuple, frozenset, bool, bytes
# # # # # # # # # #    • Cannot be changed after creation
# # # # # # # # # #    • Operations create new objects

# # # # # # # # # # 2. MUTABLE TYPES:
# # # # # # # # # #    • list, dict, set, custom classes
# # # # # # # # # #    • Can be changed after creation
# # # # # # # # # #    • Operations modify the same object

# # # # # # # # # # 3. DICTIONARY KEYS:
# # # # # # # # # #    • Must be immutable (hashable)
# # # # # # # # # #    • Ensures hash remains constant
# # # # # # # # # #    • Lists, sets, dicts cannot be keys

# # # # # # # # # # 4. MUTABLE DEFAULT ARGUMENTS:
# # # # # # # # # #    • NEVER use mutable defaults: def func(x=[])
# # # # # # # # # #    • Use None instead: def func(x=None)
# # # # # # # # # #    • Create new object inside function

# # # # # # # # # # 5. COPYING:
# # # # # # # # # #    • Shallow copy: copy.copy() - nested objects still referenced
# # # # # # # # # #    • Deep copy: copy.deepcopy() - completely independent

# # # # # # # # # # 6. FUNCTION ARGUMENTS:
# # # # # # # # # #    • Immutable: Changes don't affect original
# # # # # # # # # #    • Mutable: Changes affect original (pass by reference)
# # # # # # # # # # """)

# # # # # # # # # # print("=" * 60)

# # # # # # # # # # 5. Python's Memory Management 
# # # # # # # # # # Topic 5: Python's Memory Management
# # # # # # # # # # Reference Counting & Garbage Collection

# # # # # # # # # import sys
# # # # # # # # # import gc

# # # # # # # # # print("=" * 60)
# # # # # # # # # print("TOPIC 5: Python's Memory Management")
# # # # # # # # # print("=" * 60)

# # # # # # # # # # ========== PART 1: Reference Counting ==========
# # # # # # # # # print("\n" + "─" * 60)
# # # # # # # # # print("PART 1: Reference Counting (Primary Mechanism)")
# # # # # # # # # print("─" * 60)

# # # # # # # # # print("""
# # # # # # # # # Reference Counting:
# # # # # # # # #   • Every object has a reference count
# # # # # # # # #   • Count increases when object is referenced
# # # # # # # # #   • Count decreases when reference is removed
# # # # # # # # #   • Object is deleted when count reaches 0
# # # # # # # # #   • Immediate and automatic
# # # # # # # # # """)

# # # # # # # # # # Example 1: Basic reference counting
# # # # # # # # # print("\n1. Basic Reference Counting:")
# # # # # # # # # x = [1, 2, 3]  # Object created, ref count = 1
# # # # # # # # # print(f"   x = [1, 2, 3]")
# # # # # # # # # print(f"   Reference count: {sys.getrefcount(x)}")  # Note: getrefcount includes its own reference

# # # # # # # # # y = x  # Another reference, ref count = 2
# # # # # # # # # print(f"   y = x")
# # # # # # # # # print(f"   Reference count: {sys.getrefcount(x)}")

# # # # # # # # # z = x  # Another reference, ref count = 3
# # # # # # # # # print(f"   z = x")
# # # # # # # # # print(f"   Reference count: {sys.getrefcount(x)}")

# # # # # # # # # del y  # Remove one reference, ref count = 2
# # # # # # # # # print(f"   del y")
# # # # # # # # # print(f"   Reference count: {sys.getrefcount(x)}")

# # # # # # # # # del z  # Remove another reference, ref count = 1
# # # # # # # # # print(f"   del z")
# # # # # # # # # print(f"   Reference count: {sys.getrefcount(x)}")

# # # # # # # # # del x  # Remove last reference, ref count = 0 → object deleted
# # # # # # # # # print(f"   del x")
# # # # # # # # # print("   Object is now deleted (garbage collected)")

# # # # # # # # # # Example 2: Function references
# # # # # # # # # print("\n2. Function References:")
# # # # # # # # # def get_ref_count(obj):
# # # # # # # # #     """Function parameter creates temporary reference"""
# # # # # # # # #     return sys.getrefcount(obj)

# # # # # # # # # my_list = [1, 2, 3]
# # # # # # # # # print(f"   my_list = [1, 2, 3]")
# # # # # # # # # print(f"   Reference count: {sys.getrefcount(my_list)}")
# # # # # # # # # print("   Note: getrefcount() adds 1 for its own parameter!")

# # # # # # # # # # Example 3: Local scope
# # # # # # # # # print("\n3. Local Scope:")
# # # # # # # # # def test_function():
# # # # # # # # #     local_var = [1, 2, 3]
# # # # # # # # #     print(f"   Inside function: {sys.getrefcount(local_var)}")
# # # # # # # # #     return local_var

# # # # # # # # # result = test_function()
# # # # # # # # # print(f"   After function returns: {sys.getrefcount(result)}")
# # # # # # # # # print("   Local variable deleted when function exits")

# # # # # # # # # # ========== PART 2: When Objects Are Deleted ==========
# # # # # # # # # print("\n" + "─" * 60)
# # # # # # # # # print("PART 2: When Are Objects Deleted?")
# # # # # # # # # print("─" * 60)

# # # # # # # # # print("""
# # # # # # # # # Objects are deleted when:
# # # # # # # # #   1. Reference count reaches 0
# # # # # # # # #   2. Variable goes out of scope
# # # # # # # # #   3. Explicitly deleted with 'del'
# # # # # # # # #   4. Reassigned (old object's ref count decreases)
# # # # # # # # # """)

# # # # # # # # # # Example 1: Out of scope
# # # # # # # # # print("\n1. Out of Scope:")
# # # # # # # # # def create_object():
# # # # # # # # #     obj = [1, 2, 3]
# # # # # # # # #     print(f"   Created object: {obj}")
# # # # # # # # #     return obj

# # # # # # # # # obj = create_object()
# # # # # # # # # print(f"   Object still exists: {obj}")
# # # # # # # # # print("   Original 'obj' in function is deleted when function exits")

# # # # # # # # # # Example 2: Reassignment
# # # # # # # # # print("\n2. Reassignment:")
# # # # # # # # # x = [1, 2, 3]
# # # # # # # # # print(f"   x = [1, 2, 3]")
# # # # # # # # # x = [4, 5, 6]  # Old [1,2,3] object's ref count decreases
# # # # # # # # # print(f"   x = [4, 5, 6]")
# # # # # # # # # print("   Old [1,2,3] object is deleted (ref count = 0)")

# # # # # # # # # # ========== PART 3: Circular References Problem ==========
# # # # # # # # # print("\n" + "─" * 60)
# # # # # # # # # print("PART 3: Circular References (Reference Counting Limitation)")
# # # # # # # # # print("─" * 60)

# # # # # # # # # print("""
# # # # # # # # # Circular Reference:
# # # # # # # # #   • Object A references Object B
# # # # # # # # #   • Object B references Object A
# # # # # # # # #   • Reference count never reaches 0
# # # # # # # # #   • Reference counting alone can't delete them
# # # # # # # # #   • This is where Garbage Collection comes in!
# # # # # # # # # """)

# # # # # # # # # # Example: Circular reference
# # # # # # # # # print("\n1. Creating Circular Reference:")
# # # # # # # # # class Node:
# # # # # # # # #     def __init__(self, value):
# # # # # # # # #         self.value = value
# # # # # # # # #         self.next = None
    
# # # # # # # # #     def __repr__(self):
# # # # # # # # #         return f"Node({self.value})"

# # # # # # # # # # Create circular reference
# # # # # # # # # node1 = Node(1)
# # # # # # # # # node2 = Node(2)
# # # # # # # # # node1.next = node2
# # # # # # # # # node2.next = node1  # Circular!

# # # # # # # # # print(f"   node1 = {node1}")
# # # # # # # # # print(f"   node2 = {node2}")
# # # # # # # # # print(f"   node1.next = {node1.next}")
# # # # # # # # # print(f"   node2.next = {node2.next}")

# # # # # # # # # print("\n   Even if we delete references:")
# # # # # # # # # del node1
# # # # # # # # # del node2
# # # # # # # # # print("   del node1")
# # # # # # # # # print("   del node2")
# # # # # # # # # print("   Objects still exist in memory (circular reference)")
# # # # # # # # # print("   Reference counting can't handle this!")

# # # # # # # # # # ========== PART 4: Garbage Collection ==========
# # # # # # # # # print("\n" + "─" * 60)
# # # # # # # # # print("PART 4: Garbage Collection (Handles Circular References)")
# # # # # # # # # print("─" * 60)

# # # # # # # # # print("""
# # # # # # # # # Garbage Collection (GC):
# # # # # # # # #   • Handles circular references
# # # # # # # # #   • Runs periodically (not immediate)
# # # # # # # # #   • Uses cycle detection algorithm
# # # # # # # # #   • Can be controlled manually
# # # # # # # # #   • Slower than reference counting
# # # # # # # # # """)

# # # # # # # # # # Check GC status
# # # # # # # # # print("\n1. Garbage Collection Status:")
# # # # # # # # # print(f"   GC is enabled: {gc.isenabled()}")
# # # # # # # # # print(f"   GC thresholds: {gc.get_threshold()}")

# # # # # # # # # # Manual garbage collection
# # # # # # # # # print("\n2. Manual Garbage Collection:")
# # # # # # # # # print("   You can force GC to run:")
# # # # # # # # # print("   gc.collect()  # Runs garbage collection")

# # # # # # # # # # Example: Collecting circular references
# # # # # # # # # print("\n3. Collecting Circular References:")

# # # # # # # # # # Create circular reference
# # # # # # # # # class Circular:
# # # # # # # # #     def __init__(self, name):
# # # # # # # # #         self.name = name
# # # # # # # # #         self.ref = None

# # # # # # # # # a = Circular("A")
# # # # # # # # # b = Circular("B")
# # # # # # # # # a.ref = b
# # # # # # # # # b.ref = a  # Circular reference

# # # # # # # # # print(f"   Created circular reference: a ↔ b")
# # # # # # # # # print(f"   Objects before GC: {len(gc.get_objects())}")

# # # # # # # # # # Delete references
# # # # # # # # # del a
# # # # # # # # # del b

# # # # # # # # # # Force garbage collection
# # # # # # # # # collected = gc.collect()
# # # # # # # # # print(f"   gc.collect() returned: {collected}")
# # # # # # # # # print("   Circular references are now cleaned up!")

# # # # # # # # # # ========== PART 5: GC Generations ==========
# # # # # # # # # print("\n" + "─" * 60)
# # # # # # # # # print("PART 5: Generational Garbage Collection")
# # # # # # # # # print("─" * 60)

# # # # # # # # # print("""
# # # # # # # # # Python uses Generational GC:
# # # # # # # # #   • Generation 0: New objects (checked most frequently)
# # # # # # # # #   • Generation 1: Survived one GC cycle
# # # # # # # # #   • Generation 2: Survived multiple GC cycles
# # # # # # # # #   • Older objects checked less frequently
# # # # # # # # #   • Based on observation: most objects die young
# # # # # # # # # """)

# # # # # # # # # print("\nGC Thresholds (when GC runs):")
# # # # # # # # # thresholds = gc.get_threshold()
# # # # # # # # # print(f"   Generation 0: {thresholds[0]} allocations")
# # # # # # # # # print(f"   Generation 1: {thresholds[1]} collections")
# # # # # # # # # print(f"   Generation 2: {thresholds[2]} collections")

# # # # # # # # # # ========== PART 6: Monitoring Memory ==========
# # # # # # # # # print("\n" + "─" * 60)
# # # # # # # # # print("PART 6: Monitoring Memory Usage")
# # # # # # # # # print("─" * 60)

# # # # # # # # # # Get object count
# # # # # # # # # print("\n1. Object Count:")
# # # # # # # # # print(f"   Total objects tracked: {len(gc.get_objects())}")

# # # # # # # # # # Get statistics
# # # # # # # # # print("\n2. GC Statistics:")
# # # # # # # # # stats = gc.get_stats()
# # # # # # # # # for i, stat in enumerate(stats):
# # # # # # # # #     print(f"   Generation {i}:")
# # # # # # # # #     print(f"     Collections: {stat['collections']}")
# # # # # # # # #     print(f"     Collected: {stat['collected']}")
# # # # # # # # #     print(f"     Uncollectable: {stat['uncollectable']}")

# # # # # # # # # # ========== PART 7: Weak References ==========
# # # # # # # # # print("\n" + "─" * 60)
# # # # # # # # # print("PART 7: Weak References (Advanced)")
# # # # # # # # # print("─" * 60)

# # # # # # # # # import weakref

# # # # # # # # # print("""
# # # # # # # # # Weak References:
# # # # # # # # #   • Don't increase reference count
# # # # # # # # #   • Allow object to be garbage collected
# # # # # # # # #   • Useful for caches, observers, callbacks
# # # # # # # # # """)

# # # # # # # # # print("\n1. Regular Reference (increases count):")
# # # # # # # # # obj = [1, 2, 3]
# # # # # # # # # ref = obj
# # # # # # # # # print(f"   obj = [1, 2, 3]")
# # # # # # # # # print(f"   ref = obj")
# # # # # # # # # print(f"   Reference count: {sys.getrefcount(obj)}")

# # # # # # # # # print("\n2. Weak Reference (doesn't increase count):")
# # # # # # # # # obj2 = [4, 5, 6]
# # # # # # # # # weak_ref = weakref.ref(obj2)
# # # # # # # # # print(f"   obj2 = [4, 5, 6]")
# # # # # # # # # print(f"   weak_ref = weakref.ref(obj2)")
# # # # # # # # # print(f"   Reference count: {sys.getrefcount(obj2)}")
# # # # # # # # # print(f"   Weak ref alive: {weak_ref() is not None}")

# # # # # # # # # del obj2
# # # # # # # # # print(f"   del obj2")
# # # # # # # # # print(f"   Weak ref alive: {weak_ref() is not None}")  # Now None

# # # # # # # # # # ========== PART 8: Memory Management Best Practices ==========
# # # # # # # # # print("\n" + "─" * 60)
# # # # # # # # # print("PART 8: Best Practices & Interview Tips")
# # # # # # # # # print("─" * 60)

# # # # # # # # # print("""
# # # # # # # # # Best Practices:

# # # # # # # # # 1. Let Python handle memory automatically
# # # # # # # # #    • Reference counting handles 99% of cases
# # # # # # # # #    • GC handles circular references

# # # # # # # # # 2. Avoid circular references when possible
# # # # # # # # #    • Use weak references for caches
# # # # # # # # #    • Break cycles explicitly if needed

# # # # # # # # # 3. Use 'del' for large objects
# # # # # # # # #    • Helps free memory immediately
# # # # # # # # #    • Good practice, not always necessary

# # # # # # # # # 4. Monitor memory in production
# # # # # # # # #    • Use tools like memory_profiler
# # # # # # # # #    • Watch for memory leaks

# # # # # # # # # 5. Don't disable GC unless you know what you're doing
# # # # # # # # #    • gc.disable() stops automatic GC
# # # # # # # # #    • Only for performance-critical code
# # # # # # # # # """)

# # # # # # # # # # ========== SUMMARY ==========
# # # # # # # # # print("\n" + "=" * 60)
# # # # # # # # # print("SUMMARY - Key Takeaways for Interviews")
# # # # # # # # # print("=" * 60)

# # # # # # # # # print("""
# # # # # # # # # 1. REFERENCE COUNTING (Primary):
# # # # # # # # #    • Every object has a reference count
# # # # # # # # #    • Count increases with each reference
# # # # # # # # #    • Count decreases when reference removed
# # # # # # # # #    • Object deleted when count = 0
# # # # # # # # #    • Immediate and automatic
# # # # # # # # #    • Handles 99% of memory management

# # # # # # # # # 2. GARBAGE COLLECTION (Secondary):
# # # # # # # # #    • Handles circular references
# # # # # # # # #    • Uses generational algorithm
# # # # # # # # #    • Runs periodically (not immediate)
# # # # # # # # #    • Slower than reference counting
# # # # # # # # #    • Can be controlled manually

# # # # # # # # # 3. CIRCULAR REFERENCES:
# # # # # # # # #    • Object A → Object B → Object A
# # # # # # # # #    • Reference counting can't handle
# # # # # # # # #    • GC detects and cleans up cycles

# # # # # # # # # 4. GENERATIONAL GC:
# # # # # # # # #    • Generation 0, 1, 2
# # # # # # # # #    • New objects checked more frequently
# # # # # # # # #    • Based on "most objects die young"

# # # # # # # # # 5. BEST PRACTICES:
# # # # # # # # #    • Let Python handle automatically
# # # # # # # # #    • Use 'del' for large objects
# # # # # # # # #    • Avoid circular references when possible
# # # # # # # # #    • Use weak references for caches
# # # # # # # # # """)

# # # # # # # # # print("=" * 60)

# # # # # # # # # Topic 6: Deep Copy vs Shallow Copy

# # # # # # # # import copy

# # # # # # # # print("=" * 60)
# # # # # # # # print("TOPIC 6: Deep Copy vs Shallow Copy")
# # # # # # # # print("=" * 60)

# # # # # # # # # ========== PART 1: Understanding Assignment ==========
# # # # # # # # print("\n" + "─" * 60)
# # # # # # # # print("PART 1: Regular Assignment (Reference)")
# # # # # # # # print("─" * 60)

# # # # # # # # print("""
# # # # # # # # Regular Assignment (=):
# # # # # # # #   • Creates a reference to the same object
# # # # # # # #   • Both variables point to same memory location
# # # # # # # #   • Changes to one affect the other
# # # # # # # # """)

# # # # # # # # original = [1, 2, 3]
# # # # # # # # reference = original  # Just a reference, not a copy

# # # # # # # # print(f"\n1. Regular Assignment:")
# # # # # # # # print(f"   original = {original}")
# # # # # # # # print(f"   reference = original")
# # # # # # # # print(f"   reference = {reference}")

# # # # # # # # reference.append(4)
# # # # # # # # print(f"\n   After reference.append(4):")
# # # # # # # # print(f"   original = {original}")  # Changed!
# # # # # # # # print(f"   reference = {reference}")  # Changed!
# # # # # # # # print(f"   id(original) == id(reference): {id(original) == id(reference)}")
# # # # # # # # print("   ⚠️  Both point to the same object!")

# # # # # # # # # ========== PART 2: Shallow Copy ==========
# # # # # # # # print("\n" + "─" * 60)
# # # # # # # # print("PART 2: Shallow Copy")
# # # # # # # # print("─" * 60)

# # # # # # # # print("""
# # # # # # # # Shallow Copy:
# # # # # # # #   • Creates a NEW top-level object
# # # # # # # #   • Copies references to nested objects
# # # # # # # #   • Nested objects are still shared
# # # # # # # #   • Changes to nested objects affect both
# # # # # # # # """)

# # # # # # # # # Method 1: Using copy.copy()
# # # # # # # # original_list = [1, 2, [3, 4]]
# # # # # # # # shallow1 = copy.copy(original_list)

# # # # # # # # # Method 2: Using list.copy() (for lists)
# # # # # # # # shallow2 = original_list.copy()

# # # # # # # # # Method 3: Using slicing (for lists)
# # # # # # # # shallow3 = original_list[:]

# # # # # # # # # Method 4: Using list() constructor
# # # # # # # # shallow4 = list(original_list)

# # # # # # # # print("\n1. Creating Shallow Copy (Multiple Methods):")
# # # # # # # # print(f"   original_list = {original_list}")

# # # # # # # # print("\n   Method 1: copy.copy()")
# # # # # # # # print(f"   shallow1 = copy.copy(original_list)")

# # # # # # # # print("\n   Method 2: list.copy()")
# # # # # # # # print(f"   shallow2 = original_list.copy()")

# # # # # # # # print("\n   Method 3: Slicing")
# # # # # # # # print(f"   shallow3 = original_list[:]")

# # # # # # # # print("\n   Method 4: list() constructor")
# # # # # # # # print(f"   shallow4 = list(original_list)")

# # # # # # # # # Test shallow copy behavior
# # # # # # # # print("\n2. Shallow Copy Behavior:")

# # # # # # # # # Modify top-level element
# # # # # # # # shallow1[0] = 100
# # # # # # # # print(f"   After shallow1[0] = 100:")
# # # # # # # # print(f"   original_list = {original_list}")  # [1, 2, [3, 4]] - unchanged
# # # # # # # # print(f"   shallow1 = {shallow1}")           # [100, 2, [3, 4]] - changed

# # # # # # # # # Modify nested object
# # # # # # # # shallow1[2].append(5)
# # # # # # # # print(f"\n   After shallow1[2].append(5):")
# # # # # # # # print(f"   original_list = {original_list}")  # [1, 2, [3, 4, 5]] - nested changed!
# # # # # # # # print(f"   shallow1 = {shallow1}")           # [100, 2, [3, 4, 5]] - nested changed!

# # # # # # # # print("\n   Key Point:")
# # # # # # # # print("   • Top-level changes: Independent")
# # # # # # # # print("   • Nested changes: Shared!")

# # # # # # # # # ========== PART 3: Deep Copy ==========
# # # # # # # # print("\n" + "─" * 60)
# # # # # # # # print("PART 3: Deep Copy")
# # # # # # # # print("─" * 60)

# # # # # # # # print("""
# # # # # # # # Deep Copy:
# # # # # # # #   • Creates completely independent copy
# # # # # # # #   • Recursively copies all nested objects
# # # # # # # #   • No shared references
# # # # # # # #   • Changes are completely independent
# # # # # # # # """)

# # # # # # # # original_list2 = [1, 2, [3, 4]]
# # # # # # # # deep = copy.deepcopy(original_list2)

# # # # # # # # print("\n1. Creating Deep Copy:")
# # # # # # # # print(f"   original_list2 = {original_list2}")
# # # # # # # # print(f"   deep = copy.deepcopy(original_list2)")

# # # # # # # # # Modify top-level element
# # # # # # # # deep[0] = 100
# # # # # # # # print(f"\n2. After deep[0] = 100:")
# # # # # # # # print(f"   original_list2 = {original_list2}")  # [1, 2, [3, 4]] - unchanged
# # # # # # # # print(f"   deep = {deep}")                      # [100, 2, [3, 4]] - changed

# # # # # # # # # Modify nested object
# # # # # # # # deep[2].append(5)
# # # # # # # # print(f"\n3. After deep[2].append(5):")
# # # # # # # # print(f"   original_list2 = {original_list2}")  # [1, 2, [3, 4]] - unchanged!
# # # # # # # # print(f"   deep = {deep}")                      # [100, 2, [3, 4, 5]] - changed

# # # # # # # # print("\n   Key Point:")
# # # # # # # # print("   • Top-level changes: Independent")
# # # # # # # # print("   • Nested changes: Independent!")

# # # # # # # # # ========== PART 4: Visual Comparison ==========
# # # # # # # # print("\n" + "─" * 60)
# # # # # # # # print("PART 4: Side-by-Side Comparison")
# # # # # # # # print("─" * 60)

# # # # # # # # # Setup
# # # # # # # # original = [1, 2, [3, 4]]
# # # # # # # # shallow = copy.copy(original)
# # # # # # # # deep = copy.deepcopy(original)

# # # # # # # # print("\nInitial State:")
# # # # # # # # print(f"   original = {original}")
# # # # # # # # print(f"   shallow = {shallow}")
# # # # # # # # print(f"   deep = {deep}")

# # # # # # # # # Modify nested list
# # # # # # # # print("\nAfter modifying nested list:")
# # # # # # # # shallow[2].append(5)
# # # # # # # # deep[2].append(6)

# # # # # # # # print(f"   original = {original}")  # [1, 2, [3, 4, 5]] - affected by shallow!
# # # # # # # # print(f"   shallow = {shallow}")   # [1, 2, [3, 4, 5]] - same as original
# # # # # # # # print(f"   deep = {deep}")         # [1, 2, [3, 4, 6]] - independent!

# # # # # # # # print("\n   Summary:")
# # # # # # # # print("   • Shallow copy: Nested objects shared → both changed")
# # # # # # # # print("   • Deep copy: Nested objects independent → only deep changed")

# # # # # # # # # ========== PART 5: Dictionaries ==========
# # # # # # # # print("\n" + "─" * 60)
# # # # # # # # print("PART 5: Shallow vs Deep Copy with Dictionaries")
# # # # # # # # print("─" * 60)

# # # # # # # # original_dict = {
# # # # # # # #     "name": "Python",
# # # # # # # #     "versions": [3.8, 3.9, 3.10],
# # # # # # # #     "info": {"creator": "Guido", "year": 1991}
# # # # # # # # }

# # # # # # # # shallow_dict = copy.copy(original_dict)
# # # # # # # # deep_dict = copy.deepcopy(original_dict)

# # # # # # # # print("\n1. Original Dictionary:")
# # # # # # # # print(f"   {original_dict}")

# # # # # # # # # Modify nested list
# # # # # # # # shallow_dict["versions"].append(3.11)
# # # # # # # # deep_dict["versions"].append(3.12)

# # # # # # # # print("\n2. After modifying nested list:")
# # # # # # # # print(f"   original_dict = {original_dict}")  # versions changed!
# # # # # # # # print(f"   shallow_dict = {shallow_dict}")   # versions changed!
# # # # # # # # print(f"   deep_dict = {deep_dict}")         # versions independent!

# # # # # # # # # Modify nested dict
# # # # # # # # shallow_dict["info"]["year"] = 2024
# # # # # # # # deep_dict["info"]["year"] = 2025

# # # # # # # # print("\n3. After modifying nested dictionary:")
# # # # # # # # print(f"   original_dict = {original_dict}")  # year changed!
# # # # # # # # print(f"   shallow_dict = {shallow_dict}")   # year changed!
# # # # # # # # print(f"   deep_dict = {deep_dict}")         # year independent!

# # # # # # # # # ========== PART 6: Custom Objects ==========
# # # # # # # # print("\n" + "─" * 60)
# # # # # # # # print("PART 6: Custom Objects")
# # # # # # # # print("─" * 60)

# # # # # # # # class Person:
# # # # # # # #     def __init__(self, name, friends=None):
# # # # # # # #         self.name = name
# # # # # # # #         self.friends = friends if friends else []
    
# # # # # # # #     def __repr__(self):
# # # # # # # #         return f"Person({self.name}, friends={self.friends})"

# # # # # # # # person1 = Person("Alice", [Person("Bob")])
# # # # # # # # person2 = copy.copy(person1)      # Shallow copy
# # # # # # # # person3 = copy.deepcopy(person1)  # Deep copy

# # # # # # # # print("\n1. Original Person:")
# # # # # # # # print(f"   person1 = {person1}")

# # # # # # # # # Modify nested list
# # # # # # # # person2.friends.append(Person("Charlie"))
# # # # # # # # person3.friends.append(Person("David"))

# # # # # # # # print("\n2. After modifying friends list:")
# # # # # # # # print(f"   person1 = {person1}")  # friends changed!
# # # # # # # # print(f"   person2 = {person2}")  # friends changed!
# # # # # # # # print(f"   person3 = {person3}")  # friends independent!

# # # # # # # # # ========== PART 7: When to Use Each ==========
# # # # # # # # print("\n" + "─" * 60)
# # # # # # # # print("PART 7: When to Use Shallow vs Deep Copy")
# # # # # # # # print("─" * 60)

# # # # # # # # print("""
# # # # # # # # Use SHALLOW COPY when:
# # # # # # # #   ✓ Object has no nested mutable objects
# # # # # # # #   ✓ You want faster performance
# # # # # # # #   ✓ Nested objects can be shared
# # # # # # # #   ✓ Flat structures (list of numbers, strings)

# # # # # # # # Use DEEP COPY when:
# # # # # # # #   ✓ Object has nested mutable objects
# # # # # # # #   ✓ You need complete independence
# # # # # # # #   ✓ Nested objects must not be shared
# # # # # # # #   ✓ Complex nested structures
# # # # # # # #   ✓ You're unsure (safer default)
# # # # # # # # """)

# # # # # # # # # Example: When shallow copy is fine
# # # # # # # # print("\n1. Shallow Copy is Fine (Flat Structure):")
# # # # # # # # flat_list = [1, 2, 3, 4, 5]
# # # # # # # # shallow_flat = copy.copy(flat_list)
# # # # # # # # shallow_flat[0] = 100
# # # # # # # # print(f"   original = {flat_list}")      # [1, 2, 3, 4, 5]
# # # # # # # # print(f"   shallow = {shallow_flat}")    # [100, 2, 3, 4, 5]
# # # # # # # # print("   ✓ No nested objects, shallow copy works perfectly")

# # # # # # # # # Example: When deep copy is needed
# # # # # # # # print("\n2. Deep Copy is Needed (Nested Structure):")
# # # # # # # # nested_list = [[1, 2], [3, 4], [5, 6]]
# # # # # # # # shallow_nested = copy.copy(nested_list)
# # # # # # # # deep_nested = copy.deepcopy(nested_list)

# # # # # # # # shallow_nested[0].append(7)
# # # # # # # # deep_nested[0].append(8)

# # # # # # # # print(f"   original = {nested_list}")      # [[1, 2, 7], [3, 4], [5, 6]]
# # # # # # # # print(f"   shallow = {shallow_nested}")    # [[1, 2, 7], [3, 4], [5, 6]]
# # # # # # # # print(f"   deep = {deep_nested}")          # [[1, 2, 8], [3, 4], [5, 6]]
# # # # # # # # print("   ⚠️  Shallow copy shares nested lists!")

# # # # # # # # # ========== PART 8: Performance Comparison ==========
# # # # # # # # print("\n" + "─" * 60)
# # # # # # # # print("PART 8: Performance Considerations")
# # # # # # # # print("─" * 60)

# # # # # # # # import time

# # # # # # # # large_nested = [[i for i in range(1000)] for _ in range(1000)]

# # # # # # # # # Shallow copy timing
# # # # # # # # start = time.time()
# # # # # # # # shallow_copy = copy.copy(large_nested)
# # # # # # # # shallow_time = time.time() - start

# # # # # # # # # Deep copy timing
# # # # # # # # start = time.time()
# # # # # # # # deep_copy = copy.deepcopy(large_nested)
# # # # # # # # deep_time = time.time() - start

# # # # # # # # print(f"\nPerformance Test (1000x1000 nested list):")
# # # # # # # # print(f"   Shallow copy: {shallow_time:.6f} seconds")
# # # # # # # # print(f"   Deep copy: {deep_time:.6f} seconds")
# # # # # # # # print(f"   Deep copy is {deep_time/shallow_time:.1f}x slower")
# # # # # # # # print("\n   Reason: Deep copy recursively copies all nested objects")

# # # # # # # # # ========== PART 9: Common Pitfalls ==========
# # # # # # # # print("\n" + "─" * 60)
# # # # # # # # print("PART 9: Common Pitfalls & Gotchas")
# # # # # # # # print("─" * 60)

# # # # # # # # print("\n1. Pitfall: Thinking shallow copy is independent")
# # # # # # # # original = [1, [2, 3]]
# # # # # # # # shallow = copy.copy(original)
# # # # # # # # shallow[1].append(4)
# # # # # # # # print(f"   original = {original}")  # [1, [2, 3, 4]] - changed!
# # # # # # # # print("   ⚠️  Shallow copy shares nested objects!")

# # # # # # # # print("\n2. Pitfall: Using = instead of copy")
# # # # # # # # original = [1, 2, 3]
# # # # # # # # wrong = original  # Not a copy!
# # # # # # # # wrong.append(4)
# # # # # # # # print(f"   original = {original}")  # [1, 2, 3, 4] - changed!
# # # # # # # # print("   ⚠️  This is just a reference, not a copy!")

# # # # # # # # print("\n3. Solution: Always use copy.copy() or copy.deepcopy()")
# # # # # # # # original = [1, 2, 3]
# # # # # # # # correct = copy.copy(original)
# # # # # # # # correct.append(4)
# # # # # # # # print(f"   original = {original}")  # [1, 2, 3] - unchanged!
# # # # # # # # print("   ✓ Correct way to copy")

# # # # # # # # # ========== SUMMARY ==========
# # # # # # # # print("\n" + "=" * 60)
# # # # # # # # print("SUMMARY - Key Takeaways for Interviews")
# # # # # # # # print("=" * 60)

# # # # # # # # print("""
# # # # # # # # 1. SHALLOW COPY (copy.copy()):
# # # # # # # #    • Creates new top-level object
# # # # # # # #    • Copies references to nested objects
# # # # # # # #    • Nested objects are shared
# # # # # # # #    • Faster performance
# # # # # # # #    • Use for flat structures

# # # # # # # # 2. DEEP COPY (copy.deepcopy()):
# # # # # # # #    • Creates completely independent copy
# # # # # # # #    • Recursively copies all nested objects
# # # # # # # #    • No shared references
# # # # # # # #    • Slower performance
# # # # # # # #    • Use for nested structures

# # # # # # # # 3. METHODS TO CREATE COPIES:
# # # # # # # #    • Shallow: copy.copy(), list.copy(), list[:], list()
# # # # # # # #    • Deep: copy.deepcopy() (only method)

# # # # # # # # 4. WHEN TO USE:
# # # # # # # #    • Shallow: Flat objects, performance critical
# # # # # # # #    • Deep: Nested objects, need independence

# # # # # # # # 5. COMMON MISTAKES:
# # # # # # # #    • Using = instead of copy
# # # # # # # #    • Using shallow copy for nested structures
# # # # # # # #    • Not understanding shared references
# # # # # # # # """)

# # # # # # # # print("=" * 60)
# # # # # # # # Topic 7: Python's GIL (Global Interpreter Lock)
# # # # # # # # How does it affect threading?

# # # # # # # import threading
# # # # # # # import time
# # # # # # # import multiprocessing
# # # # # # # import sys

# # # # # # # print("=" * 60)
# # # # # # # print("TOPIC 7: Python's GIL (Global Interpreter Lock)")
# # # # # # # print("=" * 60)

# # # # # # # # ========== PART 1: What is the GIL? ==========
# # # # # # # print("\n" + "─" * 60)
# # # # # # # print("PART 1: What is the GIL?")
# # # # # # # print("─" * 60)

# # # # # # # print("""
# # # # # # # Global Interpreter Lock (GIL):
# # # # # # #   • A mutex (lock) that protects access to Python objects
# # # # # # #   • Only ONE thread can execute Python bytecode at a time
# # # # # # #   • Prevents multiple threads from modifying Python objects simultaneously
# # # # # # #   • Exists in CPython (default Python implementation)
# # # # # # #   • Does NOT exist in Jython, IronPython, or PyPy
# # # # # # # """)

# # # # # # # print("\nKey Points:")
# # # # # # # print("  • GIL is a single lock on the entire interpreter")
# # # # # # # print("  • Only one thread can execute Python code at a time")
# # # # # # # print("  • Other threads must wait for the GIL to be released")
# # # # # # # print("  • This prevents race conditions in CPython's memory management")

# # # # # # # # ========== PART 2: Why Does Python Have a GIL? ==========
# # # # # # # print("\n" + "─" * 60)
# # # # # # # print("PART 2: Why Does Python Have a GIL?")
# # # # # # # print("─" * 60)

# # # # # # # print("""
# # # # # # # Reasons for GIL:

# # # # # # # 1. Memory Management:
# # # # # # #    • CPython uses reference counting for memory management
# # # # # # #    • Without GIL, multiple threads could modify ref counts simultaneously
# # # # # # #    • This would cause memory corruption and crashes

# # # # # # # 2. C Extension Compatibility:
# # # # # # #    • Many Python libraries are C extensions
# # # # # # #    • GIL makes it easier to write thread-safe C extensions
# # # # # # #    • Prevents complex locking in every C extension

# # # # # # # 3. Simplicity:
# # # # # # #    • Simpler implementation
# # # # # # #    • Easier to maintain
# # # # # # #    • Prevents many concurrency bugs
# # # # # # # """)

# # # # # # # print("\nTrade-off:")
# # # # # # # print("  ✓ Simpler, safer memory management")
# # # # # # # print("  ✗ Limits true parallelism for CPU-bound tasks")

# # # # # # # # ========== PART 3: GIL and CPU-Bound Tasks ==========
# # # # # # # print("\n" + "─" * 60)
# # # # # # # print("PART 3: GIL Impact on CPU-Bound Tasks")
# # # # # # # print("─" * 60)

# # # # # # # print("""
# # # # # # # CPU-Bound Task Example:
# # # # # # #   • Tasks that do heavy computation
# # # # # # #   • Multiple threads DON'T help (GIL prevents parallel execution)
# # # # # # #   • Threads take turns, not truly parallel
# # # # # # # """)

# # # # # # # def cpu_bound_task(n):
# # # # # # #     """CPU-intensive task"""
# # # # # # #     count = 0
# # # # # # #     for i in range(n):
# # # # # # #         count += i ** 2
# # # # # # #     return count

# # # # # # # # Sequential execution
# # # # # # # print("\n1. Sequential Execution (Baseline):")
# # # # # # # start = time.time()
# # # # # # # result1 = cpu_bound_task(10000000)
# # # # # # # result2 = cpu_bound_task(10000000)
# # # # # # # sequential_time = time.time() - start
# # # # # # # print(f"   Time: {sequential_time:.4f} seconds")

# # # # # # # # Threaded execution (won't be faster!)
# # # # # # # print("\n2. Threaded Execution (GIL Limits Parallelism):")
# # # # # # # start = time.time()

# # # # # # # def run_task():
# # # # # # #     return cpu_bound_task(10000000)

# # # # # # # thread1 = threading.Thread(target=run_task)
# # # # # # # thread2 = threading.Thread(target=run_task)

# # # # # # # thread1.start()
# # # # # # # thread2.start()
# # # # # # # thread1.join()
# # # # # # # thread2.join()

# # # # # # # threaded_time = time.time() - start
# # # # # # # print(f"   Time: {threaded_time:.4f} seconds")
# # # # # # # print(f"   Speedup: {sequential_time/threaded_time:.2f}x")
# # # # # # # print("   ⚠️  Threading doesn't help CPU-bound tasks due to GIL!")

# # # # # # # # ========== PART 4: GIL and I/O-Bound Tasks ==========
# # # # # # # print("\n" + "─" * 60)
# # # # # # # print("PART 4: GIL and I/O-Bound Tasks (Threading WORKS!)")
# # # # # # # print("─" * 60)

# # # # # # # print("""
# # # # # # # I/O-Bound Task Example:
# # # # # # #   • Tasks that wait for I/O (network, disk, etc.)
# # # # # # #   • Threads release GIL during I/O operations
# # # # # # #   • Multiple threads CAN run concurrently
# # # # # # #   • Threading IS beneficial here!
# # # # # # # """)

# # # # # # # def io_bound_task(duration):
# # # # # # #     """Simulate I/O operation (waiting)"""
# # # # # # #     time.sleep(duration)
# # # # # # #     return f"Completed after {duration}s"

# # # # # # # # Sequential execution
# # # # # # # print("\n1. Sequential I/O Execution:")
# # # # # # # start = time.time()
# # # # # # # result1 = io_bound_task(1)
# # # # # # # result2 = io_bound_task(1)
# # # # # # # sequential_io_time = time.time() - start
# # # # # # # print(f"   Time: {sequential_io_time:.4f} seconds")

# # # # # # # # Threaded execution (WILL be faster!)
# # # # # # # print("\n2. Threaded I/O Execution:")
# # # # # # # start = time.time()

# # # # # # # results = []
# # # # # # # def run_io_task(duration):
# # # # # # #     results.append(io_bound_task(duration))

# # # # # # # thread1 = threading.Thread(target=run_io_task, args=(1,))
# # # # # # # thread2 = threading.Thread(target=run_io_task, args=(1,))

# # # # # # # thread1.start()
# # # # # # # thread2.start()
# # # # # # # thread1.join()
# # # # # # # thread2.join()

# # # # # # # threaded_io_time = time.time() - start
# # # # # # # print(f"   Time: {threaded_io_time:.4f} seconds")
# # # # # # # print(f"   Speedup: {sequential_io_time/threaded_io_time:.2f}x")
# # # # # # # print("   ✓ Threading helps I/O-bound tasks!")

# # # # # # # # ========== PART 5: When GIL is Released ==========
# # # # # # # print("\n" + "─" * 60)
# # # # # # # print("PART 5: When Does the GIL Get Released?")
# # # # # # # print("─" * 60)

# # # # # # # print("""
# # # # # # # GIL is Released During:
# # # # # # #   1. I/O Operations:
# # # # # # #      • File operations (read/write)
# # # # # # #      • Network operations (socket send/receive)
# # # # # # #      • time.sleep()
# # # # # # #      • Database queries

# # # # # # #   2. C Extensions:
# # # # # # #      • NumPy operations (can release GIL)
# # # # # # #      • Image processing libraries
# # # # # # #      • Some C extensions explicitly release GIL

# # # # # # #   3. After Certain Bytecode Instructions:
# # # # # # #      • Python periodically switches threads
# # # # # # #      • After N bytecode instructions
# # # # # # #      • Allows other threads to run
# # # # # # # """)

# # # # # # # print("\nGIL is NOT Released During:")
# # # # # # # print("  • Pure Python computation")
# # # # # # # print("  • Most Python operations")
# # # # # # # print("  • List comprehensions")
# # # # # # # print("  • Mathematical operations")

# # # # # # # # ========== PART 6: Threading vs Multiprocessing ==========
# # # # # # # print("\n" + "─" * 60)
# # # # # # # print("PART 6: Threading vs Multiprocessing")
# # # # # # # print("─" * 60)

# # # # # # # print("""
# # # # # # # Threading (with GIL):
# # # # # # #   ✓ Good for I/O-bound tasks
# # # # # # #   ✗ Not good for CPU-bound tasks
# # # # # # #   ✓ Shared memory (easier data sharing)
# # # # # # #   ✓ Lower overhead

# # # # # # # Multiprocessing (no GIL):
# # # # # # #   ✓ Good for CPU-bound tasks
# # # # # # #   ✓ True parallelism (separate processes)
# # # # # # #   ✗ Separate memory (harder data sharing)
# # # # # # #   ✗ Higher overhead
# # # # # # # """)

# # # # # # # def cpu_intensive(n):
# # # # # # #     """CPU-intensive task"""
# # # # # # #     total = 0
# # # # # # #     for i in range(n):
# # # # # # #         total += i ** 2
# # # # # # #     return total

# # # # # # # # Multiprocessing example (commented to avoid issues in some environments)
# # # # # # # print("\n1. Multiprocessing for CPU-Bound Tasks:")
# # # # # # # print("   Each process has its own Python interpreter")
# # # # # # # print("   Each process has its own GIL")
# # # # # # # print("   True parallelism across processes")
# # # # # # # print("   Use multiprocessing for CPU-bound tasks!")

# # # # # # # # Example structure (not executed to avoid issues)
# # # # # # # print("""
# # # # # # #    Example:
# # # # # # #    from multiprocessing import Process
   
# # # # # # #    def worker(n):
# # # # # # #        return cpu_intensive(n)
   
# # # # # # #    p1 = Process(target=worker, args=(10000000,))
# # # # # # #    p2 = Process(target=worker, args=(10000000,))
# # # # # # #    p1.start()
# # # # # # #    p2.start()
# # # # # # #    p1.join()
# # # # # # #    p2.join()
# # # # # # #    # This WILL run in parallel!
# # # # # # # """)

# # # # # # # # ========== PART 7: Real-World Examples ==========
# # # # # # # print("\n" + "─" * 60)
# # # # # # # print("PART 7: Real-World Use Cases")
# # # # # # # print("─" * 60)

# # # # # # # print("""
# # # # # # # Use Threading For:
# # # # # # #   ✓ Web scraping (I/O-bound)
# # # # # # #   ✓ Downloading files (I/O-bound)
# # # # # # #   ✓ API calls (I/O-bound)
# # # # # # #   ✓ Database queries (I/O-bound)
# # # # # # #   ✓ File processing with I/O (I/O-bound)

# # # # # # # Use Multiprocessing For:
# # # # # # #   ✓ Image processing (CPU-bound)
# # # # # # #   ✓ Data analysis (CPU-bound)
# # # # # # #   ✓ Scientific computations (CPU-bound)
# # # # # # #   ✓ Video encoding (CPU-bound)
# # # # # # #   ✓ Machine learning training (CPU-bound)
# # # # # # # """)

# # # # # # # # Example: Web scraping with threading
# # # # # # # print("\n1. Example: Web Scraping (Threading is Good):")
# # # # # # # print("""
# # # # # # #    import requests
# # # # # # #    import threading
   
# # # # # # #    urls = ['url1', 'url2', 'url3']
   
# # # # # # #    def fetch(url):
# # # # # # #        response = requests.get(url)  # I/O operation
# # # # # # #        return response.text
   
# # # # # # #    threads = []
# # # # # # #    for url in urls:
# # # # # # #        t = threading.Thread(target=fetch, args=(url,))
# # # # # # #        t.start()
# # # # # # #        threads.append(t)
   
# # # # # # #    # Threading helps because requests.get() releases GIL
# # # # # # #    """)

# # # # # # # # Example: Image processing with multiprocessing
# # # # # # # print("\n2. Example: Image Processing (Multiprocessing is Better):")
# # # # # # # print("""
# # # # # # #    from multiprocessing import Pool
# # # # # # #    from PIL import Image
   
# # # # # # #    def process_image(image_path):
# # # # # # #        img = Image.open(image_path)
# # # # # # #        # CPU-intensive operations
# # # # # # #        return img.filter(ImageFilter.BLUR)
   
# # # # # # #    with Pool() as pool:
# # # # # # #        results = pool.map(process_image, image_paths)
   
# # # # # # #    # Multiprocessing helps because it's CPU-bound
# # # # # # #    """)

# # # # # # # # ========== PART 8: GIL Details ==========
# # # # # # # print("\n" + "─" * 60)
# # # # # # # print("PART 8: GIL Technical Details")
# # # # # # # print("─" * 60)

# # # # # # # print("""
# # # # # # # GIL Behavior:
# # # # # # #   • Thread acquires GIL before executing Python bytecode
# # # # # # #   • Thread releases GIL after certain operations
# # # # # # #   • Other threads compete for GIL
# # # # # # #   • Context switching happens periodically

# # # # # # # GIL Switching:
# # # # # # #   • Happens after N bytecode instructions (default: 100)
# # # # # # #   • Can be controlled with sys.setswitchinterval()
# # # # # # #   • Threads voluntarily release GIL during I/O
# # # # # # # """)

# # # # # # # print(f"\nCurrent GIL Switch Interval:")
# # # # # # # print(f"   {sys.getswitchinterval()} seconds")
# # # # # # # print("   (Can be changed with sys.setswitchinterval())")

# # # # # # # # ========== PART 9: Common Misconceptions ==========
# # # # # # # print("\n" + "─" * 60)
# # # # # # # print("PART 9: Common Misconceptions")
# # # # # # # print("─" * 60)

# # # # # # # print("""
# # # # # # # Misconception 1: "Python can't do multithreading"
# # # # # # #   ✗ Wrong! Python CAN do multithreading
# # # # # # #   ✓ It's just limited for CPU-bound tasks
# # # # # # #   ✓ Threading works great for I/O-bound tasks

# # # # # # # Misconception 2: "GIL makes Python slow"
# # # # # # #   ✗ GIL doesn't make Python inherently slow
# # # # # # #   ✓ GIL limits parallelism for CPU-bound tasks
# # # # # # #   ✓ For I/O-bound tasks, GIL doesn't matter

# # # # # # # Misconception 3: "Threading is useless in Python"
# # # # # # #   ✗ Wrong! Threading is useful for I/O-bound tasks
# # # # # # #   ✓ Web servers, file processing, network I/O
# # # # # # #   ✓ Threading is the right choice for these

# # # # # # # Misconception 4: "Multiprocessing is always better"
# # # # # # #   ✗ Wrong! Use threading for I/O-bound tasks
# # # # # # #   ✓ Use multiprocessing for CPU-bound tasks
# # # # # # #   ✓ Choose based on task type
# # # # # # # """)

# # # # # # # # ========== PART 10: How to Work Around GIL ==========
# # # # # # # print("\n" + "─" * 60)
# # # # # # # print("PART 10: Working Around the GIL")
# # # # # # # print("─" * 60)

# # # # # # # print("""
# # # # # # # Solutions for CPU-Bound Tasks:

# # # # # # # 1. Multiprocessing:
# # # # # # #    • Separate processes, separate GILs
# # # # # # #    • True parallelism
# # # # # # #    • Best for CPU-bound tasks

# # # # # # # 2. C Extensions:
# # # # # # #    • Write CPU-intensive code in C
# # # # # # #    • Release GIL in C code
# # # # # # #    • NumPy, SciPy do this

# # # # # # # 3. Alternative Implementations:
# # # # # # #    • Jython (no GIL, but slower)
# # # # # # #    • IronPython (no GIL, but slower)
# # # # # # #    • PyPy (has GIL, but faster)

# # # # # # # 4. Async/Await:
# # # # # # #    • For I/O-bound tasks
# # # # # # #    • Single-threaded but efficient
# # # # # # #    • asyncio module
# # # # # # # """)

# # # # # # # # ========== SUMMARY ==========
# # # # # # # print("\n" + "=" * 60)
# # # # # # # print("SUMMARY - Key Takeaways for Interviews")
# # # # # # # print("=" * 60)

# # # # # # # print("""
# # # # # # # 1. WHAT IS GIL:
# # # # # # #    • Global Interpreter Lock in CPython
# # # # # # #    • Only one thread executes Python bytecode at a time
# # # # # # #    • Prevents race conditions in memory management

# # # # # # # 2. WHY GIL EXISTS:
# # # # # # #    • Simplifies memory management (reference counting)
# # # # # # #    • Makes C extensions easier to write
# # # # # # #    • Prevents many concurrency bugs

# # # # # # # 3. GIL IMPACT:
# # # # # # #    • CPU-bound tasks: Threading doesn't help (use multiprocessing)
# # # # # # #    • I/O-bound tasks: Threading works great (GIL released during I/O)

# # # # # # # 4. THREADING VS MULTIPROCESSING:
# # # # # # #    • Threading: I/O-bound tasks, shared memory, lower overhead
# # # # # # #    • Multiprocessing: CPU-bound tasks, separate memory, true parallelism

# # # # # # # 5. WHEN GIL IS RELEASED:
# # # # # # #    • During I/O operations (file, network, sleep)
# # # # # # #    • In C extensions that explicitly release it
# # # # # # #    • Periodically after N bytecode instructions

# # # # # # # 6. BEST PRACTICES:
# # # # # # #    • Use threading for I/O-bound tasks
# # # # # # #    • Use multiprocessing for CPU-bound tasks
# # # # # # #    • Use asyncio for async I/O operations
# # # # # # #    • Don't fight the GIL, work with it!
# # # # # # # """)

# # # # # # # print("=" * 60)

# # # # # # # Concurrency vs Parallelism vs Multiprocessing

# # # # # # import threading
# # # # # # import multiprocessing
# # # # # # import time
# # # # # # import asyncio

# # # # # # print("=" * 60)
# # # # # # print("Concurrency vs Parallelism vs Multiprocessing")
# # # # # # print("=" * 60)

# # # # # # # ========== PART 1: Sequential (Baseline) ==========
# # # # # # print("\n" + "─" * 60)
# # # # # # print("PART 1: Sequential Execution (No Concurrency)")
# # # # # # print("─" * 60)

# # # # # # def task(name, duration):
# # # # # #     """Simulate a task"""
# # # # # #     print(f"   {name} starting...")
# # # # # #     time.sleep(duration)
# # # # # #     print(f"   {name} completed")
# # # # # #     return f"{name} done"

# # # # # # print("\n1. Sequential Execution:")
# # # # # # start = time.time()
# # # # # # result1 = task("Task 1", 1)
# # # # # # result2 = task("Task 2", 1)
# # # # # # sequential_time = time.time() - start
# # # # # # print(f"   Total time: {sequential_time:.2f} seconds")
# # # # # # print("   Tasks run one after another")

# # # # # # # ========== PART 2: Concurrency (Threading) ==========
# # # # # # print("\n" + "─" * 60)
# # # # # # print("PART 2: Concurrency (Threading)")
# # # # # # print("─" * 60)

# # # # # # print("""
# # # # # # Concurrency with Threading:
# # # # # #   • Multiple tasks make progress
# # # # # #   • Tasks may not run simultaneously
# # # # # #   • Good for I/O-bound tasks
# # # # # #   • Python's GIL limits true parallelism
# # # # # # """)

# # # # # # print("\n1. Concurrent Execution (Threading):")
# # # # # # start = time.time()

# # # # # # def run_task(name, duration):
# # # # # #     return task(name, duration)

# # # # # # thread1 = threading.Thread(target=run_task, args=("Task 1", 1))
# # # # # # thread2 = threading.Thread(target=run_task, args=("Task 2", 1))

# # # # # # thread1.start()
# # # # # # thread2.start()
# # # # # # thread1.join()
# # # # # # thread2.join()

# # # # # # concurrent_time = time.time() - start
# # # # # # print(f"   Total time: {concurrent_time:.2f} seconds")
# # # # # # print(f"   Speedup: {sequential_time/concurrent_time:.2f}x")
# # # # # # print("   ✓ Tasks run concurrently (overlapping)")

# # # # # # # ========== PART 3: Parallelism (Multiprocessing) ==========
# # # # # # print("\n" + "─" * 60)
# # # # # # print("PART 3: Parallelism (Multiprocessing)")
# # # # # # print("─" * 60)

# # # # # # print("""
# # # # # # Parallelism with Multiprocessing:
# # # # # #   • Multiple tasks run simultaneously
# # # # # #   • Requires multiple CPU cores
# # # # # #   • True parallelism in Python
# # # # # #   • Each process has its own memory space
# # # # # # """)

# # # # # # print("\n1. Parallel Execution (Multiprocessing):")
# # # # # # print("   (Commented out - may not work in all environments)")
# # # # # # print("""
# # # # # #    start = time.time()
   
# # # # # #    def run_task(name, duration):
# # # # # #        return task(name, duration)
   
# # # # # #    p1 = multiprocessing.Process(target=run_task, args=("Task 1", 1))
# # # # # #    p2 = multiprocessing.Process(target=run_task, args=("Task 2", 1))
   
# # # # # #    p1.start()
# # # # # #    p2.start()
# # # # # #    p1.join()
# # # # # #    p2.join()
   
# # # # # #    parallel_time = time.time() - start
# # # # # #    print(f"   Total time: {parallel_time:.2f} seconds")
# # # # # #    print("   ✓ Tasks run in parallel (simultaneously)")
# # # # # #    """)

# # # # # # # ========== PART 4: Key Differences ==========
# # # # # # print("\n" + "─" * 60)
# # # # # # print("PART 4: Key Differences")
# # # # # # print("─" * 60)

# # # # # # print("""
# # # # # # ┌─────────────────┬──────────────────┬────────────────────┐
# # # # # # │                 │   Concurrency    │    Parallelism     │
# # # # # # ├─────────────────┼──────────────────┼────────────────────┤
# # # # # # │ Definition      │ Multiple tasks   │ Multiple tasks     │
# # # # # # │                 │ make progress    │ run simultaneously │
# # # # # # ├─────────────────┼──────────────────┼────────────────────┤
# # # # # # │ Requires        │ Single core OK   │ Multiple cores     │
# # # # # # ├─────────────────┼──────────────────┼────────────────────┤
# # # # # # │ Execution       │ Interleaved      │ Simultaneous       │
# # # # # # ├─────────────────┼──────────────────┼────────────────────┤
# # # # # # │ Example         │ Threading        │ Multiprocessing    │
# # # # # # │                 │ Async/Await      │ Multiple CPUs      │
# # # # # # ├─────────────────┼──────────────────┼────────────────────┤
# # # # # # │ Use Case        │ I/O-bound        │ CPU-bound          │
# # # # # # └─────────────────┴──────────────────┴────────────────────┘
# # # # # # """)

# # # # # # # ========== PART 5: Concurrency Patterns ==========
# # # # # # print("\n" + "─" * 60)
# # # # # # print("PART 5: Concurrency Patterns in Python")
# # # # # # print("─" * 60)

# # # # # # print("""
# # # # # # 1. Threading (Concurrency):
# # # # # #    • Multiple threads in one process
# # # # # #    • Shared memory
# # # # # #    • Good for I/O-bound tasks
# # # # # #    • Limited by GIL for CPU-bound tasks

# # # # # # 2. Multiprocessing (Parallelism):
# # # # # #    • Multiple processes
# # # # # #    • Separate memory
# # # # # #    • Good for CPU-bound tasks
# # # # # #    • True parallelism

# # # # # # 3. Async/Await (Concurrency):
# # # # # #    • Single thread, event loop
# # # # # #    • Cooperative multitasking
# # # # # #    • Excellent for I/O-bound tasks
# # # # # #    • Not for CPU-bound tasks
# # # # # # """)

# # # # # # # Example: Async/Await (Concurrency)
# # # # # # print("\n3. Async/Await (Concurrency Pattern):")
# # # # # # print("""
# # # # # #    async def async_task(name, duration):
# # # # # #        print(f"{name} starting...")
# # # # # #        await asyncio.sleep(duration)  # Non-blocking
# # # # # #        print(f"{name} completed")
# # # # # #        return f"{name} done"
   
# # # # # #    async def main():
# # # # # #        await asyncio.gather(
# # # # # #            async_task("Task 1", 1),
# # # # # #            async_task("Task 2", 1)
# # # # # #        )
   
# # # # # #    # Tasks run concurrently (not in parallel)
# # # # # #    # Single thread, but tasks overlap
# # # # # #    """)

# # # # # # # ========== PART 6: Real-World Examples ==========
# # # # # # print("\n" + "─" * 60)
# # # # # # print("PART 6: Real-World Examples")
# # # # # # print("─" * 60)

# # # # # # print("""
# # # # # # CONCURRENCY Examples:
# # # # # #   ✓ Web server handling multiple requests
# # # # # #   ✓ Downloading multiple files
# # # # # #   ✓ Processing multiple API calls
# # # # # #   ✓ Reading from multiple files

# # # # # # PARALLELISM Examples:
# # # # # #   ✓ Image processing (multiple images)
# # # # # #   ✓ Video encoding
# # # # # #   ✓ Scientific computations
# # # # # #   ✓ Machine learning training
# # # # # #   ✓ Data analysis on large datasets
# # # # # # """)

# # # # # # # ========== PART 7: When to Use What ==========
# # # # # # print("\n" + "─" * 60)
# # # # # # print("PART 7: When to Use What?")
# # # # # # print("─" * 60)

# # # # # # print("""
# # # # # # Use THREADING (Concurrency) when:
# # # # # #   ✓ I/O-bound tasks (network, file I/O)
# # # # # #   ✓ Tasks that wait a lot
# # # # # #   ✓ Need shared memory
# # # # # #   ✓ Lower overhead is important

# # # # # # Use MULTIPROCESSING (Parallelism) when:
# # # # # #   ✓ CPU-bound tasks (computation)
# # # # # #   ✓ Need true parallelism
# # # # # #   ✓ Tasks are independent
# # # # # #   ✓ Can handle separate memory

# # # # # # Use ASYNC/AWAIT (Concurrency) when:
# # # # # #   ✓ Many I/O-bound tasks
# # # # # #   ✓ High concurrency needed
# # # # # #   ✓ Network operations
# # # # # #   ✓ Want efficient single-threaded solution
# # # # # # """)

# # # # # # # ========== PART 8: Python-Specific Considerations ==========
# # # # # # print("\n" + "─" * 60)
# # # # # # print("PART 8: Python-Specific Considerations")
# # # # # # print("─" * 60)

# # # # # # print("""
# # # # # # Python's GIL Impact:

# # # # # # Threading (Concurrency):
# # # # # #   • GIL prevents true parallelism
# # # # # #   • Threads take turns (concurrent, not parallel)
# # # # # #   • Still useful for I/O-bound tasks
# # # # # #   • GIL released during I/O operations

# # # # # # Multiprocessing (Parallelism):
# # # # # #   • Each process has its own GIL
# # # # # #   • True parallelism across processes
# # # # # #   • No GIL interference between processes
# # # # # #   • Best for CPU-bound tasks

# # # # # # Async/Await (Concurrency):
# # # # # #   • Single thread, no GIL issues
# # # # # #   • Cooperative multitasking
# # # # # #   • Very efficient for I/O-bound
# # # # # #   • Not affected by GIL
# # # # # # """)

# # # # # # # ========== PART 9: Visual Comparison ==========
# # # # # # print("\n" + "─" * 60)
# # # # # # print("PART 9: Visual Timeline Comparison")
# # # # # # print("─" * 60)

# # # # # # print("""
# # # # # # SEQUENTIAL:
# # # # # # Time →  [Task A][Task B][Task C]
# # # # # #         0s      1s      2s      3s
# # # # # #         Total: 3 seconds

# # # # # # CONCURRENCY (Threading):
# # # # # # Time →  [Task A]
# # # # # #         [Task B]
# # # # # #         [Task C]
# # # # # #         0s      1s      2s
# # # # # #         Total: ~2 seconds (overlapping)

# # # # # # PARALLELISM (Multiprocessing):
# # # # # # Time →  [Task A]
# # # # # #         [Task B]
# # # # # #         [Task C]
# # # # # #         0s      1s
# # # # # #         Total: ~1 second (simultaneous)
# # # # # # """)

# # # # # # # ========== PART 10: Common Confusions ==========
# # # # # # print("\n" + "─" * 60)
# # # # # # print("PART 10: Common Confusions Clarified")
# # # # # # print("─" * 60)

# # # # # # print("""
# # # # # # Confusion 1: "Concurrency = Parallelism"
# # # # # #   ✗ Wrong! They're different:
# # # # # #   • Concurrency: Structure (dealing with multiple things)
# # # # # #   • Parallelism: Execution (doing multiple things simultaneously)
# # # # # #   • You can have concurrency without parallelism
# # # # # #   • You can have parallelism without concurrency (rare)

# # # # # # Confusion 2: "Threading = Parallelism"
# # # # # #   ✗ Wrong! In Python:
# # # # # #   • Threading provides concurrency
# # # # # #   • GIL prevents true parallelism
# # # # # #   • Multiprocessing provides parallelism

# # # # # # Confusion 3: "More threads = Faster"
# # # # # #   ✗ Wrong! For CPU-bound tasks:
# # # # # #   • More threads don't help (GIL)
# # # # # #   • Use multiprocessing instead
# # # # # #   • Threads help for I/O-bound tasks

# # # # # # Confusion 4: "Async = Parallel"
# # # # # #   ✗ Wrong! Async is:
# # # # # #   • Concurrency, not parallelism
# # # # # #   • Single thread
# # # # # #   • Cooperative multitasking
# # # # # #   • Not simultaneous execution
# # # # # # """)

# # # # # # # ========== SUMMARY ==========
# # # # # # print("\n" + "=" * 60)
# # # # # # print("SUMMARY - Key Takeaways")
# # # # # # print("=" * 60)

# # # # # # print("""
# # # # # # 1. CONCURRENCY:
# # # # # #    • Multiple tasks make progress
# # # # # #    • May not run simultaneously
# # # # # #    • About structure and design
# # # # # #    • Examples: Threading, Async/Await

# # # # # # 2. PARALLELISM:
# # # # # #    • Multiple tasks run simultaneously
# # # # # #    • Requires multiple cores
# # # # # #    • About execution
# # # # # #    • Examples: Multiprocessing

# # # # # # 3. MULTIPROCESSING:
# # # # # #    • Way to achieve parallelism
# # # # # #    • Multiple processes, separate memory
# # # # # #    • Each process has own GIL
# # # # # #    • True parallelism in Python

# # # # # # 4. RELATIONSHIP:
# # # # # #    • Concurrency ≠ Parallelism
# # # # # #    • Parallelism is a subset of concurrency
# # # # # #    • You can have concurrency without parallelism
# # # # # #    • Parallelism requires concurrency structure

# # # # # # 5. IN PYTHON:
# # # # # #    • Threading: Concurrency (I/O-bound)
# # # # # #    • Multiprocessing: Parallelism (CPU-bound)
# # # # # #    • Async/Await: Concurrency (I/O-bound)
# # # # # #    • GIL limits threading parallelism

# # # # # # 6. CHOOSING:
# # # # # #    • I/O-bound → Threading or Async
# # # # # #    • CPU-bound → Multiprocessing
# # # # # #    • Many I/O tasks → Async/Await
# # # # # #    • Independent CPU tasks → Multiprocessing
# # # # # # """)

# # # # # # print("=" * 60)

# # # # # # Topic 8: Python's Data Model
# # # # # # __str__, __repr__, __eq__, __lt__, and more

# # # # # print("=" * 60)
# # # # # print("TOPIC 8: Python's Data Model (Dunder Methods)")
# # # # # print("=" * 60)

# # # # # # ========== PART 1: What are Dunder Methods? ==========
# # # # # print("\n" + "─" * 60)
# # # # # print("PART 1: What are Dunder Methods?")
# # # # # print("─" * 60)

# # # # # print("""
# # # # # Dunder Methods (Magic Methods):
# # # # #   • Special methods with double underscores (__method__)
# # # # #   • Called automatically by Python
# # # # #   • Define how objects behave with built-in operations
# # # # #   • Allow you to customize object behavior
# # # # #   • Examples: __init__, __str__, __repr__, __eq__, __add__
# # # # # """)

# # # # # # ========== PART 2: __str__ vs __repr__ ==========
# # # # # print("\n" + "─" * 60)
# # # # # print("PART 2: __str__ vs __repr__ (Most Common Interview Question!)")
# # # # # print("─" * 60)

# # # # # print("""
# # # # # __str__:
# # # # #   • User-friendly string representation
# # # # #   • Called by str() and print()
# # # # #   • For end users
# # # # #   • Should be readable

# # # # # __repr__:
# # # # #   • Developer-friendly string representation
# # # # #   • Called by repr()
# # # # #   • Should be unambiguous
# # # # #   • Ideally: can recreate object from string
# # # # #   • Fallback for __str__ if not defined
# # # # # """)

# # # # # class Person:
# # # # #     def __init__(self, name, age):
# # # # #         self.name = name
# # # # #         self.age = age
    
# # # # #     def __str__(self):
# # # # #         """User-friendly representation"""
# # # # #         return f"{self.name} is {self.age} years old"
    
# # # # #     def __repr__(self):
# # # # #         """Developer-friendly representation"""
# # # # #         return f"Person(name='{self.name}', age={self.age})"

# # # # # person = Person("Alice", 30)

# # # # # print("\n1. Using __str__ and __repr__:")
# # # # # print(f"   str(person): {str(person)}")
# # # # # print(f"   repr(person): {repr(person)}")
# # # # # print(f"   print(person): ", end="")
# # # # # print(person)

# # # # # # What happens without __str__?
# # # # # class Person2:
# # # # #     def __init__(self, name, age):
# # # # #         self.name = name
# # # # #         self.age = age
    
# # # # #     def __repr__(self):
# # # # #         return f"Person2(name='{self.name}', age={self.age})"
# # # # #     # No __str__ defined

# # # # # person2 = Person2("Bob", 25)
# # # # # print("\n2. Without __str__ (uses __repr__ as fallback):")
# # # # # print(f"   str(person2): {str(person2)}")
# # # # # print(f"   repr(person2): {repr(person2)}")
# # # # # print(f"   print(person2): ", end="")
# # # # # print(person2)

# # # # # # Best practice: __repr__ should be unambiguous
# # # # # print("\n3. Best Practice for __repr__:")
# # # # # print("   __repr__ should ideally allow object recreation:")
# # # # # print(f"   eval(repr(person)) == person: {eval(repr(person)) == person}")

# # # # # # ========== PART 3: Comparison Methods ==========
# # # # # print("\n" + "─" * 60)
# # # # # print("PART 3: Comparison Methods (__eq__, __lt__, etc.)")
# # # # # print("─" * 60)

# # # # # print("""
# # # # # Comparison Methods:
# # # # #   • __eq__: == (equality)
# # # # #   • __ne__: != (not equal)
# # # # #   • __lt__: < (less than)
# # # # #   • __le__: <= (less than or equal)
# # # # #   • __gt__: > (greater than)
# # # # #   • __ge__: >= (greater than or equal)
# # # # # """)

# # # # # class Point:
# # # # #     def __init__(self, x, y):
# # # # #         self.x = x
# # # # #         self.y = y
    
# # # # #     def __eq__(self, other):
# # # # #         """Define equality"""
# # # # #         if not isinstance(other, Point):
# # # # #             return NotImplemented
# # # # #         return self.x == other.x and self.y == other.y
    
# # # # #     def __lt__(self, other):
# # # # #         """Define less than (compare by distance from origin)"""
# # # # #         if not isinstance(other, Point):
# # # # #             return NotImplemented
# # # # #         return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)
    
# # # # #     def __repr__(self):
# # # # #         return f"Point({self.x}, {self.y})"

# # # # # p1 = Point(1, 2)
# # # # # p2 = Point(1, 2)
# # # # # p3 = Point(3, 4)

# # # # # print("\n1. Equality (__eq__):")
# # # # # print(f"   p1 = {p1}")
# # # # # print(f"   p2 = {p2}")
# # # # # print(f"   p1 == p2: {p1 == p2}")  # True
# # # # # print(f"   p1 == p3: {p1 == p3}")  # False

# # # # # print("\n2. Less Than (__lt__):")
# # # # # print(f"   p1 = {p1} (distance: {(p1.x**2 + p1.y**2)**0.5:.2f})")
# # # # # print(f"   p3 = {p3} (distance: {(p3.x**2 + p3.y**2)**0.5:.2f})")
# # # # # print(f"   p1 < p3: {p1 < p3}")  # True (p1 is closer to origin)

# # # # # # Using functools.total_ordering for convenience
# # # # # from functools import total_ordering

# # # # # @total_ordering
# # # # # class Student:
# # # # #     def __init__(self, name, score):
# # # # #         self.name = name
# # # # #         self.score = score
    
# # # # #     def __eq__(self, other):
# # # # #         return self.score == other.score
    
# # # # #     def __lt__(self, other):
# # # # #         return self.score < other.score
    
# # # # #     def __repr__(self):
# # # # #         return f"Student({self.name}, {self.score})"

# # # # # s1 = Student("Alice", 85)
# # # # # s2 = Student("Bob", 90)
# # # # # s3 = Student("Charlie", 85)

# # # # # print("\n3. Using @total_ordering (auto-generates other comparisons):")
# # # # # print(f"   s1 = {s1}")
# # # # # print(f"   s2 = {s2}")
# # # # # print(f"   s1 < s2: {s1 < s2}")
# # # # # print(f"   s1 <= s2: {s1 <= s2}")  # Auto-generated!
# # # # # print(f"   s1 > s2: {s1 > s2}")    # Auto-generated!
# # # # # print(f"   s1 >= s2: {s1 >= s2}")  # Auto-generated!
# # # # # print(f"   s1 == s3: {s1 == s3}")  # Same score

# # # # # # ========== PART 4: Arithmetic Operations ==========
# # # # # print("\n" + "─" * 60)
# # # # # print("PART 4: Arithmetic Operations")
# # # # # print("─" * 60)

# # # # # print("""
# # # # # Arithmetic Methods:
# # # # #   • __add__: + (addition)
# # # # #   • __sub__: - (subtraction)
# # # # #   • __mul__: * (multiplication)
# # # # #   • __truediv__: / (division)
# # # # #   • __mod__: % (modulo)
# # # # #   • __pow__: ** (power)
# # # # # """)

# # # # # class Vector:
# # # # #     def __init__(self, x, y):
# # # # #         self.x = x
# # # # #         self.y = y
    
# # # # #     def __add__(self, other):
# # # # #         """Vector addition"""
# # # # #         if not isinstance(other, Vector):
# # # # #             return NotImplemented
# # # # #         return Vector(self.x + other.x, self.y + other.y)
    
# # # # #     def __sub__(self, other):
# # # # #         """Vector subtraction"""
# # # # #         if not isinstance(other, Vector):
# # # # #             return NotImplemented
# # # # #         return Vector(self.x - other.x, self.y - other.y)
    
# # # # #     def __mul__(self, scalar):
# # # # #         """Scalar multiplication"""
# # # # #         if not isinstance(scalar, (int, float)):
# # # # #             return NotImplemented
# # # # #         return Vector(self.x * scalar, self.y * scalar)
    
# # # # #     def __rmul__(self, scalar):
# # # # #         """Right multiplication (scalar * vector)"""
# # # # #         return self.__mul__(scalar)
    
# # # # #     def __repr__(self):
# # # # #         return f"Vector({self.x}, {self.y})"

# # # # # v1 = Vector(1, 2)
# # # # # v2 = Vector(3, 4)

# # # # # print("\n1. Vector Operations:")
# # # # # print(f"   v1 = {v1}")
# # # # # print(f"   v2 = {v2}")
# # # # # print(f"   v1 + v2 = {v1 + v2}")
# # # # # print(f"   v2 - v1 = {v2 - v1}")
# # # # # print(f"   v1 * 3 = {v1 * 3}")
# # # # # print(f"   3 * v1 = {3 * v1}")  # Uses __rmul__

# # # # # # ========== PART 5: Container Methods ==========
# # # # # print("\n" + "─" * 60)
# # # # # print("PART 5: Container Methods (Making Objects Indexable)")
# # # # # print("─" * 60)

# # # # # print("""
# # # # # Container Methods:
# # # # #   • __len__: len() function
# # # # #   • __getitem__: [] indexing
# # # # #   • __setitem__: [] assignment
# # # # #   • __delitem__: del statement
# # # # #   • __contains__: in operator
# # # # # """)

# # # # # class ShoppingCart:
# # # # #     def __init__(self):
# # # # #         self.items = []
    
# # # # #     def add_item(self, item):
# # # # #         self.items.append(item)
    
# # # # #     def __len__(self):
# # # # #         """Called by len()"""
# # # # #         return len(self.items)
    
# # # # #     def __getitem__(self, index):
# # # # #         """Called by cart[index]"""
# # # # #         return self.items[index]
    
# # # # #     def __setitem__(self, index, value):
# # # # #         """Called by cart[index] = value"""
# # # # #         self.items[index] = value
    
# # # # #     def __delitem__(self, index):
# # # # #         """Called by del cart[index]"""
# # # # #         del self.items[index]
    
# # # # #     def __contains__(self, item):
# # # # #         """Called by 'item in cart'"""
# # # # #         return item in self.items
    
# # # # #     def __repr__(self):
# # # # #         return f"ShoppingCart({self.items})"

# # # # # cart = ShoppingCart()
# # # # # cart.add_item("Apple")
# # # # # cart.add_item("Banana")
# # # # # cart.add_item("Orange")

# # # # # print("\n1. Container Methods:")
# # # # # print(f"   cart = {cart}")
# # # # # print(f"   len(cart): {len(cart)}")
# # # # # print(f"   cart[0]: {cart[0]}")
# # # # # print(f"   cart[1] = 'Mango': ", end="")
# # # # # cart[1] = "Mango"
# # # # # print(f"{cart}")
# # # # # print(f"   'Apple' in cart: {'Apple' in cart}")
# # # # # print(f"   del cart[0]: ", end="")
# # # # # del cart[0]
# # # # # print(f"{cart}")

# # # # # # ========== PART 6: Callable Objects ==========
# # # # # print("\n" + "─" * 60)
# # # # # print("PART 6: Callable Objects (__call__)")
# # # # # print("─" * 60)

# # # # # print("""
# # # # # __call__:
# # # # #   • Makes object callable like a function
# # # # #   • Called when you use object()
# # # # #   • Useful for callable objects, decorators
# # # # # """)

# # # # # class Counter:
# # # # #     def __init__(self):
# # # # #         self.count = 0
    
# # # # #     def __call__(self):
# # # # #         """Makes Counter callable"""
# # # # #         self.count += 1
# # # # #         return self.count
    
# # # # #     def __repr__(self):
# # # # #         return f"Counter(count={self.count})"

# # # # # counter = Counter()
# # # # # print("\n1. Callable Object:")
# # # # # print(f"   counter = {counter}")
# # # # # print(f"   counter(): {counter()}")
# # # # # print(f"   counter(): {counter()}")
# # # # # print(f"   counter(): {counter()}")
# # # # # print(f"   counter = {counter}")

# # # # # # Example: Callable decorator
# # # # # class CallableDecorator:
# # # # #     def __init__(self, func):
# # # # #         self.func = func
# # # # #         self.call_count = 0
    
# # # # #     def __call__(self, *args, **kwargs):
# # # # #         self.call_count += 1
# # # # #         print(f"Function called {self.call_count} times")
# # # # #         return self.func(*args, **kwargs)

# # # # # @CallableDecorator
# # # # # def greet(name):
# # # # #     return f"Hello, {name}!"

# # # # # print("\n2. Callable Decorator:")
# # # # # print(f"   greet('Alice'): {greet('Alice')}")
# # # # # print(f"   greet('Bob'): {greet('Bob')}")

# # # # # # ========== PART 7: Context Manager Methods ==========
# # # # # print("\n" + "─" * 60)
# # # # # print("PART 7: Context Manager Methods (__enter__, __exit__)")
# # # # # print("─" * 60)

# # # # # print("""
# # # # # Context Manager Methods:
# # # # #   • __enter__: Called when entering 'with' block
# # # # #   • __exit__: Called when exiting 'with' block
# # # # #   • Used for resource management
# # # # # """)

# # # # # class FileManager:
# # # # #     def __init__(self, filename, mode):
# # # # #         self.filename = filename
# # # # #         self.mode = mode
# # # # #         self.file = None
    
# # # # #     def __enter__(self):
# # # # #         """Called when entering 'with' block"""
# # # # #         print(f"   Opening {self.filename}")
# # # # #         self.file = open(self.filename, self.mode)
# # # # #         return self.file
    
# # # # #     def __exit__(self, exc_type, exc_val, exc_tb):
# # # # #         """Called when exiting 'with' block"""
# # # # #         print(f"   Closing {self.filename}")
# # # # #         if self.file:
# # # # #             self.file.close()
# # # # #         return False  # Don't suppress exceptions

# # # # # print("\n1. Context Manager:")
# # # # # print("   with FileManager('test.txt', 'w') as f:")
# # # # # print("       f.write('Hello')")
# # # # # print("   # File automatically closed")

# # # # # # ========== PART 8: Other Important Methods ==========
# # # # # print("\n" + "─" * 60)
# # # # # print("PART 8: Other Important Dunder Methods")
# # # # # print("─" * 60)

# # # # # class Example:
# # # # #     def __init__(self, value):
# # # # #         """Constructor - called when object is created"""
# # # # #         self.value = value
# # # # #         print(f"   __init__ called: value = {value}")
    
# # # # #     def __del__(self):
# # # # #         """Destructor - called when object is deleted"""
# # # # #         print(f"   __del__ called: cleaning up {self.value}")
    
# # # # #     def __bool__(self):
# # # # #         """Called by bool() and in if statements"""
# # # # #         return bool(self.value)
    
# # # # #     def __hash__(self):
# # # # #         """Called by hash() - needed for dict keys, sets"""
# # # # #         return hash(self.value)
    
# # # # #     def __getattr__(self, name):
# # # # #         """Called when attribute doesn't exist"""
# # # # #         return f"Attribute '{name}' not found"
    
# # # # #     def __setattr__(self, name, value):
# # # # #         """Called when setting attribute"""
# # # # #         print(f"   Setting {name} = {value}")
# # # # #         super().__setattr__(name, value)

# # # # # print("\n1. __init__ and __del__:")
# # # # # obj = Example(42)
# # # # # del obj

# # # # # print("\n2. __bool__:")
# # # # # obj2 = Example(0)
# # # # # print(f"   bool(obj2): {bool(obj2)}")
# # # # # obj3 = Example(10)
# # # # # print(f"   bool(obj3): {bool(obj3)}")
# # # # # if obj3:
# # # # #     print("   obj3 is truthy")

# # # # # print("\n3. __hash__:")
# # # # # obj4 = Example(5)
# # # # # print(f"   hash(obj4): {hash(obj4)}")

# # # # # print("\n4. __getattr__:")
# # # # # obj5 = Example(1)
# # # # # print(f"   obj5.nonexistent: {obj5.nonexistent}")

# # # # # # ========== PART 9: Complete Example ==========
# # # # # print("\n" + "─" * 60)
# # # # # print("PART 9: Complete Example - Bank Account")
# # # # # print("─" * 60)

# # # # # class BankAccount:
# # # # #     def __init__(self, owner, balance=0):
# # # # #         self.owner = owner
# # # # #         self.balance = balance
    
# # # # #     def __str__(self):
# # # # #         return f"Account({self.owner}): ${self.balance:.2f}"
    
# # # # #     def __repr__(self):
# # # # #         return f"BankAccount(owner='{self.owner}', balance={self.balance})"
    
# # # # #     def __eq__(self, other):
# # # # #         if not isinstance(other, BankAccount):
# # # # #             return NotImplemented
# # # # #         return self.balance == other.balance
    
# # # # #     def __lt__(self, other):
# # # # #         if not isinstance(other, BankAccount):
# # # # #             return NotImplemented
# # # # #         return self.balance < other.balance
    
# # # # #     def __add__(self, amount):
# # # # #         """Deposit money"""
# # # # #         if not isinstance(amount, (int, float)):
# # # # #             return NotImplemented
# # # # #         return BankAccount(self.owner, self.balance + amount)
    
# # # # #     def __sub__(self, amount):
# # # # #         """Withdraw money"""
# # # # #         if not isinstance(amount, (int, float)):
# # # # #             return NotImplemented
# # # # #         return BankAccount(self.owner, self.balance - amount)
    
# # # # #     def __bool__(self):
# # # # #         """Account is truthy if balance > 0"""
# # # # #         return self.balance > 0

# # # # # account1 = BankAccount("Alice", 1000)
# # # # # account2 = BankAccount("Bob", 500)

# # # # # print("\nBank Account Example:")
# # # # # print(f"   account1 = {account1}")
# # # # # print(f"   account2 = {account2}")
# # # # # print(f"   account1 == account2: {account1 == account2}")
# # # # # print(f"   account1 < account2: {account1 < account2}")
# # # # # print(f"   account1 + 200 = {account1 + 200}")
# # # # # print(f"   bool(account1): {bool(account1)}")
# # # # # print(f"   bool(BankAccount('Empty', 0)): {bool(BankAccount('Empty', 0))}")

# # # # # # ========== SUMMARY ==========
# # # # # print("\n" + "=" * 60)
# # # # # print("SUMMARY - Key Takeaways for Interviews")
# # # # # print("=" * 60)

# # # # # print("""
# # # # # 1. DUNDER METHODS:
# # # # #    • Special methods with __method__ syntax
# # # # #    • Called automatically by Python
# # # # #    • Customize object behavior

# # # # # 2. __str__ vs __repr__:
# # # # #    • __str__: User-friendly (print, str())
# # # # #    • __repr__: Developer-friendly (repr(), debugger)
# # # # #    • __repr__ should ideally recreate object
# # # # #    • __repr__ is fallback for __str__

# # # # # 3. COMPARISON METHODS:
# # # # #    • __eq__, __lt__, __le__, __gt__, __ge__, __ne__
# # # # #    • Use @total_ordering to auto-generate others
# # # # #    • Return NotImplemented for unsupported types

# # # # # 4. ARITHMETIC METHODS:
# # # # #    • __add__, __sub__, __mul__, __truediv__, etc.
# # # # #    • __rmul__ for right-side operations
# # # # #    • Return NotImplemented for unsupported types

# # # # # 5. CONTAINER METHODS:
# # # # #    • __len__, __getitem__, __setitem__, __delitem__
# # # # #    • __contains__ for 'in' operator
# # # # #    • Make objects behave like lists/dicts

# # # # # 6. OTHER IMPORTANT:
# # # # #    • __init__: Constructor
# # # # #    • __call__: Make object callable
# # # # #    • __enter__/__exit__: Context managers
# # # # #    • __bool__: Truthiness
# # # # #    • __hash__: For dict keys, sets

# # # # # 7. BEST PRACTICES:
# # # # #    • Always implement __repr__
# # # # #    • Return NotImplemented for unsupported types
# # # # #    • __repr__ should be unambiguous
# # # # #    • Use @total_ordering for comparisons
# # # # # """)

# # # # # print("=" * 60)

# # # # # Topic 9: @staticmethod, @classmethod, and Instance Methods

# # # # print("=" * 60)
# # # # print("TOPIC 9: @staticmethod, @classmethod, and Instance Methods")
# # # # print("=" * 60)

# # # # # ========== PART 1: Instance Methods ==========
# # # # print("\n" + "─" * 60)
# # # # print("PART 1: Instance Methods (Default)")
# # # # print("─" * 60)

# # # # print("""
# # # # Instance Methods:
# # # #   • First parameter: self (instance)
# # # #   • Access instance attributes and methods
# # # #   • Access class attributes and methods
# # # #   • Called on instance: obj.method()
# # # #   • Most common type of method
# # # # """)

# # # # class Person:
# # # #     species = "Homo sapiens"  # Class attribute
    
# # # #     def __init__(self, name, age):
# # # #         self.name = name      # Instance attribute
# # # #         self.age = age
    
# # # #     # Instance method
# # # #     def introduce(self):
# # # #         """Instance method - has access to self"""
# # # #         return f"Hi, I'm {self.name}, {self.age} years old"
    
# # # #     def get_birth_year(self, current_year):
# # # #         """Instance method using instance data"""
# # # #         return current_year - self.age
    
# # # #     def is_adult(self):
# # # #         """Instance method checking instance state"""
# # # #         return self.age >= 18

# # # # person1 = Person("Alice", 25)
# # # # person2 = Person("Bob", 16)

# # # # print("\n1. Instance Methods:")
# # # # print(f"   person1.introduce(): {person1.introduce()}")
# # # # print(f"   person1.get_birth_year(2024): {person1.get_birth_year(2024)}")
# # # # print(f"   person1.is_adult(): {person1.is_adult()}")
# # # # print(f"   person2.is_adult(): {person2.is_adult()}")

# # # # # ========== PART 2: @classmethod ==========
# # # # print("\n" + "─" * 60)
# # # # print("PART 2: @classmethod")
# # # # print("─" * 60)

# # # # print("""
# # # # @classmethod:
# # # #   • First parameter: cls (class, not instance)
# # # #   • Receives class as first argument
# # # #   • Can access class attributes
# # # #   • Cannot access instance attributes directly
# # # #   • Called on class or instance: Person.method() or person.method()
# # # #   • Common use: Alternative constructors
# # # # """)

# # # # class Person:
# # # #     species = "Homo sapiens"
# # # #     population = 0
    
# # # #     def __init__(self, name, age):
# # # #         self.name = name
# # # #         self.age = age
# # # #         Person.population += 1
    
# # # #     @classmethod
# # # #     def get_population(cls):
# # # #         """Class method - works with class, not instance"""
# # # #         return f"Total population: {cls.population}"
    
# # # #     @classmethod
# # # #     def from_birth_year(cls, name, birth_year, current_year=2024):
# # # #         """Alternative constructor - common use case"""
# # # #         age = current_year - birth_year
# # # #         return cls(name, age)
    
# # # #     @classmethod
# # # #     def create_baby(cls, name):
# # # #         """Another alternative constructor"""
# # # #         return cls(name, 0)
    
# # # #     def introduce(self):
# # # #         return f"Hi, I'm {self.name}, {self.age} years old"

# # # # # Using class methods
# # # # print("\n1. Class Methods - Accessing Class Attributes:")
# # # # print(f"   Person.get_population(): {Person.get_population()}")

# # # # p1 = Person("Alice", 25)
# # # # print(f"   After creating person: {Person.get_population()}")

# # # # p2 = Person("Bob", 30)
# # # # print(f"   After creating another: {Person.get_population()}")

# # # # print("\n2. Class Methods - Alternative Constructors:")
# # # # # Create from birth year instead of age
# # # # p3 = Person.from_birth_year("Charlie", 1995)
# # # # print(f"   Person.from_birth_year('Charlie', 1995): {p3.introduce()}")

# # # # # Create a baby
# # # # p4 = Person.create_baby("David")
# # # # print(f"   Person.create_baby('David'): {p4.introduce()}")

# # # # print("\n3. Class Methods - Can be called on instance too:")
# # # # print(f"   p1.get_population(): {p1.get_population()}")
# # # # print("   (But it still receives the class, not instance)")

# # # # # ========== PART 3: @staticmethod ==========
# # # # print("\n" + "─" * 60)
# # # # print("PART 3: @staticmethod")
# # # # print("─" * 60)

# # # # print("""
# # # # @staticmethod:
# # # #   • No special first parameter (no self, no cls)
# # # #   • Cannot access instance or class directly
# # # #   • Just a regular function inside a class
# # # #   • Called on class or instance: Person.method() or person.method()
# # # #   • Common use: Utility functions related to the class
# # # # """)

# # # # class MathHelper:
# # # #     @staticmethod
# # # #     def add(a, b):
# # # #         """Static method - no self or cls"""
# # # #         return a + b
    
# # # #     @staticmethod
# # # #     def multiply(a, b):
# # # #         """Static method - just a utility function"""
# # # #         return a * b
    
# # # #     @staticmethod
# # # #     def is_even(n):
# # # #         """Static method - related to class but doesn't need instance/class"""
# # # #         return n % 2 == 0

# # # # print("\n1. Static Methods:")
# # # # print(f"   MathHelper.add(5, 3): {MathHelper.add(5, 3)}")
# # # # print(f"   MathHelper.multiply(4, 7): {MathHelper.multiply(4, 7)}")
# # # # print(f"   MathHelper.is_even(10): {MathHelper.is_even(10)}")

# # # # # Can also call on instance (but not recommended)
# # # # helper = MathHelper()
# # # # print(f"\n   helper.add(2, 3): {helper.add(2, 3)}")
# # # # print("   (Works, but not the typical way)")

# # # # # ========== PART 4: Complete Example ==========
# # # # print("\n" + "─" * 60)
# # # # print("PART 4: Complete Example - All Three Types")
# # # # print("─" * 60)

# # # # class Date:
# # # #     def __init__(self, day, month, year):
# # # #         self.day = day
# # # #         self.month = month
# # # #         self.year = year
    
# # # #     # Instance method
# # # #     def display(self):
# # # #         """Instance method - uses instance data"""
# # # #         return f"{self.day}/{self.month}/{self.year}"
    
# # # #     # Class method - alternative constructor
# # # #     @classmethod
# # # #     def from_string(cls, date_string):
# # # #         """Parse date from string format: 'DD-MM-YYYY'"""
# # # #         day, month, year = map(int, date_string.split('-'))
# # # #         return cls(day, month, year)
    
# # # #     @classmethod
# # # #     def today(cls):
# # # #         """Create Date object for today (simplified)"""
# # # #         # In real code, you'd use datetime module
# # # #         return cls(15, 3, 2024)  # Example date
    
# # # #     # Static method - utility function
# # # #     @staticmethod
# # # #     def is_leap_year(year):
# # # #         """Check if year is leap year - doesn't need instance or class"""
# # # #         return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
# # # #     @staticmethod
# # # #     def days_in_month(month, year):
# # # #         """Get number of days in month - utility function"""
# # # #         days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# # # #         if month == 2 and Date.is_leap_year(year):
# # # #             return 29
# # # #         return days[month - 1]

# # # # # Using all three types
# # # # print("\n1. Instance Method:")
# # # # date1 = Date(15, 3, 2024)
# # # # print(f"   date1.display(): {date1.display()}")

# # # # print("\n2. Class Method (Alternative Constructor):")
# # # # date2 = Date.from_string("20-12-2023")
# # # # print(f"   Date.from_string('20-12-2023'): {date2.display()}")

# # # # date3 = Date.today()
# # # # print(f"   Date.today(): {date3.display()}")

# # # # print("\n3. Static Method (Utility Function):")
# # # # print(f"   Date.is_leap_year(2024): {Date.is_leap_year(2024)}")
# # # # print(f"   Date.is_leap_year(2023): {Date.is_leap_year(2023)}")
# # # # print(f"   Date.days_in_month(2, 2024): {Date.days_in_month(2, 2024)}")
# # # # print(f"   Date.days_in_month(2, 2023): {Date.days_in_month(2, 2023)}")

# # # # # ========== PART 5: Key Differences ==========
# # # # print("\n" + "─" * 60)
# # # # print("PART 5: Key Differences - Side by Side")
# # # # print("─" * 60)

# # # # class Example:
# # # #     class_var = "I'm a class variable"
    
# # # #     def __init__(self, instance_var):
# # # #         self.instance_var = instance_var
    
# # # #     # Instance method
# # # #     def instance_method(self):
# # # #         """Has access to self (instance)"""
# # # #         return f"Instance: {self.instance_var}, Class: {self.class_var}"
    
# # # #     # Class method
# # # #     @classmethod
# # # #     def class_method(cls):
# # # #         """Has access to cls (class)"""
# # # #         return f"Class: {cls.class_var}"
# # # #         # Cannot access: self.instance_var (no self!)
    
# # # #     # Static method
# # # #     @staticmethod
# # # #     def static_method():
# # # #         """No access to self or cls"""
# # # #         return "I'm just a function"
# # # #         # Cannot access: self.instance_var or cls.class_var

# # # # obj = Example("instance value")

# # # # print("\nComparison Table:")
# # # # print("""
# # # # ┌─────────────────┬──────────────┬──────────────┬──────────────┐
# # # # │                 │ Instance     │ Class        │ Static       │
# # # # ├─────────────────┼──────────────┼──────────────┼──────────────┤
# # # # │ First Parameter │ self         │ cls          │ None         │
# # # # ├─────────────────┼──────────────┼──────────────┼──────────────┤
# # # # │ Access Instance │ ✓ Yes        │ ✗ No         │ ✗ No         │
# # # # ├─────────────────┼──────────────┼──────────────┼──────────────┤
# # # # │ Access Class    │ ✓ Yes        │ ✓ Yes        │ ✗ No         │
# # # # ├─────────────────┼──────────────┼──────────────┼──────────────┤
# # # # │ Called On       │ Instance     │ Class/Instance│ Class/Instance│
# # # # ├─────────────────┼──────────────┼──────────────┼──────────────┤
# # # # │ Use Case        │ Work with    │ Alternative  │ Utility      │
# # # # │                 │ instance data│ constructors │ functions    │
# # # # └─────────────────┴──────────────┴──────────────┴──────────────┘
# # # # """)

# # # # print("\nExamples:")
# # # # print(f"   obj.instance_method(): {obj.instance_method()}")
# # # # print(f"   Example.class_method(): {Example.class_method()}")
# # # # print(f"   Example.static_method(): {Example.static_method()}")

# # # # # ========== PART 6: When to Use Each ==========
# # # # print("\n" + "─" * 60)
# # # # print("PART 6: When to Use Each Type")
# # # # print("─" * 60)

# # # # print("""
# # # # Use INSTANCE METHODS when:
# # # #   ✓ You need to access or modify instance attributes
# # # #   ✓ Method behavior depends on instance state
# # # #   ✓ Most common case (default choice)
# # # #   ✓ Example: obj.get_name(), obj.set_age(25)

# # # # Use @classmethod when:
# # # #   ✓ You need alternative constructors
# # # #   ✓ You need to access class attributes
# # # #   ✓ Factory methods
# # # #   ✓ Example: Person.from_birth_year(), Date.today()

# # # # Use @staticmethod when:
# # # #   ✓ Utility function related to class but doesn't need instance/class
# # # #   ✓ Function could be outside class but logically belongs there
# # # #   ✓ No access to self or cls needed
# # # #   ✓ Example: MathHelper.add(), Date.is_leap_year()
# # # # """)

# # # # # ========== PART 7: Real-World Examples ==========
# # # # print("\n" + "─" * 60)
# # # # print("PART 7: Real-World Examples")
# # # # print("─" * 60)

# # # # # Example 1: Database Model
# # # # class User:
# # # #     users = []  # Class variable (simplified)
    
# # # #     def __init__(self, username, email):
# # # #         self.username = username
# # # #         self.email = email
# # # #         self.id = len(User.users) + 1
# # # #         User.users.append(self)
    
# # # #     # Instance method
# # # #     def get_profile(self):
# # # #         return f"User: {self.username} ({self.email})"
    
# # # #     # Class method - find user
# # # #     @classmethod
# # # #     def find_by_username(cls, username):
# # # #         """Find user by username - class method"""
# # # #         for user in cls.users:
# # # #             if user.username == username:
# # # #                 return user
# # # #         return None
    
# # # #     @classmethod
# # # #     def create_admin(cls):
# # # #         """Factory method - create admin user"""
# # # #         admin = cls("admin", "admin@example.com")
# # # #         return admin
    
# # # #     # Static method - validation
# # # #     @staticmethod
# # # #     def is_valid_email(email):
# # # #         """Check if email is valid - utility function"""
# # # #         return "@" in email and "." in email.split("@")[1]

# # # # print("\n1. User Management Example:")
# # # # user1 = User("alice", "alice@example.com")
# # # # user2 = User("bob", "bob@example.com")

# # # # print(f"   user1.get_profile(): {user1.get_profile()}")
# # # # print(f"   User.find_by_username('alice'): {User.find_by_username('alice').get_profile()}")
# # # # print(f"   User.is_valid_email('test@example.com'): {User.is_valid_email('test@example.com')}")
# # # # print(f"   User.is_valid_email('invalid'): {User.is_valid_email('invalid')}")

# # # # # Example 2: Configuration
# # # # class Config:
# # # #     api_key = None
# # # #     base_url = "https://api.example.com"
    
# # # #     def __init__(self, api_key):
# # # #         self.api_key = api_key
    
# # # #     # Instance method
# # # #     def get_headers(self):
# # # #         """Instance method - uses instance data"""
# # # #         return {"Authorization": f"Bearer {self.api_key}"}
    
# # # #     # Class method - load from file
# # # #     @classmethod
# # # #     def from_file(cls, filename):
# # # #         """Load config from file - alternative constructor"""
# # # #         # Simplified - in real code, read from file
# # # #         return cls("loaded_api_key")
    
# # # #     # Static method - validation
# # # #     @staticmethod
# # # #     def validate_url(url):
# # # #         """Validate URL format - utility"""
# # # #         return url.startswith("http://") or url.startswith("https://")

# # # # print("\n2. Configuration Example:")
# # # # config = Config("my_api_key")
# # # # print(f"   config.get_headers(): {config.get_headers()}")
# # # # print(f"   Config.validate_url('https://api.com'): {Config.validate_url('https://api.com')}")

# # # # # ========== PART 8: Common Mistakes ==========
# # # # print("\n" + "─" * 60)
# # # # print("PART 8: Common Mistakes")
# # # # print("─" * 60)

# # # # print("""
# # # # Mistake 1: Using @staticmethod when you need @classmethod
# # # #   ✗ @staticmethod
# # # #     def create_user(name):
# # # #         return User(name)  # Error! Can't access User class
  
# # # #   ✓ @classmethod
# # # #     def create_user(cls, name):
# # # #         return cls(name)  # Correct!

# # # # Mistake 2: Forgetting self in instance method
# # # #   ✗ def method():  # Missing self!
# # # #       return self.value
  
# # # #   ✓ def method(self):
# # # #       return self.value

# # # # Mistake 3: Using instance method when static would work
# # # #   ✗ def add(self, a, b):  # Doesn't need self!
# # # #       return a + b
  
# # # #   ✓ @staticmethod
# # # #     def add(a, b):
# # # #       return a + b

# # # # Mistake 4: Confusing when to use each
# # # #   • Need instance data? → Instance method
# # # #   • Need class or alternative constructor? → @classmethod
# # # #   • Just a utility function? → @staticmethod
# # # # """)

# # # # # ========== PART 9: Method Resolution ==========
# # # # print("\n" + "─" * 60)
# # # # print("PART 9: How Python Calls Each Method Type")
# # # # print("─" * 60)

# # # # class Demo:
# # # #     @classmethod
# # # #     def class_method(cls):
# # # #         print(f"   Called with class: {cls}")
    
# # # #     @staticmethod
# # # #     def static_method():
# # # #         print("   Static method called")

# # # # obj = Demo()

# # # # print("\n1. Class Method:")
# # # # print("   Demo.class_method():")
# # # # Demo.class_method()
# # # # print("   obj.class_method():")
# # # # obj.class_method()
# # # # print("   (Both receive the class)")

# # # # print("\n2. Static Method:")
# # # # print("   Demo.static_method():")
# # # # Demo.static_method()
# # # # print("   obj.static_method():")
# # # # obj.static_method()
# # # # print("   (Both work the same way)")

# # # # # ========== SUMMARY ==========
# # # # print("\n" + "=" * 60)
# # # # print("SUMMARY - Key Takeaways for Interviews")
# # # # print("=" * 60)

# # # # print("""
# # # # 1. INSTANCE METHODS:
# # # #    • First parameter: self
# # # #    • Access instance and class
# # # #    • Most common type
# # # #    • Called on instance: obj.method()

# # # # 2. @classmethod:
# # # #    • First parameter: cls (class)
# # # #    • Access class, not instance
# # # #    • Common use: Alternative constructors
# # # #    • Called on class or instance: Class.method()

# # # # 3. @staticmethod:
# # # #    • No special first parameter
# # # #    • No access to instance or class
# # # #    • Just a function in a class
# # # #    • Called on class or instance: Class.method()

# # # # 4. WHEN TO USE:
# # # #    • Instance: Need instance data (default choice)
# # # #    • Class: Alternative constructors, factory methods
# # # #    • Static: Utility functions related to class

# # # # 5. KEY DIFFERENCES:
# # # #    • Instance: self → instance + class access
# # # #    • Class: cls → class access only
# # # #    • Static: nothing → no access to instance/class

# # # # 6. COMMON PATTERNS:
# # # #    • from_string(), from_dict() → @classmethod
# # # #    • is_valid(), calculate() → @staticmethod
# # # #    • get_*, set_*, process_* → Instance method
# # # # """)

# # # # print("=" * 60)

# # # # # Topic 22: Iterators vs Generators
# # # # my_list = [1, 2, 3]
# # # # iterator = iter(my_list)
# # # # print(next(iterator))

# # # # Topic 22: Iterators vs Generators

# # # print("=" * 60)
# # # print("TOPIC 22: Iterators vs Generators")
# # # print("=" * 60)

# # # # ========== PART 1: Understanding Iterables ==========
# # # print("\n" + "─" * 60)
# # # print("PART 1: Iterables vs Iterators")
# # # print("─" * 60)

# # # print("\n1. Iterables (Can be iterated):")
# # # print("   • Lists, tuples, strings, dicts, sets")
# # # print("   • Have __iter__() method")

# # # my_list = [1, 2, 3]
# # # print(f"   my_list = {my_list}")

# # # # Convert to iterator
# # # iterator = iter(my_list)
# # # print(f"   iterator = iter(my_list)")
# # # print(f"   type(iterator) = {type(iterator)}")

# # # # Use next() to get items
# # # print("\n2. Using next() on Iterator:")
# # # print(f"   next(iterator) = {next(iterator)}")
# # # print(f"   next(iterator) = {next(iterator)}")
# # # print(f"   next(iterator) = {next(iterator)}")
# # # # next(iterator)  # Would raise StopIteration

# # # # ========== PART 2: Custom Iterator ==========
# # # print("\n" + "─" * 60)
# # # print("PART 2: Creating Custom Iterator")
# # # print("─" * 60)

# # # class CountDown:
# # #     """Custom iterator that counts down"""
    
# # #     def __init__(self, start):
# # #         self.current = start
    
# # #     def __iter__(self):
# # #         return self
    
# # #     def __next__(self):
# # #         if self.current <= 0:
# # #             raise StopIteration
# # #         self.current -= 1
# # #         return self.current + 1

# # # print("\n1. Custom Iterator Class:")
# # # countdown = CountDown(5)
# # # print(f"   countdown = CountDown(5)")

# # # print("   Iterating:")
# # # for num in countdown:
# # #     print(f"     {num}")

# # # # ========== PART 3: Generator Function ==========
# # # print("\n" + "─" * 60)
# # # print("PART 3: Generator Functions")
# # # print("─" * 60)

# # # def simple_generator():
# # #     """Simple generator function"""
# # #     yield 1
# # #     yield 2
# # #     yield 3

# # # print("\n1. Simple Generator:")
# # # gen = simple_generator()
# # # print(f"   gen = simple_generator()")
# # # print(f"   type(gen) = {type(gen)}")

# # # print("   Using next():")
# # # print(f"     next(gen) = {next(gen)}")
# # # print(f"     next(gen) = {next(gen)}")
# # # print(f"     next(gen) = {next(gen)}")

# # # # Generator with loop
# # # def countdown_generator(n):
# # #     """Generator that counts down"""
# # #     while n > 0:
# # #         yield n
# # #         n -= 1

# # # print("\n2. Generator with Loop:")
# # # for num in countdown_generator(5):
# # #     print(f"     {num}")

# # # # ========== PART 4: Generator Expression ==========
# # # print("\n" + "─" * 60)
# # # print("PART 4: Generator Expressions")
# # # print("─" * 60)

# # # # List comprehension (eager)
# # # squares_list = [x**2 for x in range(5)]
# # # print("\n1. List Comprehension (Eager - creates all at once):")
# # # print(f"   squares_list = {squares_list}")

# # # # Generator expression (lazy)
# # # squares_gen = (x**2 for x in range(5))
# # # print("\n2. Generator Expression (Lazy - generates on demand):")
# # # print(f"   squares_gen = {squares_gen}")
# # # print(f"   type(squares_gen) = {type(squares_gen)}")
# # # print(f"   list(squares_gen) = {list(squares_gen)}")

# # # # Memory comparison
# # # print("\n3. Memory Efficiency:")
# # # print("   List: Stores all values in memory")
# # # print("   Generator: Generates values on demand")

# # # # ========== PART 5: Practical Examples ==========
# # # print("\n" + "─" * 60)
# # # print("PART 5: Practical Examples")
# # # print("─" * 60)

# # # # Example 1: Fibonacci Generator
# # # def fibonacci_generator(n):
# # #     """Generate first n Fibonacci numbers"""
# # #     a, b = 0, 1
# # #     count = 0
# # #     while count < n:
# # #         yield a
# # #         a, b = b, a + b
# # #         count += 1

# # # print("\n1. Fibonacci Generator:")
# # # fib = fibonacci_generator(10)
# # # print(f"   First 10 Fibonacci numbers: {list(fib)}")

# # # # Example 2: Infinite Generator
# # # def infinite_counter():
# # #     """Infinite counter generator"""
# # #     count = 0
# # #     while True:
# # #         yield count
# # #         count += 1

# # # print("\n2. Infinite Generator:")
# # # counter = infinite_counter()
# # # print("   next(counter) =", next(counter))
# # # print("   next(counter) =", next(counter))
# # # print("   next(counter) =", next(counter))
# # # print("   (Can generate values forever)")

# # # # Example 3: Reading Large File
# # # def read_large_file(filename):
# # #     """Generator to read file line by line (memory efficient)"""
# # #     with open(filename, 'r') as f:
# # #         for line in f:
# # #             yield line.strip()

# # # print("\n3. File Reading Generator:")
# # # print("   def read_large_file(filename):")
# # # print("       with open(filename, 'r') as f:")
# # # print("           for line in f:")
# # # print("               yield line.strip()")
# # # print("   # Memory efficient - doesn't load entire file")

# # # # ========== PART 6: Generator vs Iterator ==========
# # # print("\n" + "─" * 60)
# # # print("PART 6: Generator vs Iterator Comparison")
# # # print("─" * 60)

# # # # Iterator approach
# # # class SquareIterator:
# # #     """Iterator that squares numbers"""
# # #     def __init__(self, n):
# # #         self.n = n
# # #         self.current = 0
    
# # #     def __iter__(self):
# # #         return self
    
# # #     def __next__(self):
# # #         if self.current >= self.n:
# # #             raise StopIteration
# # #         result = self.current ** 2
# # #         self.current += 1
# # #         return result

# # # # Generator approach
# # # def square_generator(n):
# # #     """Generator that squares numbers"""
# # #     for i in range(n):
# # #         yield i ** 2

# # # print("\n1. Iterator Approach (More Code):")
# # # iter_squares = SquareIterator(5)
# # # print(f"   list(iter_squares) = {list(iter_squares)}")

# # # print("\n2. Generator Approach (Less Code):")
# # # gen_squares = square_generator(5)
# # # print(f"   list(gen_squares) = {list(gen_squares)}")

# # # print("\n3. Key Differences:")
# # # print("   Iterator:")
# # # print("     • Requires class with __iter__ and __next__")
# # # print("     • More verbose")
# # # print("     • More control")
# # # print("   Generator:")
# # # print("     • Simple function with yield")
# # # print("     • Less code")
# # # print("     • Automatic state management")

# # # # ========== PART 7: Generator State ==========
# # # print("\n" + "─" * 60)
# # # print("PART 7: Generator State Preservation")
# # # print("─" * 60)

# # # def stateful_generator():
# # #     """Generator that maintains state"""
# # #     total = 0
# # #     for i in range(5):
# # #         total += i
# # #         yield total

# # # print("\n1. State Preservation:")
# # # gen = stateful_generator()
# # # print("   Generator remembers state between calls:")
# # # for value in gen:
# # #     print(f"     {value}")

# # # # ========== PART 8: Generator Methods ==========
# # # print("\n" + "─" * 60)
# # # print("PART 8: Generator Methods")
# # # print("─" * 60)

# # # def advanced_generator():
# # #     """Generator with send(), throw(), close()"""
# # #     value = yield "First"
# # #     while True:
# # #         value = yield f"Received: {value}"

# # # print("\n1. Generator Methods:")
# # # gen = advanced_generator()
# # # print(f"   next(gen) = {next(gen)}")
# # # print(f"   gen.send('Hello') = {gen.send('Hello')}")
# # # print(f"   gen.send('World') = {gen.send('World')}")

# # # # ========== SUMMARY ==========
# # # print("\n" + "=" * 60)
# # # print("SUMMARY - Key Takeaways")
# # # print("=" * 60)

# # # print("""
# # # 1. ITERATORS:
# # #    • Objects with __iter__() and __next__()
# # #    • Manual state management
# # #    • More control, more code

# # # 2. GENERATORS:
# # #    • Special type of iterator
# # #    • Created with yield keyword
# # #    • Automatic state management
# # #    • Memory efficient (lazy evaluation)

# # # 3. GENERATOR TYPES:
# # #    • Generator functions: def with yield
# # #    • Generator expressions: (x for x in range())

# # # 4. WHEN TO USE:
# # #    • Iterator: Complex logic, reusable class
# # #    • Generator: Simple sequences, memory efficiency

# # # 5. KEY BENEFITS:
# # #    • Lazy evaluation (generate on demand)
# # #    • Memory efficient
# # #    • Clean, readable code
# # #    • State preservation
# # # """)

# # # print("=" * 60)

# # # Context Manager
# # class FileManager:
# #     def __init__(self, filename, mode):
# #         self.filename = filename
# #         self.mode = mode
# #         self.file = None

# #     def __enter__(self):
# #         print("Opening file...")
# #         self.file = open(self.filename, self.mode)
# #         return self.file

# #     def __exit__(self, exc_type, exc_val, exc_tb):
# #         print("Closing file...")
# #         if self.file:
# #             self.file.close()
# #         if exc_type:
# #             print(f"Error occurred: {exc_type}")
# #         return False  # re-raises exception if any

# # Closure & Lambda Function
# # A. Closure
# def outer_function(message):
#     def inner_function():
#         print(f"Hello {message}")
    
#     return inner_function

# say_hello = outer_function("Sachin")
# say_hello() # Output: Message:

# # 2. Lambda
# sum = lambda x, y: x + y
# print(sum(2, 3))

