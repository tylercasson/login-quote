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
import random
import time
import os

message = ''


"""Fetches and returns a random quote

:param url:      webpage containing quotes
:type url:       string

:return message: randomly selected quote
:type message:   string

"""
def get_quote(url):
	global message
	page1 = urllib2.urlopen(url.format('')).read()
	page2 = urllib2.urlopen(url.format('2')).read()
	page3 = urllib2.urlopen(url.format('3')).read()
	page4 = urllib2.urlopen(url.format('4')).read()
	page5 = urllib2.urlopen(url.format('5')).read()
	soup = BeautifulSoup(page1 + page2 + page3 + page4 + page5)
	bricks = soup.find_all(title='view quote')
	r = random.randint(0,len(bricks))
	author = soup.find_all(title='view author')
	message = bricks[r].text + "\n-" + author[r].text
	#message = choice(bricks).text
	print message.replace('"', '\"')
	return message.replace('"', '\"')


"""Sets the login window's message

:param quote:      quote to be used as the message
:type quote:       string

"""
def set_login_message(quote):
	os.system('defaults write /Library/Preferences/com.apple.loginwindow LoginwindowText \"{0}\"'.format(quote))


"""Writes latest quote to the history file

"""
def write_data():
	localtime = time.asctime(time.localtime(time.time()))
	try:
		open('/Library/Application Support/Login Quote/login_message_history.txt', 'r')
	except Exception, e:
		os.system('mkdir /Library/Application\ Support/Login\ Quote')
	f = open('/Library/Application Support/Login Quote/login_message_history.txt', 'a')
	f.write(localtime + '     ' + message + '\n')
	f.close()


set_login_message(get_quote('http://www.brainyquote.com/quotes/topics/topic_motivational{0}.html'))
write_data()
