
class AirLiquideSimulation:
    """
        models and projects the long-term growth of an investment in
        Air Liquide shares over a given number of years.
    """
    def __init__(self, initial_share_price:float, initial_shares:int, initial_dividend:float, 
                 annual_growth_rate:float, dividend_growth_rate:float, years:int, 
                 reinvest_dividends:bool, loyalty_bonus:bool,monthly_investment:float):
        """
        Initialize simulation parameters:
        
        :param initial_share_price: Initial stock price 
        :param initial_shares: Number of shares initially owned 
        :param initial_dividend: Annual dividend per share 
        :param annual_growth_rate: Expected annual stock price growth rate
        :param dividend_growth_rate: Description
        :param years: Duration of the simulation in years
        :param reinvest_dividends:  Whether dividends are reinvested 
        :param loyalty_bonus: Whether the Air Liquide loyalty bonus is enabled 
        :param monthly_investment: Additional fixed monthly investment amount
        """
        self.initial_share_price = initial_share_price
        self.initial_shares = initial_shares
        self.initial_dividend = initial_dividend
        self.annual_growth_rate = annual_growth_rate
        self.dividend_growth_rate = dividend_growth_rate
        self.years = years
        self.reinvest_dividends = reinvest_dividends
        self.loyalty_bonus = loyalty_bonus
        self.monthly_investment = monthly_investment
        
    def _apply_loyalty_bonus(self, year: int, shares: float, dividends: float) -> tuple[float, float]:
        NotImplemented
        
    def run_simulation(self):
        NotImplemented
        
    def plot_results(self):
        NotImplemented
    