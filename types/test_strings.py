model = '2600XM'
slots = 4
ios = 12.3
str1 = "Cisco model: {}, {} WAN slots, IOS {}".format(model, slots * 2, ios)
print(str1)

str2 = "O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2"
print(str2)
print(str2[str2.find("10.11"): 15])
print(str2[5:])
print(str2[: 15])
print("\nPrinting string backwards:\n" + str2[::-1])

numbers = "0123456789"
print("Printing even numbers: " + numbers[::2] + "\nPrinting odd numbers: " + numbers[1::2])
print("Printing odd numbers lower than 7: " + numbers[1:7:2])

my_string = "a0:12:90:00:80:43"

print(my_string.split(":"))