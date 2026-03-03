# Air Liquide Investment Projection Simulator

A **deterministic** projection tool to estimate the long-term growth of an investment in **Air Liquide** shares over a chosen time horizon. 
This project includes a **Streamlit** interface: users can adjust parameters (growth rates, dividend reinvestment, loyalty bonus, monthly contributions) and see results and charts update instantly.

---

## Purpose

- Provide a **clear long-term projection** and help users understand how key assumptions impact outcomes.
- Keep the model **simple**, readable, and easy to extend (taxes, fees, volatility, more realistic timing, etc.).

---

## Table of Contents

- [Features](#features)


## Features

### Growth model
- Deterministic annual **share price** growth: `annual_growth_rate`
- Deterministic annual **dividend per share** growth: `dividend_growth_rate`

### Cash & purchases (no fractional shares)
- Shares are purchased as **whole integers only**.
- Leftover cash (dividends, "rompus", remaining cash after purchases) is tracked in **Cash**.

### Investing
- Fixed monthly contribution: `monthly_investment`
- Reinvesting dividends option: `reinvest_dividends`
  - If enabled: available cash is used to buy whole shares and any remainder stays as cash.

### Loyalty bonus (registered shares + 2-year rule)
This model approximates Air Liquide’s loyalty program using a simple yearly approach:

- Loyalty benefits apply to shares held in registered form (nominatif) for more than two full calendar years.
- Dividends:
  - All shares receive the standard dividend.
  - Eligible shares receive a +10% dividend bonus.
- Free share attributions:
  - Every 2 years: free shares are granted based on eligible shares
  - Base: 1 free share per 10 eligible shares
  - Registered (nominatif) bonus: +10% on free shares (equivalent to +1 free share per 100 eligible shares)
  - Fractions ("rompus") are paid as cash.

---

## Limitations / Key assumptions

This project is designed for **long-term estimation**, not exact forecasting. Real-world results may differ because:

- **No taxes**, no broker fees, no spread, no withholding taxes.
- The model is **annual**: real timing (dividend payment dates, attribution dates, price at the exact date) is not modelled.
- Free share attributions are assumed to occur **regularly every 2 years** (not guaranteed in reality).
- Loyalty rules are a **simplified** representation to keep the model readable.
- No randomness: no volatility, no Monte Carlo, no scenario analysis.

---

## Installation

1. Clone the repository:
2. Go into the project directory:
    ```bash
    git clone https://github.com/Pstkdev/Air-Liquide-Investment-Projection-Simulator-Tool.git
    cd Air-Liquide-Investment-Projection-Simulator-Tool/
    ```
3. Create a virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
4. Install dependencies
    ```bash 
        pip install -r requirements.txt
    ```
5. Run the app (Streamlit)
From the project root:

    ```bash 
        streamlit run app.py
    ```

Streamlit will display a local URL (often http://localhost:8501).

## How to use

In the sidebar you can set:

- Initial share price, initial shares, initial dividend
- Annual growth rates (price and dividend)
- Time horizon (years) and start year (e.g., 2026)
- Monthly investment amount
- Toggles:
    - Reinvest dividends
    - Loyalty bonus (nominatif + 2-year rule)

The app shows:

- Summary metrics (final value, shares, cash, total dividends, total invested, total return %)
- Interactive charts (portfolio value, number of shares)
- A detailed results table
