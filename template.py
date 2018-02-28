from jinja2 import Template

def render(filename):
    with open(filename) as f:
        data = ''.join(f.readlines())
        template = Template(data)
        return template.render(name="cats")

print(render("templates/yellowstone/index.html"))