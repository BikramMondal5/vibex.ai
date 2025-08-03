import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(
    page_title="VibexAI Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# App title and description
st.title("VibexAI Dashboard")
st.markdown("### A simple interactive data visualization app")

# Sidebar
st.sidebar.header("Settings")

# Sample data generation
def generate_sample_data(size=100):
    dates = pd.date_range('20250101', periods=size)
    data = pd.DataFrame({
        'date': dates,
        'data_value': np.random.randn(size).cumsum(),  # Changed 'value' to 'data_value'
        'category': np.random.choice(['A', 'B', 'C'], size=size)
    })
    return data

# Data options
data_size = st.sidebar.slider("Sample data size", 10, 500, 100)
data = generate_sample_data(data_size)

# Display options
st.sidebar.subheader("Display Options")
show_raw_data = st.sidebar.checkbox("Show raw data", False)
chart_type = st.sidebar.selectbox(
    "Chart Type", 
    ["Line Chart", "Bar Chart", "Scatter Plot"]
)

# Main content area
st.header("Data Visualization")

# Visualize the data
if chart_type == "Line Chart":
    # Fixed approach: provide the DataFrame with date as index
    chart_data = data.set_index('date')
    st.line_chart(chart_data['data_value'])
elif chart_type == "Bar Chart":
    # Group by category and use the renamed column
    bar_data = data.groupby('category')['data_value'].sum().reset_index()
    st.bar_chart(bar_data.set_index('category'))
else:
    fig, ax = plt.subplots()
    ax.scatter(data['date'], data['data_value'], c=data['category'].astype('category').cat.codes)
    st.pyplot(fig)

# Show raw data if selected
if show_raw_data:
    st.subheader("Raw Data")
    st.dataframe(data)

# App footer
st.markdown("---")
st.markdown("Built with Streamlit by VibexAI")