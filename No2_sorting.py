numbers = [8,1,5,6,4,3,9,2,7,-5]
print(numbers)
sorted = []
i=0
while i<len(numbers):
    x = min(numbers)
    sorted.append(x)
    numbers.remove(x)
print(sorted)