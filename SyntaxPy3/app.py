# weight = int(input('Weight: '))
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == 'L':
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"You are {converted} pounds")

# while condition
# i = 1
# while i <= 5:
#     print('*'*i)
#     i = i + 1
# print("Done")

# command = ""
# started = False
# while True:
#     command = input("> ")
#     if command.lower() == "start":
#         if started:
#             print("Car is allready started!")
#         else:
#             started = True
#             print("Car starter...")
#     elif command.lower() == "stop":
#         if not started:
#             print('Car is allready stopped!')
#         else:
#             started = False
#             print('Car stopped.')
#     elif command.lower() == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)
#     elif command.lower() == "quit":
#         break
#     else:
#         print("Sorry, command that u enter is not valid.")