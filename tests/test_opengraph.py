# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from unittest import TestCase

from opengraph import OpenGraph


class TestOpenGraph(TestCase):
    def test_tmp_test(self):
        html = (
            '<html><head><meta property="og:title" content="Test tittle">'
            '</head></html>'
        )
        og = OpenGraph(html=html)
        self.assertIsInstance(og, object)
