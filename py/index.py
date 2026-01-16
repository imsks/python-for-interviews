# # # # # # # 1. *args and **kwargs
# # # # # # def greet(name, *args, **kwargs):
# # # # # #     print(f"Hello, {name}!")

# # # # # #     if args:
# # # # # #         print(f"Additional arguments: {args}")

# # # # # #     if kwargs:
# # # # # #         print(f"Additional keyword arguments:")
# # # # # #         for key, value in kwargs.items():
# # # # # #             print(f"  {key}: {value}")

# # # # # # greet("John", "Jane", "Jim", "Jill", age=25, city="New York")
# # # # # # ## Output:
# # # # # # # Hello, John!
# # # # # # # Additional arguments: ('Jane', 'Jim', 'Jill')
# # # # # # # Additional keyword arguments:
# # # # # # #   age: 25
# # # # # # #   city: New York

# # # # # # 2. Python decorators
# # # # # def logging(func):
# # # # #     def wrapper(*args, **kwargs):
# # # # #         print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
# # # # #         result = func(*args, **kwargs)
# # # # #         print(f"Result: {result}")
# # # # #         return result
# # # # #     return wrapper

# # # # # @logging
# # # # # def add(a, b):
# # # # #     return a + b

# # # # # print(add(1, 2))
# # # # # ## Output:
# # # # # # Calling add with args: (1, 2) and kwargs: {}
# # # # # # Result: 3
# # # # # # 3

# # # # # is vs == in Python
# # # # # Topic 3: is vs == in Python

# # # # print("=" * 50)
# # # # print("TOPIC 3: is vs == in Python")
# # # # print("=" * 50)

# # # # # ========== Value Comparison (==) ==========
# # # # print("\n1. Value Comparison (==):")
# # # # a = [1, 2, 3]
# # # # b = [1, 2, 3]
# # # # print(f"a = {a}")
# # # # print(f"b = {b}")
# # # # print(f"a == b: {a == b}")      # True - same values
# # # # print(f"a is b: {a is b}")      # False - different objects in memory

# # # # # ========== Identity Comparison (is) ==========
# # # # print("\n2. Identity Comparison (is):")
# # # # c = a
# # # # print(f"c = a")
# # # # print(f"a is c: {a is c}")      # True - same object
# # # # print(f"id(a): {id(a)}")
# # # # print(f"id(c): {id(c)}")
# # # # print(f"Same id? {id(a) == id(c)}")

# # # # # ========== Integer Caching ==========
# # # # print("\n3. Integer Caching (Python optimization):")
# # # # x = 256
# # # # y = 256
# # # # print(f"x = 256, y = 256")
# # # # print(f"x is y: {x is y}")      # True (Python caches -5 to 256)

# # # # x = 257
# # # # y = 257
# # # # print(f"\nx = 257, y = 257")
# # # # print(f"x is y: {x is y}")      # False (or True - implementation dependent)
# # # # print(f"x == y: {x == y}")      # Always True

# # # # # ========== Always use 'is' for None, True, False ==========
# # # # print("\n4. Use 'is' for None, True, False:")
# # # # value = None

# # # # # Correct way
# # # # if value is None:
# # # #     print("✓ Correct: value is None")

# # # # # Works but not Pythonic
# # # # if value == None:
# # # #     print("✗ Works but not recommended")

# # # # # ========== String Interning ==========
# # # # print("\n5. String Interning:")
# # # # str1 = "hello"
# # # # str2 = "hello"
# # # # print(f"str1 = 'hello', str2 = 'hello'")
# # # # print(f"str1 is str2: {str1 is str2}")  # Usually True (interning)

# # # # str3 = "hello world"
# # # # str4 = "hello world"
# # # # print(f"\nstr3 = 'hello world', str4 = 'hello world'")
# # # # print(f"str3 is str4: {str3 is str4}")  # May be False (not always interned)
# # # # print(f"str3 == str4: {str3 == str4}")  # Always True

# # # # # ========== Practical Examples ==========
# # # # print("\n6. Practical Examples:")

# # # # def check_none(value):
# # # #     """Always use 'is' for None checks"""
# # # #     return value is None

# # # # def check_equality(a, b):
# # # #     """Use '==' for value comparison"""
# # # #     return a == b

# # # # print(f"check_none(None): {check_none(None)}")
# # # # print(f"check_equality([1,2], [1,2]): {check_equality([1,2], [1,2])}")

# # # # # Common mistake
# # # # print("\n7. Common Mistake:")
# # # # my_list = [1, 2, 3]
# # # # if my_list == None:  # Wrong! Should use 'is None'
# # # #     print("This won't execute")
# # # # else:
# # # #     print("List is not None, but this check is inefficient")

# # # # 4. Mutable vs Immutable Types
# # # # Topic 4: Mutable vs Immutable Types
# # # # How does it affect dictionary keys?

# # # print("=" * 60)
# # # print("TOPIC 4: Mutable vs Immutable Types")
# # # print("=" * 60)

# # # # ========== PART 1: Understanding Immutability ==========
# # # print("\n" + "─" * 60)
# # # print("PART 1: What are Immutable Types?")
# # # print("─" * 60)

# # # print("\nImmutable Types (CANNOT be changed after creation):")
# # # print("  • int, float, complex")
# # # print("  • str")
# # # print("  • tuple")
# # # print("  • frozenset")
# # # print("  • bool")
# # # print("  • bytes")

# # # # Example 1: Integers are immutable
# # # print("\n1. Integers (Immutable):")
# # # x = 10
# # # print(f"   x = {x}, id(x) = {id(x)}")
# # # x = x + 5  # This creates a NEW object, doesn't modify the old one
# # # print(f"   After x = x + 5:")
# # # print(f"   x = {x}, id(x) = {id(x)}")  # Different id!

# # # # Example 2: Strings are immutable
# # # print("\n2. Strings (Immutable):")
# # # name = "Python"
# # # print(f"   name = '{name}', id(name) = {id(name)}")
# # # name = name + "!"  # Creates new string object
# # # print(f"   After name = name + '!':")
# # # print(f"   name = '{name}', id(name) = {id(name)}")  # Different id!

# # # # Try to modify string (will error)
# # # # name[0] = "p"  # TypeError: 'str' object does not support item assignment

# # # # Example 3: Tuples are immutable
# # # print("\n3. Tuples (Immutable):")
# # # tup = (1, 2, 3)
# # # print(f"   tup = {tup}")
# # # # tup[0] = 10  # TypeError: 'tuple' object does not support item assignment
# # # print("   tup[0] = 10  # ERROR! Cannot modify tuple")

