# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import requests


class OpenGraph(object):
    def __init__(self, url=None, html=''):
        content = html or self._fetch(url)  # NOQA

    def _fetch(self, url):
        response = requests.get(url)
        return response.text
