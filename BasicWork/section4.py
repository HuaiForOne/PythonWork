bicycles = ['trek', 'cannondale', 'redline', 'specialized']
for bicycle in bicycles:
    print(bicycle)
for value in range(3, 6):
    print(value)
    
numbers = list(range(2, 15, 2))
print(numbers)

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

plusone = [value+1 for value in range(3, 32, 5)]
print(plusone)
print(plusone[-2:-1])

dimensions = (4, 5)
print(dimensions)

for dimen in dimensions:
    if dimen == 4:
        print(dimen)

alien = {1 : '6666'}
print(alien[1])
alien['2'] = 7
print(alien)
alien['2'] = 3
print(alien)
del alien[1]
print(alien)
