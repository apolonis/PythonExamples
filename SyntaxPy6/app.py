# customer = {
#     "name":"David Beckham",
#     "age":30,
#     "isVerified":True
# }
# # customer["name"] ---like getter
# customer["name"] = "Ryan Gigs"#Update, like setter
# print(customer["name"])

phone = input("Phone: ")
digitsMapping = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}
output = ""
for ch in phone:
    output += digitsMapping.get(ch, "!")+" "
print(output)