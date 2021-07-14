vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]

for each_vendor in vendors:
    print(each_vendor)

for vendor in vendors:
    print("Length of vendor name:", len(vendor))

print("looping over the same  list by indexes:")

for index in range(len(vendors)):
    print(vendors[index])

r = range(10)
for i in r:
    print(i * 2)

#enumerate can help itearate over the elements:

for index, element in enumerate(vendors):
    print("index: " + str(index) + ", element: " + element)