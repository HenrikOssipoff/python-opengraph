# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import re

import requests
from bs4 import BeautifulSoup


class OpenGraph(object):
    useragent = None
    __data__ = {}

    def __init__(self, url=None, html=None, useragent=None):
        if useragent:
            self.useragent = useragent
        content = html or self._fetch(url)
        self._parse(content)

    def __contains__(self, item):
        return item in self.__data__

    def __getattr__(self, name):
        if name in self.__data__:
            return self.__data__[name]
        raise AttributeError(
            'Open Graph object has no attribute "{}"'.format(name))

    def __repr__(self):
        return self.__data__.__str__()

    def __str__(self):
        return self.__repr__()

    def _fetch(self, url):
        headers = {}
        if self.useragent:
            headers = {
                'user-agent': self.useragent
            }
        response = requests.get(url, headers=headers)
        return response.text

    def _parse(self, html):
        doc = BeautifulSoup(html)
        ogs = doc.html.head.findAll(property=re.compile(r'^og'))

        for og in ogs:
            if og.has_attr('content'):
                self.__data__[og['property'][3:]] = og['content']
