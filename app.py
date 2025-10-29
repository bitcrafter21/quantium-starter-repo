import pandas as pd
import dash
from dash import html, dcc
import plotly.express as px

# Load processed data
df = pd.read_csv("processed_data/pink_morsel_sales.csv")

# Ensure proper sorting and date type
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    color="region",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Total Sales ($)", "region": "Region"},
)

# Add vertical line for price increase (15 Jan 2021)
fig.add_vline(x="2021-01-15", line_width=2, line_dash="dash", line_color="red")

# Dash app setup
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods: Pink Morsel Sales Visualiser", style={"textAlign": "center"}),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
