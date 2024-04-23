import streamlit as st
import dash
from dash import dcc, html
import panel as pn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

# Log running times
def log_running_time(name, time_taken):
    with open("running_times.log", "a") as f:
        f.write(f"{name}: {time_taken}\n")

# Streamlit 
def streamlit_example():
    st.title('Streamlit Example')
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    st.line_chart(data={'x': x, 'y': y})

# Dash 
def dash_example():
    app = dash.Dash(__name__)
    app.layout = html.Div([
        html.H1('Dash Example'),
        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': np.linspace(0, 10, 100), 'y': np.sin(np.linspace(0, 10, 100)), 'type': 'line', 'name': 'sin(x)'},
                ],
                'layout': {
                    'title': 'Dash Plot'
                }
            }
        )
    ])
    
    return app

# Panel 
def panel_example():
    pn.extension()
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title('Panel Example')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    pn.pane.Matplotlib(plt.gcf())
    pn.Row(plt.gcf())

# Measure running time for Panel
start_time = time.time()
panel_example()
panel_time = time.time() - start_time
print("Panel Running Time:", panel_time)
log_running_time("Panel", panel_time)


# Measure running time for Streamlit
start_time = time.time()
streamlit_example()
streamlit_time = time.time() - start_time
print("Streamlit Running Time:", streamlit_time)
log_running_time("Streamlit", streamlit_time)

# Measure setup time for Dash
start_time = time.time()
dash_app = dash_example()
dash_setup_time = time.time() - start_time
print("Dash Example Setup Time:", dash_setup_time)
log_running_time("Dash Setup", dash_setup_time)

start_time = time.time()
dash_app.run_server(port=8050, debug=False)
dash_running_time = time.time() - start_time
print("Dash Running Time:", dash_running_time)
log_running_time("Dash Running", dash_running_time)

