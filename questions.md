# Python Interview Questions - Learning Checklist

## Core Python Fundamentals

1. [x] What are \*args and \*\*kwargs? Use-cases?
2. [x] What are Python decorators? Write a custom decorator with arguments.
3. [x] What is the difference between is vs == in Python?
4. [x] Mutable vs Immutable types — how does it affect dictionary keys?
5. [x] Explain Python's memory management (reference counting, garbage collection).
6. [x] Difference between deep copy and shallow copy?
7. [x] Explain Python's GIL (Global Interpreter Lock). How does it affect threading?
8. [x] Explain Python's data model (**str**, **repr**, **eq**, **lt**, etc.)
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
23. [x] What are context managers? Implement with using **enter** and **exit**.
24. [x] What is a closure in Python? How is it different from a lambda?
25. [x] How does Python implement multithreading? When to use threading vs multiprocessing?
26. [x] How does Python handle exceptions? Can you customize them?
27. [x] Explain monkey patching in Python.
28. [x] Explain the use of functools.lru_cache.
29. [x] What's the difference between @dataclass and a regular class?
30. [x] How do you enforce type checking in Python? (type hints + mypy)
31. [x] Explain the asyncio module — how does Python handle async programming?

## Django Interview Questions

32. [x] Explain Django’s MVT architecture.
33. [x] What is the difference between **str** and **repr** in Django models?
34. [x] What are Django signals and when should you use them?
35. [x] What is the use of Meta class in Django models?
36. [x] Explain the Django request-response lifecycle.
37. [x] How does Django ORM work under the hood?
38. [x] How to write raw SQL queries using Django ORM?
39. [x] Difference between null=True vs blank=True in models?
40. [x] What are related_name, on_delete, and reverse relationships in models?
41. [x] How to use custom managers in Django?
42. [x] How is middleware implemented in Django? Give a real-world use case.
43. [x] Explain Class-based vs Function-based views. When to use which?
44. [x] What are mixins? How are they useful?.
45. [x] Difference between Form and ModelForm?
46. [x] How to add custom validation to Django forms?
47. [x] How do Django serializers (with DRF) differ from regular forms?
48. [x] What is CSRF protection and how does Django enforce it?
49. [x] How does Django handle sessions and cookies?
50. [x] How to secure sensitive views and prevent unauthorized access?
51. [x] How would you handle file uploads in Django?
52. [x] Difference between MEDIA_ROOT vs STATIC_ROOT?
53. [x] How to scale Django apps? (Caching, DB optimization, async views)
54. [x] Explain Django’s caching framework — per-view, template fragment, low-level cache.
55. [x] How would you use Redis in Django for caching or background tasks?
56. [x] What are custom Django commands and how are they written?
57. [x] How does Django support async views (since v3.1)?
58. [x] When to use Celery with Django?
59. [x] Difference between select_related and prefetch_related?

## Flask Interview Questions

60. [ ] What is Flask and why is it called a microframework?
61. [ ] Compare Flask with Django — when would you choose one over the other?
62. [ ] What is the application context and request context in Flask?
63. [ ] How does Flask handle routing internally?
64. [ ] Explain Flask’s app factory pattern. Why is it useful?
65. [ ] Describe the lifecycle of a request in a Flask app.
66. [ ] What are Flask’s request and response objects? How do they work?
67. [ ] How to build RESTful APIs using Flask?
68. [ ] Compare Flask-RESTful vs Flask-classful vs writing routes manually.
69. [ ] How to implement CSRF protection in Flask?
70. [ ] What are common Flask vulnerabilities and how to mitigate them?
71. [ ] How do you securely manage user sessions in Flask?
72. [ ] How do you deploy a Flask app with Gunicorn and Nginx?
73. [ ] How to use environment variables and .env files securely?
74. [ ] How do you scale a Flask app (horizontal/vertical scaling, caching, DB pooling)?
75. [ ] How do you handle logging and monitoring in Flask apps?

## FastAPI Interview Questions

84. [ ] What is FastAPI? Why is it considered “fast”?
85. [ ] How is FastAPI different from Flask and Django?
86. [ ] What are ASGI and Uvicorn? How do they relate to FastAPI?
87. [ ] What is Pydantic and how is it used in FastAPI?
88. [ ] How does FastAPI leverage Python type hints?
89. [ ] Describe the lifecycle of a FastAPI request.
90. [ ] How does FastAPI handle path, query, and body parameters?
91. [ ] What are Depends and how does dependency injection work in FastAPI?
92. [ ] How to return custom responses and status codes?
93. [ ] How to handle headers, cookies, and form data?
94. [ ] What is the difference between BaseModel, Field, and Config in Pydantic?
95. [ ] How do you add validation rules in FastAPI using Pydantic?
96. [ ] How do you create nested models and reuse them across endpoints?
97. [ ] How do you implement JWT-based authentication in FastAPI?
98. [ ] What are OAuth2PasswordBearer and OAuth2PasswordRequestForm?
99. [ ] How does FastAPI support role-based access control (RBAC)?
100.    [ ] How to use middleware for logging, auth, or security headers?
101.    [ ] How does FastAPI handle async and sync code? When to use each?
102.    [ ] What is BackgroundTasks in FastAPI and how is it used?
103.    [ ] How to create custom dependencies with Depends()?
104.    [ ] How to use Response and Request classes to control output?
105.    [ ] How to stream large files using FastAPI?
106.    [ ] How do you test FastAPI apps using TestClient?
107.    [ ] How do you mock dependencies or DB calls during tests?
108.    [ ] How do you test async endpoints?
109.    [ ] How do you integrate SQLAlchemy with FastAPI?
110.    [ ] How to manage DB sessions per request using Depends()?
111.    [ ] Compare Tortoise ORM vs SQLAlchemy in FastAPI.
112.    [ ] How do you run background tasks in FastAPI (using BackgroundTasks)?
113.    [ ] How do you integrate Celery or RQ with FastAPI?
114.    [ ] How do you deploy FastAPI with Uvicorn and Gunicorn?
115.    [ ] What are workers in Uvicorn/Gunicorn? How do you scale?
116.    [ ] How do you use asyncpg for high-performance DB access?
117.    [ ] How to implement rate limiting in FastAPI?
118.    [ ] How do you cache API responses (e.g., using Redis)?
