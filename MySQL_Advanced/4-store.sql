-- Script that creates a trigger that
-- decreases the quantity of an item
items (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  quantity INT
);

orders (
  id INT PRIMARY KEY,
  item_id INT,
  quantity INT,
  created_at TIMESTAMP
);