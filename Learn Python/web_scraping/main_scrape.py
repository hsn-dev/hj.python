'''
	Scraping means parsing the content from the website and pulling out exactly what you want.

	Login to a website:
		Session is created to maintain a login info throughout web pages.
'''

import requests
from bs4 import BeautifulSoup

with requests.Session() as s:
	url = "http://192.168.1.1"
	headers = {
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
	}
	login_data = {
		'uname': 'admin',
		'passwd': "00cabd76ba7178aaeccb0ed247043cb4"
	}
	# r = s.get(url, headers=headers)
	r = s.post(url, data=login_data, headers=headers)
	
	# print(r.text)
	
	soup = BeautifulSoup(r.text, 'html.parser')

	# navi_con = soup.find_all(id='navi-connection')
	# navi_con = soup.find_all("font", token="connection")
	# result = soup.find_all(lambda tag: tag.name == 'li' and tag.get('class') == ['menu-status'])
	# print(result)

	tag = soup.find('div', id="battery_capacity")
	print(tag)

	# display tag info
	# print(type(tag))

	# display tag name
	# print(tag.name)

	# display tag
	# print(tag)

	# change will be reflected in HTML original document.
	# tag.name = "div"

	# You can access a tag’s attributes by treating the tag like a dictionary
	# print(tag['id'])

	# You can access that dictionary directly as .attrs:
	# print(tag.attrs)

	# Add or Modify tag attr
	# tag['id'] = 'newValue'

	# Remove tag attr
	# del tag['id']

	# After removing attr:
	# tag['id']
	# KeyError: 'id'
	# print(tag.get('id'))
	# None

	# The most common multi-valued attribute is class (that is, a tag can have more than one CSS class).
	# css_soup = BeautifulSoup('<p class="body strikeout"></p>')
	# css_soup.p['class']
	# ["body", "strikeout"]

	# You can use `get_attribute_list to get a value that’s always a list, whether or not it’s a multi-valued atribute:
	# css_soup.p['class']
	# ["body", "strikeout"]

	# print(tag.string)
	# print(type(tag.string))
	# <class 'bs4.element.NavigableString'>

	# unicode_string = unicode(tag.string)
	# type(unicode_string)
	# <type 'unicode'>

	# tag.string.replace_with("No longer bold")