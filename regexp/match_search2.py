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

# re.subn returns the string with replaced chars and the number of replacements

my_regex_str = '200.10.2.0 255.255.255.0 200.20.5.2 1 205 T#1 S IB 5'
a = re.search(r"(.+?) +\d\d(\d)\.([0-9]{2,})\.([0-9]{1,3})\.(\d) +(.+)1 +(\d{3}) +(\w{1})#.+S(\s+)(\w)\w +(.*)", my_regex_str)

print(a.group(0))


regex_str = "123.456.789   0 PYTHON 3"

regex = re.search(r"(.+)\s{2,}", regex_str)

print(regex.group(1))

regex = re.search(r"(.+)\s{2,}", regex_str)

print('|%s|' % regex.group(1))

regex = re.sub(r"[a-zA-Z0-9]", '%', regex_str)

print('|%s|' % regex)