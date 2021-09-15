import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
from datetime import datetime


"""
# See your money grow :dollar:

"""

# Formula in latex

st.latex(r'''
\text{Future Value} = P \left( 1 + \frac{r}{n} \right) ^{nt} + \frac{\left( 1 + \frac{r}{n} \right)^{nt} - 1}{\left(\frac{r}{n}\right)}
''')

principle = st.number_input("Principle",value=1000,step=100,min_value=0)
growth_rate = st.number_input("Growth Rate (%)",min_value=0,value=8,step=1)
rate_var = st.number_input("Variation (% points)", value=2,min_value=0,step=1)
years = st.number_input("Years",step=1,value=10,min_value=0)
monthly_contribution = st.number_input("Monthly Contribution",value=500,min_value=0,step=25)



def valuate(principle, growth_rate, years, monthly_contribution):
    r = growth_rate/100
    t = years
    P = principle
    PMT = monthly_contribution
    n = 12
    principal_with_interest = P*((1 + r/n)**(n*t))
    FVS = PMT * (((1 + r/n)**(n*t) - 1) / (r/n)) * (1 + r/n)

    return principal_with_interest + FVS


# st.bar_chart(data)
today = datetime.today()
avg = [valuate(principle,growth_rate,years=year,monthly_contribution=monthly_contribution) for year in range(int(years))]
low = [valuate(principle,growth_rate-rate_var,year,monthly_contribution) for year in range(int(years))]
high = [valuate(principle,growth_rate+rate_var,year,monthly_contribution) for year in range(int(years))]

df = pd.DataFrame({'Year': [int(year) + int(today.year) for year in range(int(years))],'Avg':avg,'Low':low,'High':high})

melted = pd.melt(df,id_vars=['Year'],value_vars=['Avg','Low','High'],var_name='Rate')

fig = px.line(melted,x='Year',y='value',color='Rate')
st.plotly_chart(fig)

final_year_avg = melted[melted['Rate'] == 'Avg'].iloc[-1]


final_value = "${:,.2f}".format(final_year_avg.value)


st.metric('Final Value',final_value)

# st.write(final_year_avg)



