import pandas as pd
import matplotlib.pyplot as plt


class AirLiquideSimulation:
    """Deterministic long-term investment simulator for Air Liquide shares.
    v1:
    - deterministic annual growth for price and dividend
    - optional dividend reinvestment
    - optional loyalty bonus (dividend + free shares)
    - optional fixed monthly investment
    """

    def __init__(
        self,
        initial_share_price: float,
        initial_shares: int,
        initial_dividend: float,
        annual_growth_rate: float,
        dividend_growth_rate: float,
        years: int,
        reinvest_dividends: bool,
        loyalty_bonus: bool,
        monthly_investment: float,
    ) -> None:
        """
        Initialize simulation parameters:

        :param initial_share_price: Initial stock price
        :param initial_shares: Number of shares initially owned
        :param initial_dividend: Annual dividend per share
        :param annual_growth_rate: Expected annual stock price growth rate
        :param dividend_growth_rate: Expected annual dividend growth rate
        :param years: Duration of the simulation in years
        :param reinvest_dividends:  Whether dividends are reinvested
        :param loyalty_bonus: Whether the Air Liquide loyalty bonus is enabled (nominatif)
        :param monthly_investment: Additional fixed monthly investment amount
        """
        self.initial_share_price = initial_share_price

        if initial_share_price <= 0:
            raise ValueError("initial_share_price must be > 0")

        self.initial_shares = initial_shares

        if not isinstance(initial_shares, int):
            raise TypeError("initial_shares must be an int (no fractional shares).")
        if initial_shares < 0:
            raise ValueError("initial_shares must be >= 0")

        self.initial_dividend = initial_dividend
        self.annual_growth_rate = annual_growth_rate
        self.dividend_growth_rate = dividend_growth_rate

        self.years = years
        if years <= 0:
            raise ValueError("years must be >= 1")

        self.reinvest_dividends = reinvest_dividends
        self.loyalty_bonus = loyalty_bonus
        self.monthly_investment = monthly_investment

        self.cash = 0.0  # leftover cash
        self.lots = {
            0: initial_shares
        }  # handle 2 years rule : {year_acquired: shares nb}

        self.results: pd.DataFrame | None = None

    def _total_shares(self) -> int:
        return sum(self.lots.values())

    def _eligible_shares(self, year: int) -> int:
        gap = year - 2
        return sum(shares for y, shares in self.lots.items() if y <= gap)

    def _apply_free_share_attribution(
        self, year: int, share_price: float
    ) -> tuple[int, float]:
        """
        Share attribution logic (based on the rule quoted by Air Liquide in FICHES PRATIQUES DE L'ACTIONNAIRE 2025):
        - Only eligible shares (held for >= 2 full calendar years) receive free shares
        - Base: 1 free share per 10 eligible shares
        - If loyalty_bonus (nominatif): +10% on free shares => 1 extra free share per 100 eligible shares
        - Fractions (rompus) are paid in cash
        Returns: (free_shares_number, rompu_cash_amount)
        """
        eligible = self._eligible_shares(year)

        # base case : 1 for 10
        base_exact = eligible / 10
        base_int = eligible // 10
        base_rompu = (base_exact - base_int) * share_price

        if not self.loyalty_bonus:
            return int(base_int), float(base_rompu)

        # Prime nominatif: +10% on free shares
        prime_exact = eligible / 100
        prime_int = eligible // 100
        prime_rompu = (prime_exact - prime_int) * share_price

        free_shares = base_int + prime_int
        rompu = base_rompu + prime_rompu

        return free_shares, rompu

    def _is_attribution_year(self, year: int) -> bool:
        return year % 2 == 0

    def _calculate_dividends(self, year: int, dividend_per_share: float) -> float:
        total = self._total_shares()

        if not self.loyalty_bonus:
            return total * dividend_per_share

        eligible = self._eligible_shares(year)
        not_eligible = total - eligible
        base_dividend = not_eligible * dividend_per_share
        prime_dividend = eligible * (dividend_per_share * 1.10)
        total_dividend = base_dividend + prime_dividend

        return total_dividend

    def _buy_shares_with_cash(self, year: int, share_price: float) -> tuple[int, float]:

        if share_price <= 0:
            raise ValueError("Share price must be > 0")

        if self.cash < share_price:
            return 0, 0.0

        shares_bought = int(self.cash // share_price)
        cash_spent = shares_bought * share_price
        self.cash -= cash_spent

        self.lots[year] = self.lots.get(year, 0) + shares_bought

        return shares_bought, cash_spent

    def run_simulation(self) -> pd.DataFrame:
        """Run the simulation and store yearly results in self.results"""
        raise NotImplementedError

    def plot_results(self):
        """Display portfolio value and total shares over time"""
        raise NotImplementedError
