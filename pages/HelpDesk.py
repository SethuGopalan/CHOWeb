
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from chatterbot.logic import LogicAdapter
from chatterbot import ChatBot
import chatterbot
import dash_mantine_components as dmc
from dash_labs.plugins.pages import register_page
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc
import dash
from dash import Dash, html, dcc, callback, dash_table, Input, Output, State
import logging
# from dash_extensions import chatApi
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML


import numpy as np
import pandas as pd

import requests
import time
import datetime

time.clock = time.time

register_page(__name__, path="/")


chatbot = ChatBot(
    'Liza',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)
chatbot.storage.drop()

logic_adapters = [



    {

        "import_path": "chatterbot.logic.BestMatch",
        # "statement_comparison_function": chatterbot.comparisons.LevenshteinDistance,
        # "response_selection_method": chatterbot.response_selection.get_first_response
        'default_response': 'I am sorry, but I do not understand.',

        'maximum_similarity_threshold': 0.90

    }


]


# logger = logging.getLogger()
# logger.setLevel(logging.CRITICAL)
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    'chatterbot_corpus\data\english'
)
# -----------------------------------------------------------------------------------------------------------------------------------------chat bot


layout = dbc.Container([

    dbc.Row([

        dbc.Col([
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Div([

                html.P("Welcome to ", style={'color': 'black', 'fontSize':  '2.3125rem',
                       'font-family': 'var(--bs-body-font-family)', 'display': 'inline-block', 'inline': 'left'}),
                html.P(["HelpDeskonline."], style={'color': '#335eea', 'fontSize':  '2.3125rem',
                       'font-family': 'var(--bs-body-font-family)', 'display': 'inline-block', 'inline': 'right', "margin-left": "5px"}),
                html.P(["IT support for any  OS or Cloud  infrastructure issues and Devolopment Projects "], style={
                    'color': 'black', 'fontSize': '2.3125rem', 'font-family': 'var(--bs-body-font-family)', 'display': 'inline-block'}),

                html.P(["We help you to resolve isues  on Windows, Mac & Linux cloud systems instantly", html.Br(), "best support experence without any registration"], style={
                    'color': 'black', 'fontSize': '1.3125rem', 'font-family': 'var(--bs-body-font-family)'}),
                # html.P("which you need to care about to avoid trouble. ",style={
                #             'color': 'black', 'fontSize': '1.3125rem', 'font-family': 'var(--bs-body-font-family)'}),
                html.Br(),
                html.Br(),
                html.Br(),
                dbc.Button('Remote Support', style={'inline': True, 'fontSize':  '1.3125rem', 'font-family': 'var(--bs-body-font-family)',
                           "width": '262.016px', "hight": '67.1875px', "align": "center"}, size='xl'),
                DashIconify(icon="la:desktop", width=40,
                            height=40,

                            style={'inline': True, "margin-left": "15px"},
                            ),
                dbc.Button("Chat support", id='support-id', n_clicks=0, color="light", style={'inline': True, 'fontSize':  '1.3125rem', 'font-family': 'var(--bs-body-font-family)',
                                                                                              "color": "#335eea", "width": '262.016px', "hight": '67.1875px', "align": "center", "margin-left": "25px"}, size='xl'),
                DashIconify(icon="la:comment-dots-solid", width=40,
                            height=40,

                            style={'inline': True, "margin-left": "15px"},


                            ),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),


                html.Div(id='sup-Output')
















            ]),






            # ], width={'size': 3, 'offset': 0})

        ], width={'size': 7, 'offset': 0}),


        dbc.Col([

            html.Div([
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                dbc.CardImg(src="assets\Support-Cart2.png",
                            style={"width": "45rem", "margin-right": "825px"})

            ]),



            html.Div([
                html.Br(),
                # html.Br(),
                # html.Br(),

                html.H5(" Hey I am Liza:", style={
                        'display': 'inline', 'display': 'inline-block'}),
                html.Br(),
                html.H5("How can I help you?", className="typing-demo",
                        #  style={
                        #         "overflow": "-moz-hidden-unscrollable",
                        #         "borderRight": ".15em solid orange",
                        #         "whiteSpace": "nowrap",
                        #         "margin": "0 auto",
                        #         "letterSpacing": ".15em",
                        #         "animation": "typewriter 1s steps(20) infinite",
                        # "animation": 'mymove 5s infinite',

                        style={'display': 'inline', 'display': 'inline-block', "margin-left": "95px"}),
                html.Br(),

                dcc.Input(id="input_bot", type="text",
                          placeholder=" type your text here", value="", style={'color': 'blue', 'border': 'blue',  'font-family': 'var(--bs-body-font-family)', "margin-left": "95px"}),
                html.Button(id='submit-bot', type='submit',

                            children='Submit', style={'color': 'blue', 'border': 'white',  'font-family': 'var(--bs-body-font-family)'}),
                # html.Br(),
                # html.Br(),
                # html.Br(),
                html.Div([
                    dbc.CardImg(src='assets\AVATAR_2.png', style={
                        "width": "10rem", "border-radius": "50%",   "margin-right": "825px"}),

                    html.Div(id="outpit_bot", style={
                        'font-family': 'Sans-serif', 'color': 'black', 'fontSize': 14,  "margin-left": "125px"}),







                ]),


            ]),






        ], width={'size': 4, 'offset': 1}),


        #     dbc.Col([

        #         html.Div(id='sup-Output')


        #     ], width={'size': 3, 'offset': 0})



    ]),
    # dbc.Row([






    # ])  # ------------------------------------------------------------------------------------------------------------------------------------chatbot call back end

])


