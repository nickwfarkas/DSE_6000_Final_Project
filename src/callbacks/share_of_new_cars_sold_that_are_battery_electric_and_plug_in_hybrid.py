from dash.dependencies import Input, Output
from visualize import *
import pandas as pd
from assets.theme import theme

def share_of_new_cars_sold_that_are_battery_electric_and_plug_in_hybrid(app, data):
    @app.callback(
        Output('share_of_new_cars_sold_that_are_battery_electric_and_plug_in_hybrid_bar_faceted_plot', 'figure'),
        Input('region-filter-3', 'value')  # Value from dropdown
    )
    def update_graph(selected_regions):
        # Filter Data Based on Selected Regions
        if selected_regions:
            filtered_data = data[data['region'].isin(selected_regions)]
        else:
            filtered_data = data[data['region'].isin(['World'])]

        viz = Visualization(filtered_data,theme)

        fig = viz.bar_stacked_facet(
            x="year",
            y="plug_in_hybrid_percentage",
            title="Share of new cars sold that are battery-electric and plug-in hybrid",
            xlabel="Year",
            ylabel="EV Share (%)",
            facet_col="region",
            layer="powertrain"
        )
        return fig