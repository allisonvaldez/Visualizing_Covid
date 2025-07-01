"""
This project explores Covid-19 data from ___ and will visualize it using Ployly
Express in Python. It will provide more than a dozen of bar charts, line graphs,
bubble charts, and scatter plots. Exploration of the data will help people to
understand likely complex scenarios unfolding to make predictions for the future.
It will examine the impacts of conducting preventative measures and other 
hygenic practices. It will provide some arguements on which health resources will
best manage the outbreak. In closing, this project will summerize modeling,
simulation, and analysis.

Tools and technology used in the project: Google Colab(Runtime type - GPU).

Requirements to Build the Project: 
    Basic knowledge of Python
    Basic understanding of graphs and charts
    Data visualization
    Pandas
    Numpy
    Matplotlib
    Plotly Express
    Choropleth
    Wordcloud
"""

# STEP 1: IMPORT DEPENDENCIES AND LIBRARIES
# Import libraries for data analysis and manipulation
import plotly.graph_objs as go
import plotly.io as pio
import plotly.express as px
import pandas as pd

print(f"Plotly version: {plotly.__version__}")
print(f"Pandas version: {pandas.__version__}")
print(f"Matplotlib version: {matplotlib.__version__}")

# Import libraries for data visualization
import matplotlib.pyplot as plt

# Importing Plotly's offline verision 
import plotly.offline as py
py.init_notebook_mode(connected=True)

# Initialize Plotly
pio.renderers.default = 'colab'

# STEP 2: IMPORT DATASETS
"""
The following data is contained in the files:
1. covid.csv- contains Country/Region, Continent,  Population, TotalCases, 
    NewCases, TotalDeaths, NewDeaths,  TotalRecovered, NewRecovered, ActiveCases,
    Serious, Critical, Tot Cases/1M pop, Deaths/1M pop, TotalTests, Tests/1M pop,
    WHO Region, iso_alpha.
2. covid_grouped: contains Date(from 20-01-22 to 20-07-27), Country/Region, 
    Confirmed, Deaths, Recovered, Active, New cases, New deaths, New recovered,
    WHO Region, iso_alpha.
3. coviddeath: contains real-world examples of a number of Covid-19 deaths and the 
    reasons behind the deaths.
"""

dataset1 = pd.read_csv("./data/covid.csv")
dataset1.head()
