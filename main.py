import numpy as np

from bokeh.io import output_file, show
from bokeh.models import HoverTool
from bokeh.plotting import figure

n = 250
x = 2 + 2*np.random.standard_normal(n)
y = 2 + 2*np.random.standard_normal(n)

p = figure(title=f"Hexbin for {n} points",
           match_aspect=True,
           tools="wheel_zoom,reset,pan",
           background_fill_color='#440154')
p.grid.visible = False

r, bins = p.hexbin(x, y, size=0.75, hover_color="pink", hover_alpha=0.8)

p.circle(x, y, color="white", size=1)

p.add_tools(HoverTool(
    tooltips=[("count", "@c"), ("(q,r)", "(@q, @r)")],
    mode="mouse",
    point_policy="follow_mouse",
    renderers=[r],

))

output_file("hexbin_modified.html")

show(p)