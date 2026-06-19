-- Write a SQL script that 
-- creates a stored procedure AddBonus
users (
  id INT PRIMARY KEY,
  name VARCHAR(255)
);

projects (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) UNIQUE
);

corrections (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT,
  project_id INT,
  score INT
);