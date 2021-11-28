CREATE TABLE IF NOT EXISTS price (
    ticker VARCHAR PRIMARY KEY,
    date DATE,
    open DECIMAL,
    close DECIMAL,
    high DECIMAL,
    low DECIMAL,
    volume BIGINT,
    divident DECIMAL,
    stock_split DECIMAL
);