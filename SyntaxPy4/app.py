# for item in 'Python':
#     print(item)

# for item in ['David',"Paul", 'Ryan']:
#     print(item)

# for i in range(4,10): #This prints i from 4(and 4) to 10(not 10)
#     print(i)

# prices = [10,20,30]
# sum = 0;
# for i in prices:
#     sum += i
# print(sum)

# for x in range(4):
#     for y in range(3):
#         print(f'({x},{y})')

# numbers = [5,2,5,2,2]
# for x in numbers:
#     print('x' *x)

# names = ['Mike','John','Ashley','Young','Luke']
# print(names[2:4])#This prints valuse from 2 to 4 indexes

numbers = [3,5,7,9,2,6]
max = numbers[0]
for i in numbers:
    # print(i)
    if i>max:
        max = i
print(max)