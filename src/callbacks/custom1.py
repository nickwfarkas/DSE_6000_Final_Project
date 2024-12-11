from dash.dependencies import Input, Output
from visualize import *
import pandas as pd
from assets.theme import theme

def custom1(app, data):
    @app.callback(
        Output('custom1_graph', 'figure'),
        Input('region-filter-5', 'value')  # Value from dropdown
    )
    def update_graph(selected_regions):
        # Filter Data Based on Selected Regions
        if selected_regions:
            filtered_data = data[data['region'].isin(selected_regions)]
        else:
            filtered_data = data[data['region'].isin(['World'])]

        viz = Visualization(filtered_data,theme)

        fig = viz.line(
            x="year",
            y="value",
            title="Oil Displacement Mbd",
            xlabel="Year",
            ylabel="Milion barrels per day"
        )
        return fig