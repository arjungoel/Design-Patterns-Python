Indexing during Iteration:-


# Don't do this:-

index = 0
for value in collection:
    print(index, value)
    index += 1


# Nor do this:-

for index in range(len(collection)):
    value = collection[index]
    print(index, value)


# Definitely don't do this:-

index = 0
while index < len(collection):
    value = collection[index]
    print(index,value)
    index += 1

# Instead do this:-

for index, value in enumerate(collection):
    print(index, value)  # returns a tuple as the result

