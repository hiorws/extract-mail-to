#!/usr/bin/env python
# -*-coding:utf-8-*-

__author__ = 'hiorws'

"""
Simple script to extract mail address from a page source

"""

import sys
from BeautifulSoup import BeautifulSoup
import urllib2

total = len(sys.argv)
cmdargs = str(sys.argv)


def extract_from_url(url):
    try:

        email_list = []
        html_page = urllib2.urlopen(url)
        soup = BeautifulSoup(html_page)
        for link in soup.findAll('a'):
            new_link = link.get('href')
            if "mailto" in new_link:
                new_link = str(new_link)
                new_link = new_link[7:]
                email_list.append(new_link)

        return email_list
    except urllib2.URLError:
        print "Something is wrong. Check url and try again."
        sys.exit()

if total == 2 and str(sys.argv[1]) == "--url":
    url_to_extract = str(sys.argv[2])

else:
    print "sample usage:"
    print "python extract_mail.py --url http://www.ozgurkod.com"

    sys.exit(1)

mail_list = extract_from_url(url=url_to_extract)
print "Extracted e-mail address(es):"
print "#############################"
for i in range(0, len(mail_list)):
    print mail_list[i]
print "#############################"
