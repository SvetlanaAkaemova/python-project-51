import bs4
import os
import requests
import urllib
from page_loader.modules.parse_url import url_parse, new_path, new_dir, new_file


def element_download(tag, attribute, soup, url, url_netloc, directory, new_dir_name):
    elements = soup.find_all(tag, {attribute: True})
    for element in elements:
        element_netloc = urllib.parse.urlparse(element.attrs[attribute]).netloc
        if element_netloc == url_netloc or element_netloc == '':
            element_content = requests.get(urllib.parse.urljoin(url, element.attrs[attribute])).content
            new_name_for_element = new_file(element.attrs[attribute], url)
            path_to_element = directory + '/' + new_dir_name + '/' + new_name_for_element
            with open(path_to_element, 'wb') as e:
                e.write(element_content)
            element[attribute] = new_dir_name + '/' + new_name_for_element
        else:
            pass
    return soup


def download(url, directory=os.getcwd()):
    url_netloc = urllib.parse.urlparse(url).netloc
    url_part = url_parse(url)
    get_page = requests.request('GET', url)
    page_content = get_page.text
    soup = bs4.BeautifulSoup(page_content, 'html.parser')
    new_dir_name = new_dir(url_part)
    if not os.path.isdir(new_dir_name):
        os.mkdir(directory + '/' + new_dir_name)

    element_download('img', 'src', soup, url, url_netloc, directory, new_dir_name)
    element_download('link', 'href', soup, url, url_netloc, directory, new_dir_name)
    element_download('script', 'src', soup, url, url_netloc, directory, new_dir_name)
    path_to_file = new_path(url_part, directory)
    with open(path_to_file, 'w', encoding='utf-8') as output_file:
        output_file.write(soup.prettify())
    return path_to_file
