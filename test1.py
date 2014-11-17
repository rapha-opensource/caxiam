#!/usr/bin/env python3

import re

URL = word = ""

# the next 2 while are to prevent people from inputing empty strings"

while not word:
	word = input("Enter a word: ")

while not URL:
	URL = input("Enter a URL: ")


print(word +" appears "+ str(len(re.findall(word, URL))) + " times in " + URL)