# # # # ========== PART 2: Understanding Mutability ==========
# # # print("\n" + "─" * 60)
# # # print("PART 2: What are Mutable Types?")
# # # print("─" * 60)

# # # print("\nMutable Types (CAN be changed after creation):")
# # # print("  • list")
# # # print("  • dict")
# # # print("  • set")
# # # print("  • custom classes")

# # # # Example 1: Lists are mutable
# # # print("\n1. Lists (Mutable):")
# # # my_list = [1, 2, 3]
# # # print(f"   my_list = {my_list}, id(my_list) = {id(my_list)}")
# # # my_list.append(4)  # Modifies the same object
# # # print(f"   After my_list.append(4):")
# # # print(f"   my_list = {my_list}, id(my_list) = {id(my_list)}")  # Same id!

# # # # Example 2: Reference behavior
# # # print("\n2. Reference Behavior (Critical!):")
# # # list1 = [1, 2, 3]
# # # list2 = list1  # Both point to the SAME object
# # # print(f"   list1 = {list1}, id(list1) = {id(list1)}")
# # # print(f"   list2 = {list2}, id(list2) = {id(list2)}")
# # # print(f"   list1 is list2: {list1 is list2}")  # True!
# # # print(f"   list1 == list2: {list1 == list2}")  # True!

# # # list2.append(4)
# # # print(f"\n   After list2.append(4):")
# # # print(f"   list1 = {list1}")  # list1 also changed!
# # # print(f"   list2 = {list2}")
# # # print(f"   Both reference the same object!")

# # # # Example 3: Dictionaries are mutable
# # # print("\n3. Dictionaries (Mutable):")
# # # my_dict = {"a": 1, "b": 2}
# # # print(f"   my_dict = {my_dict}")
# # # my_dict["c"] = 3  # Can modify
# # # print(f"   After my_dict['c'] = 3:")
# # # print(f"   my_dict = {my_dict}")

# # # # ========== PART 3: Dictionary Keys Must Be Immutable ==========
# # # print("\n" + "─" * 60)
# # # print("PART 3: Why Dictionary Keys Must Be Immutable")
# # # print("─" * 60)

# # # print("\nDictionary keys must be 'hashable' (immutable):")
# # # print("  • Dictionaries use hash tables internally")
# # # print("  • Hash of a key must remain constant")
# # # print("  • If key changes, hash changes → dictionary breaks!")

# # # # Valid dictionary keys (all immutable)
# # # valid_dict = {
# # #     "string": "value",           # String is immutable ✓
# # #     123: "integer",              # Integer is immutable ✓
# # #     (1, 2, 3): "tuple",         # Tuple is immutable ✓
# # #     frozenset([1, 2]): "frozen", # Frozenset is immutable ✓
# # #     True: "boolean",             # Bool is immutable ✓
# # # }

# # # print("\n✓ Valid dictionary keys:")
# # # for key, value in valid_dict.items():
# # #     print(f"   {key} ({type(key).__name__}): {value}")

# # # # Invalid dictionary keys (mutable)
# # # print("\n✗ Invalid dictionary keys (will cause TypeError):")
# # # print("   [1, 2, 3]  # List is mutable")
# # # print("   {1, 2, 3}  # Set is mutable")
# # # print("   {'a': 1}   # Dict is mutable") 

# # # # Uncomment to see the error:
# # # # invalid_dict = {
# # # #     [1, 2, 3]: "list"  # TypeError: unhashable type: 'list'
# # # # }

# # # # Why this matters
# # # print("\nWhy this matters:")
# # # print("  If a list could be a key:")
# # # print("    key = [1, 2]")
# # # print("    d[key] = 'value'")
# # # print("    key.append(3)  # Key changed!")
# # # print("    # Now d[key] is broken - hash changed!")

# # # # ========== PART 4: Mutable Default Argument Bug ==========
# # # print("\n" + "─" * 60)
# # # print("PART 4: The Mutable Default Argument Bug (COMMON INTERVIEW QUESTION!)")
# # # print("─" * 60)

# # # print("\n⚠️  THE BUG:")
# # # def add_item_bad(item, target_list=[]):  # DANGER: Mutable default!
# # #     """This function has a bug!"""
# # #     target_list.append(item)
# # #     return target_list

# # # print("   Bad function:")
# # # result1 = add_item_bad(1)
# # # print(f"   add_item_bad(1) → {result1}")  # [1]

# # # result2 = add_item_bad(2)
# # # print(f"   add_item_bad(2) → {result2}")  # [1, 2] ← Bug! Previous items still there!

# # # result3 = add_item_bad(3)
# # # print(f"   add_item_bad(3) → {result3}")  # [1, 2, 3] ← Keeps growing!

# # # print("\n   Why this happens:")
# # # print("   • Default arguments are evaluated ONCE when function is defined")
# # # print("   • The same list object is reused across all function calls")
# # # print("   • Modifications persist between calls!")

# # # print("\n✅ THE FIX:")
# # # def add_item_good(item, target_list=None):
# # #     """Correct: Use None as default, create new list inside."""
# # #     if target_list is None:
# # #         target_list = []
# # #     target_list.append(item)
# # #     return target_list

# # # print("   Good function:")
# # # result1 = add_item_good(1)
# # # print(f"   add_item_good(1) → {result1}")  # [1]

# # # result2 = add_item_good(2)
# # # print(f"   add_item_good(2) → {result2}")  # [2] ← Correct!

# # # result3 = add_item_good(3)
# # # print(f"   add_item_good(3) → {result3}")  # [3] ← Correct!

# # # # ========== PART 5: Function Arguments Behavior ==========
# # # print("\n" + "─" * 60)
# # # print("PART 5: How Mutability Affects Function Arguments")
# # # print("─" * 60)

# # # def modify_immutable(x):
# # #     """Immutable arguments: changes don't affect original"""
# # #     x = x + 10
# # #     print(f"   Inside function: x = {x}")

# # # def modify_mutable(lst):
# # #     """Mutable arguments: changes affect original!"""
# # #     lst.append(100)
# # #     print(f"   Inside function: lst = {lst}")

# # # # Immutable argument
# # # print("\n1. Immutable argument (int):")
# # # num = 5
# # # print(f"   Before: num = {num}")
# # # modify_immutable(num)
# # # print(f"   After: num = {num}")  # Unchanged!

# # # # Mutable argument
# # # print("\n2. Mutable argument (list):")
# # # my_list = [1, 2, 3]
# # # print(f"   Before: my_list = {my_list}")
# # # modify_mutable(my_list)
# # # print(f"   After: my_list = {my_list}")  # Changed!

# # # print("\n   Key takeaway:")
# # # print("   • Immutable: Function gets a copy (sort of)")
# # # print("   • Mutable: Function gets a reference to the same object")

