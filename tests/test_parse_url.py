from page_loader.modules.parse_url import url_parse, new_path, new_dir, new_file


def test_url_parse():
    assert url_parse('https://ru.hexlet/io/courses3.txt') == 'ru-hexlet-io-courses3'


def test_new_path():
    assert new_path('ru-hexlet-io-courses3', '/var/tmp') == '/var/tmp/ru-hexlet-io-courses3.html'


def test_new_dir():
    assert new_dir('ru-hexlet-io-courses3') == 'ru-hexlet-io-courses3_files'


def test_new_file():
    assert new_file(
        '/assets/professions/nodejs.jpg',
        'https://ru.hexlet.io/courses3.txt') == 'ru-hexlet-io-assets-professions-nodejs.jpg' 
