from callbacks.custom1 import custom1
from callbacks.custom2 import custom2
from callbacks.share_of_new_electric_cars_that_are_fully_battery_electric import share_of_new_electric_cars_that_are_fully_battery_electric
from callbacks.share_of_new_cars_sold_that_are_battery_electric_and_plug_in_hybrid import share_of_new_cars_sold_that_are_battery_electric_and_plug_in_hybrid
from callbacks.share_of_new_cars_sold_that_are_electric import share_of_new_cars_sold_that_are_electric
from callbacks.share_of_new_cars_sold_that_are_electric_2023 import share_of_new_cars_sold_that_are_electric_2023
from dash.dependencies import Input, Output
from visualize import *
from datetime import datetime

def register_callbacks(app, data):
    share_of_new_cars_sold_that_are_electric_df = data[data["parameter"] == "EV sales share"][['region','year','value']]
    share_of_new_cars_sold_that_are_electric_df = share_of_new_cars_sold_that_are_electric_df.groupby(['region', 'year']).mean().reset_index()
    share_of_new_cars_sold_that_are_electric(app,share_of_new_cars_sold_that_are_electric_df)
    
    share_of_new_cars_sold_that_are_electric_2023_df = data[(data["parameter"] == "EV sales share") & (data["year"] == datetime(2023, 1, 1))][['region','value']]
    share_of_new_cars_sold_that_are_electric_2023(app,share_of_new_cars_sold_that_are_electric_2023_df)
    
    share_of_new_cars_sold_that_are_battery_electric_and_plug_in_hybrid_df = data[data["parameter"] == "EV sales"]
    total_per_year = share_of_new_cars_sold_that_are_battery_electric_and_plug_in_hybrid_df.groupby('year')['value'].transform('sum')
    share_of_new_cars_sold_that_are_battery_electric_and_plug_in_hybrid_df['plug_in_hybrid_percentage'] = (share_of_new_cars_sold_that_are_battery_electric_and_plug_in_hybrid_df['value'] / total_per_year) * 100
    share_of_new_cars_sold_that_are_battery_electric_and_plug_in_hybrid(app, share_of_new_cars_sold_that_are_battery_electric_and_plug_in_hybrid_df)

    share_of_new_electric_cars_that_are_fully_battery_electric_df = data[data["parameter"] == "EV sales"][['region','year','value']]
    share_of_new_electric_cars_that_are_fully_battery_electric_df['full_ev_percentage'] = (share_of_new_electric_cars_that_are_fully_battery_electric_df['value'] / total_per_year) * 100
    share_of_new_electric_cars_that_are_fully_battery_electric_df = share_of_new_electric_cars_that_are_fully_battery_electric_df.groupby(['region', 'year']).mean().reset_index()
    share_of_new_electric_cars_that_are_fully_battery_electric(app, share_of_new_electric_cars_that_are_fully_battery_electric_df)
    
    custom1_df = data[data["parameter"] == "Oil displacement Mbd"][['region','year','value']]
    custom1_df = custom1_df.groupby(['region', 'year']).sum().reset_index()
    custom1(app, custom1_df)
    
    custom2_df = data[data["parameter"] == "Oil displacement Mbd"][['region','year','value']]
    custom2_df = custom2_df.groupby(['region', 'year']).sum().reset_index()
    custom2(app, custom2_df)