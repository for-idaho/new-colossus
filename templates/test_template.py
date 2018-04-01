import tempfile
import template
import os

def _tmp(content):
    f, path = tempfile.mkstemp() 
    os.write(f, content)
    os.close(f)
    return path

def test_ext():
    assert template._ext("jazz/foo.html.map") == "map"
    assert template._ext("jazz/foo.html") == "html"

def test_read():
    f = _tmp("jazz")
    assert template._read(f) == "jazz"

def test_templateFile():
    f = _tmp("{{pet}}, {{name}}")
    data = template._templateFile({"pet": "cat", "name": "george"},f)
    assert data == "cat, george"

def test_templateDirectory():
    assert os.path.exists(template._templateDirectory("dummy"))

def test_pruneTemplateDirectory():
    assert template._pruneTemplateDirectory("dummy", "html/dummy/foo.html") == "foo.html"
