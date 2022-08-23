CREATE TABLE IF NOT EXISTS portfolio (
    customer_id VARCHAR NOT NULL,
    ticker VARCHAR NOT NULL,
    action VARCHAR(10) NOT NULL,
    qty NUMERIC NOT NULL,
    date TIMESTAMP NOT NULL,
    price DECIMAL NOT NULL,
    is_open BOOLEAN NOT NULL
);