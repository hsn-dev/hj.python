import re

'''

	-------------------------------------------------------------------------
	|  Metachar  |			             Meaning			    			|
	-------------------------------------------------------------------------
	|	 .	     | Any char except newline	 								|
	|	\d		 | Digit (0-9)							     				|
	|   \D       | Not a digit (0-9) 										|
	|	\w		 | Word character (a-z, A-Z, 0-9, underscore)				|
	|	\W		 | Not a word character										|
	|	\s		 | Whitespace (space, tab, newline)							|
	|   \S		 | Not a Whitespace											|
	|	\b		 | Word boundary (space, \n, \t) before or after text		|
	|	\B		 | Not having a word boundary				     		    |
	|	^		 | Beginning of a string									|
	|	$		 | End of a string					    					|
	|	[]		 | Matches Characters in CharacterSet (brackets)	    	|
	|	[^ ]	 | Matches Characters not in CharacterSet (brackets)	    |
	-------------------------------------------------------------------------
'''
'''
	Raw Strings:
		print('\tTab')
		print(r'\tTab')
	Output:
			Tab
		Tab
	
	[1-5]	-> range of characters
	[.-+]	-> . or - or + 
'''

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPRQSTUVWXYZ

1234567890.
Ha HaHa

321-555-4321
800.555.1234
900.555.1234
123.555-1234
321-555--4321

coreyms.com
-+_*^

cat
mat
pat
bat

Iraq is a country

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
corey@gmail.com.pk
'''
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
sentence = 'Start a class and then bring it to an end'

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)

# subbed_urls = pattern.sub(r'\2\3', urls)
# print(subbed_urls)

for match in matches:
	print(match)
# 	print(match.group(3))

## Find mobile numbers from a list of data using RegEx.

# with open('data.txt', 'r') as f:
# with open('data.txt', 'r', encoding='utf-8') as f:
# 	contents = f.read()
# 	matches = pattern.finditer(contents)		
# 	for match in matches:
# 		print(match)
 
'''
	findall() => return a list of groups in tuples 
				 if no groups in regex then a match is return
	
	pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
	matches = pattern.findall(urls)
'''

'''
	__FOR SEARCH AT THE BEGINNING OF STRING__
	
	match() => return a first match found.
	Note: If search pattern is at the beginning of the string then it will return match
		  otherwise, None
	pattern = re.compile(r'Start') => OK
	pattern = re.compile(r'class') => None
'''

'''
	__FOR SEARCH IN THE ENTIRE STRING__

	search() => return a first match found.
	pattern = re.compile(r'class') => OK
	pattern = re.compile(r'dne') => None
'''

'''
	__IGNORECASE FLAG__

	pattern = re.compile(r'start', re.IGNORECASE) => Start
	pattern = re.compile(r'start', re.I) => Start
	
	and there are many other flags ...
'''