# # # # ========== PART 6: Copying Mutable Objects ==========
# # # print("\n" + "─" * 60)
# # # print("PART 6: Shallow Copy vs Deep Copy")
# # # print("─" * 60)

# # # import copy

# # # # Shallow copy
# # # print("\n1. Shallow Copy (copy.copy() or list.copy()):")
# # # original = [1, 2, [3, 4]]
# # # shallow = original.copy()  # or copy.copy(original) or list(original) or original[:]

# # # print(f"   original = {original}")
# # # print(f"   shallow = {shallow}")

# # # # Modify top-level
# # # shallow[0] = 100
# # # print(f"\n   After shallow[0] = 100:")
# # # print(f"   original = {original}")  # [1, 2, [3, 4]] - unchanged
# # # print(f"   shallow = {shallow}")     # [100, 2, [3, 4]] - changed

# # # # Modify nested object
# # # shallow[2].append(5)
# # # print(f"\n   After shallow[2].append(5):")
# # # print(f"   original = {original}")  # [1, 2, [3, 4, 5]] - nested list changed!
# # # print(f"   shallow = {shallow}")    # [100, 2, [3, 4, 5]] - nested list changed!

# # # print("\n   Shallow copy:")
# # # print("   • Creates new top-level object")
# # # print("   • But nested objects are still references")

# # # # Deep copy
# # # print("\n2. Deep Copy (copy.deepcopy()):")
# # # original2 = [1, 2, [3, 4]]
# # # deep = copy.deepcopy(original2)

# # # print(f"   original2 = {original2}")
# # # print(f"   deep = {deep}")

# # # # Modify nested object
# # # deep[2].append(5)
# # # print(f"\n   After deep[2].append(5):")
# # # print(f"   original2 = {original2}")  # [1, 2, [3, 4]] - unchanged!
# # # print(f"   deep = {deep}")            # [1, 2, [3, 4, 5]] - changed

# # # print("\n   Deep copy:")
# # # print("   • Creates completely independent copy")
# # # print("   • All nested objects are also copied")

# # # # ========== PART 7: Interview Scenarios ==========
# # # print("\n" + "─" * 60)
# # # print("PART 7: Common Interview Scenarios")
# # # print("─" * 60)

# # # # Scenario 1: Tuple with mutable elements
# # # print("\n1. Tuple with Mutable Elements:")
# # # tup = ([1, 2], [3, 4])
# # # print(f"   tup = {tup}")
# # # # tup[0] = [5, 6]  # ERROR! Can't modify tuple
# # # tup[0].append(5)   # But can modify the list inside!
# # # print(f"   After tup[0].append(5):")
# # # print(f"   tup = {tup}")  # ([1, 2, 5], [3, 4])

# # # print("   • Tuple is immutable, but its contents can be mutable")
# # # print("   • You can't reassign tuple elements")
# # # print("   • But you can modify mutable elements inside")

# # # # Scenario 2: Set with immutable elements
# # # print("\n2. Set Requirements:")
# # # # Sets can only contain immutable (hashable) elements
# # # valid_set = {1, 2, 3, "hello", (4, 5)}
# # # print(f"   valid_set = {valid_set}")

# # # # Uncomment to see error:
# # # # invalid_set = {[1, 2], [3, 4]}  # TypeError: unhashable type: 'list'

# # # print("   • Sets can only contain immutable elements")
# # # print("   • Same reason as dictionary keys: must be hashable")

# # # # ========== SUMMARY ==========
# # # print("\n" + "=" * 60)
# # # print("SUMMARY - Key Takeaways for Interviews")
# # # print("=" * 60)

# # # print("""
# # # 1. IMMUTABLE TYPES:
# # #    • int, float, str, tuple, frozenset, bool, bytes
# # #    • Cannot be changed after creation
# # #    • Operations create new objects

# # # 2. MUTABLE TYPES:
# # #    • list, dict, set, custom classes
# # #    • Can be changed after creation
# # #    • Operations modify the same object

# # # 3. DICTIONARY KEYS:
# # #    • Must be immutable (hashable)
# # #    • Ensures hash remains constant
# # #    • Lists, sets, dicts cannot be keys

# # # 4. MUTABLE DEFAULT ARGUMENTS:
# # #    • NEVER use mutable defaults: def func(x=[])
# # #    • Use None instead: def func(x=None)
# # #    • Create new object inside function

# # # 5. COPYING:
# # #    • Shallow copy: copy.copy() - nested objects still referenced
# # #    • Deep copy: copy.deepcopy() - completely independent

# # # 6. FUNCTION ARGUMENTS:
# # #    • Immutable: Changes don't affect original
# # #    • Mutable: Changes affect original (pass by reference)
# # # """)

# # # print("=" * 60)

# # # 5. Python's Memory Management 
# # # Topic 5: Python's Memory Management
# # # Reference Counting & Garbage Collection

# # import sys
# # import gc

# # print("=" * 60)
# # print("TOPIC 5: Python's Memory Management")
# # print("=" * 60)

# # # ========== PART 1: Reference Counting ==========
# # print("\n" + "─" * 60)
# # print("PART 1: Reference Counting (Primary Mechanism)")
# # print("─" * 60)

# # print("""
# # Reference Counting:
# #   • Every object has a reference count
# #   • Count increases when object is referenced
# #   • Count decreases when reference is removed
# #   • Object is deleted when count reaches 0
# #   • Immediate and automatic
# # """)

# # # Example 1: Basic reference counting
# # print("\n1. Basic Reference Counting:")
# # x = [1, 2, 3]  # Object created, ref count = 1
# # print(f"   x = [1, 2, 3]")
# # print(f"   Reference count: {sys.getrefcount(x)}")  # Note: getrefcount includes its own reference

# # y = x  # Another reference, ref count = 2
# # print(f"   y = x")
# # print(f"   Reference count: {sys.getrefcount(x)}")

# # z = x  # Another reference, ref count = 3
# # print(f"   z = x")
# # print(f"   Reference count: {sys.getrefcount(x)}")

# # del y  # Remove one reference, ref count = 2
# # print(f"   del y")
# # print(f"   Reference count: {sys.getrefcount(x)}")

# # del z  # Remove another reference, ref count = 1
# # print(f"   del z")
# # print(f"   Reference count: {sys.getrefcount(x)}")

# # del x  # Remove last reference, ref count = 0 → object deleted
# # print(f"   del x")
# # print("   Object is now deleted (garbage collected)")

# # # Example 2: Function references
# # print("\n2. Function References:")
# # def get_ref_count(obj):
# #     """Function parameter creates temporary reference"""
# #     return sys.getrefcount(obj)

