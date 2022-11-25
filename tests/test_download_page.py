import os
import pytest
import requests
import requests_mock
import tempfile
from page_loader import download


@pytest.fixture
def content_from_page():
    return 'tests/fixtures/content_from_page.html'


@pytest.fixture
def expected_html():
    return 'tests/fixtures/expected_html.html'


@pytest.fixture
def image_content():
    return 'tests/fixtures/image_content.png'


def test_download(requests_mock, content_from_page, expected_html, image_content):
    url = 'https://page-loader.hexlet.repl.co/'
    new_temp_path = tempfile.TemporaryDirectory()
    new_path_to_file = new_temp_path.name + '/page-loader-hexlet-repl-co-.html'
    with open(content_from_page, encoding='utf-8') as c:
        content_of_page = c.read()
        data = requests_mock.get(url, text=content_of_page)
        image_url = '/assets/professions/nodejs.png'
        img_content = open(image_content, 'rb').read()
        image = requests_mock.get('https://page-loader.hexlet.repl.co' + image_url, content=img_content)
        result = download(url, new_temp_path.name)
        if not os.path.isdir(new_temp_path.name + '/page-loader-hexlet-repl-co-_files'):
            os.mkdir(new_temp_path.name + '/page-loader-hexlet-repl-co-_files')
        new_image_path = new_temp_path.name + '/page-loader-hexlet-repl-co-_files/page-loader-hexlet-repl-co-assets-professions-nodejs.png'
        with open(new_image_path, 'rb') as i:
            assert i.read() == img_content
        assert result == new_path_to_file
        with open(result, encoding='utf-8') as r:
            assert r.read() == open(expected_html, encoding='utf-8').read()
