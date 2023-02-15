import json
# install dash with pip install -U dash
import dash
import dash_leaflet as dl
import dash_html_components as html
from dash.dependencies import Input, Output, ALL
import webbrowser

# create map object
map = dash.Dash()
map.layout = dl.Map(dl.TileLayer(),center=[33.4526221, -88.7872477], zoom=100, style={'width': '1000px', 'height': '500px'})

# Callback for interactivity.
@map.callback(Output("log", "children"), Input(dict(id=ALL), "n_clicks"))
def log_position(_):
    idx = json.loads(dash.callback_context.triggered[0]['prop_id'].split(".")[0])["id"]
    location = locations[idx]
    print(location)  # print location to console
    return location  # print location to ui

# modify html here

# run server and open web browser
if __name__ == '__main__':
    map.run_server()
webbrowser.open_new_tab("http://localhost:8050")