# # my_list = [1, 2, 3]
# # print(f"   my_list = [1, 2, 3]")
# # print(f"   Reference count: {sys.getrefcount(my_list)}")
# # print("   Note: getrefcount() adds 1 for its own parameter!")

# # # Example 3: Local scope
# # print("\n3. Local Scope:")
# # def test_function():
# #     local_var = [1, 2, 3]
# #     print(f"   Inside function: {sys.getrefcount(local_var)}")
# #     return local_var

# # result = test_function()
# # print(f"   After function returns: {sys.getrefcount(result)}")
# # print("   Local variable deleted when function exits")

# # # ========== PART 2: When Objects Are Deleted ==========
# # print("\n" + "─" * 60)
# # print("PART 2: When Are Objects Deleted?")
# # print("─" * 60)

# # print("""
# # Objects are deleted when:
# #   1. Reference count reaches 0
# #   2. Variable goes out of scope
# #   3. Explicitly deleted with 'del'
# #   4. Reassigned (old object's ref count decreases)
# # """)

# # # Example 1: Out of scope
# # print("\n1. Out of Scope:")
# # def create_object():
# #     obj = [1, 2, 3]
# #     print(f"   Created object: {obj}")
# #     return obj

# # obj = create_object()
# # print(f"   Object still exists: {obj}")
# # print("   Original 'obj' in function is deleted when function exits")

# # # Example 2: Reassignment
# # print("\n2. Reassignment:")
# # x = [1, 2, 3]
# # print(f"   x = [1, 2, 3]")
# # x = [4, 5, 6]  # Old [1,2,3] object's ref count decreases
# # print(f"   x = [4, 5, 6]")
# # print("   Old [1,2,3] object is deleted (ref count = 0)")

# # # ========== PART 3: Circular References Problem ==========
# # print("\n" + "─" * 60)
# # print("PART 3: Circular References (Reference Counting Limitation)")
# # print("─" * 60)

# # print("""
# # Circular Reference:
# #   • Object A references Object B
# #   • Object B references Object A
# #   • Reference count never reaches 0
# #   • Reference counting alone can't delete them
# #   • This is where Garbage Collection comes in!
# # """)

# # # Example: Circular reference
# # print("\n1. Creating Circular Reference:")
# # class Node:
# #     def __init__(self, value):
# #         self.value = value
# #         self.next = None
    
# #     def __repr__(self):
# #         return f"Node({self.value})"

# # # Create circular reference
# # node1 = Node(1)
# # node2 = Node(2)
# # node1.next = node2
# # node2.next = node1  # Circular!

# # print(f"   node1 = {node1}")
# # print(f"   node2 = {node2}")
# # print(f"   node1.next = {node1.next}")
# # print(f"   node2.next = {node2.next}")

# # print("\n   Even if we delete references:")
# # del node1
# # del node2
# # print("   del node1")
# # print("   del node2")
# # print("   Objects still exist in memory (circular reference)")
# # print("   Reference counting can't handle this!")

# # # ========== PART 4: Garbage Collection ==========
# # print("\n" + "─" * 60)
# # print("PART 4: Garbage Collection (Handles Circular References)")
# # print("─" * 60)

# # print("""
# # Garbage Collection (GC):
# #   • Handles circular references
# #   • Runs periodically (not immediate)
# #   • Uses cycle detection algorithm
# #   • Can be controlled manually
# #   • Slower than reference counting
# # """)

# # # Check GC status
# # print("\n1. Garbage Collection Status:")
# # print(f"   GC is enabled: {gc.isenabled()}")
# # print(f"   GC thresholds: {gc.get_threshold()}")

# # # Manual garbage collection
# # print("\n2. Manual Garbage Collection:")
# # print("   You can force GC to run:")
# # print("   gc.collect()  # Runs garbage collection")

# # # Example: Collecting circular references
# # print("\n3. Collecting Circular References:")

# # # Create circular reference
# # class Circular:
# #     def __init__(self, name):
# #         self.name = name
# #         self.ref = None

# # a = Circular("A")
# # b = Circular("B")
# # a.ref = b
# # b.ref = a  # Circular reference

# # print(f"   Created circular reference: a ↔ b")
# # print(f"   Objects before GC: {len(gc.get_objects())}")

# # # Delete references
# # del a
# # del b

# # # Force garbage collection
# # collected = gc.collect()
# # print(f"   gc.collect() returned: {collected}")
# # print("   Circular references are now cleaned up!")

# # # ========== PART 5: GC Generations ==========
# # print("\n" + "─" * 60)
# # print("PART 5: Generational Garbage Collection")
# # print("─" * 60)

# # print("""
# # Python uses Generational GC:
# #   • Generation 0: New objects (checked most frequently)
# #   • Generation 1: Survived one GC cycle
# #   • Generation 2: Survived multiple GC cycles
# #   • Older objects checked less frequently
# #   • Based on observation: most objects die young
# # """)

# # print("\nGC Thresholds (when GC runs):")
# # thresholds = gc.get_threshold()
# # print(f"   Generation 0: {thresholds[0]} allocations")
# # print(f"   Generation 1: {thresholds[1]} collections")
# # print(f"   Generation 2: {thresholds[2]} collections")

# # # ========== PART 6: Monitoring Memory ==========
# # print("\n" + "─" * 60)
# # print("PART 6: Monitoring Memory Usage")
# # print("─" * 60)

# # # Get object count
# # print("\n1. Object Count:")
# # print(f"   Total objects tracked: {len(gc.get_objects())}")

# # # Get statistics
# # print("\n2. GC Statistics:")
# # stats = gc.get_stats()
# # for i, stat in enumerate(stats):
# #     print(f"   Generation {i}:")
# #     print(f"     Collections: {stat['collections']}")
# #     print(f"     Collected: {stat['collected']}")
# #     print(f"     Uncollectable: {stat['uncollectable']}")

# # # ========== PART 7: Weak References ==========
# # print("\n" + "─" * 60)
# # print("PART 7: Weak References (Advanced)")
# # print("─" * 60)

# # import weakref

# # print("""
# # Weak References:
# #   • Don't increase reference count
# #   • Allow object to be garbage collected
# #   • Useful for caches, observers, callbacks
# # """)

# # print("\n1. Regular Reference (increases count):")
# # obj = [1, 2, 3]
# # ref = obj
# # print(f"   obj = [1, 2, 3]")
# # print(f"   ref = obj")
# # print(f"   Reference count: {sys.getrefcount(obj)}")

# # print("\n2. Weak Reference (doesn't increase count):")
# # obj2 = [4, 5, 6]
# # weak_ref = weakref.ref(obj2)
# # print(f"   obj2 = [4, 5, 6]")
# # print(f"   weak_ref = weakref.ref(obj2)")
# # print(f"   Reference count: {sys.getrefcount(obj2)}")
# # print(f"   Weak ref alive: {weak_ref() is not None}")

