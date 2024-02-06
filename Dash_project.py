from dash import dcc, html, Input, Output, callback
from sklearn.datasets import load_wine 
import pandas as pd 
import dash
import plotly.express as px

## Loading the dataset 
def load_data():
    wine=load_wine()
    wine_df=pd.DataFrame(wine.data,columns=wine.feature_names)
    wine_df['WineType']=[wine.target_names[t] for t in wine.target]
    return  wine_df

wine_df=load_data()
wine_df.head()

ingredients=wine_df.columns[:-1]

avg_wine_df=wine_df.groupby('WineType').mean().reset_index()
avg_wine_df

def create_scatter_plot(x_axis='alcohol',y_axis='flavanoids',color_encode=False):
    fig=px.scatter(data_frame=wine_df,x=x_axis,y=y_axis,color='WineType' if color_encode else None,
                  title='{} vs {}'.format(x_axis,y_axis))
    fig.update_layout(height=600)
    return fig 

def create_bar_chart(ingredients=['alcohol','malic_acid','ash']):
    bar_fig = px.bar(avg_wine_df,x='WineType',y=ingredients,title='Avg Ingredients in Winetypes')
    bar_fig.update_layout(height=600)
    return bar_fig

x_axis=dcc.Dropdown(id ='x_axis',options=ingredients, value='alcohol',clearable=False)
y_axis=dcc.Dropdown(id ='y_axis',options=ingredients, value='flavanoids',clearable=False)

color_encode=dcc.Checklist(id='color_encode',options=['Color-Encode'])

multi_select=dcc.Dropdown(id='mutli_select',options=ingredients,value=['alcohol','malic_acid','ash'])

app=dash.Dash(title="Wine Analysis")

app.layout=html.Div(
    children=[
        html.H1('Wine Analysis DashBoard',style={'text-align':'center','font_size':24,'color':'#0000FF'}),
        html.Div('Explore the relationship between Different WineTypes',style={'text-align':'center','font_size':24,'color':'#088F8F'}),
        html.Br(),
        html.Div(
            children=[
                x_axis,y_axis,color_encode,
                dcc.Graph(id='Scatter_plot',figure=create_scatter_plot())
            ],
            style={'display':'inline-block','width':'47%'},
        ),
        html.Div(
            children=[
                multi_select,html.Br(),
                dcc.Graph(id='bar_plot',figure=create_bar_chart())
            ],
            style={'display':'inline-block','width':'47%'},
        )
    ],
    style={'padding':'50px'}
)
@callback(Output('Scatter_plot','figure'),
         [Input('x_axis','value'),Input('y_axis','value'),Input('color_encode','value')])
def update_scatter_plot(x_axis,y_axis,color_encode):
    return create_scatter_plot(x_axis,y_axis,color_encode)

@callback(Output('bar_plot','figure'),
         [Input('mutli_select','value')])
def update_bar_plot(ingredients):
    return create_bar_chart(ingredients)


if __name__=='__main__':
    app.run_server(port=8000,debug=True)
