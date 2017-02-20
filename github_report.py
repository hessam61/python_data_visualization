import requests
import pygal
from pygal.style import LightColorizedStyle as lcs, LightenStyle as ls

language = 'php'
url = 'https://api.github.com/search/repositories?q=language:'+language+'&sort=stars'
r = requests.get(url)

print("Status code: ", r.status_code)

#convert returned json to python dict
response = r.json()

repo_dicts = response['items']

names, stars = [], []
for r in repo_dicts:
    names.append(r['name'])
    stars.append(r['stargazers_count'])

chart_style = ls('#333366', base_style=lcs)
chart = pygal.Bar(style=chart_style, x_label_rotation=45, show_legend=False)
chart.title = language.title() + ' projects on Github'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file(language+'_repos.svg')