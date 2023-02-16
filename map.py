import json
import dash # install dash with pip install -U dash
import dash_leaflet as dl
from dash import html
from dash.dependencies import Input, Output, ALL

# initialize locations
waypoints = []

# create front end
FE = dash.Dash(prevent_initial_callbacks=True)
FE.layout = html.Div(children=[
    html.H1("L.O.T.U.S. Dashboard"),

    dl.Map(
        [dl.TileLayer(), dl.LayerGroup(id="layer")],
        id="map",
        style={'width': '1000px', 'height': '50vh', 'margin': "auto", "display": "block"},
        center=[33.4526221, -88.7872477],
        zoom=100
    ),
])

# store click lat longs
@FE.callback(Output("layer", "children"), [Input("map", "click_lat_lng")])
def map_click(click_lat_lng):
    location = (click_lat_lng)
    # appends the waypoints vector with the coordinates
    waypoints.append("{:.8f},{:.8f}".format(*click_lat_lng))
    print(location)
    return [dl.Marker(position=click_lat_lng, children=dl.Tooltip("({:.3f}, {:.3f})".format(*click_lat_lng)))]

# run server
if __name__ == '__main__':
    FE.run_server()
