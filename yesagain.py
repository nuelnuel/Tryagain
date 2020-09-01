names = ['Ninu','Calsa', 'Litus', 'Aquep']
for i, name in enumerate(names):
    print(f"name {i} is {name}")


def generate(n):
    i=0
    while i < n:
        yield i
        i += 1

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)