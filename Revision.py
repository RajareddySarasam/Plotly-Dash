import dash 
from dash import html, dcc, Input, Output, callback
import plotly.express as px 

app=dash.Dash(__name__)

app.layout=html.Div([
    html.H1('HI User!!!!!!'),
     dcc.Dropdown(
       id="city_dropdown",
       options=[
           {'label':'NYC','value':'N'},
           {'label':'HYD','value':'H'},
           {'label':'NZB','value':'n'}
       ],
       value='HYD',
       placeholder="Select a City",
   ),
   dcc.Input(
       id='TextBox',
       type="text",
       placeholder='Enter about your city'

   ),
   dcc.RadioItems(
       id="Radio_items",
       options=[
           'car','Ship',"bike",'Bicycle'
       ],
       value='sumo'
   ),
    dcc.Graph(
        id='SimpleChart',
        figure={
            'data':[
                {   'x':[1,2,3],
                    'y':[12,23,35],
                    'type':'bar',
                    'name':'Bar_chart'
                }
            ],
            'layout':{
                'title':"BARCHART"
            }
        }
    )
  
    
    
])

if __name__=='__main__':
    app.run_server()