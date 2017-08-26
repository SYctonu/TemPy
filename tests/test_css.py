# -*- coding: utf-8 -*-
"""
@author: Federico Cerchiari <federicocerchiari@gmail.com>
"""
import unittest
from copy import copy

from tempy import Css
from tempy.exceptions import WrongContentError


class TestTag(unittest.TestCase):

    def setUp(self):
        self.css_dict = {
            'html': {
                'background-color': 'lightblue'
                },
            'h1': {
                'color': 'white',
                'text-align': 'center'
                }
            }

    def test_init(self):
        # Test init from dict
        css = Css(self.css_dict)
        self.assertTrue(all(item in css.attrs['css_attrs'].items() for item in self.css_dict.items()))

        # Test init unpacked dict
        css = Css(**self.css_dict)
        self.assertTrue(all(item in css.attrs['css_attrs'].items() for item in self.css_dict.items()))

        # Test init list of dicts
        css_dict2 = {'div': {'color': 'blue'}}
        compare_dict = copy(self.css_dict)
        compare_dict.update(css_dict2)
        css = Css([self.css_dict, css_dict2])
        self.assertTrue(all(item in css.attrs['css_attrs'].items() for item in compare_dict.items()))

        # Test init generator of dicts
        css_dict2 = {'div': {'color': 'blue'}}
        compare_dict = copy(self.css_dict)
        compare_dict.update(css_dict2)
        css = Css((self.css_dict, css_dict2))
        self.assertTrue(all(item in css.attrs['css_attrs'].items() for item in compare_dict.items()))

        with self.assertRaises(WrongContentError):
            Css('test', 'wrong')

        with self.assertRaises(WrongContentError):
            Css(['test', 'wrong'])

    def test_render(self):
        expected = '<style>html { background-color: lightblue; } h1 { color: white; text-align: center; } </style>'
        css = Css(self.css_dict)
        rendered_css = css.render()
        self.assertEqual(rendered_css, expected)


if __name__ == '__main__':
    unittest.main()
