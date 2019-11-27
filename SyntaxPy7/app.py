# def greatUser(name, lastname):
#     print("Hi "+name+" "+lastname)# print(f"Hi {name} {lastname}")
#     print("Welcome aboard")
#
# print("Start")
# greatUser("David", "Beckham")# greatUser(name = "Viktorija", lastname="Beckham")
# print("End")

def square(number):
    try:
        return number/number
    except ZeroDivisionError:
        return "Error with 0"
    except ValueError:
        return 0
print(square(0))




