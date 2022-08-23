class ActionPoint:
    def __init__(self, buy, sell):
        self.buy = buy
        self.sell = sell

    def __repr__(self):
        return f"buy date:{self.buy}, sell date:{self.sell}>"

    def __str__(self):
        return f"buy date {self.buy}, sell date {self.sell}"
