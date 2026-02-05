# Python Interview Questions - Learning Checklist

## Core Python Fundamentals

1. [x] What are *args and **kwargs? Use-cases?
2. [x] What are Python decorators? Write a custom decorator with arguments.
3. [x] What is the difference between is vs == in Python?
4. [x] Mutable vs Immutable types — how does it affect dictionary keys?
5. [x] Explain Python's memory management (reference counting, garbage collection).
6. [x] Difference between deep copy and shallow copy?
7. [x] Explain Python's GIL (Global Interpreter Lock). How does it affect threading?
8. [x] Explain Python's data model (__str__, __repr__, __eq__, __lt__, etc.)
9. [x] What is the difference between @staticmethod, @classmethod, and instance methods?

## Python Special Attributes & Dunder Methods

10. [x] What is `__name__` in Python? How is it used?
11. [x] What are other important `__dunder__` methods? (`__init__`, `__main__`, `__file__`, `__doc__`, etc.)
12. [x] How does `if __name__ == "__main__"` work? Why is it important?

## Python Data Types

13. [x] What are Lists in Python? How do they differ from arrays?
14. [x] What are Tuples? When to use tuples vs lists?
15. [x] What are Dictionaries? How are they implemented internally?
16. [x] What are Sets? How do they differ from lists and tuples?
17. [x] What is the difference between List, Tuple, Set, and Dictionary?
18. [x] How do you create and work with Arrays in Python? (array module vs NumPy)
19. [x] What are the key differences between mutable and immutable data types?
20. [x] How do you iterate over different data types efficiently?
21. [x] What are dictionary comprehensions, list comprehensions, and set comprehensions?

## Advanced Python

22. [x] Explain Python's Iterators vs Generators. Write a generator manually.
23. [x] What are context managers? Implement with using __enter__ and __exit__.
24. [x] What is a closure in Python? How is it different from a lambda?
25. [x] How does Python implement multithreading? When to use threading vs multiprocessing?
26. [x] How does Python handle exceptions? Can you customize them?
27. [x] Explain monkey patching in Python.
28. [x] Explain the use of functools.lru_cache.
29. [x] What's the difference between @dataclass and a regular class?
30. [x] How do you enforce type checking in Python? (type hints + mypy)
31. [x] Explain the asyncio module — how does Python handle async programming?

## Django Interview Questions
32. [ ] Explain Django’s MVT architecture.
33. [ ] What is the difference between __str__ and __repr__ in Django models?
34. [ ] What are Django signals and when should you use them?
36. [ ] How does Django ORM work under the hood? Write raw SQL using the ORM.
37. [ ] How is middleware implemented in Django? Give a real-world use case.
38. [ ] Explain how Django handles sessions and cookies.
39. [ ] What is CSRF protection and how does Django enforce it?
40. [ ] How would you handle file uploads in Django?
41. [ ] Difference between null=True vs blank=True in models?
42. [ ] How to scale Django apps? (Caching, DB optimization, async views)

## Flask Interview Questions
43. [ ] How is Flask different from Django?
44. [ ] WSGI Server & GUVICORN
45. [ ] What are Flask Blueprints and why are they used?
46. [ ] How does request lifecycle work in Flask?
47. [ ] How do you implement middleware in Flask?
48. [ ] How do you secure APIs in Flask? (JWT/Auth)
49. [ ] How do you handle background jobs in Flask? (Celery, RQ)
50. [ ] What is Flask’s application context vs request context?
51. [ ] How to create custom error handlers in Flask?
52. [ ] How to handle CORS in Flask?
53. [ ] How do you deploy Flask apps (Gunicorn + Nginx)?

## FastAPI Interview Questions
54. [ ] What makes FastAPI faster than Flask and Django?
55. [ ] How does FastAPI handle data validation? (Pydantic models)
56. [ ] Difference between Depends() and regular injection in FastAPI?
57. [ ] How does FastAPI support asynchronous endpoints?
58. [ ] How to add custom middleware in FastAPI?
59. [ ] How to use background tasks in FastAPI?
60. [ ] How do you implement JWT authentication in FastAPI?
61. [ ] How does FastAPI auto-generate OpenAPI docs?
62. [ ] What are response models in FastAPI? Why are they useful?
63. [ ] How would you integrate FastAPI with a frontend (CORS, Auth, etc.)?