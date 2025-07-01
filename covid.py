# Import libraries for data analysis and manipulation
import plotly.graph_objs as go
import plotly.io as pio
import plotly.express as px
import pandas as pd

# Import libraries for data visualization
import matplotlib.pyplot as plt

# Importing Plotly's offline verision 
import plotly.offline as py
py.init_notebook_mode(connected=True)

# Initializing Plotly
pio.renderers.default = 'colab'