@callback(Output("outpit_bot", 'children'),
          #   Output("input_Id","children"),
          Input('submit-bot', 'n_clicks'),

          #   State("outpit_bot", "value"),
          State("input_bot", "value"),
          #   State("input_bot", ),

          )
def responce_update(clicks, resp):

    # reset=resp.clear()

    if clicks is not None:
        # if clicks > 0:

        response = chatbot.get_response(resp)

        return dbc.Card(
            [
                dbc.CardBody([

                    html.Ul([html.P("You : {}".format(resp.capitalize()))], style={
                        'color': 'black', 'font-family': 'var(--bs-body-font-family)'}), html.Ul([html.P("Liza : {}".format(response))], style={
                            'color': 'black', 'font-family': 'var(--bs-body-font-family)'})
                ], style={'color': "green", 'font-family': 'var(--bs-body-font-family)'})
            ], style={"width": "18rem", 'color': "success", 'border': 'white'}, ), resp == ""
    # else:
    #     return resp == ""


@callback(Output("sup-Output", "children"),
          Input('support-id', 'n_clicks')

          )
def chatbox_open(n_clicks):

    if n_clicks > 0:

        # if n_clicks is not None:

        # return dbc.Card([

        #     dbc.CardHeader("Chat User1"),

        #     dbc.CardBody(
        #         [

        #             html.H5("Example chat", className="card-title"),
        #             html.P("This is an example chat window."),

        #         ]

        #     ),
        #     dbc.CardFooter("Type your question here"),
        # ],
        #     color="primary",
        #     inverse=True,
        #     style={"width": "25rem"},

        # )

        return html.Script(

            '''
            <script type="text/javascript">
                    (function(w, d, x, id){
                        s=d.createElement('script');
                        s.src='https://dtn7rvxwwlhud.cloudfront.net/amazon-connect-chat-interface-client.js';
                        s.async=1;
                        s.id=id;
                        d.getElementsByTagName('head')[0].appendChild(s);
                        w[x] =  w[x] || function() { (w[x].ac = w[x].ac || []).push(arguments) };
                    })(window, document, 'amazon_connect', 'd8aa5cf1-9f39-4188-987c-5128d92076c6');
                    amazon_connect('styles', { openChat: { color: '#ffffff', backgroundColor: '#123456'}, closeChat: { color: '#ffffff', backgroundColor: '#123456'} });
                    amazon_connect('snippetId', 'QVFJREFIakZhMVo2ZGZmSXpGSnpJS2lYakthYVBxMmJIU0ZPbnhET3AyalJDV1F3UWdFeVh1NG5FZnU1MTJLd2ducnBxV1ZYQUFBQWJqQnNCZ2txaGtpRzl3MEJCd2FnWHpCZEFnRUFNRmdHQ1NxR1NJYjNEUUVIQVRBZUJnbGdoa2dCWlFNRUFTNHdFUVFNbnNWWVNPS2JaN2o2VU5rdEFnRVFnQ3NzSVdDRGUzZS9PeWVzUmV3NXM0WlRJWnQyMndJTmdiclY3WjdCY3ZwRFF1cEtPcDBSQ0FPUEhBVG86OjBhelRiODhxbG5WbTdicmxpcFpoOUIrVXFJRDAvTHBKL0JubDMvM0FreTB3M2k0bFA2aGExamlWV1ZFcWFiS3Z6M0NKR3hHMWdxU2p2QXh0YlhreWhrTTlJZ2pKNjFmWTBnaFpseWIzMGhNdUIvTXd0U3NuNC9tZGhYaENFSGdqL2oxR3FlWjUyQS9zNUEvc0pJMERONjV1bmQ1ZHZOQT0=');
                    amazon_connect('supportedMessagingContentTypes', [ 'text/plain', 'text/markdown' ]);
                </script>
            
            '''


        ),
