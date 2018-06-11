with open('pinum.txt') as file_pi:
 #   contents = file_pi.read()
    contentslist = file_pi.readlines()
    
print(contentslist)

try:
    with open('writetest.txt', w) as file_w:
        file_w.write('1111111\n')
        file_w.write('2222222\n')
except:
    print('error')
else:
    print('yes')

title = 'a, b ,c'
print((title.split()))

import json
numbers = [1,2,3,4]
filename = 'numbers.json'
with open(filename, 'w') as filejson:
    json.dump(numbers, filejson)