# # del obj2
# # print(f"   del obj2")
# # print(f"   Weak ref alive: {weak_ref() is not None}")  # Now None

# # # ========== PART 8: Memory Management Best Practices ==========
# # print("\n" + "─" * 60)
# # print("PART 8: Best Practices & Interview Tips")
# # print("─" * 60)

# # print("""
# # Best Practices:

# # 1. Let Python handle memory automatically
# #    • Reference counting handles 99% of cases
# #    • GC handles circular references

# # 2. Avoid circular references when possible
# #    • Use weak references for caches
# #    • Break cycles explicitly if needed

# # 3. Use 'del' for large objects
# #    • Helps free memory immediately
# #    • Good practice, not always necessary

# # 4. Monitor memory in production
# #    • Use tools like memory_profiler
# #    • Watch for memory leaks

# # 5. Don't disable GC unless you know what you're doing
# #    • gc.disable() stops automatic GC
# #    • Only for performance-critical code
# # """)

# # # ========== SUMMARY ==========
# # print("\n" + "=" * 60)
# # print("SUMMARY - Key Takeaways for Interviews")
# # print("=" * 60)

# # print("""
# # 1. REFERENCE COUNTING (Primary):
# #    • Every object has a reference count
# #    • Count increases with each reference
# #    • Count decreases when reference removed
# #    • Object deleted when count = 0
# #    • Immediate and automatic
# #    • Handles 99% of memory management

# # 2. GARBAGE COLLECTION (Secondary):
# #    • Handles circular references
# #    • Uses generational algorithm
# #    • Runs periodically (not immediate)
# #    • Slower than reference counting
# #    • Can be controlled manually

# # 3. CIRCULAR REFERENCES:
# #    • Object A → Object B → Object A
# #    • Reference counting can't handle
# #    • GC detects and cleans up cycles

# # 4. GENERATIONAL GC:
# #    • Generation 0, 1, 2
# #    • New objects checked more frequently
# #    • Based on "most objects die young"

# # 5. BEST PRACTICES:
# #    • Let Python handle automatically
# #    • Use 'del' for large objects
# #    • Avoid circular references when possible
# #    • Use weak references for caches
# # """)

# # print("=" * 60)

# # Topic 6: Deep Copy vs Shallow Copy

# import copy

# print("=" * 60)
# print("TOPIC 6: Deep Copy vs Shallow Copy")
# print("=" * 60)

# # ========== PART 1: Understanding Assignment ==========
# print("\n" + "─" * 60)
# print("PART 1: Regular Assignment (Reference)")
# print("─" * 60)

# print("""
# Regular Assignment (=):
#   • Creates a reference to the same object
#   • Both variables point to same memory location
#   • Changes to one affect the other
# """)

# original = [1, 2, 3]
# reference = original  # Just a reference, not a copy

# print(f"\n1. Regular Assignment:")
# print(f"   original = {original}")
# print(f"   reference = original")
# print(f"   reference = {reference}")

# reference.append(4)
# print(f"\n   After reference.append(4):")
# print(f"   original = {original}")  # Changed!
# print(f"   reference = {reference}")  # Changed!
# print(f"   id(original) == id(reference): {id(original) == id(reference)}")
# print("   ⚠️  Both point to the same object!")

# # ========== PART 2: Shallow Copy ==========
# print("\n" + "─" * 60)
# print("PART 2: Shallow Copy")
# print("─" * 60)

# print("""
# Shallow Copy:
#   • Creates a NEW top-level object
#   • Copies references to nested objects
#   • Nested objects are still shared
#   • Changes to nested objects affect both
# """)

# # Method 1: Using copy.copy()
# original_list = [1, 2, [3, 4]]
# shallow1 = copy.copy(original_list)

# # Method 2: Using list.copy() (for lists)
# shallow2 = original_list.copy()

# # Method 3: Using slicing (for lists)
# shallow3 = original_list[:]

# # Method 4: Using list() constructor
# shallow4 = list(original_list)

# print("\n1. Creating Shallow Copy (Multiple Methods):")
# print(f"   original_list = {original_list}")

# print("\n   Method 1: copy.copy()")
# print(f"   shallow1 = copy.copy(original_list)")

# print("\n   Method 2: list.copy()")
# print(f"   shallow2 = original_list.copy()")

# print("\n   Method 3: Slicing")
# print(f"   shallow3 = original_list[:]")

# print("\n   Method 4: list() constructor")
# print(f"   shallow4 = list(original_list)")

# # Test shallow copy behavior
# print("\n2. Shallow Copy Behavior:")

# # Modify top-level element
# shallow1[0] = 100
# print(f"   After shallow1[0] = 100:")
# print(f"   original_list = {original_list}")  # [1, 2, [3, 4]] - unchanged
# print(f"   shallow1 = {shallow1}")           # [100, 2, [3, 4]] - changed

# # Modify nested object
# shallow1[2].append(5)
# print(f"\n   After shallow1[2].append(5):")
# print(f"   original_list = {original_list}")  # [1, 2, [3, 4, 5]] - nested changed!
# print(f"   shallow1 = {shallow1}")           # [100, 2, [3, 4, 5]] - nested changed!

# print("\n   Key Point:")
# print("   • Top-level changes: Independent")
# print("   • Nested changes: Shared!")

# # ========== PART 3: Deep Copy ==========
# print("\n" + "─" * 60)
# print("PART 3: Deep Copy")
# print("─" * 60)

# print("""
# Deep Copy:
#   • Creates completely independent copy
#   • Recursively copies all nested objects
#   • No shared references
#   • Changes are completely independent
# """)

# original_list2 = [1, 2, [3, 4]]
# deep = copy.deepcopy(original_list2)

# print("\n1. Creating Deep Copy:")
# print(f"   original_list2 = {original_list2}")
# print(f"   deep = copy.deepcopy(original_list2)")

# # Modify top-level element
# deep[0] = 100
# print(f"\n2. After deep[0] = 100:")
# print(f"   original_list2 = {original_list2}")  # [1, 2, [3, 4]] - unchanged
# print(f"   deep = {deep}")                      # [100, 2, [3, 4]] - changed

# # Modify nested object
# deep[2].append(5)
# print(f"\n3. After deep[2].append(5):")
# print(f"   original_list2 = {original_list2}")  # [1, 2, [3, 4]] - unchanged!
# print(f"   deep = {deep}")                      # [100, 2, [3, 4, 5]] - changed

# print("\n   Key Point:")
# print("   • Top-level changes: Independent")
# print("   • Nested changes: Independent!")

