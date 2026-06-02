# EV Market Forecast Dashboard


# Install Libraries:
# py -m pip install dash plotly pandas numpy scikit-learn

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html

# ---------------------------------------------------
# Dataset
# ---------------------------------------------------

data = {
    "Year": [2018, 2019, 2020, 2021, 2022, 2023],
    "Global_EV_Sales_Million": [2.1, 2.3, 3.2, 6.6, 10.5, 14.0],
    "Government_Subsidy_Billion": [12, 15, 20, 28, 35, 40],
    "Charging_Stations_Million": [0.3, 0.5, 0.8, 1.2, 1.8, 2.5]
}

df = pd.DataFrame(data)

# ---------------------------------------------------
# Machine Learning Forecast
# ---------------------------------------------------

X = df[["Year"]]
y = df["Global_EV_Sales_Million"]

model = LinearRegression()
model.fit(X, y)

future_years = np.array([2024, 2025, 2026, 2027, 2028]).reshape(-1, 1)
predictions = model.predict(future_years)

forecast_df = pd.DataFrame({
    "Year": future_years.flatten(),
    "Predicted_EV_Sales_Million": predictions
})

# ---------------------------------------------------
# Graph 1 - EV Sales Trend
# ---------------------------------------------------

fig_sales = px.line(
    df,
    x="Year",
    y="Global_EV_Sales_Million",
    markers=True,
    title="Global EV Sales Trend"
)

fig_sales.update_layout(
    template="plotly_dark",
    paper_bgcolor="#1e1e2f",
    plot_bgcolor="#1e1e2f",
    title_x=0.5
)

# ---------------------------------------------------
# Graph 2 - Forecast
# ---------------------------------------------------

fig_forecast = go.Figure()

fig_forecast.add_trace(
    go.Scatter(
        x=df["Year"],
        y=df["Global_EV_Sales_Million"],
        mode='lines+markers',
        name='Actual Sales'
    )
)

fig_forecast.add_trace(
    go.Scatter(
        x=forecast_df["Year"],
        y=forecast_df["Predicted_EV_Sales_Million"],
        mode='lines+markers',
        name='Forecast Sales'
    )
)

fig_forecast.update_layout(
    title="EV Market Forecast",
    template="plotly_dark",
    paper_bgcolor="#1e1e2f",
    plot_bgcolor="#1e1e2f",
    title_x=0.5
)

# ---------------------------------------------------
# Graph 3 - Subsidy Analysis
# ---------------------------------------------------

fig_policy = px.bar(
    df,
    x="Year",
    y="Government_Subsidy_Billion",
    title="Government Subsidy Analysis"
)

fig_policy.update_layout(
    template="plotly_dark",
    paper_bgcolor="#1e1e2f",
    plot_bgcolor="#1e1e2f",
    title_x=0.5
)

# ---------------------------------------------------
# Graph 4 - Charging Stations
# ---------------------------------------------------

fig_station = px.line(
    df,
    x="Year",
    y="Charging_Stations_Million",
    markers=True,
    title="Charging Station Growth"
)

fig_station.update_layout(
    template="plotly_dark",
    paper_bgcolor="#1e1e2f",
    plot_bgcolor="#1e1e2f",
    title_x=0.5
)

# ---------------------------------------------------
# Graph 5 - EV Adoption Map
# ---------------------------------------------------

country_data = pd.DataFrame({
    "Country": ["USA", "China", "India", "Germany", "UK"],
    "EV_Adoption": [15, 40, 8, 20, 18]
})

fig_map = px.choropleth(
    country_data,
    locations="Country",
    locationmode="country names",
    color="EV_Adoption",
    title="Global EV Adoption Map"
)

fig_map.update_layout(
    template="plotly_dark",
    paper_bgcolor="#1e1e2f",
    plot_bgcolor="#1e1e2f",
    title_x=0.5
)

# ---------------------------------------------------
# Dash App
# ---------------------------------------------------

app = Dash(__name__)

app.layout = html.Div(

    style={
        'background': 'linear-gradient(to right, #141e30, #243b55)',
        'padding': '20px',
        'fontFamily': 'Arial'
    },

    children=[

        html.H1(
            "EV MARKET FORECAST DASHBOARD",
            style={
                'textAlign': 'center',
                'color': 'cyan',
                'fontSize': '45px',
                'padding': '20px'
            }
        ),

        html.H3(
            "Interactive Analysis of Global Electric Vehicle Growth",
            style={
                'textAlign': 'center',
                'color': 'white',
                'marginBottom': '30px'
            }
        ),

        # Features Box
        html.Div(

            children=[

                html.H2(
                    "Project Features",
                    style={
                        'color': 'yellow',
                        'textAlign': 'center'
                    }
                ),

                html.Ul([

                    html.Li(
                        "EV Sales Trend Analysis",
                        style={'color': 'white', 'fontSize': '18px'}
                    ),

                    html.Li(
                        "Machine Learning Forecast",
                        style={'color': 'white', 'fontSize': '18px'}
                    ),

                    html.Li(
                        "Government Subsidy Analysis",
                        style={'color': 'white', 'fontSize': '18px'}
                    ),

                    html.Li(
                        "Charging Station Growth",
                        style={'color': 'white', 'fontSize': '18px'}
                    ),

                    html.Li(
                        "Global EV Adoption Map",
                        style={'color': 'white', 'fontSize': '18px'}
                    ),

                    html.Li(
                        "Interactive Plotly Dashboard",
                        style={'color': 'white', 'fontSize': '18px'}
                    )

                ])

            ],

            style={
                'backgroundColor': '#1e1e2f',
                'padding': '20px',
                'borderRadius': '15px',
                'marginBottom': '30px',
                'boxShadow': '0px 0px 15px cyan'
            }

        ),

        dcc.Graph(figure=fig_sales),

        dcc.Graph(figure=fig_forecast),

        dcc.Graph(figure=fig_policy),

        dcc.Graph(figure=fig_station),

        dcc.Graph(figure=fig_map)

    ]
)

# ---------------------------------------------------
# Run App
# ---------------------------------------------------

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
