-- Write a SQL script that creates a
-- stored procedure ComputeAverageScoreForUser
corrections (
  id INT PRIMARY KEY,
  user_id INT,
  project_id INT,
  score DECIMAL(10,2)
);