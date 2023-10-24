from dash import Dash, dcc               # pip install dash
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
mytext = dcc.Markdown(children="# Hello World - let's build web apps in Python!")

# Customize your own Layout
app.layout = dbc.Container([mytext])

# Run app
if __name__=='__main__':
    app.run_server(port=8051)