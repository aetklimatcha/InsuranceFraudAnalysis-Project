# utils 를 잘 활용하면 다른 노트북 파일에서 import 해오는 식으로 활용 가능함
# from utils import * or from utils import 가져오고 싶은 것들 지정

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# 인풋과 아웃풋 정의 제공
def plot_count_plot(df: pd.DataFrame, column_name: str) -> px.histogram:
    """
    **docstring 형태로 넣어두면 나중에 활용하기가 훨씬 편함**

    Generate a count plot for a specified column in the DataFrame using Plotly.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing the data.
    column_name : str
        The name of the column for which to create the count plot.

    Returns
    -------
    plotly.graph_objs._figure.Figure
        The Plotly figure object representing the count plot.
    """
    fig = px.histogram(
        df,
        x=column_name,
        title=f"Count Plot of {column_name}",
        category_orders={column_name: df[column_name].value_counts().index},
    )
    return fig


def plot_histogram(df: pd.DataFrame, column_name: str) -> px.histogram:
    """
    Generate a histogram for a specified column in the DataFrame using Plotly.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing the data.
    column_name : str
        The name of the column for which to create the histogram.

    Returns
    -------
    plotly.graph_objs._figure.Figure
        The Plotly figure object representing the histogram.
    """
    fig = px.histogram(df, x=column_name, title=f"Histogram of {column_name}")
    return fig


def plot_dataframe(df: pd.DataFrame) -> None:
    """
    Generate and display count plots or histograms for all columns in the DataFrame.
    For numeric columns, generate histograms.
    For categorical columns, generate count plots.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing the data.

    Returns
    -------
    None
    """
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            fig = plot_histogram(df, column)
        elif pd.api.types.is_object_dtype(df[column]):
            fig = plot_count_plot(df, column)
        else:
            continue
        fig.show()
