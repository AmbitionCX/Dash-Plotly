import plotly
import plotly.express as px
import plotly.graph_objects as go

import numpy as np
import math

n = 12; x = np.arange(1,n+1)

y = np.random.random(n)*10
y_min = np.min(y)
y_min_ind = np.argmin(y)
y_max = np.max(y)
y_max_ind = np.argmax(y)

fig = go.Figure(data=go.Bar(x=x,y=y,name='Bars'))
fig.add_trace(go.Scatter(x=x,y=y,name = 'Lines'))
fig.add_trace(go.Scatter(x=[y_min_ind+1],y=[y_min+0.5],name='Min'))
fig.add_trace(go.Scatter(x=[y_max_ind+1],y=[y_max+0.5],name='Max'))
fig.add_annotation(text="Min",x=y_min_ind+1, y=y_min+1,name ='Min_Ano',showarrow=False)
fig.add_annotation(text="Max",x=y_max_ind+1, y=y_max+1,name ='Max_Ano',showarrow=False)
fig.update_layout(xaxis={'title':'Month','dtick':1},yaxis={'title':'Sale'})

# df = df.query('country in ["China","Japan"]')
# fig = px.line(df, x="year", y="lifeExp", color="country")