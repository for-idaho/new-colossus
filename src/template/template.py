from jinja2 import Template

def getTemplate(filename):
    with open(filename) as f:
        data = ''.join(f.readlines())
        return Template(data)

def render(template, params):
    return template.render(**params)

template = getTemplate("templates/dummy/index.html")

print(render(template, {
    "name" : "Maria",
    "volunteer_url" : "https://google.com",
    "donate_url": "https://twitter.com",
    "bio": "I am a person",
    "issues": "Here are my issues",
    "events": "Come to my event"
}))