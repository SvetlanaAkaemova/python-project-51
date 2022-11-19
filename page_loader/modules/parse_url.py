import os
import re


def url_parse(url):
    url_part = url.split('/', 2)[2]
    root, ext = os.path.splitext(url_part)
    modified_root = '-'.join(re.split(r'[\W]', root))
    return modified_root


def new_path(modified_root, directory):
    return directory + '/' + modified_root + '.html'
