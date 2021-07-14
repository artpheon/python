import re

string = '22.22.22.1    0   b4:a9:5a:ff:c8:45  VLAN#222   10.57.82.13      L'
a = re.findall(r"\d\d\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", string)
# . means an escape sequence here

print(a)
print(type(a))

a = re.findall(r"(\d\d)\.(\d{2})\.([0-9][0-9])\.([0-9]{1,3})", string)
print(a)

b = re.sub(r"\d", "7", string)
print(b)

str1 = 'I enjoy learning programming languages 29.04.1997'

# \D opposite of \d - everything except for digits

result = re.search(r"\D+", str1)
print('|%s|' % result.group())

result = re.search(r"\S+", str1)
print('|%s|' % result.group())

result = re.search(r"\W+", str1)
print('|%s|' % result.group())

result = re.search(r"\AI", str1)
print('|%s|' % result.group())

result = re.findall(r"[012356789]", str1)
print(result)

result = re.findall(r"\d[^9^4]", str1)
print(result)


testStr = '+7-996-336-42-76 # this is my phone number'
result = re.sub(r'#.*$', '', testStr)
print(result)
result = re.sub(r'\D', '', testStr)
print("Ready phone number:", result)