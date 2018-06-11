#message = input('please\n')
#print(message)

n = 3
while n >= 0:
    print(n-1)
    n -= 2

def add(a, b):
    print(a+b)

add(2,3)

def testChange(num):
    num = 3
    return num

temp = 2
testChange(temp)
print(testChange(temp))
print(temp)

testList =  [1, 2, 3]
def changeList(lists):
    lists.pop()

changeList(testList)

print(testList)
