import plotly.express as px


def line_chart(df, x, y, title):
    fig = px.line(
        df,
        x=x,
        y=y,
        title=title
    )

    return fig


def histogram(df, column, title):
    fig = px.histogram(
        df,
        x=column,
        title=title
    )

    return fig