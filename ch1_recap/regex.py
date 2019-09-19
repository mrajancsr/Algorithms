"""code written for Scoville Name match to split strings into street number, street name, street type"""
import re
s = "1 HURON ST BLDG 5	"

pattern = re.compile(r"(?P<first>[(0-9 /0-9a-z)?(!@#%&)?0-9]+)"
	r" (?P<middle>[(!@#%&*a-zA-Z )?]+)"
	r" (?P<last>[a-zA-Z ]+)")
ans = pattern.search(s)
#chk = re.sub("\D","",ans.group('first'))
#print(chk)
#print(ans.group('first'))
print(ans.group('first'))
print(ans.group('middle'))
print(ans.group('last'))

def str_pattern(s):
	pattern = re.compile(r"(?P<first>[(0-9 /0-9a-z)?(!@#%&)?0-9]+)"
	r" (?P<middle>[(!@#%&*a-zA-Z )?]+)"
	r" (?P<last>[a-zA-Z ]+)")

	result = pattern.search(s)

	if result is None:
		return dict(StreetNumber=None,StreetName=None,StreetType=None)
	else:
		street_number = result.group('first')
		street_name = result.group('middle')
		street_type = result.group('last')
		return dict(StreetNumber=street_number,
			StreetName=street_name,
			StreetType=street_type)

x = str_pattern(s)