# # ========== PART 4: Visual Comparison ==========
# print("\n" + "─" * 60)
# print("PART 4: Side-by-Side Comparison")
# print("─" * 60)

# # Setup
# original = [1, 2, [3, 4]]
# shallow = copy.copy(original)
# deep = copy.deepcopy(original)

# print("\nInitial State:")
# print(f"   original = {original}")
# print(f"   shallow = {shallow}")
# print(f"   deep = {deep}")

# # Modify nested list
# print("\nAfter modifying nested list:")
# shallow[2].append(5)
# deep[2].append(6)

# print(f"   original = {original}")  # [1, 2, [3, 4, 5]] - affected by shallow!
# print(f"   shallow = {shallow}")   # [1, 2, [3, 4, 5]] - same as original
# print(f"   deep = {deep}")         # [1, 2, [3, 4, 6]] - independent!

# print("\n   Summary:")
# print("   • Shallow copy: Nested objects shared → both changed")
# print("   • Deep copy: Nested objects independent → only deep changed")

# # ========== PART 5: Dictionaries ==========
# print("\n" + "─" * 60)
# print("PART 5: Shallow vs Deep Copy with Dictionaries")
# print("─" * 60)

# original_dict = {
#     "name": "Python",
#     "versions": [3.8, 3.9, 3.10],
#     "info": {"creator": "Guido", "year": 1991}
# }

# shallow_dict = copy.copy(original_dict)
# deep_dict = copy.deepcopy(original_dict)

# print("\n1. Original Dictionary:")
# print(f"   {original_dict}")

# # Modify nested list
# shallow_dict["versions"].append(3.11)
# deep_dict["versions"].append(3.12)

# print("\n2. After modifying nested list:")
# print(f"   original_dict = {original_dict}")  # versions changed!
# print(f"   shallow_dict = {shallow_dict}")   # versions changed!
# print(f"   deep_dict = {deep_dict}")         # versions independent!

# # Modify nested dict
# shallow_dict["info"]["year"] = 2024
# deep_dict["info"]["year"] = 2025

# print("\n3. After modifying nested dictionary:")
# print(f"   original_dict = {original_dict}")  # year changed!
# print(f"   shallow_dict = {shallow_dict}")   # year changed!
# print(f"   deep_dict = {deep_dict}")         # year independent!

# # ========== PART 6: Custom Objects ==========
# print("\n" + "─" * 60)
# print("PART 6: Custom Objects")
# print("─" * 60)

# class Person:
#     def __init__(self, name, friends=None):
#         self.name = name
#         self.friends = friends if friends else []
    
#     def __repr__(self):
#         return f"Person({self.name}, friends={self.friends})"

# person1 = Person("Alice", [Person("Bob")])
# person2 = copy.copy(person1)      # Shallow copy
# person3 = copy.deepcopy(person1)  # Deep copy

# print("\n1. Original Person:")
# print(f"   person1 = {person1}")

# # Modify nested list
# person2.friends.append(Person("Charlie"))
# person3.friends.append(Person("David"))

# print("\n2. After modifying friends list:")
# print(f"   person1 = {person1}")  # friends changed!
# print(f"   person2 = {person2}")  # friends changed!
# print(f"   person3 = {person3}")  # friends independent!

# # ========== PART 7: When to Use Each ==========
# print("\n" + "─" * 60)
# print("PART 7: When to Use Shallow vs Deep Copy")
# print("─" * 60)

# print("""
# Use SHALLOW COPY when:
#   ✓ Object has no nested mutable objects
#   ✓ You want faster performance
#   ✓ Nested objects can be shared
#   ✓ Flat structures (list of numbers, strings)

# Use DEEP COPY when:
#   ✓ Object has nested mutable objects
#   ✓ You need complete independence
#   ✓ Nested objects must not be shared
#   ✓ Complex nested structures
#   ✓ You're unsure (safer default)
# """)

# # Example: When shallow copy is fine
# print("\n1. Shallow Copy is Fine (Flat Structure):")
# flat_list = [1, 2, 3, 4, 5]
# shallow_flat = copy.copy(flat_list)
# shallow_flat[0] = 100
# print(f"   original = {flat_list}")      # [1, 2, 3, 4, 5]
# print(f"   shallow = {shallow_flat}")    # [100, 2, 3, 4, 5]
# print("   ✓ No nested objects, shallow copy works perfectly")

# # Example: When deep copy is needed
# print("\n2. Deep Copy is Needed (Nested Structure):")
# nested_list = [[1, 2], [3, 4], [5, 6]]
# shallow_nested = copy.copy(nested_list)
# deep_nested = copy.deepcopy(nested_list)

# shallow_nested[0].append(7)
# deep_nested[0].append(8)

# print(f"   original = {nested_list}")      # [[1, 2, 7], [3, 4], [5, 6]]
# print(f"   shallow = {shallow_nested}")    # [[1, 2, 7], [3, 4], [5, 6]]
# print(f"   deep = {deep_nested}")          # [[1, 2, 8], [3, 4], [5, 6]]
# print("   ⚠️  Shallow copy shares nested lists!")

# # ========== PART 8: Performance Comparison ==========
# print("\n" + "─" * 60)
# print("PART 8: Performance Considerations")
# print("─" * 60)

# import time

# large_nested = [[i for i in range(1000)] for _ in range(1000)]

# # Shallow copy timing
# start = time.time()
# shallow_copy = copy.copy(large_nested)
# shallow_time = time.time() - start

# # Deep copy timing
# start = time.time()
# deep_copy = copy.deepcopy(large_nested)
# deep_time = time.time() - start

# print(f"\nPerformance Test (1000x1000 nested list):")
# print(f"   Shallow copy: {shallow_time:.6f} seconds")
# print(f"   Deep copy: {deep_time:.6f} seconds")
# print(f"   Deep copy is {deep_time/shallow_time:.1f}x slower")
# print("\n   Reason: Deep copy recursively copies all nested objects")

# # ========== PART 9: Common Pitfalls ==========
# print("\n" + "─" * 60)
# print("PART 9: Common Pitfalls & Gotchas")
# print("─" * 60)

# print("\n1. Pitfall: Thinking shallow copy is independent")
# original = [1, [2, 3]]
# shallow = copy.copy(original)
# shallow[1].append(4)
# print(f"   original = {original}")  # [1, [2, 3, 4]] - changed!
# print("   ⚠️  Shallow copy shares nested objects!")

# print("\n2. Pitfall: Using = instead of copy")
# original = [1, 2, 3]
# wrong = original  # Not a copy!
# wrong.append(4)
# print(f"   original = {original}")  # [1, 2, 3, 4] - changed!
# print("   ⚠️  This is just a reference, not a copy!")

