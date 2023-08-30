import plotly.graph_objects as go
import pandas as pd

# Read the CSV file into a DataFrame
data = pd.read_csv('skills_data_with_color.csv')

# Define the color scale based on the specified color ranges
color_scale = [
    [0.00, 'rgb(0, 255, 0)'],
    [0.15, 'rgb(0, 238, 0)'],
    [0.30, 'rgb(0, 205, 0)'],
    [0.45, 'rgb(0, 139, 0)'],
    [0.60, 'rgb(0, 128, 0)'],
    [0.75, 'rgb(154, 205, 50)'],
    [0.90, 'rgb(255, 223, 0)'],
    [1.00, 'rgb(255, 223, 0)'],
]

# Create a heatmap figure
fig = go.Figure()

for index, row in data.iterrows():
    value = row['Value']
    skill = row['Skill']

    # Map value to color based on the defined color scale
    color = 'rgb(0, 255, 0)'  # Default color
    for threshold, col in color_scale:
        if value >= threshold:
            color = col
            break

    fig.add_shape(
        type='rect',
        x0=index - 0.5,
        x1=index + 0.5,
        y0=0,
        y1=value,
        fillcolor=color,
        opacity=0.8,
        layer='below'
    )

    fig.add_annotation(
        x=index,
        y=value / 2,
        text=f"Skill: {skill}<br>Value: {value}",
        showarrow=False,
        font=dict(size=8, color='black'),
    )

# Update the layout
fig.update_layout(
    title="Skill Value Heatmap",
    xaxis_title="Skills",
    yaxis_title="Value",
    xaxis=dict(tickvals=list(range(len(data))), ticktext=data['Skill']),
)

# Show the figure
fig.show()
