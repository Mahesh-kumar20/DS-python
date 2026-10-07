d = {"name": "Mahesh",
     "age" : 24}
print(d.setdefault("name", "Ravi"))
# Mahesh
print(d.setdefault("course", "Python"))
# Python
print(d)
# {"name": "Mahesh", "course": "Python"}