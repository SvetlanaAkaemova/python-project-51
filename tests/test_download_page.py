import os
import pytest
import requests
import requests_mock
import tempfile
import bs4
from page_loader import download
from page_loader.modules.download_page import element_download


def test_element_download(requests_mock, content_from_page, image_content):
    image_url = '/assets/professions/nodejs.png'
    with open(content_from_page, encoding='utf-8') as c:
        content_of_page = c.read()
        soup = bs4.BeautifulSoup(content_of_page, 'html.parser')  
        img_content = open(image_content, 'rb').read()
        image = requests_mock.get('https://page-loader.hexlet.repl.co' + image_url, content=img_content)
        new_temp_path = tempfile.TemporaryDirectory()
        if not os.path.isdir(new_temp_path.name + '/page-loader-hexlet-repl-co-_files'):
            os.mkdir(new_temp_path.name + '/page-loader-hexlet-repl-co-_files')
        element_download('img', 'src', soup, 'https://page-loader.hexlet.repl.co/', 'page-loader.hexlet.repl.co', new_temp_path.name, 'page-loader-hexlet-repl-co-_files')
        new_image_path = new_temp_path.name + '/page-loader-hexlet-repl-co-_files/page-loader-hexlet-repl-co-assets-professions-nodejs.png'
        with open(new_image_path, 'rb') as i:
            assert i.read() == img_content


def test_download(requests_mock, content_from_page, expected_html, image_content, css_content, js_content, course_content):
    url = 'https://page-loader.hexlet.repl.co/'
    new_temp_path = tempfile.TemporaryDirectory()
    new_path_to_file = new_temp_path.name + '/page-loader-hexlet-repl-co-.html'
    with open(content_from_page, encoding='utf-8') as c:
        content_of_page = c.read()
        data = requests_mock.get(url, text=content_of_page)
        image_url = '/assets/professions/nodejs.png'
        img_content = open(image_content, 'rb').read()
        image = requests_mock.get('https://page-loader.hexlet.repl.co' + image_url, content=img_content)
        css_url = '/assets/application.css'
        css_cont = open(css_content, 'rb').read()
        css = requests_mock.get('https://page-loader.hexlet.repl.co' + css_url, content=css_cont)
        js_url = '/script.js'
        js_cont = open(js_content, 'rb').read()
        js = requests_mock.get('https://page-loader.hexlet.repl.co' + js_url, content=js_cont)
        course_url = '/courses'
        course_cont = open(course_content, 'rb').read()
        course = requests_mock.get('https://page-loader.hexlet.repl.co' + course_url, content=course_cont)
        result = download(url, new_temp_path.name)
        if not os.path.isdir(new_temp_path.name + '/page-loader-hexlet-repl-co-_files'):
            os.mkdir(new_temp_path.name + '/page-loader-hexlet-repl-co-_files')
        assert result == new_path_to_file
        with open(result, encoding='utf-8') as r:
            assert r.read() == open(expected_html, encoding='utf-8').read()
