from jinja2 import Template
import os
from glob import glob

ACCEPTED_FILE_TYPES = ["html", "css", "js", "jpeg", "png"]
ACCEPTED_TEMPLATE_FILE_TYPES = ["html", "css", "js"]

def _ext(filepath):
    return filepath.split(".")[-1]

def _read(path, binary=False):
    binaryFlag = "b" if binary else ""
    with open (path, 'r' + binaryFlag) as file:
        return file.read()

def _templateFile(data, path):
    src = _read(path)

    # If we're able to read this file
    # We should absolutely never encounter an empty
    # file since this is in source
    assert src 

    return Template(src).render(**data)

def _templateDirectory(name):
    return os.path.join("html", name)

def _pruneTemplateDirectory(name, path):
    return path.replace(_templateDirectory(name) + "/", '', 1)

def _listFiles(name):
    files = glob(_templateDirectory(name) + '/**/*.**', recursive=True)

    # Filter out src files or other junk that may have found its way in
    return [file for file in files if _ext(file) in ACCEPTED_FILE_TYPES]

def _createPathToHTMLDict(name, data, files):
    htmls = {}

    for file in files:
        key = _pruneTemplateDirectory(name, file)
        if _ext(file) in ACCEPTED_TEMPLATE_FILE_TYPES:
            htmls[key] = _templateFile(data, file)
        else:
            htmls[key] = _read(file, binary=True)

    return htmls


def template(data, name="dummy"):
    """
    Read a file and fill in it's template 
    
    :param dict data: A dictionary representing the jinja2 info
    :param str name: the folder name inside /tempalte/html/*
    :return: a dictionary where the keys are the filepaths and
         the values are the templated data
    """

    files = _listFiles(name)
    return _createPathToHTMLDict(name, data, files)