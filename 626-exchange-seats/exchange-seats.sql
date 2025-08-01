# Write your MySQL query statement below
SELECT id, student
FROM (
  SELECT 
    CASE 
      WHEN id % 2 = 1 AND id + 1 <= (SELECT MAX(id) FROM Seat) THEN id + 1
      WHEN id % 2 = 0 THEN id - 1
      ELSE id
    END AS id,
    student
  FROM Seat
) AS swapped
ORDER BY id;