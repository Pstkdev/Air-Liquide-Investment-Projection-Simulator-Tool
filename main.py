from src.AirLiquideSimulation import AirLiquideSimulation


def main():
    sim = AirLiquideSimulation(
        initial_share_price=165.0,
        initial_shares=10,
        initial_dividend=3.20,
        annual_growth_rate=0.06,
        dividend_growth_rate=0.05,
        years=20,
        reinvest_dividends=True,
        loyalty_bonus=True,
        monthly_investment=200.0,
    )

    df = sim.run_simulation()

    sim.plot_results()


if __name__ == "__main__":
    main()
