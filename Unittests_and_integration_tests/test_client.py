#!/usr/bin/env python3
""" Unit tests for GithubOrgClient """
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """ Test GithubOrgClient.public_repos """
        test_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = test_payload

        with patch.object(GithubOrgClient, "_public_repos_url",
                          new_callable=PropertyMock) as mock_url:

            mock_url.return_value = "http://test_url.com"
            client = GithubOrgClient("test_org")

            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2"])

            mock_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Test GithubOrgClient.has_license """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3],
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration tests for GithubOrgClient """

    @classmethod
    def setUpClass(cls):
        """ Prepare the mock for requests.get before tests """
        org_url = f"https://api.github.com/orgs/{cls.org_payload['login']}"
        repos_url = cls.org_payload['repos_url']

        payloads = {
            org_url: cls.org_payload,
            repos_url: cls.repos_payload
        }

        def get_payload(url):
            """ Function to simulate requests.get(url).json() """
            if url in payloads:
                return Mock(**{'json.return_value': payloads[url]})
            return None

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """ Stop patching after tests """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Integration test for public_repos """
        client = GithubOrgClient(self.org_payload["login"])
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """ Integration test for public_repos with license """
        client = GithubOrgClient(self.org_payload["login"])
        self.assertEqual(client.public_repos(license="apache-2.0"),
                         self.apache2_repos)
