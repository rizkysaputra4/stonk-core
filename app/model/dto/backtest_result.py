class BackTestResult:
    def __init__(self, ticker, profit):
        self.ticker = ticker
        self.profit = profit

    def __repr__(self):
        return f"ticker:{self.ticker}, profit:{self.profit}\n"

    def __str__(self):
        return f"ticker {self.ticker}, profit {self.profit}"