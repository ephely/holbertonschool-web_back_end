#!/usr/bin/env python3
"""
Unit tests for utils.access_nested_map
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Class for testing access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test access_nested_map returns the expected result
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    class TestAccessNestedMap(unittest.TestCase):
        self.assertEqual(access_nested_map(nested_map, path), expected)
        @parameterized.expand([
            ({}, ("a",), 'a'),
            ({"a": 1}, ("a", "b"), 'b')
        ])
        def test_access_nested_map_exception(self, nested_map, path, expected_key):
            """ Test that access_nested_map raises KeyError correctly
            """
            with self.assertRaises(KeyError) as cm:
                access_nested_map(nested_map, path)
            self.assertEqual(str(cm.exception), expected_key)
    
    class TestGetJson(unittest.TestCase):
        @parameterized.expand([
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ])
        def test_get_json(self, test_url, test_payload):
            """ Test that get_json returns the expected payload without making a real request """
            with patch("requests.get") as mock_get:
                mock_get.return_value.json.return_value = test_payload
                result = get_json(test_url)
                
                with self.assertRaises(KeyError) as cm:
                    mock_get.assert_called_once_with(test_url)
                self.assertEqual(str(cm.exception), test_url)
                
                self.assertEqual(result, test_payload)
