import os
import re
import urllib
from pathlib import Path


def url_parse(url):
    url_part = urllib.parse.urlparse(url)
    root, ext = os.path.splitext(url_part.netloc + url_part.path)
    modified_root = '-'.join(re.split(r'[\W]', root))
    return modified_root


def new_path(modified_root, directory):
    return directory + '/' + modified_root + '.html'


def new_dir(modified_root):
    new_dir_name = modified_root + '_files'
    return new_dir_name


def new_file(path, url):
    netloc = urllib.parse.urlparse(url).netloc
    full_path = netloc + path
    new_name = url_parse(full_path) + Path(path).suffix
    return new_name
