import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
@st.cache_data
def load_data():
    # Load your dataset here
    # For example:
    data = pd.read_csv("sensor_data.csv")
    return data

# Main function
def main():
    st.title("Interactive Plots")

    # Load the data
    data = load_data()

    # Print the DataFrame
    st.write("Dataframe:", data)

    # Interactive Time Series Plot
    st.title("Interactive Time Series Plot")
    y_variable = st.selectbox("Select Y-axis variable", data.columns[1:])  # Assuming the first column is datetime
    fig_time_series = px.line(data, x='Datetime', y=y_variable, title=f"{y_variable} over Time")
    st.plotly_chart(fig_time_series, use_container_width=True)

    # Seismic Graph
    st.title("Seismic Graph")
    fig_seismic = go.Figure()
    for axis in ['X', 'Y', 'Z']:
        fig_seismic.add_trace(go.Scatter(x=data['Datetime'], y=data[axis], mode='lines', name=f'{axis}'))
    fig_seismic.update_layout(title='Seismic Graph', xaxis_title='Time', yaxis_title='Value')
    st.plotly_chart(fig_seismic, use_container_width=True)

    # Scatter Plots
    st.title("Scatter Plots")
    fig_humidity_temp = px.scatter(data, x='Humidity', y='Temperature', title="Humidity vs. Temperature")
    st.plotly_chart(fig_humidity_temp, use_container_width=True)

    fig_co2_dust = px.scatter(data, x='CO2 Level', y='Dust Density', title="CO2 Level vs. Dust Density")
    st.plotly_chart(fig_co2_dust, use_container_width=True)

    # Interactive Scatter Plot
    st.title("Interactive Scatter Plot")
    x_variable = st.selectbox("Select X-axis variable", data.columns[1:], index=1)  # Assuming the first column is datetime
    y_variable = st.selectbox("Select Y-axis variable", data.columns[1:], index=2)  # Assuming the first column is datetime
    fig_scatter = px.scatter(data, x=x_variable, y=y_variable, title=f"{x_variable} vs. {y_variable}")
    st.plotly_chart(fig_scatter, use_container_width=True)

    # Heatmap
    st.title("Heatmap")
    fig, ax = plt.subplots()
    heatmap = sns.heatmap(data.drop(columns=['Datetime']).corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

    # Stacked Area Charts
    st.title("Stacked Area Charts")
    stacked_area_columns = st.multiselect("Select columns for Stacked Area Charts", data.columns[1:])
    stacked_area = data[stacked_area_columns].cumsum()
    fig_stacked_area = px.area(stacked_area, title="Cumulative Environmental Variables over Time")
    st.plotly_chart(fig_stacked_area, use_container_width=True)

    # 3D Scatter Plots
    st.title("3D Scatter Plot")
    fig_3d_scatter = px.scatter_3d(data, x='X', y='Y', z='Z', title="3D Scatter Plot of X, Y, Z Axes Data")
    st.plotly_chart(fig_3d_scatter, use_container_width=True)

   
    # Bar Charts
    st.title("Bar Charts")
    bar_columns = st.multiselect("Select columns for Bar Charts", data.columns[1:])
    bar_fig = px.bar(data, x='Datetime', y=bar_columns, title="Bar Charts")
    st.plotly_chart(bar_fig, use_container_width=True)

if __name__ == "__main__":
    main()
