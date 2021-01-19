import re
phonenumberregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phonenumberregex.search('my number is 877098-09889')
print('Phone Number found: ' + mo.group())