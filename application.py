import dash
from dash import html, dcc, Dash
import dash_labs as dl
import dash_bootstrap_components as dbc
import dash_auth
from dash_iconify import DashIconify
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template
# from flask_socketio import SocketIO, emit


application = Dash(__name__, plugins=[dl.plugins.pages],
                   external_stylesheets=[dbc.themes.BOOTSTRAP],
                   meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}
                              ])
server = application.server

# app.layout = html.Div([html.Script(**{"data-url": "https://platform.linkedin.com/badges/js/profile.js"}, type="IN/Share")])

navbar = dbc.NavbarSimple(

    children=[

        # html.Link("linkdin",href='https://www.linkedin.com/in/sethu-gopalan-a8915367/'),
        dbc.NavItem(dbc.Label('ComputerHelpdeskOnline', style={
            'color': '#335eea', 'fontSize': '1.5rem', 'font-family': 'cursive', "margin-right": "800px"})),
        dbc.NavItem(dbc.Button('Check it IT', style={
            'color': 'white', 'fontSize': 16, 'font-family': 'cursive'})),
        dbc.NavItem(dbc.Button('TechNews', style={
            'color': 'white', 'fontSize': 16, 'font-family': 'cursive'})),




        dbc.DropdownMenu(

            [
                dbc.DropdownMenuItem(page['name'], href=page["path"])
                for page in dash.page_registry.values()
                if page['module'] != "page .not_found_404"
            ],
            nav=True,
            # in_navbar=True,
            label="MorePages",

        ),
    ],




)


application.layout = dbc.Container(

    [navbar, dl.plugins.page_container],
    fluid=True,
)
if __name__ == "__main__":
    application.run(debug=False, host='0.0.0.0', port=8001)
