import dash
import dash_leaflet as dl
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_auth

# Define valid usernames and passwords
VALID_USERNAME_PASSWORD_PAIRS = {
    'justin': 'justin',
    'jacob': 'jacob',
    'scott': 'scott',
    'patrick': 'patrick',
    'harrison' : 'harrison'
}

# Define app and server
app = dash.Dash(__name__)
server = app.server

# Create authentication object
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

# initialize locations
waypoints = []

# create front end
app.layout = html.Div([
    # Login form
    html.Div(id='login-form', children=[
        dcc.Input(id='username', type='text', placeholder='Username'),
        dcc.Input(id='password', type='password', placeholder='Password'),
        html.Button(id='login-button', n_clicks=0, children='Login')
    ], style={'display': 'inline-block', 'margin': '20px'}),

    # Map
    dl.Map(
        [dl.TileLayer(), dl.LayerGroup(id="layer")],
        id="map",
        style={'width': '1000px', 'height': '50vh', 'margin': "auto", "display": "block"},
        center=[33.4526221, -88.7872477],
        zoom=10
    ),
])

# Callback for handling login
@app.callback(Output('login-form', 'style'), Output('map', 'style'), Output('login-button', 'children'),
              [Input('login-button', 'n_clicks')], [State('username', 'value'), State('password', 'value')])
def login(n_clicks, username, password):
    if n_clicks > 0 and username in VALID_USERNAME_PASSWORD_PAIRS and VALID_USERNAME_PASSWORD_PAIRS[username] == password:
        login_style = {'display': 'none'}
        map_style = {'width': '1000px', 'height': '99vh', 'buffer-top': '-20px', 'margin': "auto", "display": "block"}
        button_text = 'Logged in as ' + username
        return login_style, map_style, button_text
    else:
        login_style = {'display': 'inline-block', 'margin': '20px'}
        map_style = {'display': 'none'}
        button_text = 'Login'
        return login_style, map_style, button_text

# Callback for storing and displaying markers
@app.callback([Output("layer", "children"), Output("map", "center"), Output("map", "zoom")], [Input("map", "click_lat_lng")])
def map_click(click_lat_lng):
    location = (click_lat_lng)
    # appends the waypoints vector with the coordinates
    waypoints.append(list(click_lat_lng))
    markers = [dl.Marker(position=point, children=dl.Tooltip("({:.3f}, {:.3f})".format(*point))) for point in waypoints]
    if len(waypoints) > 1:
        line = dl.Polyline(positions=waypoints, color="red", weight=5, opacity=0.7)
        return markers + [line], None, None
    return markers, None, None

# run server
if __name__ == '__main__':
    app.run_server()
