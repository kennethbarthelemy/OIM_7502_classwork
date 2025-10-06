
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick  # optional may be helpful for plotting percentage
import numpy as np
import pandas as pd
import seaborn as sb  # optional to set plot theme
sb.set_theme()  # optional to set plot theme

DEFAULT_START = dt.date.isoformat(dt.date.today() - dt.timedelta(365))
DEFAULT_END = dt.date.isoformat(dt.date.today())

# need yfinance
try:
    import yfinance as yf
except ImportError as e:
    raise SystemExit("yfinance is required. Install with: pip install yfinance") from e


class Stock:
    def __init__(self, symbol, start=DEFAULT_START, end=DEFAULT_END):
        self.symbol = str(symbol).upper().strip()
        self.start = start
        self.end = end
        self.data = self.get_data()

    def get_data(self):
        """
        Download daily OHLC data, keep close, set datetime index,
        and enrich with returns.
        """
        import yfinance as yf

        df = yf.download(
            self.symbol,
            start=self.start,
            end=self.end,
            auto_adjust=False,
            progress=False,
            threads=True,
        )
        if df.empty:
            raise ValueError(f"No data returned for {self.symbol}. Check symbol/dates.")

        df = df.rename(columns={"Adj Close": "adj_close", "Close": "close"})
        df = df.loc[:, ["close"]]
        df.index = pd.to_datetime(df.index)

        df = self.calc_returns(df)
        return df

    def calc_returns(self, df):
        """
        Add:
          - change: close-to-close dollar change
          - instant_return: daily log return (rounded to 4 decimals)
          - cum_return: cumulative performance from first day (decimal)
        """
        out = df.copy()
        out["change"] = out["close"].diff()
        out["instant_return"] = np.log(out["close"]).diff().round(4)
        out["cum_return"] = np.exp(out["instant_return"].fillna(0).cumsum()) - 1
        return out

    def plot_return_dist(self, bins=50):
        """Histogram of daily log returns."""
        series = self.data["instant_return"].dropna()
        if series.empty:
            raise ValueError("No returns to plot.")
        plt.figure(figsize=(9, 5))
        plt.hist(series, bins=bins)
        plt.title(f"{self.symbol}: Daily Log Return Distribution")
        plt.xlabel("Daily log return")
        plt.ylabel("Frequency")
        ax = plt.gca()
        ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
        plt.grid(alpha=0.3)
        plt.tight_layout()

    def plot_performance(self):
        """Line chart of cumulative return as % gain/loss."""
        cum = self.data["cum_return"]
        if cum.empty:
            raise ValueError("No cumulative performance to plot.")
        plt.figure(figsize=(10, 5))
        plt.plot(cum.index, cum.values, linewidth=2)
        plt.title(f"{self.symbol}: Performance Over Period")
        plt.xlabel("Date")
        plt.ylabel("Cumulative return")
        ax = plt.gca()
        ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
        plt.grid(alpha=0.3)
        plt.tight_layout()


def main():
    # Instantiate a test object (change symbol)
    test = Stock(symbol="MSFT")  #try: Stock("MSFT", start="2024-01-01", end="2024-12-31")
    print(test.data.tail(3))  # peek at the data
    test.plot_performance()
    test.plot_return_dist()

    plt.figure(1);
    plt.savefig("MSFT_return_dist.png", dpi=200, bbox_inches="tight")
    plt.figure(2);
    plt.savefig("MSFT_performance.png", dpi=200, bbox_inches="tight")

    plt.show()  # show both plots

if __name__ == "__main__":
    main()