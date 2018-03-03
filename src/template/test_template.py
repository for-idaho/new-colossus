from template import getTemplate
import os 

def test_template():
    """ We create a template from a jinja file without error """
    path = os.path.join(os.path.dirname(__file__), "assets/foo.html")
    assert getTemplate(path) != None
