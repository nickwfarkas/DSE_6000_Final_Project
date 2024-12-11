from visualize import Visualization
from dash.dependencies import Input, Output
import pandas as pd
from assets.theme import theme


def share_of_new_cars_sold_that_are_electric_2023(app, data):
    @app.callback(
        Output('share_of_new_cars_sold_that_are_electric_2023_h_bar_plot', 'figure'),
        Input('region-filter-2', 'value')  # Value from dropdown
    )
    def update_graph(selected_regions):
        # Filter Data Based on Selected Regions
        if selected_regions:
            filtered_data = data[data['region'].isin(selected_regions)].dropna()
        else:
            filtered_data = data[data['region'].isin(['World'])].dropna()  # Default: Show all data

        viz = Visualization(filtered_data,theme)
        
        fig = viz.bar(
            x="region",
            y="value",
            title="EV Share by Region",
            xlabel="Region",
            ylabel="EV Share (%)",
            orientation="v")
        return fig