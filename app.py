import streamlit as st
import plotly.express as px

from src.AirLiquideSimulation import AirLiquideSimulation


st.set_page_config(page_title="Air Liquide Simulator", layout="wide")
st.title("Air Liquide Investment Projection Simulator")

# ----- Sidebar controls -----
st.sidebar.header("Parameters")

initial_share_price = st.sidebar.number_input("Initial share price (€)", min_value=0.01, value=160.0, step=1.0)
initial_shares = st.sidebar.number_input("Initial number of shares owned", min_value=0, value=10, step=1)
initial_dividend = st.sidebar.number_input("Initial dividend per share (€)", min_value=0.0, value=3.3, step=0.1)

annual_growth_rate = st.sidebar.number_input("Annual share price growth rate", min_value=0.01, value=0.06, step=0.01)
dividend_growth_rate = st.sidebar.number_input("Annual dividend growth rate", min_value=0.01, value=0.06, step=0.01)

years = st.sidebar.number_input("Years", min_value=1, value=20, step=1)
start_year = st.sidebar.number_input("Starting year", min_value=2026, value=2026, step=1)

monthly_investment = st.sidebar.number_input("Monthly investment (€)", min_value=0.0, value=200.0, step=10.0)

reinvest_dividends = st.sidebar.checkbox("Reinvest dividends", value=True)
loyalty_bonus = st.sidebar.checkbox("Loyalty bonus (nominatif + 2 year rule)", value=True)


sim = AirLiquideSimulation(
    initial_share_price=float(initial_share_price),
    initial_shares=int(initial_shares),
    initial_dividend=float(initial_dividend),
    annual_growth_rate=float(annual_growth_rate),
    dividend_growth_rate=float(dividend_growth_rate),
    years=int(years),
    start_year=int(start_year),
    reinvest_dividends=bool(reinvest_dividends),
    loyalty_bonus=bool(loyalty_bonus),
    monthly_investment=float(monthly_investment),
)

df = sim.run_simulation()

# ----- Summary -----
last = df.iloc[-1]
final_value = float(last["Portfolio value"])
final_shares = int(last["Total shares"])
total_div = float(last["Total dividends received"])
total_invested = float(last["Total invested"])
final_cash = float(last["Cash"])
annual_div = float(last["Dividends received"])
total_free = int(last["Total free shares received"])

total_return = 0.0
if total_invested > 0:
    total_return = (final_value - total_invested) / total_invested * 100

col1, col2, col3, col4 = st.columns(4)

col1.metric("Final portfolio value", f"€{final_value:,.2f}")
col1.metric("Final shares", f"{final_shares}")

col2.metric("Total invested", f"€{total_invested:,.2f}")
col2.metric("Total dividends received", f"€{total_div:,.2f}")

col3.metric("Final cash", f"€{final_cash:,.2f}")
col3.metric("Total return", f"{total_return:.2f}%")

col4.metric("Dividend income per year", f"€{annual_div:,.2f}")
col4.metric("Total free shares received", f"{total_free}")

st.divider()

# ----- Plots -----
fig_value = px.line(df, x="Calendar year", y="Portfolio value", title="Portfolio value over time")
st.plotly_chart(fig_value, use_container_width=True)

fig_shares = px.line(df, x="Calendar year", y="Total shares", title="Total shares over time")
st.plotly_chart(fig_shares, use_container_width=True)

st.divider()
st.subheader("Simulation results")
st.dataframe(df, use_container_width=True)