# print("\n3. Solution: Always use copy.copy() or copy.deepcopy()")
# original = [1, 2, 3]
# correct = copy.copy(original)
# correct.append(4)
# print(f"   original = {original}")  # [1, 2, 3] - unchanged!
# print("   ✓ Correct way to copy")

# # ========== SUMMARY ==========
# print("\n" + "=" * 60)
# print("SUMMARY - Key Takeaways for Interviews")
# print("=" * 60)

# print("""
# 1. SHALLOW COPY (copy.copy()):
#    • Creates new top-level object
#    • Copies references to nested objects
#    • Nested objects are shared
#    • Faster performance
#    • Use for flat structures

# 2. DEEP COPY (copy.deepcopy()):
#    • Creates completely independent copy
#    • Recursively copies all nested objects
#    • No shared references
#    • Slower performance
#    • Use for nested structures

# 3. METHODS TO CREATE COPIES:
#    • Shallow: copy.copy(), list.copy(), list[:], list()
#    • Deep: copy.deepcopy() (only method)

# 4. WHEN TO USE:
#    • Shallow: Flat objects, performance critical
#    • Deep: Nested objects, need independence

# 5. COMMON MISTAKES:
#    • Using = instead of copy
#    • Using shallow copy for nested structures
#    • Not understanding shared references
# """)

# print("=" * 60)
# Topic 7: Python's GIL (Global Interpreter Lock)
# How does it affect threading?

import threading
import time
import multiprocessing
import sys

print("=" * 60)
print("TOPIC 7: Python's GIL (Global Interpreter Lock)")
print("=" * 60)

# ========== PART 1: What is the GIL? ==========
print("\n" + "─" * 60)
print("PART 1: What is the GIL?")
print("─" * 60)

print("""
Global Interpreter Lock (GIL):
  • A mutex (lock) that protects access to Python objects
  • Only ONE thread can execute Python bytecode at a time
  • Prevents multiple threads from modifying Python objects simultaneously
  • Exists in CPython (default Python implementation)
  • Does NOT exist in Jython, IronPython, or PyPy
""")

print("\nKey Points:")
print("  • GIL is a single lock on the entire interpreter")
print("  • Only one thread can execute Python code at a time")
print("  • Other threads must wait for the GIL to be released")
print("  • This prevents race conditions in CPython's memory management")

# ========== PART 2: Why Does Python Have a GIL? ==========
print("\n" + "─" * 60)
print("PART 2: Why Does Python Have a GIL?")
print("─" * 60)

print("""
Reasons for GIL:

1. Memory Management:
   • CPython uses reference counting for memory management
   • Without GIL, multiple threads could modify ref counts simultaneously
   • This would cause memory corruption and crashes

2. C Extension Compatibility:
   • Many Python libraries are C extensions
   • GIL makes it easier to write thread-safe C extensions
   • Prevents complex locking in every C extension

3. Simplicity:
   • Simpler implementation
   • Easier to maintain
   • Prevents many concurrency bugs
""")

print("\nTrade-off:")
print("  ✓ Simpler, safer memory management")
print("  ✗ Limits true parallelism for CPU-bound tasks")

# ========== PART 3: GIL and CPU-Bound Tasks ==========
print("\n" + "─" * 60)
print("PART 3: GIL Impact on CPU-Bound Tasks")
print("─" * 60)

print("""
CPU-Bound Task Example:
  • Tasks that do heavy computation
  • Multiple threads DON'T help (GIL prevents parallel execution)
  • Threads take turns, not truly parallel
""")

def cpu_bound_task(n):
    """CPU-intensive task"""
    count = 0
    for i in range(n):
        count += i ** 2
    return count

# Sequential execution
print("\n1. Sequential Execution (Baseline):")
start = time.time()
result1 = cpu_bound_task(10000000)
result2 = cpu_bound_task(10000000)
sequential_time = time.time() - start
print(f"   Time: {sequential_time:.4f} seconds")

# Threaded execution (won't be faster!)
print("\n2. Threaded Execution (GIL Limits Parallelism):")
start = time.time()

def run_task():
    return cpu_bound_task(10000000)

thread1 = threading.Thread(target=run_task)
thread2 = threading.Thread(target=run_task)

thread1.start()
thread2.start()
thread1.join()
thread2.join()

threaded_time = time.time() - start
print(f"   Time: {threaded_time:.4f} seconds")
print(f"   Speedup: {sequential_time/threaded_time:.2f}x")
print("   ⚠️  Threading doesn't help CPU-bound tasks due to GIL!")

# ========== PART 4: GIL and I/O-Bound Tasks ==========
print("\n" + "─" * 60)
print("PART 4: GIL and I/O-Bound Tasks (Threading WORKS!)")
print("─" * 60)

print("""
I/O-Bound Task Example:
  • Tasks that wait for I/O (network, disk, etc.)
  • Threads release GIL during I/O operations
  • Multiple threads CAN run concurrently
  • Threading IS beneficial here!
""")

def io_bound_task(duration):
    """Simulate I/O operation (waiting)"""
    time.sleep(duration)
    return f"Completed after {duration}s"

# Sequential execution
print("\n1. Sequential I/O Execution:")
start = time.time()
result1 = io_bound_task(1)
result2 = io_bound_task(1)
sequential_io_time = time.time() - start
print(f"   Time: {sequential_io_time:.4f} seconds")

# Threaded execution (WILL be faster!)
print("\n2. Threaded I/O Execution:")
start = time.time()

results = []
def run_io_task(duration):
    results.append(io_bound_task(duration))

