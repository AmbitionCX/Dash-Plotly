---
theme: seriph
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
info: Slidev for dash-plotly course
drawings:
  persist: false
transition: slide-left
title: Welcome to Slidev
mdc: true
---

# Data Visualization

Introduction on Dash and Plotly
<br>
Chen Xuan@FDUVIS
<br>
chenxuan@fudan.edu.cn

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

<div class="abs-br m-6 flex gap-2">
  <button @click="$slidev.nav.openInEditor()" title="Open in Editor" class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon:edit />
  </button>
  <a href="https://github.com/slidevjs/slidev" target="_blank" alt="GitHub" title="Open in GitHub"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-github />
  </a>
</div>

---
layout: default
---

# What is Dash?

- Dash is a web app framework that provides pure Python abstraction around HTML, CSS, and JavaScript.
- Basically, it is a web server. Dash is developed based on [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- Moreover, it provide methods to write webpage in Python.
  - How to write HTML, CSS, JavaScript in Python?

## What can Dash do?
Look at [Dash Gallery](https://dash.gallery/Portal/) for more examples.
- [Object Detection for Self-Driving Cars](https://dash.gallery/self-driving/)
- [US Opioid Epidemic](https://dash.gallery/dash-opioid-epidemic/)
- [Brain Surface Viewer](https://dash.gallery/dash-brain-viewer/)

---
layout: default
---

# Three core concept of Dash 

1. **Dash Components and Layout** - The basic components in a Dash app
2. **Plotly Graphs** - Draw figures in components
3. **Callback Functions** - Interaction between components

Every dash app is <span class="highlight">components</span> that are displayed on the page through the <span class="highlight">layout</span>, which interactive with each other through the <span class="highlight">callback</span>.

## How to write webpage with Dash ?

|     |     |
| --- | --- |
| Components & Layout | HTML & CSS |
| Plotly | D3.js |
| Callback | JavaScript |

<style>
.highlight {
  color: red;
  font-weight: bold;
}
</style>

---
layout: default
---

# How to use Dash

## Install
```shell
pip install dash
pip install dash-bootstrap-components
```

## A Hello World Example <span class="refer"> `helloworld.py` </span>
```python
from dash import Dash, dcc               # pip install dash
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
mytext = dcc.Markdown(children="# Hello World - let's build web apps in Python!")

# Customize your own Layout
app.layout = dbc.Container([mytext])

# Run app
if __name__=='__main__':
    app.run_server(port=8051)
```

<style>
  .refer {
    font-size: 10px;
    color: #808080;
  }
</style>

---
layout: default
---

# An Interactive Hello World Example
<span class="refer"> `interactive-app.py` </span>
<span class="refer"> `app-with-graph.py` </span>

```python
# Build your components
app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
mytext = dcc.Markdown(children='')
myinput = dbc.Input(value="# Hello World - let's build web apps in Python!")

# Customize your own Layout
app.layout = dbc.Container([mytext, myinput])

# Callback allows components to interact
@app.callback(
    Output(mytext, component_property='children'),
    Input(myinput, component_property='value')
)
def update_title(user_input):  # function arguments come from the component property of the Input
    return user_input  # returned objects are assigned to the component property of the Output


# Run app
if __name__=='__main__':
    app.run_server(port=8052)
```

<style>
  .refer {
    font-size: 10px;
    color: #808080;
  }
</style>

---
layout: default
---
# Dash Core Components

- The Dash Core Components module `dash.dcc` gives you access to many interactive components, including dropdowns, checklists, and sliders.
- Except the core components, we also have [**Dash HTML Components**](https://dash.plotly.com/dash-html-components), or [**Dash Bootstrap Components**](https://dash-bootstrap-components.opensource.faculty.ai/)
- See more components in the [Open Source Component Libraries](https://dash.plotly.com/)


###  Dropdown Example
```python
from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'], 'Montréal')
])

if __name__ == '__main__':
    app.run(debug=True)
```

---
layout: default
---
# Dash HTML Components

- Instead of writing HTML or using an HTML templating engine, you compose your layout using Python with the Dash HTML Components module `dash.html` .

```python
from dash import html

html.Div([
    html.H1('Hello Dash'),
    html.Div([
        html.P('Dash converts Python classes into HTML'),
        html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
    ])
])
```
which will be converted into the following HTML:
```html
<div>
    <h1>Hello Dash</h1>
    <div>
        <p>Dash converts Python classes into HTML</p>
        <p>This conversion happens behind the scenes by Dash's JavaScript front-end</p>
    </div>
</div>
```


---
layout: default
---
# Dash Bootstrap Components

- **What is Bootstrap?** - [Bootstrap](https://getbootstrap.com/) is an open-source CSS framework,which contains HTML, CSS and JavaScript-based design templates for typography, forms, buttons, navigation, and other interface components.
- Dash Bootstrap Components is a Dash component to use Bootstrap style sheets.

###   Example
```python
import dash
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    dbc.Alert("Hello Bootstrap!", color="success"),
    className="p-5",
)

if __name__ == "__main__":
    app.run_server()
```

---
layout: default
---
# Layouts

- The layout is a <span class="highlight">hierarchical tree of components</span>.
- Build DOM Tree with layout (Please refer to `layout-1.py` and `layout-2.py` )

```python
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for your data.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])
```

<style>
.highlight {
  color: red;
  font-weight: bold;
}
</style>

---
layout: default
---
# Dash Callbacks

- Callbacks are functions that are automatically called by Dash whenever an input component's property changes, in order to update some property in the output component.

```python
mytext = dcc.Markdown(children='')
myinput = dbc.Input(value="# Hello World - let's build web apps in Python!")

@app.callback(
    Output(mytext, component_property='children'),
    Input(myinput, component_property='value')
)
def update_title(user_input):  # function arguments come from the component property of the Input
    return user_input  # returned objects are assigned to the component property of the Output
```

- Callback function with multiple inputs. <span class="refer"> `callback-multi-input.py` </span>
- Callback function with multiple outputs. <span class="refer"> `callback-multi-output.py` </span>
- Chained callback functions: the output of one callback function could be the input of another callback function. <span class="refer"> `callback-chained.py` </span>

<style>
  .refer {
    font-size: 10px;
    color: #808080;
  }
</style>

---
layout: center
class: text-center
---

# Assignment 1
1. Take the interactive-app.py file. Add a [radioItems Dash Core Component](https://dash.plotly.com/dash-core-components/radioitems) to the layout after assigning the following colors to its `options` property: `['blue','red','green']`. Incorporate the RadioItems component into the callback so the button/color chosen updates the color of the markdown text. Hint - the callback will have a total of 2 Outputs and 2 Inputs. To color the Markdown text in purple, its `style` property is written like this: `dcc.Markdown(style={'color':'purple'})`

---
layout: center
class: text-center
---

# Assignment 2
2. Take the app-with-graph.py file. Add an empty `Alert` [Dash Mantine Component](https://dash-mantine-components.herokuapp.com/components/alert) to the layout between the markdown and the graph. Insert the Alert component as the second Output in the callback, with `children` as the component property. Modify the callback function so it returns this string, `"The data for the bar graph is highly confidential."` if user chooses a bar plot, and it returns this string, `"The scatter plot is believed to have been first published in 1833"` if user chooses a scatter plot.

---
layout: default
---
# Plotly
Please refer to `plotly.ipynb`

```python
# For plotly, there are two types
import plotly.express as px
import plotly.graph_objects as go
```

- **GO (graph_objects)** - Create and operate on graph_objects
- **Express** - Internally calls graph_objects and return a value
- The final contents generated by two methods are the same
- Plotly Express is often the better choice

---
layout: center
class: text-center
---

# Plotly Exercise
10 mins


---
layout: default
---
# Choropleth map
- A [Choropleth Map](https://plotly.com/python/choropleth-maps/) is a map composed of colored polygons. It is used to represent spatial variations of a quantity.

### Two main input for choropleth maps:
1. Geometry information
2. A list of values indexed by feature identifier.

- The GeoJSON data is passed to the geojson argument, and the data is passed into the color argument of `px.choropleth`, in the same order as the IDs are passed into the location argument.
```python
    fig = px.choropleth(data_frame=df,
                        locations='STATE',
                        locationmode="USA-states",
                        scope="usa",
                        height=600,
                        color=column_name,
                        animation_frame='YEAR')
```

---
layout: center
class: text-center
---

# Assignment 3, 4, 5
30 mins

---
layout: default
---

# Deploy Dash apps

- Deploy locally
  - Flask
- Deploy on Cloud
  - [Github Pages](https://pages.github.com/)
  - [Netlify](https://www.netlify.com/)
  - [Heroku](https://dashboard.heroku.com/)
- Deploy with container
  - docker
  - kubernetes 

---
layout: default
---

# Deploy a Dash app with Heroku

- Heroku is one of the most popular cloud PaaS (Platform as a Service)
- [Documentation](https://dash.plotly.com/deployment)

1. Prepare a Heroku account, `git` and python `virtualenv`
2. Install packages for virtual env.
3. Create your `app.py`, `.gitignore` file, `requirements.txt`, and `Procfile` for deployment
4. Deploy with `heroku` CLI

You can also deploy with [Dash Tools](https://dash-tools.readthedocs.io/en/latest/)

---
layout: center
class: text-center
---

# Thank you for listening
Chen Xuan@FDUVIS
<br>
chenxuan@fudan.edu.cn