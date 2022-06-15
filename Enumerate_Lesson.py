# Fully understanding Python's enumerate() instead of the range(len()) way I used to do things:
# From https://realpython.com/python-enumerate/
values = ["a", "b", "c"]

for count, value in enumerate(values):
    print(count, value)

# If you want your indices to start at 1, but still want to use enumerate:
for count, value in enumerate(values, start=1):
    print(count, value)