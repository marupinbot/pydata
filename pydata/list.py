#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup

class PyData:

    @classmethod
    def scraping(self):
        target_url = 'https://www.meetup.com/ja-JP/pro/pydata/#meetups'
        r = requests.get(target_url)

        soup = BeautifulSoup(r.text, 'lxml')

        group = soup.find('div', class_='chunk')
        group_title = group.find_all('div', h3='text--sectionTitle')
        print(group_title)
