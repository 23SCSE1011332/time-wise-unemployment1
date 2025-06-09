import pandas as pd
import plotly.express as px

data = {
    'Year': [2016, 2017, 2018, 2019, 2020, 2021, 2022],
    'Unemployment Rate (%)': [7.5, 7.3, 6.8, 6.5, 8.1, 7.0, 6.7]
}

df = pd.DataFrame(data)

fig = px.line(df, x='Year', y='Unemployment Rate (%)',
              title='Time-wise Unemployment Rate',
              markers=True)

fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Unemployment Rate (%)',
    template='plotly_white'
)

fig.show(renderer="browser")

# Save data as CSV
df.to_csv("unemployment_data.csv", index=False)
