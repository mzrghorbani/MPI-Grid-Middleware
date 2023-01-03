import random
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

newnames = {'one':'10 threads'}

one = [3.05,3.32,2.11,2.93,3.62,2.52,3.23,3.62,4.11,2.69]

#one.sort(reverse=True)

d = {
'x': ['1','2','3','4','5','6','7','8','9','10'],
'one': one
}

df = pd.DataFrame(d)

df.to_csv('plot.csv')

fig = px.line(df, x="x", y=["one"], markers=True, width=1600, height=600)

fig.update_traces(
    marker=dict(size=28, symbol="diamond", line=dict(width=2, color="Black")),
    selector=dict(mode="lines+markers"))

fig.update_layout(
    #title="Plot Title",
    # xaxis_title_standoff=50,
    xaxis_title="Jobs",
    # yaxis_title_standoff=50,
    # yaxis_title="Runtime (hour)",
    legend_title="",
    font=dict(
        family="Times New Roman",
        size=44,
        color="Black"), margin=dict(l=10, r=10, b=10, pad=10))
fig.for_each_trace(lambda t: t.update(name = newnames[t.name]))
# fig.update_xaxes(title='', visible=True, showticklabels=True)
fig.update_yaxes(title='', visible=True, showticklabels=True, ticklabelstep=1)
fig.update_layout(legend=dict(title_font_family="Times New Roman",font=dict(size=36)))
fig.update(layout_showlegend=False)
fig.update_layout(yaxis_ticksuffix="h")
fig.show()