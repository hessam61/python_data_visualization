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

names, plot_dicts = [], []
for r in repo_dicts:
    names.append(r['name'])
    plot_list = []
    plot_dict = {
        'value': int(r['stargazers_count']),
        'label': str(r['description']),
        }
    plot_dicts.append(plot_dict)

chart_style = ls('#333366', base_style=lcs)
chart = pygal.Bar(style=chart_style, x_label_rotation=45, show_legend=False)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=chart_style)
chart.title = language.title() + ' projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file(language+'_repos.svg')