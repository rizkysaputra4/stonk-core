class BackTestResult:
    def __init__(self, ticker, profit, hit):
        self.ticker = ticker
        self.profit = profit
        self.hit = hit

    def __repr__(self):
        return f"ticker:{self.ticker}, profit:{self.profit}, hit: {self.hit}\n"

    def __str__(self):
        return f"ticker {self.ticker}, profit {self.profit}, hit: {self.hit}"
