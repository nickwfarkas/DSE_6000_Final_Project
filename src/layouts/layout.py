from assets.theme import theme
from dash import dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd
from visualize import Visualization

def layout(data):
    ev_sales_heat_map = data[data["parameter"] == "EV sales"][['region','value']]
    ev_sales_heat_map = ev_sales_heat_map.groupby(['region']).sum().reset_index()

    viz = Visualization(ev_sales_heat_map,theme)

    heatmap_fig = viz.heat_map(
        countries="region",
        weight="value",
        title="Number of new electric cars sold",
    )
    
    return html.Div(
        style={"textAlign": "center", "marginBottom": "40px", "backgroundColor": theme["background"], "color": theme["text"], "fontFamily": theme["font"], "padding": "20px"},children=[
       dcc.Dropdown(
            id='region-filter-1',
            options=[{'label': region, 'value': region} for region in data['region'].unique()],
            multi=True,
            placeholder='Select Regions',
            style={'width': '50%', 'textAlign': 'center'},
            
        ),
        # Share of new cars sold that are electric, 2010 to 2023
        dcc.Graph(id='share_of_new_cars_sold_that_are_electric_line_faceted_plot'),

        html.P(
            """
            Electric car sales have surged in recent years, marking a significant shift in the global auto market. Starting from a low base, their growth has accelerated rapidly in many countries, driven by improved technology, government incentives, and changing consumer preferences.

            Globally, approximately 1 in 4 new cars sold in 2023 were electric. In Norway, this figure soared to over 90%, reflecting the country’s strong push towards clean energy. China, the world’s largest car market, saw nearly 40% of its new car sales come from electric models, highlighting its pivotal role in the transition.

            This analysis includes both fully battery-electric vehicles (BEVs) and plug-in hybrids (PHEVs). Use the chart below to explore these trends and see how different regions are adopting electric vehicles.
            """,
            style={"textAlign": "left", "marginBottom": "40px"}
        ),

        
        dcc.Dropdown(
            id='region-filter-2',
            options=[{'label': region, 'value': region} for region in data['region'].unique()],
            multi=True,
            placeholder='Select Regions',
            style={'width': '50%'},
            
        ),

        # Share of new cars sold that are electric, 2010 to 2023
        dcc.Graph(id='share_of_new_cars_sold_that_are_electric_2023_h_bar_plot'),
        
        dcc.Dropdown(
            id='region-filter-3',
            options=[{'label': region, 'value': region} for region in data['region'].unique()],
            multi=True,
            placeholder='Select Regions',
            style={'width': '50%'},
            
        ),

        dcc.Graph(id='share_of_new_cars_sold_that_are_battery_electric_and_plug_in_hybrid_bar_faceted_plot'),

        html.P(
            """
            “Electric cars” include two main types: battery-electric vehicles (BEVs) and plug-in hybrids (PHEVs). Fully battery-electric cars run entirely on electricity, using no internal combustion engine. In contrast, plug-in hybrids combine a rechargeable battery and electric motor with a gasoline-powered engine.

            Plug-in hybrids can function as standard petrol cars if the battery is not charged. However, their smaller batteries have a shorter electric range compared to BEVs. Over longer distances, once the battery is depleted, the car switches to running on gasoline.

            While plug-in hybrids emit less carbon than traditional petrol or diesel cars, they generally produce more emissions than fully battery-electric cars, especially if driven predominantly using the gasoline engine.

            The first chart below shows electric car sales broken down by these two technologies, expressed as a share of new cars sold each year. The second chart highlights what proportion of new electric cars sold are fully battery-electric.
            """,
            style={"textAlign": "left", "marginBottom": "40px"}
        ),
        
        dcc.Dropdown(
            id='region-filter-4',
            options=[{'label': region, 'value': region} for region in data['region'].unique()],
            multi=True,
            placeholder='Select Regions',
            style={'width': '50%'},
            
        ),

        dcc.Graph(id='share_of_new_electric_cars_that_are_fully_battery_electric_line_plot'),
        
        dcc.Graph(id='number_of_new_electric_cars_sold', figure=heatmap_fig),
        
        dcc.Dropdown(
            id='region-filter-5',
            options=[{'label': region, 'value': region} for region in data['region'].unique()],
            multi=True,
            placeholder='Select Regions',
            style={'width': '50%'},

        ),

        dcc.Graph(id='custom1_graph'),
        
        dcc.Dropdown(
            id='region-filter-6',
            options=[{'label': region, 'value': region} for region in data['region'].unique()],
            multi=True,
            placeholder='Select Regions',
            style={'width': '50%'},

        ),

        dcc.Graph(id='custom2_graph'),

        html.P(
            """
            The transition away from oil is accelerating as alternative energy sources and technologies, like electric vehicles, continue to expand. The graphs illustrate the steady growth in oil displacement, both in terms of millions of barrels per day and equivalent energy units, as these cleaner technologies gain traction globally.

            Since 2010, the pace of oil displacement has been relatively slow, but recent years have shown exponential growth, particularly after 2020. This reflects the increasing adoption of electric vehicles and other innovations that reduce reliance on petroleum products. These trends are crucial for reducing greenhouse gas emissions and advancing global energy security.

            This data highlights the pivotal role of emerging technologies in reshaping the energy landscape and driving the gradual elimination of oil from key sectors.
            """,
            style={"textAlign": "left", "marginBottom": "40px"}
        ),
    ])