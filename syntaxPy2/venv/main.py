# print(10 ** 2)#prints 10 squere

# print(round(2.5)) #round number to higher or lower

# import math
# print(math.ceil(2.8))#if u want to read more math functions u can type
#pyton 3 math module

#If statement
# isHot = False
# isCold = False
#
# if isHot:
#     print("Day is hot")
#     print("Dring coca-cola")
# elif isCold:
#     print("Day is cold")
#     print("Warm urself")
# else:
#     print("It's a lovely day")
# print("Enjoy ur day")

price = 100000
hasGoodCredit = True

if hasGoodCredit:
    downPayment = 0.1 * price
else:
    downPayment = 0.2 * price
print(f"Down payment: ${downPayment}")
# and, or - conditions like '||' and '&&' and 'Not'
if downPayment>1000:
    print("Down payment is > $1000")
else:
    print("Down payment is < $1000")

