CREATE TABLE orders
(
    id SERIAL NOT NULL PRIMARY KEY,
    product_name VARCHAR(250) NOT NULL,
    amount INT NOT NULL,
    order_date TIMESTAMP NOT NULL DEFAULT NOW()
);
    
INSERT INTO orders(product_name, amount) VALUES
 ('Iphone 13 Pro', 50),
 ('Samsung S22', 580),
 ('Iphone 12 Pro', 90),
 ('Xiami Redmi Note', 40),
 ('Samsung Flip', 402)
