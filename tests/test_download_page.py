import pytest
import requests
import requests_mock
import tempfile
from page_loader import download


@pytest.fixture
def content_from_page():
    return 'tests/fixtures/content_from_page.html'


def test_download(requests_mock, content_from_page):
    url = 'https://page-loader.hexlet.repl.co/'
    new_temp_path = tempfile.TemporaryDirectory()
    new_path_to_file = new_temp_path.name + '/page-loader-hexlet-repl-co-.html'
    with open(content_from_page, encoding='utf-8') as c:
        content_of_page = c.read()
        data = requests_mock.get(url, text=content_of_page)
        result = download(url, new_temp_path.name)
        assert result == new_path_to_file
        with open(result, encoding='utf-8') as r:
            assert r.read() == content_of_page
        
