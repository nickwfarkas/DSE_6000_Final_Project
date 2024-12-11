from dash.dependencies import Input, Output
from visualize import *
import pandas as pd
from assets.theme import theme

def custom2(app, data):
    @app.callback(
        Output('custom2_graph', 'figure'),
        Input('region-filter-6', 'value')  # Value from dropdown
    )
    def update_graph(selected_regions):
        # Filter Data Based on Selected Regions
        if selected_regions:
            filtered_data = data[data['region'].isin(selected_regions)]
        else:
            filtered_data = data[data['region'].isin(['World'])]

        viz = Visualization(filtered_data,theme)

        fig = viz.line_facet(
            x="year",
            y="value",
            facet_col="region",
            title="Oil displacement, million lge",
            xlabel="Year",
            ylabel="Oil displacement, million lge"
        )
        return fig