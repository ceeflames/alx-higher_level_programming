-- This list number of records with the same score in second_table
-- this records are ordered by descending count.
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
