line = input('Insert the first line of a random poem here : ')
length = len(line)
print('The length of your line is : ', length)
start = int(input('Initial position : '))
finish = int(input('Final position : '))
line = line[start:finish+1]
print(line)
