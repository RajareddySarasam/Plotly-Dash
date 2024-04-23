import dash 
from dash import dcc,html,Input,Output,callback
import plotly.express as px
import pandas as pd 

#Creating a Dash
app=dash.Dash(__name__)

#Adding Title to our Dash
app.title='Avocado-DashBoard'
#Reading the DataSet
Avocado=pd.read_csv('avocado-updated-2020.csv')

#Layout of Dash 
app.layout=html.Div(children=[
    html.H1(children='Avocado_DashBoard',
            style={
                "textAlign":'center',
                'color':'#FF0000',
            }),
    dcc.Dropdown(
        id="geo_dropdown",
        options=[
            {'label':i,'value':i} for i in Avocado.geography.unique()
        ],
        value='New York'
    ),
    dcc.Graph(id="Price_graph")
])

# CALLBACK FUNCTION

@app.callback(
    Output (component_id="Price_graph",component_property="figure"),
    Input (component_id="geo_dropdown",component_property="value")
    )
def update_graph(user_input):
    filtering_geo=Avocado[Avocado.geography==user_input]
    fig=px.line(data_frame=filtering_geo,x='date',y='average_price',
                color='type',
                title=f'Avocado Prices in {user_input}')
    return fig


if __name__=='__main__':
    app.run_server()