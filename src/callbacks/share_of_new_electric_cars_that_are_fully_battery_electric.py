from dash.dependencies import Input, Output
from visualize import *
import pandas as pd
from assets.theme import theme

def share_of_new_electric_cars_that_are_fully_battery_electric(app, data):
    @app.callback(
        Output('share_of_new_electric_cars_that_are_fully_battery_electric_line_plot', 'figure'),
        Input('region-filter-4', 'value')  # Value from dropdown
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
            y="full_ev_percentage",
            title="Share of new electric cars that are fully battery-electric",
            xlabel="Year",
            ylabel="EV Share (%)"
        )
        return fig