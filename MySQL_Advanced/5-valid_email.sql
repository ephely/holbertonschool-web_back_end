-- Creates a trigger that resets the attribute 
-- valid_email only when the email has been changed
users (
  id INT PRIMARY KEY,
  email VARCHAR(255),
  valid_email BOOLEAN
);