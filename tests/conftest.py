import pytest


@pytest.fixture
def content_from_page():
    return 'tests/fixtures/content_from_page.html'


@pytest.fixture
def expected_html():
    return 'tests/fixtures/expected.html'


@pytest.fixture
def image_content():
    return 'tests/fixtures/image_content.png'


@pytest.fixture
def css_content():
    return 'tests/fixtures/css_content.css'


@pytest.fixture
def js_content():
    return 'tests/fixtures/js_content.js'


@pytest.fixture
def course_content():
    return 'tests/fixtures/course_content.html'
