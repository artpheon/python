dict1 = {}
print(dict1)
print(type(dict1))
dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4"}
print(dict1)
d1 = {1: "First", 2: "Second"}
print(d1)
print(dict1["Vendor"])
dict1["RAM"] = "128"
print(dict1)
dict1["IOS"] = "14"
print(dict1)
del dict1["Model"]
print(dict1)
print(len(dict1))
print("IOS" in dict1)
print("IOsgfdhS" in dict1)
print(dict1.keys())
print(dict1.values())
dict1["RAM"] = None
print(dict1)
print(dict1.items())