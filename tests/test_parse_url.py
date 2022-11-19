from page_loader.modules.parse_url import url_parse, new_path


def test_url_parse():
    assert url_parse('https://ru.hexlet/io/courses3.txt') == 'ru-hexlet-io-courses3'


def test_new_path():
    assert new_path('ru-hexlet-io-courses3', '/var/tmp') == '/var/tmp/ru-hexlet-io-courses3.html'
