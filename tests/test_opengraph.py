# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from unittest import TestCase

from opengraph import OpenGraph


class TestOpenGraph(TestCase):
    def setUp(self):  # NOQA
        self.test_document = """
<html><head>
<meta property="og:title" content="Test title">
</head><body></body></html>
"""

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
