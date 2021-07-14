#For regular expressions мы импортируем РЕ
 
import re

# used in this format:
#a = re.match(pattern, string, oprtional flags)

myStr = 'You can learn any programming language, whether it is Python2, Python3, Perl, Java, JavaScript, or PHP'
a = re.match('You', myStr)
print('\'a\' is ', a)
print('Find it ignoring the case of letters')
a = re.match('you', myStr, re.I)
print('\'a\' is ', a)


#a = re.search(pattern, string)
arp = '22.22.22.1     0   b4:a9:5a:ff:c8:45 VLAN#222      L'
newSearch = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*", arp)
# () - is a group of symbols. dot . is any char except a newline. plus + means previous expression 
# may repeat one or more time. ? - means no 'greedy manner' (does not include spaces like above)
# \d is a single digit
# \s any whitespace char
# {2,} - expecting 2 or more occurrences of the previous expression. Comma , means 2 or more. Without
# a comma that would be strictly 2.
# (\w)* any symbol?
print("|%s|" % newSearch.group(1))
print("|%s|" % newSearch.group(2))
print("|%s|" % newSearch.group(3))
print("|%s|" % newSearch.group(4))
print(newSearch.groups())