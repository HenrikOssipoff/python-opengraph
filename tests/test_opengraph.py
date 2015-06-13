# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from unittest import TestCase

from opengraph import OpenGraph
from threading import local
import responses

data = local()


class TestOpenGraph(TestCase):
    def setUp(self):  # NOQA
        self.test_document = """
<html><head>
<meta property="og:title" content="Test title">
</head><body></body></html>
"""

    @responses.activate
    def test_loading_from_url(self):
        url = 'http://foo.bar.com/'
        responses.add(
            responses.GET, url, body=self.test_document,
            status=200, content_type='text/html')
        og = OpenGraph(url=url)
        self.assertEqual(og.title, 'Test title')

    def test_get_attr(self):
        og = OpenGraph(html=self.test_document)
        self.assertEqual(og.title, 'Test title')
        with self.assertRaises(AttributeError):
            og.attribute_does_not_exist

    def test_contains(self):
        og = OpenGraph(html=self.test_document)
        self.assertIn('title', og)

    def test_str_repr(self):
        og = OpenGraph(html=self.test_document)
        text_of_data = og.__data__.__str__()
        self.assertEqual(str(og), text_of_data)

    @responses.activate
    def test_loading_from_url(self):
        def http_callback(request):
            # Ugly, but using thread locals in order to capture the request
            # headers in the callback, to assert that it's being set correctly
            data.headers = request.headers
            return (200, {'content-type': 'text/html'}, self.test_document)

        url = 'http://foo.bar.com/'
        useragent = 'python-opengraph/0.0'
        responses.add_callback(
            responses.GET, url, callback=http_callback,
            content_type='text/html')
        og = OpenGraph(url=url, useragent=useragent)
        headers = data.headers
        self.assertEqual(og.title, 'Test title')
        self.assertEqual(headers['user-agent'], useragent)
