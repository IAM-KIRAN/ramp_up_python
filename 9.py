import plotly.graph_objects as go
import pandas as pd

# Read the CSV file into a DataFrame
data = pd.read_csv('skills_data_with_color.csv')

# Define the color scale based on the specified color ranges
color_scale = [
    [0.00, 'rgb(0, 255, 0)'],
    [0.15, 'rgb(0, 255, 0)'],
    [0.15, 'rgb(0, 238, 0)'],
    [0.30, 'rgb(0, 238, 0)'],
    [0.30, 'rgb(0, 205, 0)'],
    [0.45, 'rgb(0, 205, 0)'],
    [0.45, 'rgb(0, 139, 0)'],
    [0.60, 'rgb(0, 139, 0)'],
    [0.60, 'rgb(0, 128, 0)'],
    [0.75, 'rgb(0, 128, 0)'],
    [0.75, 'rgb(154, 205, 50)'],
    [0.90, 'rgb(154, 205, 50)'],
    [0.90, 'rgb(255, 223, 0)'],
    [1.00, 'rgb(255, 223, 0)'],
]

# Create a heatmap figure
fig = go.Figure(data=go.Heatmap(
    x=data['Skill'],
    z=data['Value'],
    #z=data['Value'],
    hoverongaps = False, # to ensure the whole heatmap is rectangular
    colorscale=color_scale,
    colorbar=dict(
        title='Skill Value',
        tickvals=list(range(31)),
        ticktext=[str(i) for i in range(31)]
    ),
))

# Update the layout
fig.update_layout(
    title="Skill Value Heatmap",
    xaxis_title="Skills",
    yaxis_title="Index",
)

# Show the figure
fig.show()