thread1 = threading.Thread(target=run_io_task, args=(1,))
thread2 = threading.Thread(target=run_io_task, args=(1,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

threaded_io_time = time.time() - start
print(f"   Time: {threaded_io_time:.4f} seconds")
print(f"   Speedup: {sequential_io_time/threaded_io_time:.2f}x")
print("   ✓ Threading helps I/O-bound tasks!")

# ========== PART 5: When GIL is Released ==========
print("\n" + "─" * 60)
print("PART 5: When Does the GIL Get Released?")
print("─" * 60)

print("""
GIL is Released During:
  1. I/O Operations:
     • File operations (read/write)
     • Network operations (socket send/receive)
     • time.sleep()
     • Database queries

  2. C Extensions:
     • NumPy operations (can release GIL)
     • Image processing libraries
     • Some C extensions explicitly release GIL

  3. After Certain Bytecode Instructions:
     • Python periodically switches threads
     • After N bytecode instructions
     • Allows other threads to run
""")

print("\nGIL is NOT Released During:")
print("  • Pure Python computation")
print("  • Most Python operations")
print("  • List comprehensions")
print("  • Mathematical operations")

# ========== PART 6: Threading vs Multiprocessing ==========
print("\n" + "─" * 60)
print("PART 6: Threading vs Multiprocessing")
print("─" * 60)

print("""
Threading (with GIL):
  ✓ Good for I/O-bound tasks
  ✗ Not good for CPU-bound tasks
  ✓ Shared memory (easier data sharing)
  ✓ Lower overhead

Multiprocessing (no GIL):
  ✓ Good for CPU-bound tasks
  ✓ True parallelism (separate processes)
  ✗ Separate memory (harder data sharing)
  ✗ Higher overhead
""")

def cpu_intensive(n):
    """CPU-intensive task"""
    total = 0
    for i in range(n):
        total += i ** 2
    return total

# Multiprocessing example (commented to avoid issues in some environments)
print("\n1. Multiprocessing for CPU-Bound Tasks:")
print("   Each process has its own Python interpreter")
print("   Each process has its own GIL")
print("   True parallelism across processes")
print("   Use multiprocessing for CPU-bound tasks!")

# Example structure (not executed to avoid issues)
print("""
   Example:
   from multiprocessing import Process
   
   def worker(n):
       return cpu_intensive(n)
   
   p1 = Process(target=worker, args=(10000000,))
   p2 = Process(target=worker, args=(10000000,))
   p1.start()
   p2.start()
   p1.join()
   p2.join()
   # This WILL run in parallel!
""")

# ========== PART 7: Real-World Examples ==========
print("\n" + "─" * 60)
print("PART 7: Real-World Use Cases")
print("─" * 60)

print("""
Use Threading For:
  ✓ Web scraping (I/O-bound)
  ✓ Downloading files (I/O-bound)
  ✓ API calls (I/O-bound)
  ✓ Database queries (I/O-bound)
  ✓ File processing with I/O (I/O-bound)

Use Multiprocessing For:
  ✓ Image processing (CPU-bound)
  ✓ Data analysis (CPU-bound)
  ✓ Scientific computations (CPU-bound)
  ✓ Video encoding (CPU-bound)
  ✓ Machine learning training (CPU-bound)
""")

# Example: Web scraping with threading
print("\n1. Example: Web Scraping (Threading is Good):")
print("""
   import requests
   import threading
   
   urls = ['url1', 'url2', 'url3']
   
   def fetch(url):
       response = requests.get(url)  # I/O operation
       return response.text
   
   threads = []
   for url in urls:
       t = threading.Thread(target=fetch, args=(url,))
       t.start()
       threads.append(t)
   
   # Threading helps because requests.get() releases GIL
   """)

# Example: Image processing with multiprocessing
print("\n2. Example: Image Processing (Multiprocessing is Better):")
print("""
   from multiprocessing import Pool
   from PIL import Image
   
   def process_image(image_path):
       img = Image.open(image_path)
       # CPU-intensive operations
       return img.filter(ImageFilter.BLUR)
   
   with Pool() as pool:
       results = pool.map(process_image, image_paths)
   
   # Multiprocessing helps because it's CPU-bound
   """)

# ========== PART 8: GIL Details ==========
print("\n" + "─" * 60)
print("PART 8: GIL Technical Details")
print("─" * 60)

print("""
GIL Behavior:
  • Thread acquires GIL before executing Python bytecode
  • Thread releases GIL after certain operations
  • Other threads compete for GIL
  • Context switching happens periodically

GIL Switching:
  • Happens after N bytecode instructions (default: 100)
  • Can be controlled with sys.setswitchinterval()
  • Threads voluntarily release GIL during I/O
""")

print(f"\nCurrent GIL Switch Interval:")
print(f"   {sys.getswitchinterval()} seconds")
print("   (Can be changed with sys.setswitchinterval())")

# ========== PART 9: Common Misconceptions ==========
print("\n" + "─" * 60)
print("PART 9: Common Misconceptions")
print("─" * 60)

print("""
Misconception 1: "Python can't do multithreading"
  ✗ Wrong! Python CAN do multithreading
  ✓ It's just limited for CPU-bound tasks
  ✓ Threading works great for I/O-bound tasks

Misconception 2: "GIL makes Python slow"
  ✗ GIL doesn't make Python inherently slow
  ✓ GIL limits parallelism for CPU-bound tasks
  ✓ For I/O-bound tasks, GIL doesn't matter

Misconception 3: "Threading is useless in Python"
  ✗ Wrong! Threading is useful for I/O-bound tasks
  ✓ Web servers, file processing, network I/O
  ✓ Threading is the right choice for these

Misconception 4: "Multiprocessing is always better"
  ✗ Wrong! Use threading for I/O-bound tasks
  ✓ Use multiprocessing for CPU-bound tasks
  ✓ Choose based on task type
""")

# ========== PART 10: How to Work Around GIL ==========
print("\n" + "─" * 60)
print("PART 10: Working Around the GIL")
print("─" * 60)

print("""
Solutions for CPU-Bound Tasks:

1. Multiprocessing:
   • Separate processes, separate GILs
   • True parallelism
   • Best for CPU-bound tasks

2. C Extensions:
   • Write CPU-intensive code in C
   • Release GIL in C code
   • NumPy, SciPy do this

3. Alternative Implementations:
   • Jython (no GIL, but slower)
   • IronPython (no GIL, but slower)
   • PyPy (has GIL, but faster)

4. Async/Await:
   • For I/O-bound tasks
   • Single-threaded but efficient
   • asyncio module
""")

# ========== SUMMARY ==========
print("\n" + "=" * 60)
print("SUMMARY - Key Takeaways for Interviews")
print("=" * 60)

print("""
1. WHAT IS GIL:
   • Global Interpreter Lock in CPython
   • Only one thread executes Python bytecode at a time
   • Prevents race conditions in memory management

2. WHY GIL EXISTS:
   • Simplifies memory management (reference counting)
   • Makes C extensions easier to write
   • Prevents many concurrency bugs

3. GIL IMPACT:
   • CPU-bound tasks: Threading doesn't help (use multiprocessing)
   • I/O-bound tasks: Threading works great (GIL released during I/O)

4. THREADING VS MULTIPROCESSING:
   • Threading: I/O-bound tasks, shared memory, lower overhead
   • Multiprocessing: CPU-bound tasks, separate memory, true parallelism

5. WHEN GIL IS RELEASED:
   • During I/O operations (file, network, sleep)
   • In C extensions that explicitly release it
   • Periodically after N bytecode instructions

6. BEST PRACTICES:
   • Use threading for I/O-bound tasks
   • Use multiprocessing for CPU-bound tasks
   • Use asyncio for async I/O operations
   • Don't fight the GIL, work with it!
""")

print("=" * 60)