import os
import requests
from page_loader.modules.parse_url import url_parse, new_path


def download(url, directory=os.getcwd()):
    get_page = requests.request('GET', url)
    page_content = get_page.text
    url_part = url_parse(url)
    path_to_file = new_path(url_part, directory)
    with open(path_to_file, 'w', encoding='utf-8') as output_file:
        output_file.write(page_content)
    return path_to_file
