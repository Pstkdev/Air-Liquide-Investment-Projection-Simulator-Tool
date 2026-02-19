
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
    def __init__(self, initial_share_price:float, 
                 initial_shares:int, 
                 initial_dividend:float, 
                 annual_growth_rate:float, 
                 dividend_growth_rate:float, 
                 years:int, 
                 reinvest_dividends:bool, 
                 loyalty_bonus:bool,
                 monthly_investment:float)-> None:
        """
        Initialize simulation parameters:
        
        :param initial_share_price: Initial stock price 
        :param initial_shares: Number of shares initially owned 
        :param initial_dividend: Annual dividend per share 
        :param annual_growth_rate: Expected annual stock price growth rate
        :param dividend_growth_rate: Expected annual dividend growth rate
        :param years: Duration of the simulation in years
        :param reinvest_dividends:  Whether dividends are reinvested 
        :param loyalty_bonus: Whether the Air Liquide loyalty bonus is enabled 
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
        
        self.cash = 0.0 # leftover cash 
        self.lots = {0: initial_shares} # handle 2 years rule : {year_acquired: shares nb}
        
        self.results: pd.DataFrame | None = None
        
        
    def _total_shares(self) -> int:
        return sum(self.lots.values())
    
    def eligible_shares(self, year:int) -> int:
        gap = year-2
        
    
    
        
    def run_simulation(self) -> pd.DataFrame:
        """Run the simulation and store yearly results in self.results."""
        raise NotImplementedError
        
    def plot_results(self):
        """Display portfolio value and total shares over time."""
        raise NotImplementedError
    