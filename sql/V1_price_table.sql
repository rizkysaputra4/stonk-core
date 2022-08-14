CREATE TABLE IF NOT EXISTS price (
    ticker VARCHAR NOT NULL,
    date DATE NOT NULL,
    open DECIMAL,
    close DECIMAL,
    adj_close DECIMAL,
    high DECIMAL,
    low DECIMAL,
    volume NUMERIC,
    dividend DECIMAL,
    stock_split DECIMAL,
    PRIMARY KEY (ticker, date)
);