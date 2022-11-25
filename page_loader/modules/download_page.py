import bs4
import os
import requests
import urllib
from page_loader.modules.parse_url import url_parse, new_path, new_dir, new_file


def download(url, directory=os.getcwd()):
    url_netloc = urllib.parse.urlparse(url).netloc
    url_part = url_parse(url)
    get_page = requests.request('GET', url)
    page_content = get_page.text
    soup = bs4.BeautifulSoup(page_content, 'html.parser')
    images = soup.find_all('img')
    for image in images:
        image_netloc = urllib.parse.urlparse(image.attrs['src']).netloc
        if image_netloc == url_netloc or image.attrs['src'].startswith('/'):
            img = requests.get(urllib.parse.urljoin(url, image.attrs['src'])).content
            new_name_for_image = new_file(image.attrs['src'], url)
            new_dir_name = new_dir(url_part)
            if not os.path.isdir(new_dir_name):
                os.mkdir(directory + '/' + new_dir_name)
            path_to_image = directory + '/' + new_dir_name + '/' + new_name_for_image
            with open(path_to_image, 'wb') as i:
                i.write(img)
            image['src'] = new_dir_name + '/' + new_name_for_image
        else:
            continue
    path_to_file = new_path(url_part, directory)
    with open(path_to_file, 'w', encoding='utf-8') as output_file:
        output_file.write(soup.prettify())
    return path_to_file
