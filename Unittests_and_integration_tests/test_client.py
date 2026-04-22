#!/usr/bin/env python3
""" Unit tests for GithubOrgClient """
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Tests for GithubOrgClient class """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """ Test GithubOrgClient.org returns correct value """
        client = GithubOrgClient(org_name)
        client.org
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """ Test GithubOrgClient._public_repos_url """
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "test_url"}
            client = GithubOrgClient("test_org")
            self.assertEqual(client._public_repos_url, "test_url")
