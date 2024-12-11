from dash.dependencies import Input, Output
from visualize import *
import pandas as pd
from assets.theme import theme

def share_of_new_cars_sold_that_are_electric(app, data):
    @app.callback(
        Output('share_of_new_cars_sold_that_are_electric_line_faceted_plot', 'figure'),
        Input('region-filter-1', 'value')  # Value from dropdown
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
            title="Share of New Cars Sold That Are Electric Over Time",
            xlabel="Year",
            ylabel="EV Share (%)",
            facet_col="region"
        )
        return fig