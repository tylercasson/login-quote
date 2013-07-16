# -*- coding: utf-8 -*-
# Reference: http://www.brainyquote.com/quotes/topics/topic_motivational.html

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Copyright (C) 2013 Tyler Casson. All rights reserved.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from bs4 import BeautifulSoup
import urllib2
from random import randint
import time
import os

message = ''
localtime = time.asctime(time.localtime(time.time()))


def get_quote(url):
	"""Fetches and returns a random quote
	:param url:         webpage containing quotes
	:type url:          string

	:return message:    randomly selected quote
	:type message:      string
	"""
	global message
	page1 = urllib2.urlopen(url.format('')).read()
	page2 = urllib2.urlopen(url.format('2')).read()
	page3 = urllib2.urlopen(url.format('3')).read()
	page4 = urllib2.urlopen(url.format('4')).read()
	page5 = urllib2.urlopen(url.format('5')).read()
	soup = BeautifulSoup(page1 + page2 + page3 + page4 + page5)
	bricks = soup.find_all(title='view quote')
	r = randint(0,len(bricks) - 1)
	author = soup.find_all(title='view author')
	message = bricks[r].text + "\n- " + author[r].text
	print message.replace('"', '\"')
	return message.replace('"', '\"')


def set_login_message(quote):
	"""Sets the login window's message
	:param quote:    quote to be used as the message
	:type quote:     string
	"""
	os.system('defaults write /Library/Preferences/com.apple.loginwindow LoginwindowText \"{0}\"'.format(quote))


def format(text, width):
	"""Formats the history output into a two column thing <<< WIP >>>
	:param text:               text to be formatted
	:type text:                string

	:param width:              desired width of the quote column in characters
	:type width:               integer

	:return formatted_text:    text formatted to fit within width
	:type formatted_text:      string
	"""
	formatted_text = ''
	text_list = text.replace('\n', '').split('-')
	quote_words = text_list[0].split(' ')
	author = text.split('-')
	author = (len(localtime) + 4) * ' ' + '-' + author[len(author) - 1]
	temp_text = ''
	word = 0
	line = 0
	for word in quote_words:
		if (len(temp_text) + len(word)) < width:
			# Word does fit within desired width
			temp_text += word + ' '
			if word == quote_words[len(quote_words) - 1]:
				# Word is the last word in the list
				if line == 0:
					formatted_text += 4 * ' ' + temp_text + '\n'
				else:
					formatted_text += (len(localtime) + 4) * ' ' + temp_text + '\n'
		else:
			# Word does not fit within desired width
			temp_text += word + ' '  # tack it on anyway because I'm tired and I can't see what I'm typing anymore
			if line == 0:
				formatted_text += 4 * ' ' + temp_text + '\n'
			else:
				formatted_text += (len(localtime) + 4) * ' ' + temp_text + '\n'
			temp_text = ''
			line += 1
	formatted_text += author
	return formatted_text


def write_data():
	"""Writes latest quote to the history file"""
	try:
		open('/Library/Application Support/Login Quote/login_message_history.txt', 'r')
	except Exception, e:
		os.system('mkdir /Library/Application\ Support/Login\ Quote')
	f = open('/Library/Application Support/Login Quote/login_message_history.txt', 'a')
	f.write(localtime + format(message, 50) + '\n\n')
	f.close()


set_login_message(get_quote('http://www.brainyquote.com/quotes/topics/topic_motivational{0}.html'))
write_data()
