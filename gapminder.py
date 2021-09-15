import streamlit as st
import plotly.express as px
import pandas as pd

gm = px.data.gapminder()

st.write(gm)

fig = px.scatter(
    gm,
    x="gdpPercap",
    y="lifeExp",
    color="continent",
    size="pop",
    animation_frame="year",
    log_x=True,
    range_y=[25, 95],
    hover_name="country",
    height=600,
    size_max=100,
)

st.write(fig)

exp = px.data.experiment()

exp = pd.melt(
    exp,
    id_vars=["gender", "group"],
    value_name="result",
    value_vars=["experiment_1", "experiment_2", "experiment_3"],
    var_name="experiment",
)
st.write(exp)

exp.experiment = exp.experiment.apply(lambda x: x.replace("experiment_", ""))

st.write(
    pd.pivot_table(
        exp, columns=["gender", "group"], index="experiment", values="result"
    )
)
