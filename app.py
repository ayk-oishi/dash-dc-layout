import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

tabtitle = 'What DC Metro looks like'
myheading1 = "I don't really like DC Metro though"
myheading2 = 'This pic is little vague'
image1 = 'favicon.ico'
image2 = 'arr.jpeg'
textbody = "I am trying to put very small text here"
sourceurl = 'https://www.wmata.com/about/back2good/index.cfm'
githublink = 'https://github.com/ayk-oishi/dash-dc-layout'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H2(myheading1),
    html.H3(myheading2),
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url(image1), style={'width': '50%', 'height': 'auto'})
        ],className='three columns'),
        html.Div([
            html.Img(src=app.get_asset_url(image2), style={'width': '80%', 'height': 'auto'}),
        ],className='three columns'),
        html.Div([
            html.Div(textbody, style={
                'padding': '22px',
                'font-size': '11px',
                'height': '120px',
                'border': 'thin red solid',
                'color': 'rgb(155, 255, 355)',
                'backgroundColor': 'rgb(57, 83, 107)',
                'textAlign': 'right',
                }),
        ],className='six columns'),
    ],className='twelve columns'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
