import pandas as pd
import plotly.express as px

class Visualization():
    def __init__(self, data, theme):
        self.data = data
        self.theme = theme

    def bar(self, x, y, title, xlabel, ylabel, orientation='v'):
        fig = px.bar(
            self.data,
            x=x,
            y=y,
            labels={x: xlabel, y: ylabel},
            title=title,
            color_discrete_sequence=['#F4D03F'],
            orientation=orientation
        )
        
        fig.update_layout(
            paper_bgcolor=self.theme["background"],
            plot_bgcolor=self.theme["background"],
            font=dict(color=self.theme["text"]),
            title_font_size=16,
            legend_title_font_size=12,
        )        
        return fig
    
    def line(self, x, y, title, xlabel, ylabel):
        fig = px.line(
            self.data,
            x=x,
            y=y,
            labels={x: xlabel, y: ylabel},
            title=title,
            color_discrete_sequence=['#F4D03F']
        )
        
        fig.update_layout(
            paper_bgcolor=self.theme["background"],
            plot_bgcolor=self.theme["background"],
            font=dict(color=self.theme["text"]),
            title_font_size=16,
            legend_title_font_size=12,
            xaxis=dict(showgrid=True, gridcolor="gray"),
            yaxis=dict(showgrid=True, gridcolor="gray")
        )
        return fig
    
    def pie(self, names, values, title):
        fig = px.pie(
            self.data,
            names=names,
            values=values,
            title=title,
            color_discrete_sequence=['#F4D03F', '#FFD700', '#FDFEFE']
        )
        
        fig.update_layout(  # Customize layout
            paper_bgcolor=self.theme["background"],
            plot_bgcolor=self.theme["background"],
            font=dict(color=self.theme["text"]),
            title_font_size=16,
            legend_title_font_size=12,
        )
        return fig

    def scatter(self, x, y, title, xlabel, ylabel):
        fig = px.scatter(
            self.data,
            x=x,
            y=y,
            labels={x: xlabel, y: ylabel},
            title=title,
            color_discrete_sequence=['#F4D03F']
        )
        
        fig.update_layout(
            paper_bgcolor=self.theme["background"],
            plot_bgcolor=self.theme["background"],
            font=dict(color=self.theme["text"]),
            title_font_size=16,
            legend_title_font_size=12,
            xaxis=dict(showgrid=True, gridcolor="gray"),
            yaxis=dict(showgrid=True, gridcolor="gray")
        )
        return fig
    
    def histogram(self, x, y, title, xlabel, ylabel):
        fig = px.histogram(
            self.data,
            x=x,
            y=y,
            labels={x: xlabel, y: ylabel},
            title=title,
            color_discrete_sequence=['#F4D03F']
        )
        
        fig.update_layout(
            paper_bgcolor=self.theme["background"],
            plot_bgcolor=self.theme["background"],
            font=dict(color=self.theme["text"]),
            title_font_size=16,
            legend_title_font_size=12,
            xaxis=dict(showgrid=True, gridcolor="gray"),
            yaxis=dict(showgrid=True, gridcolor="gray")
        )
        return fig
    
    def line_facet(self, x, y, facet_col, title, xlabel, ylabel):
        fig = px.line(
            self.data,
            x=x,
            y=y,
            facet_col=facet_col,
            labels={x: xlabel, y: ylabel, facet_col: facet_col},
            title=title,
            color_discrete_sequence=['#F4D03F'],
            facet_col_wrap=3,
            facet_row_spacing=0.01
        )
        
        fig.update_traces(connectgaps=True)
        
        fig.update_layout(
            paper_bgcolor=self.theme["background"],
            plot_bgcolor=self.theme["background"],
            font=dict(color=self.theme["text"]),
            title_font_size=16,
            legend_title_font_size=12,
            margin=dict(t=50, b=50, r=50, l=50)
        )
        return fig

    def bar_facet(self, x, y, facet_col, title, xlabel, ylabel):
        fig = px.bar(
            self.data,
            x=x,
            y=y,
            facet_col=facet_col,
            labels={x: xlabel, y: ylabel, facet_col: facet_col},
            title=title,
            color_discrete_sequence=['#F4D03F'],
            facet_col_wrap=3,
            facet_row_spacing=0.01
            
        )
        
        fig.update_layout(
            paper_bgcolor=self.theme["background"],
            plot_bgcolor=self.theme["background"],
            font=dict(color=self.theme["text"]),
            title_font_size=16,
            legend_title_font_size=12,
            xaxis=dict(showgrid=True, gridcolor="gray"),
            yaxis=dict(showgrid=True, gridcolor="gray"),
            margin=dict(t=50, b=50, r=50, l=50)
        )
        return fig
    
    def bar_stacked_facet(self, x, y, layer, facet_col, title, xlabel, ylabel):
        fig = px.bar(
            self.data,
            x=x,
            y=y,
            facet_col=facet_col,
            labels={x: xlabel, y: ylabel, facet_col: facet_col},
            title=title,
            color_discrete_sequence=['#F4D03F'],
            facet_col_wrap=3,
            facet_row_spacing=0.01,
            color=layer,
            barmode='stack' 
        )
        
        fig.update_layout(
            paper_bgcolor=self.theme["background"],
            plot_bgcolor=self.theme["background"],
            font=dict(color=self.theme["text"]),
            title_font_size=16,
            legend_title_font_size=12,
            xaxis=dict(showgrid=True, gridcolor="gray"),
            yaxis=dict(showgrid=True, gridcolor="gray"),
            margin=dict(t=50, b=50, r=50, l=50)
        )
        return fig
    
    def heat_map(self, countries, weight, title):
        fig = px.choropleth(
            self.data,
            locations=countries,  # Column with country names
            locationmode="country names",  # Match country names
            color=weight,  # Data to color-code
            color_continuous_scale="Viridis",  # Color scale
            title=title
        )
        
        fig.update_layout(
            geo=dict(
                showframe=False,
                showcoastlines=True,
                projection_type='equirectangular'  # Map projection type
            ),
            paper_bgcolor=self.theme["background"],
            plot_bgcolor=self.theme["background"],
            font=dict(color=self.theme["text"]),
            title_font_size=16,
            legend_title_font_size=12,
            xaxis=dict(showgrid=True, gridcolor="gray"),
            yaxis=dict(showgrid=True, gridcolor="gray"),
            margin=dict(t=50, b=50, r=50, l=50)
        )
        return fig
    
    def model_eval(self, actual, pred):
        fig = px.line(actual, x="year", y="value", title="Oil Displacement Forecast")
        fig.add_scatter(x=pred["year"], y=pred["value"], mode="lines+markers", name="Median Forecast")
        fig.update_layout(
            xaxis_title="Year",
            yaxis_title="Displacement",
            paper_bgcolor=self.theme["background"],
            plot_bgcolor=self.theme["background"],
            font=dict(color=self.theme["text"]),
            title_font_size=16,
            legend_title_font_size=12,
            xaxis=dict(showgrid=True, gridcolor="gray"),
            yaxis=dict(showgrid=True, gridcolor="gray"),
        )
        return fig