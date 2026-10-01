#****************************************************************
#                           Libraries
#****************************************************************

import unittest
import requests
from unittest.mock import patch

from src.api import newsapi

#****************************************************************
#                           Class
#****************************************************************
class TestCheckURLs(unittest.TestCase):

    @patch("api.newsapi.requests.get")
    def test_retrieve_news_success(self,mock_get):

        mock_response = mock_get.return_value

        response =  newsapi.RetrieveNews("https://example.com/api/news")

        mock_get.assert_called_once_with(
            "https://example.com/api/news"
        )

        assert response == mock_response


    @patch("api.newsapi.requests.get")
    def test_retrieve_news_ok(self, mock_get):

        mock_response = mock_get.return_value
        mock_response.status_code = 200

        response = newsapi.RetrieveNews(
            "https://example.com"
        )

        self.assertEqual(response.status_code, 200)
        mock_get.assert_called_once_with(
            "https://example.com"
        )

    
    @patch("api.newsapi.requests.get")
    def test_retrieve_news_timeout(self, mock_get):

        mock_get.side_effect = requests.exceptions.Timeout

        response = newsapi.RetrieveNews(
            "https://example.com"
        )

        self.assertIsNone(response)

    @patch("api.newsapi.requests.get")
    def test_retrieve_news_request_exception(self, mock_get):
        exception = requests.exceptions.RequestException("Connection error")
        mock_get.side_effect = exception

        try:
            newsapi.RetrieveNews("https://example.com/api/news")
        except SystemExit as e:
            assert str(e) == "Connection error"
        else:
            assert False, "SystemExit was not raised"
    